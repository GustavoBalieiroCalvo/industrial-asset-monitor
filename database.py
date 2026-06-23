import sqlite3

sql_equipamentos = 'CREATE TABLE IF NOT EXISTS equipamentos (' \
'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
'nome TEXT,' \
'localizacao TEXT,' \
'tipo TEXT' \
')'

sql_leituras = 'CREATE TABLE IF NOT EXISTS leituras (' \
'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
'equipamento_id INTEGER,'\
'timestamp REAL,'\
'temperatura REAL,'\
'pressao REAL,'\
'vibracao REAL)'

def conecta_banco(nome_banco):
    conn = sqlite3.connect(nome_banco)
    return conn
    

def main():
    conn = conecta_banco('fabrica.db')
    cursor = conn.cursor()
    cursor.execute(sql_equipamentos)
    cursor.execute(sql_leituras)
    conn.commit()


if __name__ == '__main__':
    main()