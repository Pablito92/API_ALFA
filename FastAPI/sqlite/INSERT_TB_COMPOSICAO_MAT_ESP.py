import pyodbc
import decimal
import sqlite3

sql_insert = ''' '''
sql_commit = ''' '''

SERVER = "SERVIDOR001\\SQL2008R2"
SERVER = "\\192.168.10.2\\SQL2008R2"
USERNAME = 'silofertil'
PASSWORD = 'aloma458'

#ODBC Driver 13 for SQL Server
#CONNSTRING = 'DRIVER={SQL Server};SERVER='+SERVER+';DATABASE=ORDEM_PRODUCAO;UID='+USERNAME+';PWD='+ PASSWORD
CONNSTRING = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+SERVER+';DATABASE=ORDEM_PRODUCAO;UID='+USERNAME+';PWD='+ PASSWORD
conn = pyodbc.connect(CONNSTRING, autocommit = False, timeout = 30)
cursor = conn.cursor()
cursor.execute("SELECT * FROM TB_COMPOSICAO_MATERIAIS_ESPECIAIS ORDER BY CODIGO_CG")
rows = cursor.fetchall()

for row in rows:
    print(row)

# listar os nomes dos campos
fields = [field[0] for field in cursor.description]
values = list()

def insert_data(rows):
    sqlite_conn = sqlite3.connect(r'C:\Users\Admin\Desktop\sqlite\sqlite_db.db')

    print('Conexão com o BD sucedida!')
    sqlite_cursor = sqlite_conn.cursor()

    for row in rows:
        try:
            for i in range(0, len(fields)):
                if type(row[i]) == decimal.Decimal:
                    values.append(float(row[i]))
                else:
                    values.append(row[i])

            sqlite_cursor.execute(sql_insert, values )# AQUI FAZ O INSERT
            sqlite_cursor.execute(sql_commit)# COMMIT

            print(values)
            values.clear()
        except Exception as e:
            print(e)
            print(row)
            return 1

        print()#quebra de linha entre os itens selecionados do banco


#insert_data(rows)