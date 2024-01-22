MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
#when u do it in all caps its a constant meaning its value won't change

def deposit():
  while True:
    amount = input("What would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("The amount must be greater than 0!")
    else:
      print("Please enter a number!")
  return amount

def get_number_of_lines():
  while True:
    number_of_lines = input("How many lines would you like to bet on? 1-"+str(MAX_LINES) + "? ")
    if number_of_lines.isdigit:
      number_of_lines = int(number_of_lines)
      if 1<=number_of_lines<=MAX_LINES:
        break
      else:
        print("Please enter a number from 1 to 3")
    else:
      print("Please enter a number")
  return number_of_lines
def get_bet():
  while True: 
    amount = input("What would you like to bet on each line? $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET<= amount <= MAX_BET:
        break
      else:
        print("The amount must be between "+str(MIN_BET)+ " and " + str(MAX_BET))
    else:
      print("Please enter a number!")
  return amount









def main():
  balance = deposit()
  number_of_lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet*number_of_lines

    if total_bet>balance:
      print("You do not have enough to bet that amount. your total balance is $" + str(balance))
    else:
      break
  print("You are betting $" +str(bet) + " on " + str(number_of_lines) + " lines.The total bet is equal to $" +str(total_bet))
  
main()