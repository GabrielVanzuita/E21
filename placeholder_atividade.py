import requests

# Simulação de "banco de dados"
usuarios = {
    "1": {"email": "ana@email.com", "senha": "1234"},
    "2": {"email": "joao@email.com", "senha": "abcd"},
    "3": {"email": "katya@email.com", "senha": "russia28"},
}

# Armazenamento local de posts criados
posts_criados = []

def login():
    """
    Realiza o login do usuário com base em email e senha.

    Retorna:
        str: ID do usuário autenticado.
    """
    while True:
        print("=== LOGIN ===")
        email = input("Email: ")
        senha = input("Senha: ")

        for user_id, info in usuarios.items():
            if info["email"] == email and info["senha"] == senha:
                print(f"Login bem-sucedido. Bem-vindo(a), {email}!\n")
                return user_id

        print("❌ Credenciais inválidas. Tente novamente.\n")

def ver_posts():
    """
    Exibe os 5 primeiros posts públicos disponíveis via JSONPlaceholder.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    for post in posts[:5]:
        print(f"{post['id']}: {post['title']}")
    print()

def ver_comentarios():
    """
    Solicita um ID de post ao usuário e exibe os comentários associados.
    """
    post_id = input("ID do post: ")
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    comentarios = response.json()
    for c in comentarios:
        print(f"- {c['email']}: {c['body']}")
    print()

def ver_meus_posts(user_id):
    """
    Exibe os posts criados localmente pelo usuário logado.

    Args:
        user_id (str): ID do usuário autenticado.
    """
    meus_posts = [post for post in posts_criados if post["userId"] == user_id]
    if not meus_posts:
        print("Você ainda não tem posts.\n")
        return
    print("=== Meus Posts Criados ===")
    for post in meus_posts:
        print(f"Título: {post['title']}\nConteúdo: {post['body']}\n")
    print()

def filtrar_posts_por_usuario():
    """
    Solicita um ID de usuário e exibe os posts públicos associados a ele via API.
    """
    user_id = input("Digite o ID do usuário (1 a 10): ")
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": user_id})
    posts = response.json()
    for post in posts:
        print(f"{post['id']}: {post['title']}")
    print()

def criar_post(user_id):
    """
    Cria um novo post e armazena localmente após simular o envio via API.

    Args:
        user_id (str): ID do usuário autenticado.
    """
    title = input("Título do post: ")
    body = input("Conteúdo: ")
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    if response.status_code == 201:
        posts_criados.append(payload)
        print("✅ Post criado com sucesso e armazenado localmente!\n")
    else:
        print("❌ Falha ao criar post.\n")

def menu():
    """
    Exibe o menu principal de opções após o login do usuário.
    """
    user_id = login()

    while True:
        print("=== MENU ===")
        print("1. Ver posts")
        print("2. Ver comentários de um post")
        print("3. Ver meus posts")
        print("4. Ver posts de outro usuário")
        print("5. Criar novo post")
        print("6. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            ver_posts()
        elif opcao == "2":
            ver_comentarios()
        elif opcao == "3":
            ver_meus_posts(user_id)
        elif opcao == "4":
            filtrar_posts_por_usuario()
        elif opcao == "5":
            criar_post(user_id)
        elif opcao == "6":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

# Início do programa
if __name__ == "__main__":
    menu()
