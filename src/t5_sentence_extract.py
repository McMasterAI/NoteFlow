from transformers import T5ForConditionalGeneration, T5Tokenizer
import spacy

nlp = spacy.load("en_core_web_sm")

def generate_summary(text, model, tokenizer):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=8192, truncation=True)
    summary_ids = model.generate(inputs, max_length=1024, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def to_bullet_points(summary):
    sentences = summary.split(". ")
    bullet_points = ["- " + sentence.strip() for sentence in sentences if sentence.strip()]
    return bullet_points

def main(input_text):
    # Load
    model_name = "t5-base"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    # ADD HERE
    #input_text = "Coined by Karl Marx, the bourgeoisie represents a social class characterized by its ownership of capital, such as factories and businesses, and its ability to accumulate wealth through the exploitation of labor. In the sociological framework, the bourgeoisie holds a position of power and influence, shaping economic structures and policies to maintain its interests. The concept emphasizes the dichotomy between the bourgeoisie and the proletariat, the working class, highlighting the inherent class struggle within capitalist societies. From a sociological perspective, the bourgeoisie not only signifies economic dominance but also wields cultural and political influence, contributing to the perpetuation of social inequalities and class-based divisions. This lens allows sociologists to analyze the dynamics of power, class conflict, and social change within the broader context of capitalist societies."

    # Generate summary
    summary = generate_summary(input_text, model, tokenizer)

    # summary to bullet points
    bullet_points = to_bullet_points(summary)

    return ("\n".join(bullet_points))