SOBRE O PROJETO<br>
Este é um Projeto de Iniciação Científica. O projeto visa a aplicação de modelos de otmização para a reconstrução de sinal do calorímetro do Atlas Experiment no contexto do LHC.
<br><br>
SOBRE O ARQUIVO<br>
Introdução<br>
O arquivo do algoritmo implementado está armazenado em um ambiente virtual, assim, o protejendo de possiveis conflitos de versão com as bibliotecas utilizadas.
<br><br>
Algoritmo de Otimização<br>
O coração do dos arquivos é o "algorithm.ipynb", nele, está implementado todo o algoritmo de otimização seguindo os conceitos do livro [1].<br>
Houve uma mudança drástica no algoritmo utilizado, ao invés de utilizar a biblioteca SciPy, optou-se por implementar o método para que se possa atribuir modificações a sua estrutura seguindo o artigo [2], assim, melhorando o desempenho do algoritmo.
<br><br>
Arquivos .csv<br>
Os arquivos do tipo csv são as bases de dados sintéticas geradas a partir do aquivo "synthetic-database.py". Essas base de dados são compostas por diversos registros de sinais, onde a "db-pileup-noise.csv" possui a inclusão de ruídos.
<br><br>
REFERÊNCIAS<br>
[1] Jorge Nocedal, Stephen J. Wright - Numerical Optimization<br>
[2] Fuchang Gao, Lixing Han - Implementing the Nelder-Mead simplex algorithm with adaptive parameters
