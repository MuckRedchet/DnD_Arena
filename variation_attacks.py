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
    miss_list_crit = ['КРИТ ПРОВАЛ ' + name + ' бьет по себе ' + damage + ' урона',
                      'КРИТ ПРОВАЛ ' + name + ' умудрился попасть по себе ' + damage + ' урона',
                      'КРИТ ПРОВАЛ ' + name + ' спотыкается и ранит себя на ' + damage + ' урона',
                      'КРИТ ПРОВАЛ ' + name + ' нанес себе ' + damage + ' урона']
    miss_crit = miss_list_crit[randint(0, 3)]
    return miss_crit
