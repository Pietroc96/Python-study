from data_center import profiles
import data_center
import random

print(data_center.logo1)
player_score = 0 
is_game_over = False 


while not is_game_over : 
    character_a = profiles[random.randint(0,len(profiles)-1)]
    character_b = profiles[random.randint(0,len(profiles)-1)]
    if character_b == character_a:
        character_b = profiles[random.randint(0,len(profiles)-1)]   
    print(rf"Character A : {character_a['name']} un\una {character_a['description']}Proviene dal\la {character_a['country']}")
    print(data_center.logo2)
    print(rf"Character B : {character_b['name']} un\una {character_a['description']}Proviene dal\la {character_a['country']}")
    user_choice = input("Who has more followers? 'A' or 'B' ? ").lower()
    if user_choice == "a" and character_a["followers"] > character_b["followers"]:
        player_score += 1
        print(f"Bravo! Hai indovinato.\n"
              f"Il tuo nuovo punteggio è : {player_score}")
    elif user_choice == "b" and character_b["followers"] > character_a["followers"]:
        player_score += 1 
        print(f"Bravo! Hai indovinato.\n"
              f"Il tuo nuovo punteggio è : {player_score}")
    else :
        print(f"Mi dispiace, hai sbagliato.\n "
              f"Il tuo punteggio è di {player_score}")
        is_game_over = True


