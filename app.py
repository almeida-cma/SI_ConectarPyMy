from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Rota principal para exibir todos os usuários
@app.route('/')
def index():
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mypy",
        port=7306
    )
    cursor = conexao.cursor()

    # Executar consulta SQL para selecionar todos os usuários
    cursor.execute("SELECT * FROM usuarios")

    # Recuperar resultados da consulta
    resultados = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    # Renderizar a página HTML com os resultados
    return render_template('index.html', resultados=resultados)

# Rota para adicionar um novo usuário
@app.route('/add_user', methods=['POST'])
def add_user():
    # Obter dados do formulário
    nome = request.form['nome']
    email = request.form['email']

    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mypy",
        port=7306
    )
    cursor = conexao.cursor()

    # Inserir novo usuário no banco de dados
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conexao.commit()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    # Redirecionar de volta para a página principal
    return redirect('/')

# Rota para excluir um usuário
@app.route('/delete_user', methods=['POST'])
def delete_user():
    # Obter o ID do usuário a ser excluído
    user_id = request.form['user_id']

    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mypy",
        port=7306
    )
    cursor = conexao.cursor()

    # Excluir o usuário do banco de dados
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
    conexao.commit()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    # Redirecionar de volta para a página principal
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
