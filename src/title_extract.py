import spacy
from transformers import T5Tokenizer, T5ForConditionalGeneration

nlp = spacy.load("en_core_web_sm")

def preprocess(bullet_points):
    preprocessed_points = []
    for point in bullet_points:
        # Process text using SpaCy
        doc = nlp(point)
        # Tokenize, remove stopwords and punctuation, and lowercase
        tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
        preprocessed_points.append(' '.join(tokens))
    return preprocessed_points


def generate_title_with_t5_base(bullet_points):
    # Combine preprocessed points into a single text
    prompt = "summarize: " + " ".join(bullet_points)

    # Initialize T5-Base
    model = T5ForConditionalGeneration.from_pretrained('t5-base')
    tokenizer = T5Tokenizer.from_pretrained('t5-base')

    # Encode and generate summary
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    summary_ids = model.generate(input_ids, max_length=60, num_return_sequences=1)

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Example usage
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
    "The video's nuanced perspective underscores the multifaceted nature of the debate on whether nuclear power is green.",
]


preprocessed_points = preprocess(bullet_points)
title = generate_title_with_t5_base(preprocessed_points)
print("Generated Title:", title)
