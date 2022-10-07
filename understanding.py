#Music_________________________
input1 = (input("what are your 3 favorite bands/musicians"))
input2 = (input("what are your 3 favorite bands/musicians"))
input3 = (input("what are your 3 favorite bands/musicians"))
favmusic = (input1,input2,input3)
print(favmusic[1])

#FOOD___________________________
food = []
for i in range(5):
    food.append(input("what is your 5 favorite foods"))
print(food[4])

#Video_Game_Pairs_______________________
gamepair= {}
print("what is your 6 favorite video game hero/villian pairs")
for i in range(6):
    hero = input("what is the hero")
    villian = input("what is the villian")
    gamepair[hero] = villian
pair = input("What pair would you like to look at")
print(gamepair[pair])
