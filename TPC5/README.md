## TPC5

Para a resolução do TPC5 é apresentada uma lista dos tokens do texto a ser processado, em conjunto com a sua POS e o seu Lemma. No caso de existirem entidades no texto, ocorre um merge com os tokens correspondentes e a sua Label é também exibida. 

```
## TOKEN  POS  LEMMA (LABEL)
```

- Por exemplo, no caso de aparecer "Ponte de Lima" no texto, exixtiriam 3 tokens: "Ponte", "de", "Lima". No entanto "Ponte de Lima" é reconhecida como entidade correspondente a uma localidade. Dessa forma, seria essa entidade que iria aparecer na lista dos resultados ao invés dos 3 tokens separados.

###### Exemplo Prático

```
# Texto a ser processado
text = "O Daniel e o André foram a Ponte de Lima a pé."
```

- Output

```
O                 DET        o                 
Daniel            PROPN      Daniel            PER
e                 CCONJ      e                 
o                 DET        o                 
André             PROPN      André             ORG
foram             AUX        ser               
a                 DET        o                 
Ponte de Lima     PROPN      Ponte de Lima     LOC
a                 ADP        a                 
pé                NOUN       pé                
.                 PUNCT      .                 

```