from flask import Flask, render_template, request, redirect, session
import dblogin
import mysql.connector

app = Flask(__name__)
app.secret_key = "qualquer_chave_segura"

# --------------------------------------------
# Conexão com banco (professor)
# --------------------------------------------
dbp = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pim_2'
)
cursorp = dbp.cursor(buffered=True)

# -------------------------------------------------
#   LOGIN DO ALUNO  (SEU SISTEMA ORIGINAL)
# -------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html', show_popup=False)

@app.route('/login', methods=["POST"])
def login():
    email = request.form["emailL"]
    senha = request.form["senhaLs"]

    if dblogin.login(email, senha):
        session["aluno"] = email
        return render_template('inicio.html')
    else:
        erro1 = "Email ou senha inválidos"
        return render_template('index.html', erro1=erro1)

@app.route('/cadastro', methods=["POST"])
def cadastro():
    email = request.form["email"]
    senha = request.form["senha"]
    senhaC = request.form["senhaC"]

    if dblogin.autenticacao(email, senha, senhaC):
        msg = dblogin.cadastro(email, senha)
        return render_template('index.html', msg=msg)
    else:
        erro2 = "Email ou senhas inválidas"
        return render_template('index.html', erro2=erro2)

# -------------------------------------------------
#   LOGOUT GERAL
# -------------------------------------------------
@app.route('/sair')
def sair():
    session.clear()
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    if "aluno" not in session:
        return redirect("/")

    #conectando com o banco de dados
    db = mysql.connector.connect(
        host = 'Localhost',
        user = 'root',
        password = '',
        database = 'pim_2'
    )
    cursor = db.cursor(buffered=True)

    # Buscar atividades disponíveis
    cursor.execute("""
        SELECT id, titulo, descricao, professor_email, data_criacao
        FROM atividades
        ORDER BY data_criacao DESC
    """)
    dados = cursor.fetchall()

    atividades = []
    for a in dados:
        atividades.append({
            "id": a[0],
            "titulo": a[1],
            "descricao": a[2],
            "professor_email": a[3],
            "data_criacao": a[4]
        })

    return render_template("inicio.html", atividades=atividades)

# =================================================
#   SISTEMA DO PROFESSOR
# =================================================

# -------------------------------
# Login do Professor
# -------------------------------
@app.route("/professor/login", methods=["GET", "POST"])
def login_professor():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        cursorp.execute("SELECT senha FROM professores WHERE email=%s", (email,))
        dado = cursorp.fetchone()

        if dado and dado[0] == senha:
            session["professor"] = email
            return redirect("/professor")
        else:
            return render_template("login_prof.html", erro="Login inválido")

    return render_template("login_prof.html")


# -------------------------------
# Painel do professor
# -------------------------------
@app.route("/professor")
def professor():
    if "professor" not in session:
        return redirect("/professor/login")
    return render_template("professor.html")

# -------------------------------
# Listagem de atividades
# -------------------------------
@app.route("/professor/atividades")
def prof_atividades():
    if "professor" not in session:
        return redirect("/professor/login")

    cursorp.execute("""
        SELECT id, titulo, descricao, data_criacao 
        FROM atividades 
        WHERE professor_email=%s
        ORDER BY data_criacao DESC
    """, (session["professor"],))

    atividades = cursorp.fetchall()

    lista = []
    for a in atividades:
        lista.append({
            "id": a[0],
            "titulo": a[1],
            "descricao": a[2],
            "data_criacao": a[3]
        })

    return render_template("prof_atividades.html", atividades=lista)



# -------------------------------
# Criar nova atividade
# -------------------------------
@app.route("/professor/atividade/nova", methods=["GET", "POST"])
def nova_atividade():
    if "professor" not in session:
        return redirect("/professor/login")

    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        prof = session["professor"]

        cursorp.execute("""
            INSERT INTO atividades (titulo, descricao, professor_email)
            VALUES (%s, %s, %s)
        """, (titulo, descricao, prof))

        dbp.commit()

        return redirect("/professor/atividades")

    return render_template("nova_atividade.html")

# --------------------------------------------
# Cadastro de Professores
# --------------------------------------------
@app.route("/professor/cadastro", methods=["GET", "POST"])
def cadastro_prof():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        senha2 = request.form["senha2"]

        if senha != senha2:
            return render_template("cadastro_prof.html", erro="As senhas não coincidem.")

        # Verifica se já existe
        cursorp.execute("SELECT id FROM professores WHERE email=%s", (email,))
        if cursorp.fetchone():
            return render_template("cadastro_prof.html", erro="Este e-mail já está cadastrado.")

        # Insere professor
        cursorp.execute("""
            INSERT INTO professores (email, senha)
            VALUES (%s, %s)
        """, (email, senha))
        dbp.commit()

        return redirect("/professor/login")

    return render_template("cadastro_prof.html")

# -------------------------------
# Ver respostas dos alunos
# -------------------------------
@app.route("/professor/atividade/<int:id>/respostas")
def ver_respostas(id):
    if "professor" not in session:
        return redirect("/professor/login")

    cursorp.execute("""
        SELECT aluno_email, resposta, data_envio
        FROM respostas
        WHERE atividade_id=%s
    """, (id,))

    dados = cursorp.fetchall()

    respostas = []
    for r in dados:
        respostas.append({
            "aluno_email": r[0],
            "resposta": r[1],
            "data_envio": r[2]
        })

    return render_template("respostas.html", respostas=respostas)



# =====================================================
# Execução
# =====================================================
if __name__ == '__main__':
    app.run(debug=True)
