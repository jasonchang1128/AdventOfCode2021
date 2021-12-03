#Part 1
my_file = open("Day1_Input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list = list(map(int, content_list))
my_file.close()

DepthLargerThanPreviousCnt = 0

for index, elem in enumerate(content_list):
    if (index - 1) >= 0:  #Do not use the first one.
        if elem > content_list[index-1]:
            DepthLargerThanPreviousCnt += 1

print(DepthLargerThanPreviousCnt)

#Part 2
DepthLargerThanPreviousCnt = 0
for index, elem in enumerate(content_list):
    if (index - 3) >= 0:  #Do not use the first one.
        PreviousThreeSum = content_list[index-3] + content_list[index-2] + content_list[index-1]
        CurThreeSum = content_list[index-2] + content_list[index-1] + elem
        if CurThreeSum > PreviousThreeSum:
            DepthLargerThanPreviousCnt += 1
            
print(DepthLargerThanPreviousCnt)



