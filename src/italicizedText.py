import spacy

def italicize_entities(text):

    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)

    # Iterate over the entities
    offset = 0
    for ent in doc.ents:
        # Check if the entity is a name, place, book, or movie
        if ent.label_ in ["PERSON", "GPE", "FAC", "ORG", "PRODUCT", "WORK_OF_ART"]:
            # Italicize the entity
            start, end = ent.start_char + offset, ent.end_char + offset
            italicized_entity = f"<i>{ent.text}</i>"
            text = text[:start] + italicized_entity + text[end:]
            offset += len(italicized_entity) - len(ent.text)

    return text


class_notes = """ In yesterday's literature class, we discussed several classics. Our teacher, Mrs. Johnson, emphasized the influence of 'To Kill a Mockingbird' by Harper Lee. She compared it with 'Pride and Prejudice' written by Jane Austen. We also examined the cultural impact of movies like 'The Godfather' directed by Francis Ford Coppola and 'Schindler's List' by Steven Spielberg.

During history class, Mr. Smith took us through the events of the French Revolution, highlighting the significance of the Storming of the Bastille. He mentioned Napoleon Bonaparte's role and how it influenced European politics. Our discussion included the ancient city of Rome and its architectural marvels like the Colosseum.

In geography, we explored the diverse landscapes of Canada, ranging from the Rocky Mountains to the Great Lakes. We compared it to the geography of Australia, focusing on the Great Barrier Reef and the Outback.

Finally, in our science session, Dr. Emily Clark introduced us to the groundbreaking book 'A Brief History of Time' by Stephen Hawking. She explained Hawking's theories on black holes and the Big Bang. We also discussed the Mars Rover missions by NASA and the latest SpaceX endeavors by Elon Musk.
"""
italicized_notes = italicize_entities(class_notes)
print(italicized_notes)
