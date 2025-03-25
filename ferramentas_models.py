from twisted.conch.insults.window import cursor


from database import conectar

class Ferramentas:

    @staticmethod
    def cadastrar_ferramenta(ferramenta_nome, descricao, campo):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute(
                '''
                INSERT INTO ferramentas (nome, descricao, campo)
                VALUES (?, ?, ?)
                ''', (ferramenta_nome, descricao, campo)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao tentar cadastrar ferramenta {e}")
        finally:
            if conexao is not None:
               conexao.close()

    @staticmethod
    def listar_ferramnetas(campo_disponibilidade):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('SELECT * FROM ferramentas WHERE campo = ?',(campo_disponibilidade,))
            resul = cur.fetchall()
            print(resul)
            conexao.commit()
        except Exception as e:
            print(f"Erro ao tentar buscar ferramentas disponiveis {e}")
        finally:
            if conexao is not None:
               conexao.close()

    @staticmethod
    def get_ferramenta(id):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('SELECT * FROM ferramentas WHERE id = ?',(id,))
            return cur.fetchall()
        except Exception as e:
            print(f"Erro ao buscar ferramenta {e} ")
        finally:
            if conexao is not None:
               conexao.close()




