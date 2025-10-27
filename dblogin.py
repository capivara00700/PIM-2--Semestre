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
    cursor.execute("SELECT * FROM `usuarios` WHERE senha = %(senha)s", ({'senha': senha, }))
    msg = cursor.fetchone()
    return msg