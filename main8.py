import random

class Enemy:
    def _init_(self,atkl,atkh):
       self.atkl=atkl
       self.atkh=atkh

    def getAtk(self):
        print(self.atkl)

enemy1=Enemy(40, 49)
enemy1.getAtk()

enemy2=Enemy(75, 90)
enemy2.getAtk()


'''

playerhp=260
enemyatkl=60
enemyatkh=80

while playerhp>0:
    dmg=random.randrange(enemyatkl,enemyatkh)
    playerhp=playerhp-dmg

    if playerhp<=30:
        playerhp=30
    print("enemy strikes for",dmg,"points of damage.current HP is",playerhp)

    if playerhp>30:
        continue
    print("You have low health.you've been temported to the nearest inn.")
    break
'''