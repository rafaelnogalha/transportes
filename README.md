# O leitor de código de barras da Loggi
A Loggi está em constante expansão e precisa da sua ajuda para conectar o Brasil.
O processo de separação de pacotes acontece de modo automático, uma esteira
inteligente lê o código de barras dos pacotes e os agrupa pelas regiões de destino.
O código de barras do pacote é composto por 15 dígitos, onde cada trinca
numérica representa uma informação do pacote.

# A Loggi precisa:

- [x] Identificar a região de destino de cada pacote, com totalização de
pacotes (soma região);
- [x] Saber quais pacotes possuem códigos de barras válidos e/ou
inválidos;
- [x] Identificar os pacotes que têm como origem a região Sul e
Brinquedos em seu conteúdo;
- [x] Listar os pacotes agrupados por região de destino (Considere apenas
pacotes válidos);
- [x] Listar o número de pacotes enviados por cada vendedor (Considere
apenas pacotes válidos);
- [x] Gerar o relatório/lista de pacotes por destino e por tipo (Considere
apenas pacotes válidos);
- [x] Se o transporte dos pacotes para o Norte passa pela Região
Centro-Oeste, quais são os pacotes que devem ser despachados no
mesmo caminhão?
- [ ] Se todos os pacotes fossem uma fila qual seria a ordem de carga
para o Norte no caminhão para descarregar os pacotes da Região
Centro Oeste primeiro;
- [ ] No item acima considerar que as jóias fossem sempre as primeiras a
serem descarregadas;
- [x] Listar os pacotes inválidos.
Caso tenha dificuldade em algum item, pode ser pulado, mas deixe a saída como:
“Não processado”.
## Linguagem e Ferramenta de Programação
Python3 e Vscode

# Como executar o programa
Basta clonar o repositório e executar a seguinte linha de comando `python3 rafaelHenriqueNogalhaDeLima_desafio_engenharia.py` ou `python2 rafaelHenriqueNogalhaDeLima_desafio_engenharia.py`

# Observações importante
A resposta para cada uma das 10 questões, exceto a 8 e a 9, estão explícitas tanto no código como no *output*, por exemplo, a função que responde as questões tem o seguinte *template* `print_qn` tendo *n* variando de 1 a 10. Logo, o código está fácil de ser lido e compreendido.
A questao 8 e 9 nao foram feitas, pois o enunciado nao foi claro quanto ao que era necessario fazer. Ficou confuso.

# Ideia do algoritmo
O algoritmo consiste em basicamente dividir o código de barras em três partes,
e cada parte(origem, destino, codigo Loggi, codigo vendedor, tipo produto) 
sera verificada e armazenda em seus respectivos dicionarios. Depois e feita
funcoes para responder cada questao, seguindo a logico dos dicionarios
de conseguir o valor de sua respectiva chave.
