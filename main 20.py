goroda = { "Магнитогорск": 1690, "Нижний Новгород": 470, "Самара": 1080, "Омск": 2750, "Новосибирск": 3400,"Благовещенск": 7800, "Красноярск": 4200,  "Анапа": 1530, "Астрахань": 1410, "Смоленск": 390  }
spisok = list(goroda.keys())
while True:
    print('Выберите город из списка, чтобы посмотреть сколько км от Москвы:')
    print(', '.join(spisok))
    city = input('> ')
    if city in goroda:
        print(f'от Москвы до {city} {goroda [city]} км.' )
        break
    else:
        print('Нет такого города! Повторите еще раз')
