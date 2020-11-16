from enemy import Enemy
from fight import fight
from random import randint

kd = [15, 15]  # коофициент доспеха
hp = [randint(20, 30), randint(20, 30)]  # Количество здоровья
strength = [1, 1]  # сила
dexterity = [2, 2]  # ловкость
att = [[1, 6], [1, 6]]  # количество кубов, наминал
add_damage = [5, 5]  # + к урону
add_hit = [5, 5]  # + к попаданию

gork = Enemy('Горк', kd[0], hp[0], strength[0], dexterity[0], att[0], add_damage[0], add_hit[0])
mork = Enemy('Морк', kd[1], hp[1], strength[1], dexterity[1], att[1], add_damage[1], add_hit[1])

fight(gork, mork)