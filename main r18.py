1
def vibrosi_musor(skiliko_musora):
    print(f'взял мосор {skiliko_musora}')
    if skiliko_musora < '3':
        print("Мне лень. Сам выброси")
    else:
        print("Пошёл выбрасывать")

while True:
    vibor = input('введи колличество мусора: ')
    vibrosi_musor(vibor)
2
def vibrosi_musor(skiliko_musora):
    print(f'взял мосор {skiliko_musora}')
    if skiliko_musora == 'Да':
        print("Мне лень. Сам выброси")
    else:
        print("Пошёл выбрасывать")

while True:
    vibor = input('введи колличество мусора: ')
    vibrosi_musor(vibor)
3
def d (a, b, c):
    print(f'Дискриминант {b**2-4*a*c}')

while True:
    a=int(input('a= '))
    b=int(input('b= '))
    c=int(input('c= '))
    d(a, b, c)
