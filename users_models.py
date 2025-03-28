from database import conectar

class Users:

    @staticmethod
    def add_users(nome, email):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('''
                        INSERT INTO usuarios (nome, email) VALUES (?,?)
                    ''', (nome, email))
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir o usuario {e} ")
        finally:
            if conexao is not None:
               conexao.close()

        return nome, email

    @staticmethod
    def update_users(nome, email, id_user):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('''UPDATE usuarios
                SET nome = ?, email = ?
                WHERE id = ?
            ''', (nome, email, id_user))
            conexao.commit()
            print("Atualizado com Sucesso")
        except Exception as e:
            print(f"Erro ao atualizar o usuario {e}")
        finally:
            if conexao is not None:
               conexao.close()

    @staticmethod
    def delete_user(user_id):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('DELETE FROM usuarios WHERE id = ? ', (user_id,))
            conexao.commit()
            print("Usuario deletado com sucesso")
        except Exception as e:
            print(f"Erro ao tentar deletar usuario {e}")
        finally:
            if conexao is not None:
                conexao.close()

    @staticmethod
    def consult_users():
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute('select * from usuarios')
            resul = cur.fetchall()
            conexao.commit()
            print(resul)
        except Exception as e:
            print(f"Erro ao tentar listar usuarios disponiveis {e}")
        finally:
            if conexao is not None:
                conexao.close()

    @staticmethod
    def get_user(id_users):
        conexao = None
        try:
            conexao = conectar()
            cur = conexao.cursor()
            cur.execute(
                '''
            SELECT * FROM usuarios WHERE id = ?
            ''', (id_users,))
            return cur.fetchall()
        except Exception as e:
            print(f"Erro ao tentar consultar id do usuario {e}")
        finally:
            if conexao is not None:
               conexao.close()


