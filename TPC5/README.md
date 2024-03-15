## TPC5

Para a resolução do TPC5 é apresentada uma lista dos tokens do texto a ser processado, em conjunto com a sua POS e o seu Lemma. No caso de existirem entidades no texto, estas são priorizadas em relação ao token normal. 

- Por exemplo, no caso de aparecer "Ponte de Lima" no texto, exixtiriam 3 tokens: "Ponte", "de", "Lima". No entanto "Ponte de Lima" é reconhecida como entidade correspondente a uma localidade. Dessa forma, seria essa entidade que iria aparecer na lista dos resultados ao invés dos 3 tokens separados.

###### Exemplo Prático

```
# Texto a ser processado
text = "O Daniel e o André foram a Ponte de Lima a pé."
```

- Output

```
TOKEN    POS    LEMMA
=========================
O    DET    o
Daniel    PER    Daniel
e    CCONJ    e
o    DET    o
André    ORG    André
foram    AUX    ser
a    DET    o
Ponte de Lima    LOC    Ponte de Lima
a    ADP    a
pé    NOUN    pé
.    PUNCT    .
```
