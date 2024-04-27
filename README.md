Здание номер 1
my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100', 5:'101010'}
del my_dict[3]
print(my_dict)
my_dict[10]='0100101'
print(my_dict)

Задание номер 2
sl = {'</>':13, 'script':1, '__init__':10, 'self':5, 'number_9':6, '#comment':100}
print(sl)
print("add key")
i = int(input())
print("add value")
o = str(input())
sl[i] = o
print(sl)

Задание номер 3
w = {}
while len(w) < 3:
    k = int(input())
    c = str(input())
    w[k] = c

print(w)
print("Конец")

Задание номер 4
all_d = {1:15, 4:80, 44:0, 256:15, 100:70, 101:70, 20:44, 3:9}
all_d.pop(1)
all_d.pop(101)
all_d.pop(3)
print(all_d)
