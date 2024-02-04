import t5_sentence_extract as summarize
import titleUsingTextRank as titleGen
import boldingItalicizationModule as bi


input_text = input("Enter text to summarize: ")

bullet_points = summarize.main(input_text)
paragraphed_points = " ".join(bullet_points).replace(" -",".").replace("- ","")
title = titleGen.generateTitle(input_text)
bullet_points = bi.boldItalicize(paragraphed_points, bullet_points)

print(title)
print("\n".join(bullet_points))
print()