from flask import Flask, render_template, request, jsonify, redirect
import pymysql
from apimercadopago import gerar_link_pagamento

app = Flask(__name__)

# Função para conectar ao banco de dados MySQL
def get_db_connection():
    return pymysql.connect(
        host="localhost",       # Host do MySQL (localhost para servidor local)
        user="root",            # Usuário root
        password="",            # Deixe a senha em branco já que você não definiu uma senha
        db="pizzaria",          # Nome do banco de dados
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor  # Retorna resultados como dicionário
    )

# Rota para a página de contato
@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get("name")
        email = request.form.get("email")
        mensagem = request.form.get("message")

        conn = None
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO mensagens_contato (nome, email, mensagem) VALUES (%s, %s, %s)',
                    (nome, email, mensagem)
                )
                conn.commit()
                print("Mensagem salva com sucesso.")  # Log de sucesso
        except Exception as e:
            print(f"Erro ao enviar mensagem de contato: {e}")
            if conn:
                conn.close()
            return jsonify({'error': 'Ocorreu um erro ao enviar sua mensagem'}), 500
        finally:
            if conn:
                conn.close()

        return render_template("mensagem.html")
    
    return render_template("contato.html")


# Rota para a página de sucesso após enviar o formulário
@app.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")

# Rota principal, renderiza a página index.html
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Rota para o cardápio
@app.route("/cardapio", methods=["GET"])
def cardapio():
    return render_template("cardapio.html")

# Rota para o checkout
@app.route("/checkout", methods=["POST"])
def checkout():
    try:
        cart = request.get_json()
        print("Carrinho recebido:", cart)  # Verifica o conteúdo do carrinho
        
        if not cart:
            return jsonify({'error': 'Carrinho vazio'}), 400

        checkout_url = gerar_link_pagamento(cart)
        return jsonify({'checkout_url': checkout_url})
    except Exception as e:
        print(f"Erro no checkout: {e}")  # Loga o erro
        return jsonify({'error': str(e)}), 500

@app.route("/negado")
def negado():
    return render_template("negado.html")

@app.route("/pendente")
def pendente():
    return render_template("pendente.html")

# Outras rotas do site
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/entrega")
def entrega():
    return render_template("entrega.html")

if __name__ == '__main__':
    app.run(debug=True)
