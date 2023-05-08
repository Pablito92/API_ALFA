import sqlite3
import codecs
import requests

from fastapi import APIRouter

router = APIRouter()

@router.put('/create/')
async def create_ticket(titulo: str, codigo_cliente : int , codigo_modulo: int):

    sql = codecs.open(r"C:/Users/pabli/Desktop/FastAPI/sqlite/INSERT_INTO_TICKET.sql", encoding='utf-8', mode='r').read()
    sql = sql.replace('\r', '').replace('\n',' ').replace('\t', '') # remove quebras de linha '\n', form feed '\f' e tabs '\t'
    sql = sql.replace('?','\''+ titulo + '\'', 1).replace('?', str(codigo_cliente), 1).replace('?', str(codigo_modulo), 1) # substitui os 3 '?' no SQL pelos parâmetros
    print(sql)
    
    conn = sqlite3.connect(r'C:/Users/pabli/Desktop/FastAPI/sqlite/sqlite_db.db') ## mudar a localização para a da sua máquina    
    cursor = conn.cursor()
    cursor.execute(sql)

    if cursor.rowcount >= 1:
        cursor.execute('commit;')
        return {'status': 'OK'}
    else:
        return {'status': 'ERROR'}

@router.get("/search/") # acessar http://127.0.0.1:8000/search/?q=carrot para exemplo
async def get_recipes(q : str = ""):
    response = requests.get("https://forkify-api.herokuapp.com/api/search/" + '?q=' + q)

    if response.status_code == 200:
        data = response.json()
        return data    
    return "Something went wrong!!"

## na rota abaixo eu assumi que se o usuário seleciona o mês a partir de um combobox com os nomes, o front já converte para o respectivo número: 01 - janeiro, 02 - fevereiro, etc...
@router.get("/tickets/")
async def get_tickets(month : str = "", year : str =""):
    if month == "": return "Informe um Mês!"
    if year == "": return "Informe um Ano!"

    conn = sqlite3.connect(r'C:/Users/pabli/Desktop/FastAPI/sqlite/sqlite_db.db') ## mudar a localização para a da sua máquina    
    cursor = conn.cursor()

    sql = codecs.open(r"C:/Users/pabli/Desktop/FastAPI/sqlite/SELECT_TICKET.sql", encoding='utf-8', mode='r').read()
    sql = sql.replace('\r', '').replace('\n',' ').replace('\t', '') # remove quebras de linha '\n', form feed '\f' e tabs '\t'
    sql = sql.replace('?', year, 1).replace('?', month, 1) # substitui os dois '?' no SQL pelos parâmetros

    #print(sql) # mostra no console

    cursor.execute(sql)
    fields = [field[0] for field in cursor.description]# extrair os nomes das colunas da consulta
    rows = cursor.fetchall()

    lista = [] # lista de todos os tickets
    ticket = {} # dicionario auxiliar para 'extrair' cada ticket de cada registro retornado do BD
    modulos = {} # armazena a contagem de tickets por módulo
    clientes = {}# armazena a contagem de tickets por cliente

    for row in rows:
        #lista.append( {fields[i]:row[i] for i in range(0, len(fields))} ) # dictionary comprehension
        for i in range(0 , len(fields)):
            ticket[fields[i]] = row[i]

            if fields[i] == 'NOME_CLIENTE':
                if row[i] in clientes:
                    clientes[row[i]] = clientes[row[i]] + 1
                else:
                    clientes[row[i]] = 1
            
            if fields[i] == 'NOME_MODULO':
                if row[i] in modulos:
                    modulos[row[i]] = modulos[row[i]] + 1
                else:
                    modulos[row[i]] = 1
        
        lista.append(ticket.copy())

    return {'clientes': clientes, 'modulos': modulos, 'tickets' : lista} # monta o dicionário final e retorna

