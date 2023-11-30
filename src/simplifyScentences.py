import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_trf")
doc = nlp("The EU is the biggest non-miliary entity in the world!")
#displacy.serve(doc, style="dep")

output_list = []
del_num = 0

for index, token in enumerate(doc):
    if (token.pos_ == "CCONJ") or (token.pos_ == "AUX") or (token.pos_ == "PRON") or (token.pos_ == "PROPN") or (token.text == "The") or (token.text == "the"):
        print("Removed: ", token.text)
        del_num += 1
    else:
        break

for index, token in enumerate(doc):
    if (del_num <= index):
        output_list.append(token.text)

for item in output_list:
    print(item, end=' ')