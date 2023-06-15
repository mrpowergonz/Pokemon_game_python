import random

def pokemon_type() :
    player_choice = input("Enter the type of pokemon you want to choose: (fire, water, plant)")
    options = ["fire" , "water" , "plant"]
    rival_choice = random.choice(options)
    choices = { "player": player_choice , "rival": rival_choice}
    return choices

def check_win(player, rival):
    print(f"You chose {player}, Rival choice {rival}")
    if player == rival:
        return "You've chose the same type of pokemon , it's a tie!"
    
    elif player =="fire":
        if rival =="plant":
            return "Fire burns plant, You win!"
        else:
            return "Water extinguish fire, You lose!"
    
    elif player =="water":
        if rival =="fire":
            return "Water extinguish fire, You win!"
        else :
            return "Plant absobs water , You lose!"
        
    elif player =="plant":
        if rival =="water":
            return "Plant absobs water , You win"
        else:
            return "Fire burns plant, You lose! "

choices = pokemon_type()
result = check_win(choices ["player"], choices ["rival"])
print (result)

            
        