import random
print("Winning rules of the game ROCK🪨 PAPER🧻 SCIRRORS✂️ are:\n"
      + "Rock🪨 vs Paper🧻 -> Paper🧻 wins \n"
      + "Rock🪨 vs Scirrors✂️ -> Rock🪨 wins \n"
      + "Paper🧻 vs Scirrors✂️ -> Scirrors✂️ wins \n")
while True:
    print("choices are: \n 1-Rock🪨 \n 2-Paper🧻 \n 3-Scirrors✂️ \n")
    choice = int(input("Enter your choice:"))
    while choice >3 or choice < 1:
        choice = int(input("Enter a valid choice please :"))
    if choice ==1:
        choice_name = 'Rock🪨'
    if choice == 2:
        choice_name = 'paper🧻'
    if choice == 3:
        choice_name = 'Scirrors✂️'
    print('Your choice is:',choice_name)
    print('\n Now its computer choice ')
    comp_choice = random.randint(1, 3)
    if comp_choice ==1:
        comp_choice_name = 'Rock🪨'
    if comp_choice == 2:
        comp_choice_name = "Paper🧻"
    if comp_choice ==3:
        comp_choice_name = 'Scirrors✂️'
    print('computer choice is:',comp_choice_name)
    print(choice_name,' vs',comp_choice_name)
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1 ) or (choice == 3 and comp_choice == 2):
        result = 'Win'
    else:
        result = 'Lose'

    if result == 'DRAW':
        print('\n == Its a tie !!! == 🫱🏻‍🫲🏻')
    elif result == 'Win':
        print('\n== You win !!! ==🎉')
    else:
        print('\n == You lose !!! == 🤭')
    
    print('\n Do you want to play again? (Yes/No)')
    ans = input()
    if ans == "No":
        print('\n Thanks for playing !!! ☺️')
        break
   