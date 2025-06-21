import art
print(art.logo)

bid = 0
bidding_finished = False
names_of_bidders = {}
while not bidding_finished:
    name = input("enter your name: ")
    price = float(input("enter your bid: $"))
    names_of_bidders[name]=price
    continue_bid = input("are there any other bidders? Type 'yes' or 'no'.\n")
    if continue_bid == "no":
        bidding_finished = True
best_number = 0
name_of_winner = ""
for key in names_of_bidders:
    if names_of_bidders[key]>best_number:
        best_number = names_of_bidders[key]
        name_of_winner = key
print(f"the winner is {name_of_winner} with a bid of ${best_number}")