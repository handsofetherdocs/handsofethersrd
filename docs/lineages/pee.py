while True:
    name = input("Name: ")
    description = input("Description: ")
    abilityscoreincrease = input("Ability Score Increase: ")
    hitpoints1stlevel = input("Hit points at first level: ")
    healthonlevelup = hitpoints1stlevel
    size = input("Size: ")
    speed = input("Speed: ")
    
    lineageskill1 = input("Lineage Skills: ")
    # Format the lineage skill
    linsplit = lineageskill1.split(")")
    lineageskill1 = "**{}.**{}".format(linsplit[0][1:], linsplit[1])
    
    lineageskill2 = input() #"Second Lineage Skill: ") # This skill is autofilled in
    # Format the lineage skill
    linsplit = lineageskill2.split(")")
    lineageskill2 = "**{}.**{}".format(linsplit[0][1:], linsplit[1])
    
    f = open("{}.md".format(name), 'w')
    f.write('''# {}

{}

### Lineage Properties
|||
|-|--|
|Ability Score Improvements| {} |
|Health at 1st Level| {} |
| Health Increase at Level Up | 1d{} |
| Size | {} |
| Speed | {} |

### Lineage Skills
{}

{}'''.format(name.capitalize(), description, abilityscoreincrease, hitpoints1stlevel, healthonlevelup, size.capitalize(), speed, lineageskill1, lineageskill2))
    f.close()
    print("\n\n\n")
