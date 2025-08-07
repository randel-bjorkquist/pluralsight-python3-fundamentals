import random

choices  = ["rock", "paper", "scissors"]
go_again = True
winner   = False

while(go_again):
  user_choice     = str(input("Do you want rock, paper, or scissors? ")).strip().lower()
  computer_choice = random.choice(choices)

  if user_choice == computer_choice:
    go_again = input("TIE: do you want to try again (y/n)? " ) == "y"

    if go_again:
      continue
    else:
      break

  match computer_choice:
    case "rock":
      winner = user_choice == choices[1]  # "paper" covers "rock"

    case "paper":
      winner = user_choice == choices[2]  # "scissors" cuts "paper"

    case "scissors":
      winner = user_choice == choices[0]  # "rock" smashes "scissors"
    
    case _:
      print("EXCEPTION: should never get here ... exiting now")
      break
        
  message  = "WINNER" if winner else "LOOSER"
  message += f" ({user_choice})"
  message += f": the computer chose '{computer_choice}'"
  message += ". Do you want to try again (y/n)? "

  go_again = input(message) == "y"
