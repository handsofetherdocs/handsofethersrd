from math import floor
from math import ceil

itemMax = 0

raw_block = input()
while True:
    add_block = input()
    if add_block != "END":
        raw_block += " " + add_block
    else:
        break


heading_seperated = raw_block.split("(")

final_items = []

for heading in heading_seperated[1:]:  # First one is always blank
    itemMax += 1
    splitheading = heading.split(")")

    body_text = splitheading[1]

    final_items.append("**{}** \n{}".format(splitheading[0], splitheading[1][1:]))
    
p = open("parseditems.txt", "w")

curItem = 0
p.write('<div style="display: grid; grid-template-columns: 1fr 1fr;">\n')
p.write('<div style="grid-column: 1/2; margin-right: 13px;">\n')

print(itemMax)

for itemblock in final_items:

    if curItem == ceil(itemMax/2):
        p.write('</div>\n')
        p.write('<div style="grid-column: 2/3; margin-right: 13px;">\n')


    p.write(itemblock)
    p.write("  \n\n")

    curItem += 1

p.write('</div>\n')
p.write('</div>\n')

p.close()

    
