#!pip install pytextrank

import spacy
import pytextrank
from spacy.tokens import Span
from spacy.lang.en.stop_words import STOP_WORDS
import re

def boldItalicize(text, bullet_points):
    # Determines keywords based on bullets in paragraph form , and applies them to the bullet points

    bold_phrases = []
    custom_stop_words = []

    # with open("texts.txt") as file:
    #     text = file.read()

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    for token in doc:
        if token.is_stop or token.pos_ in ["ADP", "PRON"]:
            custom_stop_words.append(token.text)

    stop_words = set(custom_stop_words)

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


    # Adding "**" & "*" around words based on "bold_phrases" and "italized_phrases"
    bold_phrases.sort(key=len, reverse=True)
    italicized_phrases.sort(key=len, reverse=True)

    for i in range(len(bullet_points)):
        for bold in bold_phrases:
            pattern = re.compile(r'\b' + re.escape(bold) + r'\b')
            bullet_points[i] = pattern.sub(f'**{bold}**', bullet_points[i])

        for italics in italicized_phrases:
            pattern = re.compile(r'\b' + re.escape(italics) + r'\b')
            bullet_points[i] = pattern.sub(f'*{italics}*', bullet_points[i])
    

    return bullet_points
