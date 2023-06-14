# while
# while exp_booleana
num=1
while num <=10:
    print(num)
    num+=1

# for -> iterable
myStr = "Hola"
for letter in myStr:
    print(letter,end=' ')
print()

myList=["a","b","c",12]
for item in myList:
    print(item,end=' ')
print()

# function range()
# range(fin)
for i in range(3):
    print(i,end=' ')
print()
# range(ini:fin)
for i in range(3,6):
    print(i,end=' ')
print()
# range(ini:fin:step)
for i in range(1,11,2):
    print(i, end=' ')