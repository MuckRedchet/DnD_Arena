from random import randint


def miss(attacking: str, defender: str) -> str:
    miss_list = [attacking + ' промахнулся по ' + defender,
                 defender + ' увернулся от удара ' + attacking + 'a',
                 defender + ' парировал удар ' + attacking + 'a',
                 'удар ' + attacking + 'a прошел мимо ' + defender + 'a',
                 defender + ' отразил удар ' + attacking,
                 'удар ' + attacking + 'a не пробил защиту ' + defender + 'a']
    miss_att = miss_list[randint(0, 5)]
    return miss_att


def miss_critical(name: str, damage: int) -> str:
    damage = str(damage)
    miss_crit_list = ['КРИТ ПРОВАЛ ' + name + ' бьет по себе ' + damage + ' урона',
                      'КРИТ ПРОВАЛ ' + name + ' умудрился попасть по себе ' + damage + ' урона',
                      'КРИТ ПРОВАЛ ' + name + ' спотыкается и ранит себя на ' + damage + ' урона',
                      'КРИТ ПРОВАЛ ' + name + ' нанес себе ' + damage + ' урона']
    miss_crit = miss_crit_list[randint(0, 3)]
    return miss_crit


def critical_success(attacking: str, defender: str, damage: int) -> str:
    damage = str(damage)
    crit_success_list = ['КРИТ УСПЕХ ' + attacking + ' наносит сокрушительный удар по ' + defender + ' ' + damage +
                         ' урона',
                         'КРИТ УСПЕХ ' + attacking + ' попадает точно по ' + defender + ' наносит ' + damage + ' урона',
                         'КРИТ УСПЕХ ' + attacking + ' проводит молниносную атаку ' + defender + ' получает ' + damage +
                         ' урона',
                         'КРИТ УСПЕХ ' + attacking + ' попал в уязвимость ' + defender + 'а  на ' + damage + ' урона']

    crit_success = crit_success_list[randint(0, 3)]
    return crit_success


def death(attacking: str, defender: str, damage: int) -> str:
    damage = str(damage)
    death_list = [attacking + ' наносит смертельный удар по ' + defender + 'у ' + damage + ' урона',
                  attacking + ' обезглавливает ' + defender + 'a ' + damage + ' урона',
                  defender + ' скончался от удара ' + attacking + 'a ' + damage + ' урона',
                  attacking + ' провел удар в сердце ' + defender + 'a ' + damage + ' урона']

    death = death_list[randint(0, 3)]
    return death
