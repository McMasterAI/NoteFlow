import spacy
import pytextrank


text = "Static variables belong to the class and are inherited by each object. This is good for things that are ubiquitous within all objects of a class. Static variables can still be used like non-static, to display specific information about an object, but the problem arises if you try and call them through the class, when there is no specific information available. This is where non-static comes in, since non-static cannot be called through the class, this problem goes away. Non-static is good for information that is specific to each class."
text2 = "We delved into the ethical considerations, focusing on accountability, transparency, and the potential bias embedded in algorithms. The transformative impact of AI across key sectors like healthcare, education, and business was a central theme, with an emphasis on both the opportunities and challenges these advancements present. The socio-economic implications were discussed, including the looming threat of job displacement and the urgent need for reskilling in the workforce. Real-world examples and case studies were examined to illustrate the dynamic relationship between AI and society, urging us to strike a delicate balance between innovation and ethical responsibility as we navigate this rapidly evolving technological landscape."
text3 = "The discussion began with an exploration of the geological conditions conducive to the creation of oil reserves. We focused on the organic matter, primarily ancient marine plants and microorganisms, that accumulates in sedimentary rock layers over millions of years. The lecture emphasized the significance of high pressure and temperature in these sedimentary basins, acting as catalysts for the transformation of organic material into hydrocarbons. The organic material undergoes a complex process known as diagenesis, involving the biochemical and physical changes that ultimately result in the formation of hydrocarbons, the building blocks of oil. As we delved deeper into the mechanisms of oil formation, the lecture highlighted the role of source rocks, migration pathways, and reservoir rocks in creating and preserving these valuable hydrocarbon deposits. Throughout the discussion, geological diagrams and cross-sections were used to illustrate the sequence of events leading to the development of oil reservoirs. The lecture concluded with an overview of exploration and extraction methods employed by the oil industry to tap into these reservoirs and meet the global demand for this essential energy resource."
text4 = "The discussion commenced with an overview of the fundamental principles underlying nuclear reactions. The focus was on the process of nuclear fission, wherein the nucleus of an atom splits into two or more smaller nuclei, releasing a significant amount of energy in the form of heat. The lecture then delved into the construction and operation of nuclear power plants, emphasizing the role of enriched uranium or plutonium as fuel sources. The concept of controlled chain reactions, essential for sustaining the energy release, was explained, highlighting the intricate balance required for safe and efficient operation. The applications of nuclear energy extended beyond electricity generation, as the lecture covered the use of nuclear technology in medical diagnostics and treatment, industrial processes, and even space exploration. The discussion also addressed the environmental considerations and safety measures associated with nuclear power, including the management of radioactive waste and the importance of stringent regulatory frameworks."
text5 = "The ship, boasting luxury and cutting-edge technology, set sail on a fateful night, April 14, 1912, when it collided with an iceberg. The ensuing chaos and disbelief among passengers and crew marked the beginning of an unraveling disaster. As the Titanic rapidly sank, lifeboats were in short supply, leading to both heroic tales of survival and heartbreaking losses. The tragedy left an indelible mark on maritime safety regulations, influencing a reassessment of practices to prevent future disasters. The sinking of the Titanic also became deeply ingrained in popular culture, inspiring numerous movies, books, and exhibits that continue to captivate the public's imagination. Archaeological discoveries of the wreckage have shed light on the events of that night, with ongoing efforts to preserve artifacts and document this poignant chapter in history. The human stories of survivors and victims, along with the stark social disparities on the ship, further contribute to the enduring legacy of the Titanic. Despite decades of exploration, ongoing mysteries persist, sparking debates about the role of design flaws and the insufficient number of lifeboats on that ill-fated journey. The Titanic remains a symbol of both tragedy and resilience, a story that continues to fascinate and resonate with people around the world."
text6 = "spaCy is able to compare two objects, and make a prediction of how similar they are. Predicting similarity is useful for building recommendation systems or flagging duplicates. For example, you can suggest a user content that’s similar to what they’re currently looking at, or label a support ticket as a duplicate if it’s very similar to an already existing one."
text7 = "Nuclear fission, a pivotal process in nuclear energy, unfolds when a neutron collides with the nucleus of a fissile atom, such as uranium-235 or plutonium-239, causing it to split into smaller nuclei and releasing a substantial amount of energy. This event triggers a chain reaction as the newly released neutrons go on to induce further fission reactions in neighboring nuclei. Control rods made of neutron-absorbing materials, like cadmium or boron, are strategically employed in nuclear reactors to regulate and maintain the rate of fission, preventing overheating. The heat generated is harnessed to produce steam, driving turbines connected to generators and ultimately generating electricity. This controlled process has become a cornerstone of global energy production, although ongoing research explores the potential of nuclear fusion as a cleaner and more sustainable alternative."
text8 = "The bourgeoisie, a concept deeply rooted in sociological theory, refers to the capitalist class that owns the means of production and controls economic resources within a society. Coined by Karl Marx, this term represents a social class characterized by its ownership of capital, such as factories and businesses, and its ability to accumulate wealth through the exploitation of labor. In the sociological framework, the bourgeoisie holds a position of power and influence, shaping economic structures and policies to maintain its interests. The concept emphasizes the dichotomy between the bourgeoisie and the proletariat, the working class, highlighting the inherent class struggle within capitalist societies. From a sociological perspective, the bourgeoisie not only signifies economic dominance but also wields cultural and political influence, contributing to the perpetuation of social inequalities and class-based divisions. This lens allows sociologists to analyze the dynamics of power, class conflict, and social change within the broader context of capitalist societies."

def generateTitle(text):
    nlp_tr = spacy.load("en_core_web_sm")
    nlp_post = spacy.load("en_core_web_lg")

    nlp_tr.add_pipe("textrank")
    doc = nlp_tr(text)

    top_three_raw = []
    title = []

    #for phrase in doc._.phrases:
        #print(phrase.text)
        #print(phrase.rank, phrase.count)
        #print(phrase.chunks)

    for index, phrase in enumerate(doc._.phrases):
        #print(phrase.text)
        #print(phrase.rank, phrase.count)
        #print(phrase.chunks)

        if (index == 5):
            break

        title = [phrase.text,phrase.rank]
            
        temp_doc = nlp_post(phrase.text)
        for token in temp_doc:
            if (token.shape_[0] == "X"):
                title[1] += 1
            
        top_three_raw.append(title)

    top_three = sorted(top_three_raw, key=lambda x: x[1], reverse=True)

    compare1 = nlp_post(top_three[0][0])
    compare2 = nlp_post(top_three[1][0])
    compare3 = nlp_post(top_three[2][0])

    #print("\n** Top Three Results **")
    #print("1. " + top_three[0][0], top_three[0][1])
    #print("2. " + top_three[1][0], top_three[1][1])
    #print("3. " + top_three[2][0], top_three[2][1])
    #print(top_three[0][0], "<->", top_three[1][0], compare1.similarity(compare2))
    #print(top_three[1][0], "<->", top_three[2][0], compare2.similarity(compare3))
    #print(top_three[0][0], "<->", top_three[2][0], compare1.similarity(compare3))
    average = (compare1.similarity(compare2) + compare2.similarity(compare3) + compare1.similarity(compare3))/3
    #print("Average similarity: ", average)

    title = "\n#### " + top_three[0][0] + ": " + top_three[1][0] + " & " + top_three[2][0]
    if (top_three[0][1] > 1):
        picked_confidence = top_three[0][1] - 0.8
    else:
        picked_confidence = top_three[0][1]
    print("\nTitle Confidence:", (picked_confidence + average)/1.1)
    return title

