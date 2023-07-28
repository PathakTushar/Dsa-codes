
import random
logo=''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''

print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=["spiderman","batman","superman"]
#print(word_list)
select=random.choice(word_list)
print(select)
word=[]
for i in range(0,len(select)):
    word+="-"
print(word)
life=len(stages)-1
game=True
while game:

    choice=(input("guess an alphabet\n")).lower()
    if choice in word:
        print(f"you already guessed {choice}")
    
    elif choice in select:
        print(f"wow! correct guess,life remaining={life}")
    
    else:
        life-=1
        print(f"oops! wrong guess,life remaining={life}")
        
  
    
        
    if word!=select:
            
            for i in range(0,len(select)):
                
                if choice==select[i]:
                    word[i]=choice       
            print(word)
    
    if life==0:
        print("you loose")
        game=False

    if not"-" in word:
        print("you win")
        game=False

    print(stages[life])