import mysql.connector

#conectando com o banco de dados
db = mysql.connector.connect(
    host = 'Localhost',
    user = 'root',
    password = '',
    database = 'pim_2'
)
cursor = db.cursor()

def login(email, senha):
    cursor.execute("SELECT senha FROM `usuarios` WHERE email = %(email)s", ({'email': email, }))
    msg = cursor.fetchone()

    return msg

    
def autenticacao(email, senha, senhaC):
    if senha == senhaC:
        c1 = c2 = c3 = c4 = False
        for i in senha:  # -- Verifica a senha
            if i in "!@#$%^&*()-+=[]\{}|;':\",./<>?":
                c1 = True
            if i in senha.upper():
                c2 = True
            if i.isdigit():
                c3 = True
            if len(senha) >= 6:
                c4 = True

        if c1 and c2 and c3 and c4:
            return True
        else: 
            return False
    else:
        return False

def cadastro(email, senha):
    sql = "INSERT INTO usuarios(email, senha) VALUES (%s, %s)"
    val = (email, senha)
    cursor.execute(sql, val)
    db.commit()

    return "Cadastro realizado com sucesso"
