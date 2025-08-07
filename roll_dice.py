import random

roll = random.randint(1, 6)
guess = int(input('Guess the dice roll: '))

#if guess == roll:
#  print(f"Correct! They rolled a '{roll}'")
#else:
#  print(f"Wrong! They rolled a '{roll}'")

message  = "Correct!" if guess == roll else "Wrong!"
message += " "
message += f"They rolled a '{roll}'"

print(message)