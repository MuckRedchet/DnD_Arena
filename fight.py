from variation_attacks import miss, miss_critical, critical_success, death, attack_variation
from time import sleep
from random import randint


class Fight:
    def __init__(self, figter_0, figter_1):
        self.figter_0 = figter_0
        self.figter_1 = figter_1

    def fight(self):
        figter_0 = self.figter_0
        figter_1 = self.figter_1

        print('у ', figter_0.name, figter_0.hp, 'жизней')
        print('у ', figter_1.name, figter_1.hp, 'жизней')

        while True:
            initiative = [randint(1, 20) + figter_0.dexterity, randint(1, 20) + figter_1.dexterity]  # бросок инициативы
            if initiative[0] > initiative[1]:  # сравнение инициативы
                figter_0_att = figter_0.attack()  # получение значений атаки
                if figter_0_att['dice_roll'] == 1:
                    print(miss_critical(figter_0.name, figter_0_att['damage']))
                elif figter_0_att['dice_roll'] == 20:
                    print(critical_success(figter_0.name, figter_1.name, figter_0_att['damage']))
                elif figter_0_att['dice_roll_attack'] > figter_1.kd:  # поподание против кд
                    figter_1.hp -= figter_0_att['damage']  # отнимание хп противника
                    if figter_1.hp <= 0:  # условие проиграша второго опонента
                        print(death(figter_0.name, figter_1.name, figter_0_att['damage']))
                        break
                    print(attack_variation(figter_0.name, figter_1.name, figter_0_att['damage'], figter_1.hp))
                else:
                    print(miss(figter_0.name, figter_1.name))
#
                figter_1_att = figter_1.attack()  # получение значений атаки
                if figter_1_att['dice_roll'] == 1:
                    print(miss_critical(figter_1.name, figter_1_att['damage']))
                elif figter_1_att['dice_roll'] == 20:
                    print(critical_success(figter_1.name, figter_0.name, figter_1_att['damage']))
                elif figter_1_att['dice_roll_attack'] > figter_0.kd:  # поподание против кд
                    figter_0.hp -= figter_1_att['damage']  # отнимание хп противника
                    if figter_0.hp <= 0:  # условие проиграша первого опонента
                        print(death(figter_1.name, figter_0.name, figter_1_att['damage']))
                        break
                    print(attack_variation(figter_1.name, figter_0.name, figter_1_att['damage'], figter_0.hp))
                else:
                    print(miss(figter_1.name, figter_0.name))
#
            elif initiative[0] < initiative[1]:  # сравнение инициативы
                figter_1_att = figter_1.attack()  # получение значений атаки
                if figter_1_att['dice_roll'] == 1:
                    print(miss_critical(figter_1.name, figter_1_att['damage']))
                elif figter_1_att['dice_roll'] == 20:
                    print(critical_success(figter_1.name, figter_0.name, figter_1_att['damage']))
                elif figter_1_att['dice_roll_attack'] > figter_0.kd:  # поподание против кд
                    figter_0.hp -= figter_1_att['damage']  # отнимание хп противника
                    if figter_0.hp <= 0:  # условие проиграша первого опонента
                        print(death(figter_1.name, figter_0.name, figter_1_att['damage']))
                        break
                    print(attack_variation(figter_1.name, figter_0.name, figter_1_att['damage'], figter_0.hp))
                else:
                    print(miss(figter_1.name, figter_0.name))

#

                figter_0_att = figter_0.attack()  # получение значений атаки
                if figter_0_att['dice_roll'] == 1:
                    print(miss_critical(figter_0.name, figter_0_att['damage']))
                elif figter_0_att['dice_roll'] == 20:
                    print(critical_success(figter_0.name, figter_1.name, figter_0_att['damage']))
                elif figter_0_att['dice_roll_attack'] > figter_1.kd:  # поподание против кд
                    figter_1.hp -= figter_0_att['damage']  # отнимание хп противника
                    if figter_1.hp <= 0:  # условие проиграша второго опонента
                        print(death(figter_0.name, figter_1.name, figter_0_att['damage']))
                        break
                    print(attack_variation(figter_0.name, figter_1.name, figter_0_att['damage'], figter_1.hp))
                else:
                    print(miss(figter_0.name, figter_1.name))

#
            sleep(0.8)
