import random
import string
while True:
    def gerar_senha(comprimento, caracteres):
        senha = ''
        for i in range(comprimento):
            senha += random.choice(caracteres)
        return senha

    def main():
        comprimento = int(input("Digite o comprimento da senha: "))
        caracteres = input("Digite os caracteres permitidos (deixe em branco para usar caracteres padrão): ")

        if not caracteres:
            caracteres = string.ascii_letters + string.digits + string.punctuation
        
        senha_gerada = gerar_senha(comprimento, caracteres)
        print("Senha gerada:", senha_gerada)

    if __name__ == '__main__':
        main()
