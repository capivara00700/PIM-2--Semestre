from flask import Flask, render_template, request
import dblogin

app = Flask(__name__)

# Página principal (mostra o formulário)
@app.route('/')
def index():
    return render_template('index.html', show_popup=False)

@app.route('/login', methods=["POST"])
def login():
    email = request.form["emailL"]
    senha = request.form["senhaLs"]

    return dblogin.login(email,senha)

    # if dblogin.login(email, senha):
    #     return render_template('inicio.html') 
    # else:
    #     erro1 = "Email ou senha inválidos"
    #     return render_template('index.html', erro1 = erro1)


@app.route('/cadastro', methods=["POST"])
def cadastro():
    email = request.form["email"]
    senha = request.form["senha"]
    senhaC = request.form["senhaC"]

    if dblogin.autenticacao(email, senha, senhaC):        
        msg = dblogin.cadastro(email, senha)
        return render_template('index.html', msg = msg)
    else:
        erro2 = "Email ou senhas inválidas"
        return render_template('index.html', erro2 = erro2)


if __name__ == '__main__':
    app.run(debug=True)