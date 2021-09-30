# DADOS - Questão 1

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")
![texto](https://img.shields.io/static/v1?label=ambiente&message=conda&color=orange&style=flat-square "ambiente")
![texto](https://img.shields.io/badge/completo-sem--extras-lightblack "plataforma")
![texto](https://img.shields.io/badge/plataforma-wsl2--linux-lightgrey "plataforma")



1. [Descrição do projeto](#descrição-do-projeto)  
2. [Funcionalidades](#funcionalidades)   
4. [Pré-requisitos](#pré-requisitos)  
5. [Como instalar](#como-instalar)
6. [Execução](#execucao)
7. [Desenvolvimento](#desenvolvimento)
8. [Questão original](#questão-original)


## :scroll: Descrição do projeto

Módulos para consumir API da ANA, parsear dados e plotar

## :sparkles: Funcionalidades

:wrench: Requisita estações  
:wrench: Baixa série de dados de determinada estação   
:wrench: plota 2 séries   

## :warning: Pré-requisitos

- [Python + conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (obrigatório)


## :cd: Como instalar

```bash
# 1. entre na pasta do projeto
cd respostas-dados/q1

# 3. instale/reproduza o ambiente
conda env create -f env.yaml
```

## :arrow_forward: Execução

Use o comando para abrir a idle no notebook:
```bash
jupyterlab
```
Execute o script main.ipynb para reproduzir o passo-a-passo da solução

## :construction: Desenvolvimento

:dart: Finalizar exercícios extras


## Questão original
### Dados - Q1

Consuma os dados da API do Instituto Nacional de Meteorologia (INMET).

Acesse a [documentação da API](https://portal.inmet.gov.br/manual/manual-de-uso-da-api-esta%C3%A7%C3%B5es).

Obtenha (1 pt todos):

- a lista de estações automáticas.
- uma série de 14 dias contendo todas as variáveis da uma estação qualquer.

Consolide (1 pt todos):

- a lista das estações automáticas em um dataframe.
- a série de 14 dias de dados em um dataframe.

Extras:

- use requisições assíncronas ou threadding para coletar dados de 15 estações (1 pt).
- há falhas nos dados? Crie uma forma de verificar (0.5 pt).
- há valores espúrios? Crie uma forma de verificar (0.5 pt).
- gere um gráfico de alguma variável contendo séries de duas estações (1 pt).
  - Nota: use matplotlib, plotly, altair ou qualquer outra biblioteca que você conheça (1 pt).
