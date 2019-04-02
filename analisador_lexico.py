# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:26:38 2019

@author: luis
"""

#ANALISADOR LÉXICO

#Referenciando os arquivos
dict_file = 'dict_file.txt'
entrada_file = 'entrada_file.txt'

#Abertura do arquivo em leitura contendo os simbolos do diretório
with open(dict_file, mode='r') as arquivo:
    #Passando arquivo para uma lista linha por linha com o '\n'
    lista_dict = arquivo.readlines()
    new_lista_dict = []
    #For que percorre a lista linha por linha 
    for elemento in range(len(lista_dict)):
        #Cada linha tem o '\n' substituido por vazio, e a nova linha é salvo numa variável  
        aux = lista_dict[elemento].replace('\n', '')
        #A nova linha contendo apenas os comando é adicionada numa nova lista
        new_lista_dict.append(aux)

#Mesmo esquema anterior, porém para o arquivo de entrada 
with open(entrada_file, mode='r') as arquivo:
    lista_entrada = arquivo.readlines()
    new_lista_entrada = []
    for elemento in range(len(lista_entrada)):
        aux = lista_entrada[elemento].replace('\n', '')
        new_lista_entrada.append(aux)
  
#Lista todos os comando contidos nos arquivos de entrada e diretório
print('\nLista de comandos da biblioteca: {0}'.format(new_lista_dict))
print('\nLista entradas passadas pelo usuário: {0}'.format(new_lista_entrada))


#transforma as listas em conjuntos
conjt_lista_dict = set(new_lista_dict)
conjt_lista_entrada = set(new_lista_entrada)


commum = conjt_lista_dict.intersection(conjt_lista_entrada)

for elemento in commum:
    print('O elemento {0} é comum a biblioteca'.format(elemento))


