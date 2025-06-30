offers = {}
auction = True

while auction:
    name = input("What is your name? ")
    price = int(input("What is your bid? USD "))
    offers[name] = price
    other = input("Are there any other bidders? Type 'yes' or 'no'. ")
    print("\n" * 100)
    if other == "no":
        auction = False

highest_bid = 0
winner = ""
for bidder in offers:
    if offers[bidder] > highest_bid:
        highest_bid = offers[bidder]
        winner = bidder

print(f"The highest bid is {highest_bid} by {winner}.")