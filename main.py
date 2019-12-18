import random
import time
Categories=0
Stats=0
Dead = False 
#First List is the names, Second List is the HealthPoints, Third List is the Attack Stat, Fourth List is the Defence Stat and the last one is a movement stat

Characters = [["Hero:","Rat:","Bear:","Dragon:"],[30,8,23,100],[12,2,20,30],[3,7,9,15],[15,5,25,50]]

#The Commented code underneath is a debugging code used to see if the code showed all the characters and their specific stats
#while Stats<4:
	#while Categories<5:
		#print(Characters[Categories][Stats])
		#Categories+=1
	#Stats+=1
	#Categories = 0
	#print("")
print("This is an RPG game, your aim is to kill enemies and get to the top.")
time.sleep(3)
print("There are 4 different stats: HP, Attack, Defence and Movement.")
time.sleep(3)
print("These are what each stat does: \n")
time.sleep(2)
print("Health: How much damage you can take before you die.\n")
time.sleep(4)
print("Attack: How much attack is dealt to you or your enemy.\n")
time.sleep(4)
print("Defence:If you choose to block for a turn, you will be able to reduce the amount of damage recieved if the enemy decides to attack on that same turn.\n")
time.sleep(9)
print("Movement: Movement is how long it will take to attack. If you have 5 movement, you will attack in 2.5 seconds, but if you have 15, you attack in 7.5 seconds. \n")
time.sleep(11)
print("You will be able to improve your stats based on the EXP you gain and regenerate a certain amount of health.")
time.sleep(5)
print("You may also recieve items at the end of a battle. \n")
time.sleep(3)
print("Good Luck and I hope you have fun!")
print(". \n.. \n... \n. \n.. \n... \n. \n!")

time.sleep(2)

def health (x):
  health_stat = Characters[1][x]
  return health_stat
def attack (x):
  attack_stat = Characters[2][x]
  return attack_stat
def defence (x):
  defence_stat = Characters[3][x]
  return defence_stat
def movement (x):
  MoveSpeed_stat = Characters[4][x]
  return MoveSpeed_stat
#The Subroutines above will allow a set of stats to be printed towards specific categories
def Stats(x):
  a = health(x)
  b = attack(x)
  c = defence(x)
  d = movement(x)
  return a,b,c,d
#This subroutine links to the ones above it in order to provide multiple stats into one subroutie.
print("You are the Hero, you have these stats:")
H_Health,H_Attack,H_Defence,H_Movement = Stats(0)
print("Health:",H_Health)
print("Attack:",H_Attack)
print("Defence:",H_Defence)
print("Movement:",H_Movement)
print("\n")
print("First Fight: Hero VS Rat\n")
print("Enemy's Stats:")
R_Health,R_Attack,R_Defence,R_Movement = Stats(1)
print("Health:",R_Health)
print("Attack:",R_Attack)
print("Defence:",R_Defence)
print("Movement:",R_Movement)
print("The Rat may be weak and have a low amaount of HP, but he can attack much faster than you could with a significant amount of damage, so be careful of that")
#This gives the player a brief analysis of the enemy they are about to fight. 



while Dead==False:
  while H_Movement>0 or R_Movement>0:
    if H_Movement>0:
      print("Time left until you can make a move:", H_Movement/2) #TO BE IMPORTED, TIMER (SLEEP)
      H_Movement-=1
    if R_Movement>0:
      print("Time left until enemy can make a move:", R_Movement/2)
      R_Movement-=1