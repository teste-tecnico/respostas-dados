# Dados - Q3

Colete uma hora de dados (um arquivo) MERGE. Os arquivos podem ser encontrados no [FTP do CPTEC](http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/2021/09/).

- Converta o arquivo GRIB2 para NC (0.5 pt).
- Recorte a área total da bacia do rio Tietê e salve o resultado em um novo NC (1 pt).
  - nota: utilize o shapefile disponibilizado.
- Reduza a resolução dos dados para metade da resolução original e salve o resultado em um novo NC (1.5 pt).
  - nota: crie uma grade mais grosseira.
- Crie uma listagem de todos os pontos de grade (do arquivo original) dentro da bacia do rio Tietê e salve a listagem em uma tabela (1 pt).
