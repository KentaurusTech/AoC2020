file = open('Day 2/input.txt')

def isValid(str):
    split1 = str.split(': ')
    split2 = split1[0].split(' ')
    split3 = split2[0].split('-')
    char = split2[1]
    pwd = split1[1]
    min = int(split3[0])
    max = int(split3[1])
    count = 0
    for i in pwd:
        if (i == char):
            count += 1
    return count >= min and count <= max

count = 0
for i in file:
    if (isValid(i)):
        count += 1
print(count)