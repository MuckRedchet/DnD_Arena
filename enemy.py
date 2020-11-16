from random import randint

class Enemy:
    def __init__(self, name, kd, hp, strength, dexterity, att, add_damage, add_hit):  # конструктор класса
        self.name = name  # имя
        self.kd = kd  # коофициент доспеха
        self.hp = hp  # диапозон количество здоровья
        self.strength = strength  # сила
        self.dexterity = dexterity  # ловкость
        self.att = att  # количество кубов, наминал
        self.add_damage = add_damage  # + к урону
        self.add_hit = add_hit  # + к попаданию

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