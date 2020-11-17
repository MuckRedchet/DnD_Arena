from variation_attacks import miss
from time import sleep
from random import randint

def fight(figter_0, figter_1):
    print('у ', figter_0.name, figter_0.hp, 'жизней')
    print('у ', figter_1.name, figter_1.hp, 'жизней')

    while True:
        initiative = [randint(1,20) + figter_0.dexterity, randint(1,20) + figter_1.dexterity]  # бросок инициативы
        if initiative[0] > initiative[1]:  # сравнение инициативы
            figter_0_att = figter_0.attack()  # получение значений атаки
            if figter_0_att[1] > figter_1.kd:  # поподание против кд
                figter_1.hp -= figter_0_att[2]  # отнимание хп противника
                if figter_1.hp <= 0:  # условие проиграша второго опонента
                    print(figter_0.name, 'нанес смертельный удар в', figter_0_att[2], 'УРОНА',figter_0.name, 'победил')
                    break
                print(figter_0.name, 'нанес', figter_1.name, figter_0_att[2], 'урона. у него осталось', figter_1.hp,'жизней')
            else:
                print(miss(figter_0.name, figter_1.name))
        elif initiative[0] < initiative[1]:  # сравнение инициативы
            figter_1_att = figter_1.attack()  # получение значений атаки
            if figter_1_att[1] > figter_0.kd:  # поподание против кд
                figter_0.hp -= figter_1_att[2]  # отнимание хп противника
                if figter_0.hp <= 0:  # условие проиграша первого опонента
                    print(figter_1.name, 'нанес смертельный удар в', figter_1_att[2], 'УРОНА',figter_1.name, 'победил')
                    break
                print(figter_1.name, 'нанес', figter_0.name, figter_1_att[2], 'урона. у него осталось', figter_0.hp, 'жизней')
            else:
                print(miss(figter_0.name, figter_1.name))
        sleep(0.8)