file = open('Day 2/input.txt')

def isValid(str):
    split1 = str.split(': ')
    split2 = split1[0].split(' ')
    split3 = split2[0].split('-')
    char = split2[1]
    pwd = split1[1]
    min = int(split3[0]) - 1
    max = int(split3[1]) - 1
    return (pwd[min] == char and pwd[max] != char) or (pwd[min] != char and pwd[max] == char)

count = 0
for i in file:
    if (isValid(i)):
        count += 1
print(count)

print(isValid('1-3 a: abcde'))
print(isValid('1-3 b: cdefg'))
print(isValid('2-9 c: ccccccccc'))