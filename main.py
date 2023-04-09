from getpass import getpass as input

# welcome the user
print("Welcome to Rock, Paper, Scissors")
print()
print("Pick R, P, S")
print()
# assign player 1 and 2
player_1=input("player1, pick: ")
player_2=input("player2, pick: ")
# conditions to find the answer
if player_1=="R" and player_2=="R":
  print("Rock and Rock, It's a draw")
elif player_1=="R" and player_2=="P":
  print("Paper covers Rock, player2 wins!")
elif player_1=="R" and player_2=="S":
  print("Rock smashes Scissors, player1 wins!")
elif player_1=="P" and player_2=="P":
  print("Paper and Paper, it's a draw!")
elif player_2=="P" and player_2=="R":
  print("Paper covers Rock, player2 wins!")
elif player_1=="P" and player_2=="S":
  print("Scissors cuts Paper, player2 wins!")
elif player_1=="S" and player_2=="S":
  print("Scissors and Scissors, it's a draw")
elif player_1=="S" and player_2=="R":
  print("Rock smashes Scissors, player2 wins!")
elif player_1=="S" and player_2=="P":
  print("Scissors cuts Paper, player1 wins")