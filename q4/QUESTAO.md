# DADOS - Questão 4

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

Coleta temperatura das regiões do Niño 1+2, Niño 3.4 e confluência brasil malvinas

## :sparkles: Funcionalidades

:wrench: Baixa arquivo de TSM  
:wrench: Recorta os dados nas áreas de interesse e calcula média  
:wrench: gera csv   

## :warning: Pré-requisitos

- [Python + conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (obrigatório)

## :cd: Como instalar

```bash
# 1. entre na pasta do projeto
cd respostas-dados/q4

# 2. instale/reproduza o ambiente
conda env create -f env.yaml

# 3. ative o ambiente
conda activate dados-q4
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

# Dados - Q3 (que na verdade é a Q4)

Obtenha um dia de dados de temperatura de superfície oceânica OISST.

Dados disponíveis em:
https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/202109/

Calcule (1 pt cada):

- Valor da temperatura para regiões do Niño 1+2 e 3.4
  - Considere a delimitação da área segundo [Trenberth (2020)](https://climatedataguide.ucar.edu/climate-data/nino-sst-indices-nino-12-3-34-4-oni-and-tni)
- Valor da temperatura para a confluência Brasil-Malvinas
  - Considere a delimitação da área segundo [Cataldi et al (2011)](https://www.scielo.br/j/rbmet/a/TmNk6J3bcqGC85hvgfPzkJj/?lang=pt)

Salve os valores em um arquivo CSV.
