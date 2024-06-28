
import random

words = "privilege details donner un coup poudre boulevard anguille coincidence grenade vision gemmes"
words_list = words.split()
secret = random.randint(0,len(words_list) -1)
secret_word = words_list[secret]
game = {
     "secret_word":secret_word,
     "guess_word" : "_" * len(secret_word),
     "life": 9
}

print(f"{ game["guess_word"] } | vie: {game['life']}")

while True:
    letter = input('?>')
    if letter in game["secret_word"] and letter not in game ["guess_word"]:
       guess_word_list = list(game["guess_word"]) 
       for index, current_letter in  enumerate (game['secret_word']):
          if current_letter == letter:
             guess_word_list[index] = letter
             game["guess_word"] = "".join(guess_word_list)
    elif letter not in game ["secret_word"]:
        game["life"] -= 1
    
    print(f"{game['guess_word']} | vie: {game['life']} ")

    if "_" not in game ["guess_word"]:
        
        print('gagné !')
        break
    
    elif game["life"] < 1:
       print('perdu !')
       break
    