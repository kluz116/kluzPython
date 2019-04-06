a = ['1','2','3','4','4','5','6']

b = ['10','20','40','50','90']

d = a+b

d.append('100')
d.append('349')
for i in a:
    print('The value from the list is : ',i)

for t in d:
    print('The values in list d are :',t)

print(d)

print("The Value At This Position  :",d[7])