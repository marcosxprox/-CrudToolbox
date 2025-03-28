from database import conectar

class Tools:

    @staticmethod
    def register_tool(ferramenta_nome, descricao, disponibilidade):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute(
                '''
                INSERT INTO ferramentas (nome, descricao, disponibilidade)
                VALUES (?, ?, ?)
                ''', (ferramenta_nome, descricao, disponibilidade)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao tentar cadastrar ferramenta {e}")
        finally:
            if conexao is not None:
               conexao.close()

    @staticmethod
    def list_tools():
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('SELECT * FROM ferramentas')
            resul = cur.fetchall()
            print(resul)
            conexao.commit()
        except Exception as e:
            print(f"Erro ao tentar buscar ferramentas disponiveis {e}")
        finally:
            if conexao is not None:
               conexao.close()

    @staticmethod
    def get_tool(id_tool):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('SELECT * FROM ferramentas WHERE id = ?',(id_tool,))
            return cur.fetchall()
        except Exception as e:
            print(f"Erro ao buscar ferramenta {e} ")
        finally:
            if conexao is not None:
               conexao.close()




