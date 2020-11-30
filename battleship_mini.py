import numpy as np
import random
import os
import pandas as pd

print("\nBattleship Mini:\n")
print("Played on a 5x5 grid.")
print("Each player has 3 ships at one coordinate each.")
print("First to sink all wins.\n")

board = pd.DataFrame({"1":np.array(["0","0","0","0","0"]),
					"2":np.array(["0","0","0","0","0"]),
					"3":np.array(["0","0","0","0","0"]),
					"4":np.array(["0","0","0","0","0"]),
					"5":np.array(["0","0","0","0","0"])},index=["A","B","C","D","E"])
				
compboard = pd.DataFrame({"1":np.array(["0","0","0","0","0"]),
					"2":np.array(["0","0","0","0","0"]),
					"3":np.array(["0","0","0","0","0"]),
					"4":np.array(["0","0","0","0","0"]),
					"5":np.array(["0","0","0","0","0"])},index=["A","B","C","D","E"])
					
compboardview = pd.DataFrame({"1":np.array(["0","0","0","0","0"]),
						"2":np.array(["0","0","0","0","0"]),
						"3":np.array(["0","0","0","0","0"]),
						"4":np.array(["0","0","0","0","0"]),
						"5":np.array(["0","0","0","0","0"])},index=["A","B","C","D","E"])
						
usercordlist = []
compcordlist = []

compcordlistview = ["Z0","Z1","Z2"]

nc=3
while nc>0:
	cx = random.choice(["A","B","C","D","E"])
	cy = random.choice(["1","2","3","4","5"])
	compcord = cx+cy
	if compcord in compcordlist:
		continue
	else:
		compcordlist.append(compcord)

	if "A" in cx:
		cx=0
	elif "B" in cx:
		cx=1
	elif "C" in cx:
		cx=2
	elif "D" in cx:
		cx=3
	elif "E" in cx:
		cx=4
	else:
		pass
	cy = int(cy)
	cy = cy-1
	compboard.iloc[cx][cy] = "1"
	nc-=1

print()
n = 3
ct = 1
while n>0:
	user = input("Enter coordinate {} (A1 - E5): ".format(ct))
	user = user.upper().strip()
	user = user[0] + user[-1]
	
	if user[0] not in ["A","B","C","D","E"]:
		print("Invalid coordinate.")
		continue
	
	try:
		ypos = int(user[-1])
	except:
		print("Invalid coordinate.")
		continue
	else:
		if ypos<=0 or ypos>5:
			print("Invalid coordinate.")
			continue
		else:
			pass
	
	if user in usercordlist:
		print("Coordinate has been filled. Choose a different one.")
	else:
		usercordlist.append(user)
		n-=1
		ct+=1
		
usercordlistview = usercordlist.copy()
	
for i in usercordlist:
	if "A" in i:
		x=0
	elif "B" in i:
		x=1
	elif "C" in i:
		x=2
	elif "D" in i:
		x=3
	elif "E" in i:
		x=4
	else:
		pass
		
	if "1" in i:
		y=0
	elif "2" in i:
		y=1
	elif "3" in i:
		y=2
	elif "4" in i:
		y=3
	elif "5" in i:
		y=4
	else:
		pass
		
	board.iloc[x][y] = "1"

input("\nClick enter to continue...")

os.system("cls")
print("\nP1:\n{} {}\n\nComp:\n{} {}\n".format(board,usercordlistview,compboardview,compcordlistview))

winner = 0
userguessed = []
compguessed = []
compships = 3
userships = 3

while winner==0:
	choice = input("Enter coordinate to bomb: ")
	choice = choice.upper().strip()
	choice = choice[0] + choice[-1]
	
	if choice[0] not in ["A","B","C","D","E"]:
		print("Invalid coordinate.")
		continue
	
	try:
		ypos = int(choice[-1])
	except:
		print("Invalid coordinate.")
		continue
	else:
		if ypos<=0 or ypos>5:
			print("Invalid coordinate.")
			continue
		else:
			pass
			
	if choice in userguessed:
		print("Coordinate has been guessed. Choose a different one.")
		continue
	else:
		userguessed.append(choice)
			
	if "A" in choice:
		ux=0
	elif "B" in choice:
		ux=1
	elif "C" in choice:
		ux=2
	elif "D" in choice:
		ux=3
	elif "E" in choice:
		ux=4
	else:
		pass
		
	if "1" in choice:
		uy=0
	elif "2" in choice:
		uy=1
	elif "3" in choice:
		uy=2
	elif "4" in choice:
		uy=3
	elif "5" in choice:
		uy=4
	else:
		pass
	
	if choice in compcordlist:
		print("P1: Hit! You sunk a ship!")
		compboardview.iloc[ux][uy] = "H"
		compboard.iloc[ux][uy] = "X"
		indd = compcordlist.index(choice)
		compcordlistview[indd] = "X"
		compships-=1
		if compships==0:
			winner=1
			continue
	else:
		print("P1: Miss.")
		compboardview.iloc[ux][uy] = "M"
	
	while True:
		cox = random.choice(["A","B","C","D","E"])
		coy = random.choice(["1","2","3","4","5"])
		compchoice = cox+coy
		if compchoice in compguessed:
			continue
		else:
			compguessed.append(compchoice)
			break
	print("Comp: {}".format(compchoice))
	if "A" in cox:
		cox=0
	elif "B" in cox:
		cox=1
	elif "C" in cox:
		cox=2
	elif "D" in cox:
		cox=3
	elif "E" in cox:
		cox=4
	else:
		pass
	coy = int(coy)
	coy = coy-1
	if compchoice in usercordlist:
		print("Comp: Hit! Comp sunk a ship!")
		board.iloc[cox][coy] = "X"
		ind = usercordlist.index(compchoice)
		usercordlistview[ind] = "X"
		userships-=1
		if userships==0:
			winner=2
			continue
	else:
		print("Comp: Miss.")
	
	input("\nClick enter to continue...")
	os.system("cls")
	print("\nP1:\n{} {}\n\nComp:\n{} {}\n".format(board,usercordlistview,compboardview,compcordlistview))
		
if winner==1:
	print("You win!")
elif winner==2:
	print("You lost.")

print("\nBoard view:")
print("\nP1:\n{} {}\n\nComp:\n{} {}\n".format(board,usercordlist,compboard,compcordlist))

input("Click enter to exit...")
