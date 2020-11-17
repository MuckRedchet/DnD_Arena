# DnD_Arena
assistant Dangeon master.  Помошник мастера подземелий 

Honor and good luck traveler!

This program is designed to help the Dungeon Master of the game Dangeons and Dragons.
At the moment, the arena has been implemented where you can face different monsters and test their strength in battle.

Чести и удачи путник!

Данная программа предназначена для помощи Мастеру подземелий игры Dangeons and Dragons.
На данный момент реалезована арена где можно сталкивать разных монстров и проверять их силу в бою. 



Added 3 files main.py, fight.py, enemy.py

Main.py - the main file
fight.py - the code of the battle, accepts two objects of the enemy class and conducts the battle according to the DnD rules
enemy.py - enemy class

Добавленно 3 файла main.py, fight.py, enemy.py

Main.py - главный файл
fight.py - код проведения боя, принемает два обьекта класса enemy и проводит бой по правилам DnD
enemy.py - класс противника



Moved the parameters of the opponents from the 'Enemy' class to the file 'main'.
Redesigned the constructor of the Enemy class for the parameters of the opponent when creating an instance.
Correction of minor syntactic errors.

Перенес параметры опонентов из класса 'Enemy' в файл 'main'.
Переработал констуктор класса 'Enemy' на прием параметров опонента при создании экземпляра.  
Исправление мелких синтактических ошибок. 



Transfer of parameters of opponents to lists for more convenient manipulation of values
Пересадка параметров опонентов на списки для более удобного манипулирования значениями


Fixed bug with incorrect display of damage
испрален баг неправильного отображения урона


refactoring of the script for applying damage on critical success
рефакторинг сценария нанесения урона при критическом успехе

Added a new file 'variant_attacks.py' in it there is a function 'miss' that adds variations
in the combat process in case of a miss of the opponents

Добавил новый файл 'variation_attacks.py' в нем находится функция 'miss' добавляющая вариативности
в боевой процесс в случае промоха опонентов


Converting the code to the PeP8 standard
Приведение кода к стандарту PeP8

Added new function 'miss_critical' to 'variant_attacks.py' adding variability to combat
fail roll

Добавил новую функцию 'miss_critical' в 'variation_attacks.py' добавляющую вариотивности в боевой
процесс в случае критического провала