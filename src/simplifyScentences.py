import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_trf")
doc = nlp("Thus, Apple is planning on building a new office in Toronto for 13 million U.S. Dollars.")
displacy.serve(doc, style="dep")

output_list = []
del_num = 0

for index, token in enumerate(doc):
    if (token.pos_ == "CCONJ") or (token.pos_ == "AUX") or (token.pos_ == "PRON") or (token.pos_ == "PROPN") or (token.pos_ == "ADV") or (token.text == "The") or (token.text == "the"):
        print("Removed: ", token.text)
        del_num += 1
    elif (token.text == ","):
        print("Removed: ", token.text)
        del_num += 1
        break
    else:
        break

for index, token in enumerate(doc):
    if (del_num <= index):
        output_list.append(token.text)

for item in output_list:
    print(item, end=' ')