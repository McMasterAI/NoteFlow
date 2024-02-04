!pip install pytextrank

import spacy
import pytextrank
from spacy.tokens import Span
from spacy.lang.en.stop_words import STOP_WORDS

bold_phrases = []
custom_stop_words = []

with open("texts.txt") as file:
    text = file.read()

text = "spaCy is able to compare two objects, and make a prediction of how similar they are. Predicting similarity is useful for building recommendation systems or flagging duplicates. For example, you can suggest a user content that’s similar to what they’re currently looking at, or label a support ticket as a duplicate if it’s very similar to an already existing one."

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

for token in doc:
    if token.is_stop or token.pos_ in ["ADP", "PRON"]:
        custom_stop_words.append(token.text)

stop_words = set(custom_stop_words)
print(stop_words)

@spacy.registry.misc("stop_word_scrubber")
def stop_word_scrubber():
    def scrubber(span: Span) -> str:
        while len(span) > 0 and span[0].text in stop_words:
            span = span[1:]

        return span.text
    return scrubber

def identify_important_words():

    important_words = set()

    for ent in doc.ents:
        if ent.label_ != "DATE":
            important_words.add(ent.text)

    return list(important_words)

# Example usage:
italicized_phrases = identify_important_words()

nlp.add_pipe("textrank", config={"scrubber": {"@misc": "stop_word_scrubber"}})
doc = nlp(text)

for key_term in doc._.phrases:
    if key_term.rank > 0.06:
        bold_phrases.append(key_term.text)


print(bold_phrases)
print(italicized_phrases)
