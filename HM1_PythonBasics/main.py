# exr1
def cookiesChecker(number):
    if number >= 9:
        print('Too many cookies')
    else:
        print ('The number of cookies is:' + str(number))

cookiesChecker(5)
# exr2
def function2(string):
    print(string[2:-2])

function2('Danila')

# exr3
def swapChar(string1, string2):
    print (string1[0:2] + string2[2:])
    print (string2[0:2] + string1[2:])

swapChar('Danila','Prymak')

# exr4
def number_of_strings(user_words):
    count = 0
    for i in user_words:
        if len(i) > 2:
            if i[0:1] == i[len(i) - 1:]:
                count += 1
    print(count)

number_of_strings(['Danila','cac','gang','cc'])

# exr5
def sortByX(smth):
    withX = []
    withoutX = []
    for i in smth:
        if i.startswith('x'):
            withX.append(i)
        else:
            withoutX.append(i)

    print(sorted(withX, key=lambda x: x[1]) + sorted(withoutX))#anonymous function lambda(with one output and par, dont have name
                                                               #search for x in beg of words
sortByX(['xcort','xvorm','xdan','bowl','oop','zert','dack'])

# exr6
def reduceRep(lst):
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] == lst[i - 1]:
            del lst[i]
    print(lst)

reduceRep([1,2,2,3,4,4,6,7])

# exr7
def makingDict(filename):
    name = open(filename)
    result = {}
    for i in name:
        key, value = i.split()
        result[key] = value

    print(result)

makingDict('ex1.txt')

# exr8
from collections import Counter

def wordRepCounter(filename):
    file = open(filename, "r")
    data = file.read()
    print(Counter(data.split()))

wordRepCounter('ex2.txt')






