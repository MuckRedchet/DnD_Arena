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
