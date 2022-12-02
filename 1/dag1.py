f = open("dag1puzzle.txt", "r")
input = [line.strip('\n') for line in f.readlines()]
f.close()

temp_list = []
temp = 0
for item in input:
    if item is not '':
        temp += int(item)
    else:
        temp_list.append(temp)
        temp = 0

print(max(temp_list))
temp_list.sort()
print(sum(temp_list[len(temp_list)-3:len(temp_list)]))