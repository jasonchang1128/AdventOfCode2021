#Part 1
my_file = open("Day2_Input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

HorizontalValue = 0
DepthValue = 0

for index, elem in enumerate(content_list):  #Iterate through the list.
    CommandSplit = elem.split(" ")
    if CommandSplit[0] == 'forward':
        HorizontalValue += int(CommandSplit[1])
    elif CommandSplit[0] == 'down':
        DepthValue += int(CommandSplit[1])
    elif CommandSplit[0] == 'up':
        DepthValue -= int(CommandSplit[1])

Part1Answer = HorizontalValue * DepthValue

print(Part1Answer)

#Part 2
HorizontalValue = 0
DepthValue = 0
AimValue = 0

for index, elem in enumerate(content_list):  #Iterate through the list.
    CommandSplit = elem.split(" ")
    if CommandSplit[0] == 'forward':
        HorizontalValue += int(CommandSplit[1])
        DepthValue += AimValue * int(CommandSplit[1])
    elif CommandSplit[0] == 'down':
        AimValue += int(CommandSplit[1])
    elif CommandSplit[0] == 'up':
        AimValue -= int(CommandSplit[1])

Part2Answer = HorizontalValue * DepthValue
print(Part2Answer)