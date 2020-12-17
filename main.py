from replit import clear
import art
print(art.logo)
# form art import logo
# print(logo)
test = {}


x = "yes"
#def find_highest_bidder(bidding_record):
#  highest_bid = 0
#  winner = ""
#  # bidding_record = {"Angela": 123, "James": 321}
#  for bidder in bidding_record:
#    bid_amount = bidding_record[bidder]
#    if bid_amount > highest_bid: 
#      highest_bid = bid_amount
#      winner = bidder
#  print(f"The winner is {winner} with a bid of ${highest_bid}")

while x != "no":
    X1 = input("Pls Enter your Name?")
    Y1 = int(input("Pls Enter your bid? $"))
    test[X1] = Y1
    x = input("Do you want to bid - Yes or No").lower()
    if x == "yes":
      clear()

#z = test[max(test, key=test.get)]
z = max(test, key=test.get)
#print(test)
#find_highest_bidder(test)
clear()
print(f"The Winner is {z}")