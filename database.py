import sqlite3

def conectar():
    conexao = sqlite3.connect('toolsboxDB')
    return conexao

def get_conn():
    conexao = conectar()
    cur = conexao.cursor()
    return cur