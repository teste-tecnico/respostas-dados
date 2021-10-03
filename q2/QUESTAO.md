# DADOS - Questão 2

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")
![texto](https://img.shields.io/static/v1?label=ambiente&message=conda&color=orange&style=flat-square "ambiente")
![texto](https://img.shields.io/badge/Questões-Completas-lightblack "status")
![texto](https://img.shields.io/badge/plataforma-wsl2--linux-lightgrey "plataforma")



1. [Descrição do projeto](#descrição-do-projeto)  
2. [Funcionalidades](#funcionalidades)   
4. [Pré-requisitos](#pré-requisitos)  
5. [Como instalar](#como-instalar)
6. [Execução](#execucao)
7. [Desenvolvimento](#desenvolvimento)
8. [Questão original](#questão-original)


## :scroll: Descrição do projeto

Leitura de arquivo txt e geração de saída em um formato padrão.

## :sparkles: Funcionalidades

:wrench: Ler arquivo tabular em formato txt   
:wrench: Fazer tratamento dos dados  
:wrench: Gerar string com os dados formatados   

## :warning: Pré-requisitos

- [Python + conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (obrigatório)

## :cd: Como instalar

```bash
# 1. entre na pasta do projeto
cd respostas-dados/q2

# 2. instale/reproduza o ambiente
conda env create -f env.yaml

# 3. ative o ambiente
conda activate dados-q2
```

## :arrow_forward: Execução

Use o comando para abrir a idle no notebook:
```bash
jupyter lab ou jupyter-lab
```
Execute o script main.ipynb para reproduzir o passo-a-passo da solução

## :construction: Desenvolvimento

:dart: Finalizado

## Questão original

# Dados - Q2

valor: 1.5 pt.

Leia o arquivo ```DP.txt```, onde:

- ss = subsistema, sendo:
  - 1 = seco
  - 2 = s
  - 3 = ne
  - 4 = n
  - 11 = imperatriz
- di = dia
- hi = hora
- m = meiahora (bool)
- df = desconsidere
- hf = desconsidere
- m (segunda) = desconsidere
- Demanda = demanda energética

e ajuste a estrutura de dados para o seguinte modelo (ao invés de ISODate, use datetime):

```json
{
    "subsistema" : "seco",
    "data_partida" : ISODate("2021-09-25T00:00:00.000Z"),
    "valores" : [ 
        {
            "demanda" : 36712.0,
            "data" : ISODate("2021-09-26T00:00:00.000Z")
        }, 
        {
            "demanda" : 35628.0,
            "data" : ISODate("2021-09-26T00:30:00.000Z")
        }, 
        {...}
    ]
}
```

Onde:

- subsistema: subsistema avaliado.
- data_partida: data de partida da previsão.
- valores: Lista de previsões com a data prevista.

Nota: no primeiro dia, a previsão acontece de meia em meia hora. A partir do segundo dia previsto, a previsão não possui uma frequência fixa.
