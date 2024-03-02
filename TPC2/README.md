## TPC2

- Mantêm-se as funcionalidades implementadas para o TPC1, no entanto com a possibilidade de serem realizadas em cadeia

```
# Apresenta o top 20 de palavras com maior número de ocorrências com case insensitive

word_freq -i -m 20 tests/Camilo-Amor_de_Perdicao.md
```

##### Nova funcionalidade

- -t : Apresentação das palavras mais relevantes no texto

Este cálculo é efetuado através da diferença relativa percentual do número de vezes que a palavra aparece no texto em relação ao valor médio.

O valor médio é calculado através de uma tabela de frequências da língua portuguesa extraída a partir de: https://www.linguateca.pt/acesso/tokens/formas.totalpt.txt
