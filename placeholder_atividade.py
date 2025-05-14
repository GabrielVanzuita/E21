import requests

# Simulação de "banco de dados"
usuarios = {
    "1": {"email": "ana@email.com", "senha": "1234"},
    "2": {"email": "joao@email.com", "senha": "abcd"},
    "3": {"email": "katya@email.com", "senha": "russia28"},
}

# Autenticação
def login():
    print("=== LOGIN ===")
    email = input("Email: ")
    senha = input("Senha: ")

    for user_id, info in usuarios.items():
        if info["email"] == email and info["senha"] == senha:
            print(f"Login bem-sucedido. Bem-vindo(a), {email}!\n")
            return user_id

    print("Credenciais inválidas.")
    return None
