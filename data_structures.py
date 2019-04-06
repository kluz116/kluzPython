fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
a = fruits.count('apple')

print('The Total Count Of Apples Is : ',a)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
b = fruits.index('banana')
print('Item banana Position : ',b)
fruits.pop()
fruits.pop()
fruits.pop()
print(fruits)

for i in fruits:
    print(i)



#Using list as stack

stack = ['1','2']

print(stack)
stack.append('3')
stack.append('4')
stack.append('5')
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)