import re

from textwrap import wrap

global i

# DICIONARIOS DINAMICOS

dict_regiao_origem = { }

dict_regiao_destino = { }

dict_cod_loggi = { }

dict_tipo_produto = { }

dict_codigo_de_barras = { }

dict_pacotes_destino_validos = { }

dict_vendedores = { }

dict_pacotes_invalidos = { }

dict_pacotes_validos = { }

dict_soma_regiao_destino = {
    "Centro-oeste": 0,
    "Nordeste": 0,
    "Norte": 0,
    "Sudeste": 0,
    "Sul": 0,
    "Invalido": 0
}

dict_pacote_regiao_sul = { }

dict_destino_por_tipo = { }


def main():
    i = 0
    pacotes = input("Digite o número de pacotes: ")
    while i < int(pacotes):
        codigo_de_barras = (input("Digite o código sem espaços: "))
        if (len(codigo_de_barras) != 15):
            key = "Pacote " + str(i)
            dict_pacotes_invalidos[key] = str(codigo_de_barras) + " - Tamanho do código de barras inválido"
        else:   
            key = "Pacote " + str(i)  
            dict_codigo_de_barras[key] = str(codigo_de_barras)
            codigo_de_barras_t = wrap(codigo_de_barras, 3)
            if (int(codigo_de_barras_t[3]) != 367):
                key = "Pacote " + str(i)
                verifica_regiao_de_origem(codigo_de_barras_t[0], codigo_de_barras, key)
                verifica_regiao_de_destino(codigo_de_barras_t[1], codigo_de_barras, key)
                dict_cod_loggi[key] = str(codigo_de_barras_t[2])
                verifica_tipo_produto(codigo_de_barras_t[4], codigo_de_barras, key)
            else: 
                key = "Pacote " + str(i)
                dict_pacotes_invalidos[key] = str(codigo_de_barras) + " - Vendedor com CNPJ inativo"
            if(dict_pacotes_invalidos.get(key) == None):
                contagem_produtos_regiao_destino(key)
                verifica_pacote_origem_sul_brinquedos(key)
                pacotes_regiao_destino_validos(key)
                pacotes_enviados_por_vendedor(codigo_de_barras_t[3])
                pacotes_por_destino_tipo(key)
                dict_pacotes_validos[key] = str(codigo_de_barras)
        i = i + 1
    impressao_das_questoes(i)
    

# IMPRESSAO DAS QUESTOES
def impressao_das_questoes(i):
    
    print("QUESTAO 1:")
    print_q1()
    print("\nQUESTAO 2:")
    print_q2()
    print("\nQUESTAO 3:")
    print_q3()
    print("\nQUESTAO 4:")
    print_q4()
    print("\nQUESTAO 5:")
    print_q5()
    print("\nQUESTAO 6:")
    print_q6()
    print("\nQUESTAO 7:")
    print_q7()
    print("\nQUESTAO 8:")
    print("Não processado")
    print("\nQUESTAO 9:")
    print("Não processado")
    print("\nQUESTAO 10:")
    print_q10()

def print_q1():
    for i in dict_soma_regiao_destino:
        print("Regiao de destino: ", i, " | Quantidade: ", dict_soma_regiao_destino[i])   

def print_q2():
    print("PACOTES INVALIDOS")   
    for i in dict_pacotes_invalidos:
        print(i, " - ", dict_pacotes_invalidos[i]) 
    print("PACOTES VALIDOS")   
    for i in dict_pacotes_validos:
        print(i, " - ", dict_pacotes_validos[i])    

def print_q3():
    for i in dict_pacote_regiao_sul:
        print(i, " - ", dict_soma_regiao_destino[i])    

def print_q4():
    for i in dict_pacotes_destino_validos:
        print(i, " - ", dict_pacotes_destino_validos[i])    

def print_q5():
    for i in dict_vendedores:
        print(i, " - ", dict_vendedores[i])     

def print_q6():
    for i in dict_destino_por_tipo:
        print(i, " - ", dict_destino_por_tipo[i])     

def print_q7():
    for i in dict_pacotes_destino_validos:
        print(dict_pacotes_destino_validos[i])
        if(dict_pacotes_destino_validos[i] == "Centro-oeste"):
            print(i, " - ", dict_pacotes_destino_validos[i]) 

def print_q10():
    for i in dict_pacotes_invalidos:
        print(i, " - ", dict_pacotes_invalidos[i])

# AUXILIAR QUESTAO 1
def contagem_produtos_regiao_destino(key):
    if(dict_regiao_destino[key] == "Centro-oeste"):
        dict_soma_regiao_destino["Centro-oeste"] = dict_soma_regiao_destino["Centro-oeste"] + 1
    if(dict_regiao_destino[key] == "Nordeste"):
        dict_soma_regiao_destino["Nordeste"] = dict_soma_regiao_destino["Nordeste"] + 1
    if(dict_regiao_destino[key] == "Norte"):
        dict_soma_regiao_destino["Norte"] = dict_soma_regiao_destino["Norte"] + 1
    if(dict_regiao_destino[key] == "Sudeste"):
        dict_soma_regiao_destino["Sudeste"] = dict_soma_regiao_destino["Sudeste"] + 1
    if(dict_regiao_destino[key] == "Sul"):
        dict_soma_regiao_destino["Sul"] = dict_soma_regiao_destino["Sul"] + 1
    if(dict_regiao_destino[key] == "Invalido"):
        dict_soma_regiao_destino["Invalido"] = dict_soma_regiao_destino["Invalido"] + 1

# AUXILIAR QUESTAO 3
def verifica_pacote_origem_sul_brinquedos(key):
    if (dict_regiao_origem[key] == "Sul"):
        if (dict_tipo_produto[key] == "Brinquedos"):
            dict_pacote_regiao_sul[key] = dict_codigo_de_barras[key]

# AUXILIAR QUESTAO 4
def pacotes_regiao_destino_validos(key):
    if (dict_regiao_destino[key] != "Invalido"):
        dict_pacotes_destino_validos[key] = dict_regiao_destino[key]

# AUXILIAR QUESTAO 5
def pacotes_enviados_por_vendedor(key):
    if key != "367":
        dict_vendedores[key] = dict_vendedores.get(key, 0) + 1

# AUXILIAR QUESTAO 6
def pacotes_por_destino_tipo(key):
    if (dict_tipo_produto[key] != "Invalido"):
        dict_destino_por_tipo[key] = dict_pacotes_destino_validos[key] + " - " + dict_tipo_produto[key]

def verifica_regiao_de_origem(cod_origem, codigo_de_barras, key):
    if (int(cod_origem) >= 201 and int(cod_origem) <= 299):
        dict_regiao_origem[key] = "Centro-oeste"
    elif (int(cod_origem) >= 300 and int(cod_origem) <= 399):
        dict_regiao_origem[key] = "Nordeste"
    elif (int(cod_origem) >= 400 and int(cod_origem) <= 499):
        dict_regiao_origem[key] = "Norte"
    elif (int(cod_origem) >= 1 and int(cod_origem) <= 99):
        dict_regiao_origem[key] = "Sudeste"
    elif (int(cod_origem) >= 100 and int(cod_origem) <= 199):
        dict_regiao_origem[key] = "Sul"
    else:
        dict_regiao_origem[key] = "Invalido"
        dict_pacotes_invalidos[key] = str(codigo_de_barras) + " - Região de origem inválida"

def verifica_regiao_de_destino(cod_destino, codigo_de_barras, key):
    if (int(cod_destino) >= 201 and int(cod_destino) <= 299):
        dict_regiao_destino[key] = "Centro-oeste"
    elif (int(cod_destino) >= 300 and int(cod_destino) <= 399):
        dict_regiao_destino[key] = "Nordeste"
    elif (int(cod_destino) >= 400 and int(cod_destino) <= 499):
        dict_regiao_destino[key] = "Norte"
    elif (int(cod_destino) >= 1 and int(cod_destino) <= 99):
        dict_regiao_destino[key] = "Sudeste"
    elif (int(cod_destino) >= 100 and int(cod_destino) <= 199):
        dict_regiao_destino[key] = "Sul"
    else:
        dict_regiao_destino[key] = "Invalido"
        dict_pacotes_invalidos[key] = str(codigo_de_barras)+ " - Região de destino inválida"

def verifica_tipo_produto(cod_produto, codigo_de_barras, key):
    if (int(cod_produto) == 1):
        dict_tipo_produto[key] = "Joias"
    elif (int(cod_produto) == 111):
        dict_tipo_produto[key] = "Livros"
    elif (int(cod_produto) == 333):
        dict_tipo_produto[key] = "Electronicos"
    elif (int(cod_produto) == 555):
        dict_tipo_produto[key] = "Bebidas"
    elif (int(cod_produto) == 888):
        dict_tipo_produto[key] = "Brinquedos"
    else:
        dict_tipo_produto[key] = "Invalido"
        dict_pacotes_invalidos[key] = str(codigo_de_barras) + " - Tipo de produto inválido"

if __name__ == "__main__":
    
    main()