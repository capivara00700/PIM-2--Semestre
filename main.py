from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal (mostra o formulário)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    email = request.form["emailL"]
    senha = request.form["senhaLs"]

    return  f"senha: {senha}, email {email}"

if __name__ == '__main__':
    app.run(debug=True)
