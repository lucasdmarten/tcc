<h1 align=center>Projeto Trabalho de Conclusão de Curso (Resumo):</h1>


<h2>Objetivos</h2>

<p>Este trabalho propõe uma avaliação das condições do modelo regional Weather Research and Forecast (WRF) (Skamarok, 2019), para previsões probabilísticas de curto e médio prazo do vento, principalmente a uma altura de 106 metros da superfície. Porém, além da velocidade e direção do vento nesta altura, também são comparadas variáveis em superfície como temperatura, pressão e umidade relativa do ar usando os dados das estações do Instituto Nacional de Meteorologia (INMET). Com os resultados avalia-se o desempenho do modelo em diversos aspectos, como por exemplo:</p>

    • Análise da direção e velocidade do vento a 106m de altura e também variáveis em superfície;
    • Avaliar opções de parametrização da Camada Limite Planetária e Camada Superfícial para a região estudo;
    • Avaliar o desempenho da previsão probabilística;



<h2>Domínio</h2>
<p>Configurado com uma resolução de 15km, a cobertura do domínio é centrado no complexo eólico do Cerro Chato, município de Santana do Livramento, RS - Brasil.</p>
<img align=center src="https://github.com/lucasdmarten/tcc/blob/master/tcc/imgs/dominio/projection.jpg?raw=true">

<br>
<br>

<h2>Dados usados na comparação:</h2>

<p>Os dados utilizados para calcular o erro do modelo foram coletados em um anemometro a 106 metros de altura. Abaixo cada boxplot representa um período.</p>
<p> Primeiro caso começa 23/05/2018 às 00:00:00 até dia 24/05/2018 às 23:50:00. E o segundo caso começa no dia 23/09/2018 às 00:00:00 até dia 25/09/2018 às 23:50:00 todos em horário UTC.</p>

<img align=center src="https://github.com/lucasdmarten/tcc/blob/master/img_resultados/boxplot_caso_1e2.png?raw=true">

<br>
<br>


<h2>Resultados preliminares:</h2>





<img align=center src="https://github.com/lucasdmarten/tcc/blob/master/img_resultados/painel_analise_ensemble.png?raw=true">

<img align=center src="https://github.com/lucasdmarten/tcc/blob/master/img_resultados/painel_analise_ensemble_caso2.png?raw=true">


<h2>Referências:</h2>
<br>

<p> Skamarock, W. C., J. B. Klemp, J. Dudhia, D. O. Gill, Z. Liu, J. Berner, W. Wang J. J. Powers, M. G. Duda, D. M. Baker, and X. -Y. Huang, 2019: A Description of the Advanced Research WRF Version 4. NCAR Tech. Note NCAR/TN-556+STR, 145 pp. </p>