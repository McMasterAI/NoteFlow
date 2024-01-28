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

def main():
    # Load
    model_name = "t5-base"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    # ADD HERE
    input_text = "As such, Apple is planning on building a new office in Toronto for 13 million U.S Dollars. It is also possible to make your own custom Verilog subcircuit, this is similar to a Subroutine in Java."

    # Generate summary
    summary = generate_summary(input_text, model, tokenizer)

    # summary to bullet points
    bullet_points = to_bullet_points(summary)

    print("\n".join(bullet_points))

main()