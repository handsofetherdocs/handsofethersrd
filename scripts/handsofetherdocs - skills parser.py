raw_block = input()
while True:
    add_block = input()
    if add_block != "END":
        raw_block += " " + add_block
    else:
        break


heading_seperated = raw_block.split("(")

final_skills = []

for heading in heading_seperated[1:]:  # First one is always blank
    splitheading = heading.split(")")

    body_text = splitheading[1]

    

    # Do some parsing on the main body to see if there's a list
    for character_index in range(len(body_text)):
        
        if body_text[character_index] == ":":
            content = []
            bullets = [""]
            splitByColon = body_text.split(":")

            for curSection in splitByColon[:-1]:

                for section_index in range(len(curSection)-1, 0, -1):

                    if curSection[section_index] == " ":
                        content.append(curSection[:section_index])
                        bullets.append( "{}:".format(curSection[section_index+1:]) )
                        break

            #print(bullets)
            content.append( splitByColon[-1] )

            print(bullets)
            print(content)

            putTogetherText = ""

            for putTogetherIndex in range(len(bullets)):
                if putTogetherIndex == 0:
                    putTogetherText += content[0]
                else:
                    putTogetherText += "  \n\n * <u>{}</u>".format(bullets[putTogetherIndex])
                    putTogetherText += content[putTogetherIndex]

            splitheading[1] = putTogetherText
            
            break  # Stop Parsing for Colons
   
    
    final_skills.append("**{}.**{}".format(splitheading[0], splitheading[1]))


p = open("parsedskills.txt", "w")

for skillblock in final_skills:
    p.write(skillblock)
    p.write("  \n\n")

p.close()

    
