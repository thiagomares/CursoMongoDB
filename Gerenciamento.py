# Fazendo o gerenciamento do banco de dados

from pymongo import MongoClient

db = MongoClient('localhost', 27017)
print(db.list_database_names()) # Com este método, podemos ver os bancos de dados existentes

# Coletando os dados do banco de dados
db = db["Estudo"] # Selecionando o banco de dados
print(db.list_collection_names()) # Com este método, podemos ver as coleções existentes
print(db.vendas.find()) # este método nos retorna um objeto do tipo cursor, que é um objeto iterável, então, para vermos os documentos, precisamos iterar sobre ele
for venda in db.vendas.find():
    print(venda)
    
# Lembrando sempre de uma questão que é a natureza de bancos de dados não relacionais, que é a natureza de documentos, então, ELES NÃO VÃO ESTAR DA MESMA FORMA, imbecil dos inferno, precisamos fazer a organização dos dados, como por exemplo, transformar os dados em um dataframe.

# e caso queiramos fazer uma query, podemos fazer da seguinte forma:
query = {"nome": "Thiago"}
for venda in db.vendas.find(query):
    print(f'Registros com o nome Thiago: {venda}')
    

