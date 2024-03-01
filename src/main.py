import t5_sentence_extract as sentenceGen
import titleUsingTextRank as titleGen
import boldingItalicizationModule as bi
import gradio as gr

def summarize(notes):
    bullet_points = sentenceGen.main(notes)
    paragraphed_points = " ".join(bullet_points).replace(" -",".").replace("- ","")
    title = titleGen.generateTitle(notes)
    bullet_points = bi.boldItalicize(paragraphed_points, bullet_points)
    output = title + "\n" + "\n".join(bullet_points)
    return output

demo = gr.Interface(fn=summarize,
                    inputs=["textbox"],
                    outputs=gr.Markdown()
)

demo.launch(share=True)

#Backup terminal based main
"""
input_text = input("Text to input: ")

bullet_points = sentenceGen.main(input_text)
paragraphed_points = " ".join(bullet_points).replace(" -",".").replace("- ","")
title = titleGen.generateTitle(input_text)
bullet_points = bi.boldItalicize(paragraphed_points, bullet_points)

print(title)
print("\n".join(bullet_points))
print()
"""
