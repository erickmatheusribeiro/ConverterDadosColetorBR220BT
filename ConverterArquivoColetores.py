#Author: Erick Matheus Ribeiro
#Script para conversão de arquivos do coletor br-220bt
#Para ser processado junto ao sistema A7Pharma
#Seleciona o arquivo a ser importado
filename = input('informe o caminho do arquivo a ser convertido. Exemplo: /home/alpha7/ConverterColetor/teste.txt: ')
#Abre o arquivo indicado
linhas=[]
with open(filename,'r') as file:
#Converte as linhas do arquivo em uma lista
    for linha in file:
        linhas.append(linha.rstrip())
conteudo={}
#Converte as linhas em dicionários, agrupando os valores
#e somando as quantidades de registros
for linha in linhas:
    if linha in conteudo:
        conteudo[linha] += 1
    else:
        conteudo[linha] = 1
#Seleciona o diretório onde o arquivo será salvo
filename = input('Informe o diretório do qual será importado o arquivo. Exemplo: /home/alpha7/ConverterColetor/: ') + 'LayoutAeP.txt'
with open(filename,'w') as file:
#Escreve o arquivo convertido
    for linha in conteudo:
        file.write(f'{int(linha):013}{conteudo[linha]:07}\n')
