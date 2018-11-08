# class GameRole:
#     name = '222'
#
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def wp(self, weapon):
#         self.weapon = weapon
#         self.ad = self.ad + weapon.ad
#
#     def attack(self, name):
#         name.hp -= self.ad
#
#         print("%s攻击%s,%s掉了%s,还剩%s血" % (self.name, name.name, name.name, self.ad, name.hp))
#
#
# class Weapon:
#
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#
# obj1 = GameRole('盖伦', 98, 1000)
# obj2 = GameRole('蛮王', 120, 800)
# axe = Weapon('斧子', 20)
# sword = Weapon('宝剑', 10)
# obj1.wp(axe)
# print(obj1.ad)
# print(obj1.__dict__)
# obj1.attack(obj2)
# obj2.attack(obj1)
# obj1.attack(obj2)
# obj2.attack(obj1)
# obj1.attack(obj2)
# obj2.attack(obj1)
# obj1.attack(obj2)
# obj2.attack(obj1)



