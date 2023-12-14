from pymongo import MongoClient
import pandas as pd

client = MongoClient('localhost', 27017)

db = client["Estudo"] # aqui nos fazemos duas coisas ao mesmo tempo: criamos o banco de dados e o selecionamos, caso o banco de dados já exista, apenas o selecionamos

venda = {
    "vendedor": "João",
    "valor": 100.00,
    "data": "2021-01-01",
    "id_cliente": 1
}

# o que nos estamos fazendo aqui: selecionando o banco de dados, selecionando a coleção e inserindo um documento
db.vendas.insert_one(venda)

# e neste método, nos estamos selecionando o banco de dados, selecionando a coleção e inserindo vários documentos
print(db.vendas.find()) # este método nos retorna um objeto do tipo cursor, que é um objeto iterável, então, para vermos os documentos, precisamos iterar sobre ele
for venda in db.vendas.find():
    print(venda)

df = pd.DataFrame(list(db.vendas.find()))
print(df)

client.close() # E feche sua conexão, seu tolete
 