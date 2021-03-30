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
        dice_roll = randint(1, 20) # Бросок двацатки
        dice_roll_attack = dice_roll + self.strength + self.add_hit # Вычисление атаки
        attack_m = self.att # Количество кубов атаки
        add_damage = self.add_damage
        hp = self.hp
        damage = 0

        if dice_roll == 1:  # сценарий крит провала
            damage = randint(1, add_damage) # вычисление урона
            hp -= damage # урон по себе
            return {'dice_roll':dice_roll, 'dice_roll_attack':dice_roll_attack, 'damage':damage}
        elif dice_roll == 20:  # сценарий крит успеха
            for i in range(attack_m[0]):
                damage += randint(1, attack_m[1]) * 2
            damage += add_damage
            return {'dice_roll':dice_roll, 'dice_roll_attack':dice_roll_attack, 'damage':damage}
        else:  # обычкая атака
            for i in range(attack_m[0]):
                damage += randint(1, attack_m[1])
            damage += add_damage
            return {'dice_roll':dice_roll, 'dice_roll_attack':dice_roll_attack, 'damage':damage}
