import random

# initializing list
game_list = ["Overwatch", "Dead by Daylight", "Ragnarok Online", "Tomb Raider", "Red Dead Online", "Forza Horizon 5"]

# printing original list
print("What could we take to play today : " + str(game_list))

# using random.choice() to
# get a random string
random_game = random.choice(game_list)

# printing random string
print("And the winner is : " + str(random_game))