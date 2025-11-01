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

    if msg == None:
        return False
    else: 
        return True

    
def cadastro(email, senha, senhaC):
    if senha == senhaC:
        if senha in "!@#$%^&*()-+=[]\{}|;':\",./<>?":
            return True
