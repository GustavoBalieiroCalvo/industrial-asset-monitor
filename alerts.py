import sqlite3
from typing import Final

NOME_DB: Final[str] = "fabrica.db"
TEMP_MAX: Final[float] = 75.0
PRESS_MAX: Final[float] = 8.0
VIBRA_MAX: Final[float] = 4.0

sql_comando_busca = 'SELECT leituras.id, equipamentos.nome, leituras.temperatura, leituras.pressao, leituras.vibracao' \
' FROM leituras' \
' JOIN equipamentos ON leituras.equipamento_id = equipamentos.id'

def verificar_alertas(cursor):
    cursor.execute(sql_comando_busca)
    leituras = cursor.fetchall()

    equipamentos_alerta = {}
    for leitura in leituras:
        tem_alerta = False
        alerta = f'ALERTA — {leitura["nome"]:<30}'
        if leitura[2] > TEMP_MAX:
            alerta += f' | temperatura: {leitura["temperatura"]:.2f}° (máx: {TEMP_MAX:.2f}°)'
            tem_alerta = True

        if leitura[3] > PRESS_MAX:
            alerta += f' | pressão: {leitura["pressao"]:.2f} bar (máx: {PRESS_MAX:.2f} bar)'
            tem_alerta = True

        if leitura[4] > VIBRA_MAX:
            alerta += f' | vibração: {leitura["vibracao"]:.2f} Hz (máx: {VIBRA_MAX:.2f} Hz)'
            tem_alerta = True

        if tem_alerta: 
            print(alerta)
            equipamentos_alerta[leitura["id"]] = True
    return equipamentos_alerta
def conecta_db():
    conn = sqlite3.connect(NOME_DB)
    conn.row_factory = sqlite3.Row
    return conn
