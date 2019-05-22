while True:
    name = input("Name: ")

    agility = input("Agility: ")
    might = input("Might: ")
    will = input("Will: ")
    wit = input("Wit: ")

    actions = input("Actions: ")
    health= input("Health: ")
    defense = input("Defense: ")
    speed = input("Speed: ")

    size = input("Size: ")

    skill = ""
    skills = []

    while skill != "end":
        skill = input("Skill (type end when done): ")
        beat = "null"
        if skill != "end":
            while beat != "":
                beat = input()
                skill += " {}".format(beat)
                
            splitSkill = skill[:-1].split(": ")
            skills.append(splitSkill)
            print(splitSkill)

    newbeast = open("beast.txt", "a")
    newbeast.write("\n")

    newbeast.write("<table>\n")
    newbeast.write( '<tr><td style="background-color: black; color: white; border-radius: 4px; border: 0;" colspan="4">{}</td></tr>\n'.format(name.capitalize()) )
    newbeast.write( '<tr><td style="border-top: 0;"><b>Agility</b> {}</td><td style="border-top: 0;"><b>Might</b> {}</td><td style="border-top: 0;"><b>Will</b> {}</td><td style="border-top: 0;"><b>Wit</b> {}</td></tr>\n'.format(agility, might, will, wit) )
    newbeast.write( '<tr><td><b>Actions</b> {}</td><td><b>Health</b> {}</td><td><b>Defense</b> {}</td><td><b>Speed</b> {}</td></tr>\n'.format(actions, health, defense, speed) )
    newbeast.write( '<tr><td colspan="4"><b>Size</b> {}</tr>\n'.format(size) )
    
    # Loop Through and Add Skills
    for skillIndex in range(len(skills)):
        if len(skills) > 1:
            if skillIndex == 0:
                newbeast.write( '<tr><td colspan="4" style="border-bottom: 0;"><b>{}.</b> {}</td></tr>\n'.format(skills[skillIndex][0], skills[skillIndex][1]) )
            else:
                newbeast.write( '<tr><td colspan="4" style="border-top: 0;"><b>{}.</b> {}</td></tr>\n'.format(skills[skillIndex][0], skills[skillIndex][1]) )            
        else:
            newbeast.write( '<tr><td colspan="4"><b>{}.</b> {}</td></tr>\n'.format(skills[skillIndex][0], skills[skillIndex][1]) )
        
    newbeast.write("</table>\n")
    newbeast.close()

    print("New Companion!")
    print()
