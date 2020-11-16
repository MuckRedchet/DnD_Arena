from enemy import Enemy
from fight import fight
from random import randint

kd = 15  # коофициент доспеха
hp = randint(20, 30)  # Количество здоровья
strength = -1  # сила
dexterity = 2  # лвкость
att = [1, 6]  # количество кубов, наминал
add_damage = 5  # + к урону
add_hit = 5  # + к попаданию

gork = Enemy('Горк', kd, hp, strength, dexterity, att, add_damage, add_hit)
mork = Enemy('Морк', kd, hp, strength, dexterity, att, add_damage, add_hit)

fight(gork,mork)