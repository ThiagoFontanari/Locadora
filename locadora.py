import csv
import datetime

#Cadastro dos clientes
def cadastra_cliente():
  nome = input("Insira o nome do cliente:")
  cpf = input("Insira o CPF do cliente:")
  rg = input("Insira o RG do cliente:")
  with open('clientes.csv', 'a') as arquivo:
    cadastra = csv.writer(arquivo, delimiter=";")
    cadastra.writerow([nome, rg, cpf])
    print("Cliente cadastrado com sucesso!")
    arquivo.close()

#Cadastro dos filmes
def cadastra_filmes():
  tipo = input("Insira o tipo de produto (DVD/VHS):")
  codigo = input("Insira o codigo do produto:")
  titulo = input("Insira o título do filme:")
  ano = input("Insira o ano de lançamento:")
  with open('filmes.csv', 'a') as arq:
    cad = csv.writer(arq, delimiter=";")
    cad.writerow([codigo, tipo, titulo, ano])
    print("Filme inserido com sucesso no sistema!")
    arq.close()

#Empréstimo de filmes
def emprestimo():
  usuario = input("Qual o nome do usúário que está alugando?")
  cpf = input("Digite o CPF do cliente:")
  tituulo = input("Digite o título do filme alugado:")
  item = input("Qual o código do item alugado?")
  data = datetime.date.today()
  with open('emprestimos.csv', 'a') as arqv:
    empr = csv.writer(arqv, delimiter=";")
    empr.writerow([usuario, item, data])
    print("Empréstimo registrado com sucesso!")
    arqv.close()

#Geração de relatório
def relatorio():

# Bloco onde serão armazenadas as informações obtidas a partir da leitura dos arquivos e tratamento dos dados

  hoje = datetime.date.today()
  cliente_em_atraso = []
  dias_de_atraso = []
  data_do_atrasado = []
  cpf_atrasado = []
  codigo_atrasado = []
  titulo_atrasado = []
  situacao = ["ATRASADO"]

# Bloco que verifica os empréstimos realizados que estão em atraso e insere as informações nas listas acima para retorno do relatório

  with open('emprestimos.csv', 'r') as rel:
    leitor = csv.reader(rel)
    next(leitor)
    for linha in rel:      
      data_do_emprestimo = linha.split(";")[2].strip("\n")
      emprestou_em = datetime.datetime.strptime(data_do_emprestimo, "%Y-%m-%d").date()
      atraso = hoje - emprestou_em
      if int(abs(atraso.days)) > 7:
        cliente_em_atraso.append(linha.strip("\n").split(";")[0])
        dias_de_atraso.append(int(abs(atraso.days)))
        data_do_atrasado.append(linha.strip("\n").split(";")[2])
        codigo_atrasado.append(linha.strip("\n").split(";")[1])
        with open('clientes.csv', 'r') as cli:
            leitor = csv.reader(cli)
            next(leitor)
            for linha in cli:
              if linha.strip("\n").split(";")[0] in cliente_em_atraso:
                cpf_atrasado.append(linha.strip("\n").split(";")[2])
        with open('filmes.csv', 'r') as fil:
            leitor = csv.reader(fil)
            next(leitor)
            for linha in fil:
              if linha.strip("\n").split(";")[0] in codigo_atrasado:
                titulo_atrasado.append(linha.strip("\n").split(";")[2])
              else:
                pass
        cli.close()
        fil.close()
    rel.close()
   
# Retorno dos dados dos empréstimos em atraso
    if len(cliente_em_atraso) > 0:
        print("     CPF  ", "     NOME  ", "    TÍTULO  ", "   EMPRÉSTIMO  ", " SITUAÇÃO  ", "DIAS  ")
        for item in cpf_atrasado, cliente_em_atraso, titulo_atrasado, data_do_atrasado, situacao, dias_de_atraso:
          print(str(item), end=" ")
    else:
      print("Não existem empréstimos em atraso!")
