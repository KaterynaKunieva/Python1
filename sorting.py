from random import randint
mas=[]
for i in range(38):
    a=randint(0,50)
    mas.append(a)
print('array:',mas)
mas_1=[]
mas_2=[]
for i in range(len(mas)):
    if i%2==0:
        mas_1.append(mas[i])
    else:
        mas_2.append(mas[i])
mas_1=sorted(mas_1)
mas_2=sorted(mas_2)
mas_2.reverse()
print('pair_position_sorted:',mas_1)
print('unpaired_position_sorted:',mas_2)
mas_3=[]
for i in range(len(mas_1)):
    mas_3.append(mas_1[i])
    mas_3.append(mas_2[i]) 
print('Sort_array:',mas_3)
