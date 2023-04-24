from collections import Counter
c=Counter()
mas=[]
mas=input('Введите строку:')
mas_1=[]
for i in mas:
    if i!=' ' and i!='(' and i!=')':
        mas_1.append(i)
    else:
        pass
for j in mas_1:
    c[j]+=1
print('Частота:',c)
mas=mas.split()
mas_skobki=[]
for i in mas:
    mas_1=i
    for j in mas_1:
        if j=='(' or j==')':
            mas_skobki=(mas_1)
        else:
            pass
print('Слово в скобках:',mas_skobki)
print('Кол. символов в скобках:',len(mas_skobki)-2)


    
