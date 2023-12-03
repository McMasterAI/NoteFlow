import spacy

def generate_title_from_bullet_points(bullet_points):
    nlp = spacy.load("en_core_web_sm")

    text = " ".join(bullet_points)

    doc = nlp(text)

    relevant_tokens = [token.text for token in doc if token.pos_ in ['NOUN', 'ADJ']]

    title = " ".join(relevant_tokens)

    return title


bullet_points = [
    "The video explores opinions and agendas on nuclear power.",
    "The narrator shares a personal history, initially fearing it after Chernobyl but shifting concerns to other environmental issues.",
    "Focus is on evaluating nuclear power's environmental impact and its low carbon footprint compared to other sources.",
    "Acknowledged advantages include small land use, on-demand power generation, and relative safety.",
    "Drawbacks include non-renewability, high costs, and public fear of accidents.",
    "Alternative technologies like fast breeder reactors, molten salt reactors, thorium reactors, and small modular reactors are introduced.",
    "Economic viability of these alternatives is questioned.",
    "Concerns about nuclear waste disposal are dismissed.",
    "Conclusion expresses skepticism about the economic feasibility of nuclear power.",
    "Emphasizes the need for a market-driven approach, considering local conditions and renewable resources.",
    "The video's nuanced perspective underscores the multifaceted nature of the debate on whether nuclear power is green."
]

generated_title = generate_title_from_bullet_points(bullet_points)

print("Generated Title:", generated_title)