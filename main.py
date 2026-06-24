from database import inicializa_banco
from simulator import gerar_leitura
from report import gerar_relatorio




def main():
    conn = inicializa_banco()
    cursor = conn.cursor()
    gerar_leitura(conn, cursor)
    gerar_relatorio(cursor)



if __name__ == '__main__':
    main()