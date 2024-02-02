import t5_sentence_extract
import titleUsingTextRank


input_text = input("Enter text to summarize: ")

bullet_points = t5_sentence_extract.main(input_text)
title = titleUsingTextRank.generateTitle(input_text)

print(title)
print(bullet_points)