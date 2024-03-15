import spacy

nlp = spacy.load("pt_core_news_lg")

# Process whole documents
text = ('''O Daniel e o André foram a Ponte de Lima a pé.''')
doc = nlp(text)

tokens = [(str(token),token.pos_, token.lemma_) for token in doc]

# Analyze syntax
for entity in doc.ents:
    parts = str(entity).split(" ")
    index = 0
    for i , (token,_,_) in enumerate(tokens):
        if token == parts[0]:
            index = i

    for i in range(0,len(parts)-1):
        tokens.pop(index)
    tokens[index] = (entity, entity.label_, entity.lemma_)
    
print("TOKEN    POS    LEMMA\n=========================")
for token in tokens:
    print(f"{token[0]}    {token[1]}    {token[2]}")
