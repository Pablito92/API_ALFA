# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 08:56:12 2022
@author: Admin
"""
import pyodbc
import decimal
from decimal import Decimal
import time
import sqlite3

#sql_insert = '''
#INSERT INTO TB_MATERIAIS_CIGAM
#    (DESCRICAO, PRECO_UNITARIO)
#VALUES
#    (?, ?);
#'''

sql_insert = '''
INSERT INTO materia_prima_cigam
    ( CODIGO, DESCRICAO, PR_UNITARIO, FRETE_SF, COM_FRETE, CUSTO_SF, PORCENTAGEM, DADOS_CIGAM,
     ESPECIAL, ESTOQUE, UNIDADE, CONVERTE_KG, DESCRI_CONVERTE, FORMULA, DATA_ALTERACAO,
     DATA_COMPRA, ID_GRUPO, DESC_GRUPO, ID_SUB_GRUPO, DESC_SUB_GRUPO )
VALUES
    ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

sql_commit = '''COMMIT;'''

SERVER = "SERVIDOR001\\SQL2008R2"
USERNAME = 'silofertil'
PASSWORD = 'aloma458'
CONNSTRING = 'DRIVER={SQL Server};SERVER='+SERVER+';DATABASE=ORDEM_PRODUCAO;UID='+USERNAME+';PWD='+ PASSWORD

conn = pyodbc.connect(CONNSTRING, autocommit = False, timeout = 5)
cursor = conn.cursor()
cursor.execute("select * from Custo101cigam where codigo > '0004501' ORDER BY CODIGO ASC")
rows = cursor.fetchall()

# listar os nomes dos campos
fields = [field[0] for field in cursor.description]
values = list()

def insert_data(rows):
    #C:\Users\celesio.SILOFERTIL01\fastapi\sqlite\pythonsqlite.db
    #sqlite_conn = sqlite3.connect(r'C:\Users\celesio.SILOFERTIL01\fastapi\sqlite\pythonsqlite.db')
    #C:\Users\celesio.SILOFERTIL01\fastapi\MeuProjeto\sql_app\sql_app.db
    sqlite_conn = sqlite3.connect(r'C:\Users\celesio.SILOFERTIL01\fastapi\MeuProjeto\sql_app\sql_app.db')

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


insert_data(rows)
