from math import floor

maxSpell = 1

raw_block = input()
while True:
    add_block = input()
    if add_block != "END":
        raw_block += " " + add_block
    else:
        break


heading_seperated = raw_block.split("(")

final_spells = []

for heading in heading_seperated[1:]:  # First one is always blank
    splitheading = heading.split(")")

    body_text = splitheading[1]

    spellcomponents = body_text.split(".", 4)

    newspellcomponents = ""
    for spellcomp in spellcomponents[:4]:
        s = spellcomp.split(":")
        newspellcomponents += "*{}:*{}  \n".format(s[0][1:], s[1])

    # Check for list in spell body
    spell_body = spellcomponents[4][1:]
    
    for character_index in range(len(spell_body)):
        
        if body_text[character_index] == ":":
            content = []
            bullets = [""]
            splitByColon = spell_body.split(":")

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

            spell_body = putTogetherText
            
            break  # Stop Parsing for Colons

    #print(newspellcomponents)

    final_spells.append("**{}**  \n{}  \n{}".format(splitheading[0], newspellcomponents, spell_body))
    maxSpell += 1

    


p = open("parsedspells.txt", "w")

curSpellNum = 1
for spellblock in final_spells:
    if curSpellNum == 1:
        p.write('<div style="display: grid; grid-template-columns: 1fr 1fr;">\n')
        p.write('<div style="grid-column: 1/2; margin-right: 13px;">\n')

    if curSpellNum == floor(maxSpell / 2):
        p.write('</div>\n')
        p.write('<div style="grid-columns: 2/3; margin-left: 13px">\n')
	
    p.write(spellblock)
    p.write("  \n\n")
        
    curSpellNum += 1

p.write('</div>\n')
p.write('</div>\n')

p.close()

    
