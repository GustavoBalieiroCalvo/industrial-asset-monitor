import sqlite3
from typing import Final
from alerts import verificar_alertas

NOME_DB: Final[str] = "fabrica.db"

sql_comando = 'SELECT equipamentos.id, equipamentos.nome, MAX(leituras.timestamp),'\
' leituras.id, leituras.temperatura, leituras.pressao, leituras.vibracao'\
' FROM leituras'\
' JOIN equipamentos ON leituras.equipamento_id = equipamentos.id'\
' GROUP BY equipamentos.nome'

def conecta_banco():
    conn = sqlite3.connect(NOME_DB)
    conn.row_factory = sqlite3.Row
    return conn

def gerar_relatorio(cursor):
    cursor.execute(sql_comando)
    tupl_equipamentos_ultimo_alerta = cursor.fetchall()
    dict_status_por_leitura_id = verificar_alertas(cursor)

    for equipamento in tupl_equipamentos_ultimo_alerta:
        tem_alerta = dict_status_por_leitura_id.get(equipamento[3], False)
        if tem_alerta:
            print(f'{equipamento["nome"]:<30} | {equipamento["MAX(leituras.timestamp)"]:<30} | ALERTA')

        else:
            print(f'{equipamento["nome"]:<30} | {equipamento["MAX(leituras.timestamp)"]:<30} | OK')


def main():
    conn = conecta_banco()
    cursor = conn.cursor()
    gerar_relatorio(cursor)






if __name__ == '__main__':
    main()