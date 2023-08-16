"""
CREATE
READ
UPDATE
DELETE

# CRUD
# comando=''
# cursor.execute(comando)
# conexao.commit() # Edita o banco de dados. CUD
# resultado=cursor.fetchall # Ler o banco de dados . R

"""

import os
import sys
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
user: str = os.environ["USER"]
password: str = os.environ['PASSWORD']
database: str = os.environ['DATABASE']


def check_params(params: list) -> str:
    if len(params) != 2 or params[1] not in ['-c', '-r', '-u', '-d']:
        raise Exception("Erro na chamada do arquivo", main.__doc__)
    return params[1]


def main() -> None:
    """
    -c --> Criar documento;
    -r --> Ler a tabela;
    -u --> Atualizar o documento;
    -d --> Deletar documento;


    """
    param: str = check_params(sys.argv)

    try:
        # 4 parâmetros para a conexão
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="crud-python"

        )

        cursor = conexao.cursor()
        nome_produto: str
        valor_produto: int
        match param:
            case "-c":
                nome_produto = input("Digite o nome do produto: ")
                valor_produto = int(input("Digite o valor do produto: "))
                comando = f'INSERT INTO {database} (nome_produto, valor) VALUES ("{nome_produto}", "{valor_produto}")'
                cursor.execute(comando)
                conexao.commit()
            case "-r":
                comando = f'SELECT * FROM {database}'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print(resultado)
            case "-u":
                nome_produto = input(
                    "Digite o nome do produto que você deseja alterar: ")
                valor_produto = int(
                    input("Digite o novo valor do produto: "))
                comando = f'UPDATE {database} SET valor={valor_produto} WHERE nome_produto="{nome_produto}"'
                cursor.execute(comando)
                conexao.commit()
            case "-d":
                nome_produto = input(
                    "Digite o nome do produto que você deseja deletar: ")
                comando = f'DELETE FROM {database} WHERE nome_produto="{nome_produto}"'
                cursor.execute(comando)
                conexao.commit()
            case _:
                print("Algum erro inesperado aconteceu")
        cursor.close()
        conexao.close()
    except:
        print("Algum erro inesperado aconteceu")


if __name__ == "__main__":
    main()
