## TPC6

Calculadora da frequência da combinação de dois nomes numa determinada frase.

#### Implementação

- Primeiramente o input recebido é processado frase a frase, com a deteção e respetivo merge das entidades na lista de tokens, através da funcionalidade ```add_pipe("merge_entities")``` disponibilizada pelo Spacy.

- A deteção dos nomes é efetuada através do tipo da entidade, que terá de corresponder a **PER**, e o seu POS terá de ser ser **PROPN**.

###### Excerto de Output


```
----------------------------------------
George Weasley
    Fred: 6 
    Marcus Flint: 1 
    Wood: 1 
    Katie Bell: 1 
    Gryffindor: 2 
    Slytherin: 1 
    Adrian Pucey: 1 
    Hufflepuff: 1 
----------------------------------------
Draco Malfoy
    Dudley: 1 
    Neville: 2 
    Hermione: 1 
----------------------------------------        

```