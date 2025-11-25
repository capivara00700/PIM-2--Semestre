import mysql.connector
import random
import string
import crypto.encrypt

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
    senhac = crypto.encrypt.encrypt(senha)

    if msg == None:
        return False
    else:
        if msg[0] == senhac:
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

def gerar_Ra():
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))  # duas letras maiúsculas
    numeros = ''.join(random.choices(string.digits, k=4))          # quatro números
    return letras + numeros


def cadastro(email, senha):
    ra = gerar_Ra()
    senhac = crypto.encrypt.encrypt(senha)
    sql = "INSERT INTO usuarios(Ra, email, senha) VALUES (%s, %s, %s)"
    val = (ra, email, senhac)
    cursor.execute(sql, val)
    db.commit()

    return "Cadastro realizado com sucesso"
