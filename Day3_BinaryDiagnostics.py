#Part 1
my_file = open("Day3_Input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

NumOfPositions = len(content_list[0])
NumOfBinaryVals = len(content_list)
CountOfEachPos = [0] * NumOfPositions

for index, elem in enumerate(content_list):  #Iterate through the list.
    for BitPos in range(12):
        if elem[BitPos] == '1':
            CountOfEachPos[BitPos] += 1

GammaRateList = ['0'] * NumOfPositions
EpsilonRateList = ['1'] * NumOfPositions

for BitPos in range(12):
    if CountOfEachPos[BitPos] > (NumOfBinaryVals/2):
        GammaRateList[BitPos] = '1'
        EpsilonRateList[BitPos] = '0'

GammeRate = int("".join(GammaRateList),2)
EpsilonRate = int("".join(EpsilonRateList),2)

Part1Answer = GammeRate * EpsilonRate

print(Part1Answer)

#Part 2

Part2List = content_list.copy()
IterateBitPos = 0

while len(Part2List) > 1:
    CurrentNumElems = len(Part2List)
    NumOfAsserted = 0
    KeepVal = '1'
    for index, elem in enumerate(Part2List):  #Iterate through the list.
        if elem[IterateBitPos] == '1':
            NumOfAsserted += 1
    if NumOfAsserted >= (CurrentNumElems-NumOfAsserted):
        KeepVal = '1'
    else:
        KeepVal = '0'

    Part2List = [ elem for elem in Part2List if elem[IterateBitPos] == KeepVal]

    IterateBitPos+=1

OxyRating = int("".join(Part2List),2)

Part2List = content_list.copy()
IterateBitPos = 0
while len(Part2List) > 1:
    CurrentNumElems = len(Part2List)
    NumOfAsserted = 0
    KeepVal = '1'
    for index, elem in enumerate(Part2List):  #Iterate through the list.
        if elem[IterateBitPos] == '1':
            NumOfAsserted += 1
    if NumOfAsserted >= (CurrentNumElems-NumOfAsserted):
        KeepVal = '0'
    else:
        KeepVal = '1'

    Part2List = [ elem for elem in Part2List if elem[IterateBitPos] == KeepVal]

    IterateBitPos+=1

CO2Rating = int("".join(Part2List),2)

Part2Answer = OxyRating * CO2Rating
print(Part2Answer)