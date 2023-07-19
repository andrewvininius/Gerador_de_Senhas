
# Gerador de Senhas

Este é um programa simples em Python que gera senhas aleatórias com base no comprimento e nos caracteres permitidos escolhidos pelo usuário.

## Requisitos

- Python 3.x

## Uso

1. Execute o código Python em um ambiente que tenha o Python instalado.

2. O programa solicitará ao usuário que insira o comprimento desejado para a senha.

3. Em seguida, o programa solicitará que o usuário insira os caracteres permitidos para a senha. Se o campo for deixado em branco, o programa usará uma combinação padrão de letras (maiúsculas e minúsculas), dígitos e pontuação.

4. Após receber as informações do usuário, o programa irá gerar uma senha aleatória.

5. A senha gerada será exibida na saída do programa.

6. O programa continuará solicitando ao usuário o comprimento e os caracteres permitidos para gerar senhas adicionais, até que seja interrompido pelo usuário.

## Funções

### gerar_senha(comprimento, caracteres)

Esta função recebe o comprimento desejado da senha e uma string contendo os caracteres permitidos. Ela usa a biblioteca `random` do Python para escolher aleatoriamente os caracteres e retorna a senha gerada.

### main()

A função principal do programa. Ela solicita ao usuário o comprimento e os caracteres permitidos para a senha, chama a função `gerar_senha` e exibe a senha gerada na saída.

## Exemplo de Uso

Neste exemplo, o usuário solicitou uma senha com comprimento 10 e os caracteres permitidos foram definidos como "ABC123". A senha gerada foi "B2B3A12A1C".

Você pode executar o programa quantas vezes desejar para gerar senhas diferentes com comprimentos e caracteres permitidos variados.

Lembre-se de armazenar suas senhas geradas em um local seguro e utilizar senhas fortes para aumentar a segurança de suas contas online.






