# DADOS - Questão 3

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")
![texto](https://img.shields.io/static/v1?label=ambiente&message=conda&color=orange&style=flat-square "ambiente")
![texto](https://img.shields.io/badge/Questões-Completas-lightblack "plataforma")
![texto](https://img.shields.io/badge/plataforma-wsl2--linux-lightgrey "plataforma")



1. [Descrição do projeto](#descrição-do-projeto)  
2. [Funcionalidades](#funcionalidades)   
4. [Pré-requisitos](#pré-requisitos)  
5. [Como instalar](#como-instalar)
6. [Execução](#execucao)
7. [Desenvolvimento](#desenvolvimento)
8. [Questão original](#questão-original)


## :scroll: Descrição do projeto

Códigos para trabalhar chuva observada de satélite e manipular através de shapefiles

## :sparkles: Funcionalidades

:wrench: Baixa arquivo MERGE  
:wrench: Recorta chuva com base em contorno .shp   
:wrench: converte .grib em netcdf   

## :warning: Pré-requisitos

- [Python + conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (obrigatório)
- Ter ambiente linux ou wsl2, preferencialmente Ubuntu

## :cd: Como instalar

```bash
# 1. entre na pasta do projeto
cd respostas-dados/q3

# 2. instale/reproduza o ambiente
conda env create -f env.yaml

# 3. ative o ambiente
conda activate dados-q3

# 4. instale as dependências do linux
!apt-get update
!apt-get install cdo
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

# Dados - Q3

Colete uma hora de dados (um arquivo) MERGE. Os arquivos podem ser encontrados no [FTP do CPTEC](http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/2021/09/).

- Converta o arquivo GRIB2 para NC (0.5 pt).
- Recorte a área total da bacia do rio Tietê e salve o resultado em um novo NC (1 pt).
  - nota: utilize o shapefile disponibilizado.
- Reduza a resolução dos dados para metade da resolução original e salve o resultado em um novo NC (1.5 pt).
  - nota: crie uma grade mais grosseira.
- Crie uma listagem de todos os pontos de grade (do arquivo original) dentro da bacia do rio Tietê e salve a listagem em uma tabela (1 pt).
