# Arquiteturas Paralelas e Distribuídas

1º sem 2025

## Ementa

* FUNDAMENTOS DA PROGRAMAÇÃO PARALELA

    * Introdução à programação paralela e Distribuída
    * Conceitos básicos de concorrência
    * Taxonomia de arquiteturas paralelas: SISD, SIMD, MIMD e SPMD
    * Arquitetura de hardware para comunicação entre processadores: memória compartilhada

* FUNDAMENTOS DA PROGRAMAÇÃO PARALELA E DISTRIBUÍDA

    * Memória distribuída e hierarquia de memórias
    * Programação com variáveis compartilhadas
    * Programação de processos, sincronização e monitores
    * Programação distribuída: passagem de mensagens

* PARADIGMAS E FERRAMENTAS DA PROGRAMAÇÃO PARALELA E DISTRIBUÍDA

    * RPC e paradigmas de interação entre processos
    * Definição dos passos para a criação de um programa paralelo
    * Ferramentas para programação paralela: bibliotecas MPI
    * Ferramentas para programação paralela: OpenMP

* ANÁLISE DE DESEMPENHO E DEPURAÇÃO DE PROGRAMAS PARALELOS

    * Ferramentas para programação paralela: Pthreads
    * Compiladores paralelizadores e as linguagens Linda, Java e HPF
    * Análise de desempenho e depuração de programas paralelos
    * Exemplos de programas paralelos para aplicações específicas

## Referências

* CHARÃO, A. S. Análise de desempenho de programas paralelos. [S. l.: s. n.], 2011. Disponível em: https://www-usr.inf.ufsm.br/~andrea/elc139-2011a/slides-analise-desempenho-2011a.pdf.
* CHARÃO, A. S. Programação paralela. [S. l.: s. n.], 2015. Disponível em: https://www-usr.inf.ufsm.br/~andrea/elc139/slides-programacao-paralela-2015a.pdf.
* EDUARDO ALCHIERI. Monitores. [S. l.: s. n.], 2024. Disponível em: https://www.passeidireto.com/arquivo/43853936/slides-monitores.
* FERRAZ, C. Sistemas distribuídos. [S. l.]: UFPE, 2015. Disponível em: https://www.cin.ufpe.br/~cagf/if677/2015-2/slides/23-25_SD.pdf.
* GUIDI, G. Comunicação entre processos (RPC) - sistemas distribuídos. [S. l.]: PUCRS, 2015. Disponível em: https://www.inf.pucrs.br/~gustavo/disciplinas/ppd/material/slides-rpc-novo.pdf.
* LIMA, E. Memória Distribuída e Hierarquia de Memórias. [S. l.: s. n.], 2024. Disponível em: https://www.passeidireto.com/arquivo/70818251/u-2-s-1-slide.
* PRISCILA FACCIOLLI. Sincronismo e Comunicação entre Processos. [S. l.: s. n.], 2009.
* RODRIGO; RAFAEL TELLES; THIAGO; MATHEUS; WILLIAMS. Semáforos, monitores, troca de mensagens, deadlock. [S. l.]: SlideShare, 2015. Disponível em: https://www.slideshare.net/WilliamsGomesdaSilva/apresentao-semforos-monitores-troca-de-mensagens-deadlock.
* SARAIVA, P. H. Fundamentos da programação paralela. [S. l.]: Academia.edu, 2015. Disponível em: https://www.academia.edu/38639934/FUNDAMENTOS_DA_PROGRAMA%C3%87%C3%83O_PARALELA.
* SCHEPKE, C. Programação paralela em memória compartilhada e distribuída. [S. l.: s. n.], 2018. Disponível em: https://www.inf.ufrgs.br/erad2018/downloads/minicursos/eradrs2018-mpi-openmp-slides.pdf.
* SCHNORR, Lucas M. Análise de desempenho de programas paralelos. [S. l.: s. n.], 2014. Disponível em: https://www.inf.ufrgs.br/~schnorr/download/talks/erad2014-minicurso-slides.pdf.
* SCHNORR, Lucas Mello; GUIDI, G. Projetando e construindo programas paralelos. [S. l.]: SETREM, 2015. Disponível em: https://www.setrem.com.br/erad2019/data/pdf/minicursos/mc02.pdf.
* SIQUEIRA, F. Fundamentos de computação distribuída. [S. l.]: UFSC, 2015. Disponível em: https://www.inf.ufsc.br/~frank.siqueira/INE5418/1.Fundamentos-Slides.pdf.
* SOARES, M. G. OpenMP: Programação paralela. [S. l.]: UNICAMP, 2015. Disponível em: https://www.cenapad.unicamp.br/treinamentos/apostilas/apostila_openmp.pdf.
* SOBRAL, J. B. M. Apostila de introdução ao OpenMP. [S. l.: s. n.], 2017. Disponível em: https://www.inf.ufsc.br/~bosco.sobral/ensino/ine5645/Apostila_OpenMP_Bosco.pdf.
* SOBRAL, J. B. M. Programação paralela e distribuída. [S. l.]: UFSC, 2015. Disponível em: http://www.inf.ufsc.br/~bosco.sobral/ensino/ine5645/Unidade1_urian.pdf.
* TIAGO FERRETO. Programação Paralela. [S. l.: s. n.], 2006. Disponível em: https://www.inf.pucrs.br/~gustavo/disciplinas/ppd/material/Prog_Paralela.pdf.
* MATOS, R. Computação paralela. [S. l.: s. n.], 2024. Disponível em: https://www.comp.uems.br/~rubens/ppd/. Acesso em: 27 out. 2023.
* SETZER, V. W. Paralelismo com OpenMP. [S. l.: s. n.], 2024. Disponível em: https://www.ime.usp.br/~vwsetzer/mac0422/paralelismo-openmp.html. Acesso em: 27 out. 2023.
- SILVA, G. P. Arquiteturas paralelas. [S. l.: s. n.], 2024. Disponível em: https://dcc.ufrj.br/~gabriel/arqcomp2/ArqPar1.pdf. Acesso em: 27 out. 2023.
- SOUZA, J. N. de. Arquitetura de computadores e sistemas distribuídos. [S. l.: s. n.], 2024. Disponível em: http://www.di.ufpe.br/~jns/. Acesso em: 27 out. 2023.

## Artigos

* ANDREWS, G. R.; SCHNEIDER, F. B. Concepts and notations for concurrent programming. ACM Computing Surveys (CSUR), v. 15, n. 1, p. 3–43, 1983. DOI 10.1145/356913.356914. Disponível em: https://dl.acm.org/doi/10.1145/356913.356914.
* DUBOIS, M.; SCHEURICH, C.; BRIGGS, F. A. Memory access buffering in multiprocessors. ACM SIGARCH Computer Architecture News, v. 16, n. 1, p. 156–164, 1988. DOI 10.1145/37402.37416. Disponível em: https://dl.acm.org/doi/10.1145/37402.37416.
* FLYNN, M. J. Some computer organizations and their effectiveness. IEEE Transactions on computers, v. C–21, n. 9, p. 948–960, 1972. DOI 10.1109/TOC.1972.5009071. Disponível em: https://ieeexplore.ieee.org/document/1676752.
* HOARE, C. A. R. Communicating sequential processes. Communications of the ACM, v. 21, n. 8, p. 666–677, 1978. DOI 10.1145/359576.359585. Disponível em: https://dl.acm.org/doi/10.1145/359576.359585.
* STANKOVIC, J. A. Software architecture for distributed computer systems. IEEE Transactions on Software Engineering, n. 1, p. 2–21, 1982. Disponível em: https://ieeexplore.ieee.org/document/1700465.

## Videos

* ALVES FILHO, A. [MC-SD02-III] introdução à programação paralela e vetorial. [S. l.: s. n.], 2021. Disponível em: https://m.youtube.com/live/9HF_Dp9CF9A.
* CASTRO, M. Introdução à computação paralela. [S. l.: s. n.], 7 set. 2021. Disponível em: https://www.youtube.com/watch?v=aJ1NzRmbzmE.
* CASTRO, R. OpenMP - introdução a programação paralela em C/C++. [S. l.: s. n.], 20 maio 2020. Disponível em: https://www.youtube.com/watch?v=FjI7W0d_s_g.
* DE INFORMÁTICA - UFG, I. Computação paralela - MPI - parte 1. [S. l.: s. n.], 17 jun. 2011. Disponível em: https://www.youtube.com/watch?v=YfU3a8fQf5A.
* DO VALE DO RIO DOS SINOS - UNISINOS, U. Sistemas operacionais - aula 11 - sincronização: Variáveis compartilhadas. [S. l.: s. n.], 9 jun. 2014. Disponível em: https://www.youtube.com/watch?v=j9g_0v99-6E.
* ESTRELLA, J. C. Computação paralela e distribuída. [S. l.: s. n.], 4 out. 2022. Disponível em: https://www.youtube.com/watch?v=c5MlNQTjuX4.
* FILETO, R. Sistemas distribuídos - aula 07 - chamada de procedimento remoto (RPC). [S. l.: s. n.], 29 set. 2020. Disponível em: https://www.youtube.com/watch?v=k6_W99yH_4o.
* GUBI, L. A. D. MAC0431 - introdução à computação paralela e distribuída. [S. l.: s. n.], 11 nov. 2011. Disponível em: https://www.youtube.com/watch?v=-nrTVi-2x88.
* JULIO, E. H. Sistemas distribuídos - comunicação - parte 3 - passagem de mensagens. [S. l.: s. n.], 12 jun. 2013. Disponível em: https://www.youtube.com/watch?v=p4vW935aZ6E.
* NONATO, L. G. Introdução a programação paralela - parte 1. [S. l.: s. n.], 20 out. 2014. Disponível em: https://www.youtube.com/watch?v=z8v3r8x7iC8.
* PACHECO, P. S. An introduction to parallel programming - chapter 1. [S. l.: s. n.], 2020. Disponível em: https://www.youtube.com/watch?v=qN5jE7F9rgc.
* SILBERSCHATZ, P. B. G., Abraham; Galvin. Operating system concepts - chapter 6 - synchronization - monitors. [S. l.: s. n.], 2021. Disponível em: https://www.youtube.com/watch?v=n7-59f-YkG8.

## *Links* de interesse

* GUEDES, Dorgival. Fundamentos de Sistemas Paralelos e Distribuídos. UFMG. 
  * Programa da disciplina: https://homepages.dcc.ufmg.br/~dorgival/dokuwiki/doku.php?id=fundamentos_de_sistemas_paralelos_e_distribuidos
  * Vídeos: https://www.youtube.com/playlist?list=PL-blDbur9o_59jeRUU0f6NdL-l3H9EKXX


<br><sub>Last edited: 2025-02-23 11:18:07</sub>
