from random import randint

class Enemy:
    kd = 15  # коофициент доспеха
    hp = randint(20, 30)  # Количество здоровья
    strength = -1  # сила
    dexterity = 2  # лвкость
    att = [1, 6]  # количество кубов, наминал
    add_damage = 5  # + к урону
    add_hit = 5  # + к попаданию

    def __init__(self,name):  # конструктор класса
        self.name = name  # имя


    def attack(self):
        dice_roll = randint(1, 20)
        dice_roll_attack = randint(1, 20) + self.strength + self.add_hit
        attack_m = self.att
        damage = 0
        if dice_roll == 1:
            critical_fail = randint(1, self.add_damage)
            print('КРИТ ПРОВАЛ', self.name, 'бьет по себе', critical_fail, 'урона')
            self.hp -= critical_fail
            ress = [dice_roll, dice_roll_attack, 0]
        elif dice_roll == 20:
            critical_luck = attack_m[1] * 2
            print('КРИТ УСПЕХ', self.name, 'двойной', critical_luck, 'урон')
            ress = [dice_roll, dice_roll_attack, critical_luck]
        else:
            i = 0
            while i != attack_m[0]:
                damage += randint(1, attack_m[1]) + self.add_damage
                i += 1
            ress = [dice_roll, dice_roll_attack, damage]
        return ress