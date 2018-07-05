# Registros do Bolsa Família
Trabalho da disciplina Organização e Estrutura de Arquivos

Como rodar o programa:
OBS: deve existir um arquivo em formato csv com os registros do Bolsa Família com o nome "bolsaFamilia.csv" dentro da pasta do projeto
(O arquivo pode ser baixado em http://www.portaltransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos)

1 - Executar o script criaIndice.py.
O arquivo chamado "bolsaFamiliaHash.dat" será gerado contendo os índices em forma de Hash.

2 - Operações entre conjuntos realizadas (União e Interseção):

Para ser possivel a União e Interseção entre os arquivos, é necessário ter um outro arquivo chamado "bolsaInteresecao.dat"

2.1 - União:
Executar o script uniaoArquivos.py
Será gerado um arquivo chamado "uniaoArquivos.dat", com o equivalente a união dos dois arquivos csv.

2.2 - Interseção:
Executar intersecaoArquivos.py
Será gerado um arquivo chamado "bolsaInteresecao.dat", com a interseção dos dois arquivos csv.
