from database import get_conn

from ferramentas_models import Ferramentas as f

from usuarios_models import Usuarios as u


class Emprestimos:

    @staticmethod
    def get_u(id_users):
        cur = get_conn()
        cur.execute('''
        SELECT * FROM usuarios WHERE id = ? ''', (id_users,))
        result = cur.fetchall()
        return result


    @staticmethod
    def get_f(id_ferramenta):
         cur = get_conn()
         cur.execute('''
         SELECT * FROM emprestimos WHERE ferramentasID = ?''', (id_ferramenta,))
         result = cur.fetchall()
         return result

    @staticmethod
    def emprestar_ferramenta(id_users, id_ferramenta, data_emprestimo):

        cur = get_conn()
        usuario = u.get_user(id_users)
        if not usuario:
            print("Esse usuario não está cadastrado")
            return
        ferramenta = f.get_ferramenta(id_ferramenta)
        verificar = ferramenta[0][3]
        if verificar == 1:
           if not ferramenta:
               print("Essa ferramenta não esta cadastrada")
               return
           else:
               cur.execute('''
                INSERT INTO emprestimos (usuariosID, ferramentasID, data_emprestimo) VALUES (?,?,?)''',
                (id_users, id_ferramenta, data_emprestimo))
               cur.connection.commit()
               cur.connection.close()
        else:
            print("Essa ferramenta já está alugada")
            return

    @staticmethod
    def devolver_ferramenta(id_emprestimo, data_devolucao):
        cur = get_conn()
        cur.execute('select * from emprestimos where id = ?', (id_emprestimo,))
        result = cur.fetchall()
        busca_id_ferramenta = result[0][2]
        print(busca_id_ferramenta)
        ferramenta = f.get_ferramenta(busca_id_ferramenta)
        verificar = ferramenta[0][3]
        print(verificar)
        if verificar == 0:
           cur.execute('''UPDATE ferramentas SET disponibilidade = ? WHERE id = ?''', (1, busca_id_ferramenta))
           cur.connection.commit()
           print(ferramenta)

           cur.execute('''UPDATE emprestimos SET quantidade = ?, data_devolucao = ? WHERE id = ?''', (1, data_devolucao, id_emprestimo))
           cur.connection.commit()
           print(result)

           cur.close()











