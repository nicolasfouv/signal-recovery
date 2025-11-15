SOBRE O PROJETO<br>
Este projeto tem como objetivo principal avaliar técnicas e algoritmos eficientes para melhorar a reconstrução da energia fornecida pelo principal sistema de calorimetria hadrônica do experimento ATLAS no LHC (Large Hadron Collider). Atualmente, o programa de atualização do LHC e seus experimentos para alta luminosidade (HL-LHC) se encontram em andamento. A luminosidade é proporcional ao número de interações proton-proton por colisão, e quanto maior esta quantidade, mais sinais são gerados a cada colisão, aumentando assim a probabilidade de observação do efeito de empilhamento de sinais. Assim, a operação do HL-LHC irá impor um amplo programa de atualização da eletrônica de leitura do sistema de calorimetria, assim como aumentará consideravelmente o efeito de empilhamento no sistema de calorimetria do ATLAS. Desta forma, este plano de trabalho prevê visitar algoritmos otimização empregados, tanto para operação online quanto offline, a fim de se buscar aprimoramentos que se adequem ao novo modo de processamento online dos dados e que mitiguem o efeito de empilhamento de sinais o qual degrada a eficiência do método de reconstrução da energia.
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
