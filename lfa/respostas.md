Livro: GARCIA, A. de V.; HAEUSLER, E. H. Linguagens Formais e Autômatos. Londrina: EDA, 2017.

Respostas de alguns exercícios. As respostas foram avaliadas superficialmente e podem conter imprecisões.

## Exerc. 1, pág. 23

A alternativa correta é a d). Vamos analisar cada alternativa e explicar o porquê da 'd' ser a correta:

a) Esta alternativa é muito vaga. Dizer que ambos os conjuntos contêm elementos de A, B e C não é suficiente para provar a igualdade. Eles precisam conter exatamente os mesmos elementos.

b) Esta alternativa também é imprecisa. A frase "tem elementos de A e B ou de A e C" é confusa e não captura a lógica correta da distributividade.

c) Esta alternativa está quase correta, mas falta um passo crucial. Ela mostra que se x ∈ A ∪ (B ∩ C), então x ∈ (A ∪ B) ∩ (A ∪ C). No entanto, para provar a igualdade dos conjuntos, é necessário mostrar a implicação nos dois sentidos, ou seja, também mostrar que se x ∈ (A ∪ B) ∩ (A ∪ C), então x ∈ A ∪ (B ∩ C).

d) Esta alternativa apresenta a demonstração completa e correta. Vamos detalhá-la:

* x ∈ A ∪ (B ∩ C) equivale a x ∈ A ou x ∈ (B ∩ C): Esta é a definição de união.
* x ∈ B ∩ C equivale a dizer que x pertence a ambos, ou seja, tanto B quanto C: Esta é a definição de interseção.
* Juntando tudo, temos que x ∈ A ou x ∈ B e que x ∈ A ou x ∈ C: Substituindo a segunda equivalência na primeira, obtemos: x ∈ A ou (x ∈ B e x ∈ C). Pela distributividade da lógica, isso é equivalente a (x ∈ A ou x ∈ B) e (x ∈ A ou x ∈ C).
* x ∈ A ou x ∈ B e que x ∈ A ou x ∈ C equivale a x ∈ (A ∪ B) ∩ (A ∪ C): Esta é a definição de interseção e união aplicada ao contrário.
* Como x é arbitrário, então x ∈ A ∪ (B ∩ C) é equivalente a x ∈ (A ∪ B) ∩ (A ∪ C): Como x é um elemento genérico, a equivalência vale para todos os elementos, o que prova a igualdade dos conjuntos.

e) Esta alternativa comete um erro lógico na penúltima frase. Ela afirma "Com isso temos que x ∈ B e x ∈ C ou x ∈ A". Isso não é uma consequência lógica das afirmações anteriores. A implicação correta é (x ∈ A ou x ∈ B) e (x ∈ A ou x ∈ C), que é diferente de (x ∈ B e x ∈ C) ou x ∈ A.

Demonstração Formal Completa (como na alternativa d):

Para provar A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C), precisamos provar duas inclusões:

1. A ∪ (B ∩ C) ⊆ (A ∪ B) ∩ (A ∪ C):

    * Se x ∈ A ∪ (B ∩ C), então x ∈ A ou x ∈ (B ∩ C).
    
        * Se x ∈ A, então x ∈ (A ∪ B) e x ∈ (A ∪ C), logo x ∈ (A ∪ B) ∩ (A ∪ C).
        * Se x ∈ (B ∩ C), então x ∈ B e x ∈ C. Portanto, x ∈ (A ∪ B) e x ∈ (A ∪ C), logo x ∈ (A ∪ B) ∩ (A ∪ C).

    * Em ambos os casos, x ∈ (A ∪ B) ∩ (A ∪ C).

2. (A ∪ B) ∩ (A ∪ C) ⊆ A ∪ (B ∩ C):

    * Se x ∈ (A ∪ B) ∩ (A ∪ C), então x ∈ (A ∪ B) e x ∈ (A ∪ C).

    * Isso significa que (x ∈ A ou x ∈ B) e (x ∈ A ou x ∈ C).
    
        * Se x ∈ A, então x ∈ A ∪ (B ∩ C).
        * Se x ∉ A, então, como x ∈ (A ∪ B) e x ∈ (A ∪ C), devemos ter x ∈ B e x ∈ C. Portanto, x ∈ (B ∩ C), e consequentemente x ∈ A ∪ (B ∩ C).

    * Em ambos os casos, x ∈ A ∪ (B ∩ C).

Como provamos as duas inclusões, concluímos que A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C).

Portanto, a alternativa d) é a única que apresenta a argumentação lógica completa e correta para a demonstração da igualdade.


## Exerc. 2, pág. 24

Sejam A e B conjuntos.
Assinale a alternativa verdadeira:
a) A ⊄ A ∪ ( A ∩ A )
b) Para todo o conjunto C ( B ∩ C ) ⊆ ( A ∩ C )
c) A × ( B ∪ C ) ⊄ ( A × B ) ∪ ( A × C )
d) ∅ é uma relação de A para B .
e) Se A ⊊ B e B é finito, então existe uma função injetiva f : B → A .




<br><sub>Last edited: 2025-02-23 11:54:20</sub>
