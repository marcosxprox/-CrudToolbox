from ferramentas_models import Ferramentas

from usuarios_models import Usuarios

from emprestimos_models import Emprestimos as e


#usuario.adicionar_users(nome_user, email_user)
if __name__ == "__main__":
   # nome_user = input("Digite o nome usuario:")
   # email_user = input("Digite o email do usuario:")
   # user_id = int(input("Digite o id que deseja editar:"))
   #user_id = int(input("Digite o id do usuario que deseja deletar:"))
   #consulte_id = int(input("Digite o id do usuario a qual deseja consultar:"))

    #ferramenta_nome = input("Digite o nome da ferramenta a ser cadastrada:")
    #descricao = input("Digite a desceicao da ferramenta:")
    #campo = bool(input("disponibilidade:"))
    #campo_disponibilidade = 1



    # usuario = Usuarios().adicionar_users(nome_user, email_user)
    #Usuarios().update_users(nome_user, email_user, user_id)
    #Usuarios().delete_user(user_id)
    #Usuarios().consultar_use(consulte_id)

    #Ferramentas().cadastrar_ferramenta(ferramenta_nome, descricao, campo)
    #Ferramentas().listar_ferramnetas(campo_disponibilidade)

   #id_users = int(input("Digite o id do usuario que ira alugar a ferramenta:"))
   #id_ferramenta = int(input("Digite o id da ferramenta que vai ser emprestada:"))
   #data_emprestimo = input("Digite a data do emprestimo:")
   #e.emprestar_ferramenta(id_users, id_ferramenta, data_emprestimo)

   id_emprestimo = int(input("Digite o id do emprestimo"))
   data_devolucao = input("Digite a data de devolução:")
   e.devolver_ferramenta(id_emprestimo, data_devolucao)

