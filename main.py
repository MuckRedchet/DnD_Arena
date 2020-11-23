from enemy import Enemy
from fight import fight
from random import randint

kd = [17, 18]  # коофициент доспеха
hp = [randint(10, 11), randint(10, 11)]  # Количество здоровья
strength = [6, 6]  # сила
dexterity = [3, 1]  # ловкость
att = [[3, 10], [4, 6]]  # количество кубов, наминал
add_damage = [6, 6]  # + к урону
add_hit = [1, 1]  # + к попаданию

gork = Enemy('Горк', kd[0], hp[0], strength[0], dexterity[0], att[0], add_damage[0], add_hit[0])
mork = Enemy('Морк', kd[1], hp[1], strength[1], dexterity[1], att[1], add_damage[1], add_hit[1])

fight(gork, mork)
