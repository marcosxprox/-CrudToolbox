from tools_models import Tools

from users_models import Users

from loans_models import Loans as l

def menu():
   input("1 - Cadastar Usuario\n"
         "2 - Listar usuario\n"
         "3 - Cadastrar ferramenta\n"
         "4 - Lista ferramentas disponiveis\n"
         "5 - Emprestar ferramenta\n"
         "6 - Devolver ferramenta\n"
         "7 - Sair")

if __name__ == "__main__":

   # user_id = int(input("Digite o id que deseja editar:"))
   #user_id = int(input("Digite o id do usuario que deseja deletar:"))
   #consulte_id = int(input("Digite o id do usuario a qual deseja consultar:"))
   # usuario = Usuarios().adicionar_users(nome_user, email_user)
   #Usuarios().update_users(nome_user, email_user, user_id)
   #Usuarios().delete_user(user_id)

   while True:

        menu()

        opcao = input("Escolha uma opcao:")

        if opcao == "1":
           name_user = input("Digite o nome usuario:")
           email_user = input("Digite o email do usuario:")
           Users().add_users(name_user, email_user)

        elif opcao == "2":
           Users().consult_users()

        elif opcao == "3":
            ferramenta_nome = input("Digite o nome da ferramenta a ser cadastrada:")
            descricao = input("Digite a descricao da ferramenta:")
            disponibilidade = 1
            Tools().register_tool(ferramenta_nome, descricao, disponibilidade)

        elif opcao == "4":
           Tools().list_tools()

        elif opcao == "5":
            id_users = int(input("Digite o id do usuario que ira alugar a ferramenta:"))
            id_ferramenta = int(input("Digite o id da ferramenta que vai ser emprestada:"))
            data_emprestimo = input("Digite a data do emprestimo:")

            l.loan_tools(id_users, id_ferramenta, data_emprestimo)

        elif opcao == "6":
           id_emprestimo = int(input("Digite o id do emprestimo:"))
           data_devolucao = input("Digite a data de devolução:")
           l.return_tools(id_emprestimo, data_devolucao)

        elif opcao == "7":
           print("Saindo do sistema...")
           break




