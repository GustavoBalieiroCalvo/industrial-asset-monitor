import random
import sqlite3
from datetime import datetime
equipamentos = [("Misturador Industrial A", "Linha 1 - Produção", "Misturador"),
                ("Compressor de Ar CP-01", "Utilidades", "Compressor"),
                ("Bomba Dosadora BD-03", "Linha 2 - Envase", "Bomba")
]

sql_comando = 'SELECT id, nome FROM equipamentos'

def gerar_leitura(conn, cursor):
    cursor.execute(sql_comando)
    equipamentos_db = cursor.fetchall()
    if not equipamentos_db:
        cursor.executemany(
            "INSERT INTO equipamentos (nome, localizacao, tipo) VALUES (?, ?, ?)",
            equipamentos
        )
        conn.commit()
        print("Equipamentos inseridos")
        cursor.execute(sql_comando)
        equipamentos_db = cursor.fetchall()
        # print(equipamentos_db)

    for equipamento in equipamentos_db:
        id_equipamento = equipamento[0]
        temperatura = random.uniform(20.0, 90.0)
        pressao = random.uniform(1.0, 10.0)
        vibracao = random.uniform(0.1, 5.0)
        datastamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO leituras (equipamento_id, timestamp, temperatura, vibracao, pressao) VALUES(?, ?, ?, ?, ?)",
                       (id_equipamento, datastamp, temperatura, vibracao, pressao))
        conn.commit()
    print('Motor de simulação gerou dados')
    cursor.execute("SELECT * FROM leituras")
    leituas = cursor.fetchall()
    # print(leituas)




