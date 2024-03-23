import spacy

nlp = spacy.load("pt_core_news_lg")
nlp.add_pipe("merge_entities")

text = ('''O Daniel e o André foram a Ponte de Lima a pé.''')
doc = nlp(text)


## TOKEN  POS  LEMMA (LABEL)
for token in doc:
    if token.ent_type_:
        label = token.ent_type_
    else:
        label = ""
    print(f"{str(token):<17} {token.pos_:<10} {token.lemma_:<17} {label}")
