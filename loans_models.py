from database import get_conn

from tools_models import Tools as t

from users_models import Users as u


class Loans:

    @staticmethod
    def get_user_id(id_users):
        cur = get_conn()
        cur.execute('''
        SELECT * FROM usuarios WHERE id = ? ''', (id_users,))
        result = cur.fetchall()
        return result


    @staticmethod
    def get_tools_id(id_ferramenta):
         cur = get_conn()
         cur.execute('''
         SELECT * FROM emprestimos WHERE ferramentasID = ?''', (id_ferramenta,))
         result = cur.fetchall()
         return result

    @staticmethod
    def loan_tools(id_users, id_ferramenta, data_emprestimo):

        cur = get_conn()
        usuario = u.get_user(id_users)
        if not usuario:
            print("Esse usuario não está cadastrado")
            return
        tool = t.get_tool(id_ferramenta)
        if tool[0][3] == 1:
           if not tool:
               print("Essa ferramenta não esta cadastrada")
               return
           else:
               try:
                  cur.execute('''
                  INSERT INTO emprestimos (usuariosID, ferramentasID, data_emprestimo) VALUES (?,?,?)''',
                  (id_users, id_ferramenta, data_emprestimo))
                  cur.connection.commit()
               except Exception as e:
                   print(f"Erro ao tentar emprestar ferramenta {e}")
               finally:
                    cur.connection.close()
        else:
            print("Essa ferramenta já está alugada")
            return


    @staticmethod
    def update_availability_tool(result):
        cur = get_conn()
        found_tool = t.get_tool(result[0][2])
        if found_tool[0][3] == 0:
            cur.execute('''UPDATE ferramentas SET disponibilidade = ? WHERE id = ?''', (1, result[0][2]))
            cur.connection.commit()
            print(found_tool)

    @staticmethod
    def update_loans(data_devolucao, id_emprestimo):
        cur = get_conn()
        cur.execute('''UPDATE emprestimos SET quantidade = ?, data_devolucao = ? WHERE id = ?''', (1, data_devolucao, id_emprestimo))
        cur.connection.commit()
        cur.close()

    @staticmethod
    def return_tools(id_emprestimo, data_devolucao):
        cur = get_conn()
        cur.execute('select * from emprestimos where id = ?', (id_emprestimo,))
        result = cur.fetchall()
        if not result:
            print("id do emprestimo não encontrado")
        else:
            Loans.update_availability_tool(result)
            Loans.update_loans(data_devolucao, id_emprestimo)
            cur.close()





