from math import floor

raw_block = input()
while True:
    add_block = input()
    if add_block != "END":
        raw_block += " " + add_block
    else:
        break

final_text = ""

split_description = raw_block.split("Challenge Rating")

#print(split_description)

description = split_description[0] # This is used in the final_text
stats_and_skills = split_description[1]

split_stats_and_skills = stats_and_skills.split(".", 11)

stats = split_stats_and_skills[0:11]

primary_skills_and_weakness = split_stats_and_skills[11]

newStats = []  # CR, Type, Agility, Might, Will, Wit, Actions, Health, Defense, Speed, Size

# Parsing of Stats
for stat in stats:
    newStats.append(stat.split(": ")[1])

primary_and_skillsWeakness = primary_skills_and_weakness.split("Weakness")
    
primary_ability =  primary_and_skillsWeakness[0][1:] # Gets rid of space at start

weakness = primary_and_skillsWeakness[1].split("Skills")[0]
skills = primary_and_skillsWeakness[1].split("Skills")[1]

#print(primary_ability)
#print(weakness)
#print(skills)

skills_split = skills.split("(")

final_skills = []

for cur_split_skill in skills_split[1:]:  # First one is blank
    cur_skill_heading_and_body = cur_split_skill.split(")")
    final_skills.append(["{}".format(cur_skill_heading_and_body[0]), "{}".format(cur_skill_heading_and_body[1][1:-1])])


# Assemble everything together
final_text += description
final_text += "  \n\n"

# Start of table
final_text += '<table>\n'

# Add stats
final_text += '<tr><td colspan="2"><b>Challenge Rating</b> {}</td><td colspan="2"><b>Type</b> {}</td></tr>'.format(newStats[0], newStats[1])
final_text += '<tr><td style="border-top: 0;"><b>Agility</b> {}</td><td style="border-top: 0;"><b>Might</b> {}</td><td style="border-top: 0;"><b>Will</b> {}</td><td style="border-top: 0;"><b>Wit</b> {}</td></tr>\n'.format(newStats[2], newStats[3], newStats[4], newStats[5])
final_text += '<tr><td><b>Actions</b> {}</td><td><b>Health</b> {}</td><td><b>Defense</b> {}</td><td><b>Speed</b> {}</td></tr>\n'.format(newStats[6], newStats[7], newStats[8], newStats[9])
final_text += '<tr><td colspan="4"><b>Size</b> {}</tr>\n'.format(newStats[10])

# Add Priamry Ability and Weakness
final_text += '<tr><td colspan="4"><b>{}</b><br>{}</tr>\n'.format(primary_ability.split(".", 1)[0], primary_ability.split(".", 1)[1][1:-1])
final_text += '<tr><td colspan="4"><b>Weakness:</b> {}</tr>\n'.format(weakness[2:-1])

# Add Skills
skill_index = 0
for skill in final_skills:
    if skill_index == 0:
        final_text += '<tr><td colspan="4" style="border-bottom: 0;"><b>{}.</b> {}</td></tr>'.format(skill[0], skill[1])
    else:
        final_text += '<tr><td colspan="4" style="border-top: 0;"><b>{}.</b> {}</td></tr>'.format(skill[0], skill[1])
    
    skill_index += 1

final_text += '</table>\n'

file = open("parsedenemy.txt", "w")
file.write(final_text)
file.close()
