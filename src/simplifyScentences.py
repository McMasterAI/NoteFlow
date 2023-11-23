import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_trf")
doc = nlp("This is a particularly tricky idea, Python only has Non-static variable. Static variables belong to the class, and is inherited by each object (This is good for things that are ubiquitous within all objects of a class). Static variables can still be used like non-static, to display specific information about a object, but the problem arises if you try and call them through the class, when there is no specific information available. This is where non-static comes in, since non-static cannot be called through the class, this problem goes away. Non-static is good for information that is specific to each class (non-ubiquitous)")


for token in doc:
    #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #        token.shape_, token.is_alpha, token.is_stop)
    if (token.pos_ != "AUX"):
        print(token.text, end=" ")