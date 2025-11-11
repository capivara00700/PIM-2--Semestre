import mysql.connector

#conectando com o banco de dados
db = mysql.connector.connect(
    host = 'Localhost',
    user = 'root',
    password = '',
    database = 'pim_2'
)
cursor = db.cursor(buffered=True)

def login(email, senha):
    cursor.execute("SELECT senha FROM `usuarios` WHERE email = %(email)s", ({'email': email}))
    msg = cursor.fetchone()

    if msg == None:
        return False
    else:
        if msg[0] == senha:
            return True
    
def autenticacao(email, senha, senhaC): #-- se possivel melhorar isto
    if "@gmail.com" in email:
        if senha == senhaC:  #-- Verifica a senha
            c1 = c2 = c3 = c4 = False
            for i in senha: 
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

def cadastro(email, senha):
    sql = "INSERT INTO usuarios(email, senha) VALUES (%s, %s)"
    val = (email, senha)
    cursor.execute(sql, val)
    db.commit()

    return "Cadastro realizado com sucesso"
