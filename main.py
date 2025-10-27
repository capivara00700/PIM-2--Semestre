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

    if dblogin.login(email, senha):
        return render_template('index.html', resultado=dblogin.login(email, senha))
    else:
        return render_template('index.html', show_popup=True)

if __name__ == '__main__':
    app.run(debug=True)