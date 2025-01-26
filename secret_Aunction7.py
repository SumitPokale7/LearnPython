import os

hammer = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''


def highest_Bidder(bidding_Dictionary):
    winner = ""
    highest_Bid = 0

    max(bidding_Dictionary)

    for bidder in bidding_Dictionary:
        bid_Amount = bidding_Dictionary[bidder]
        if bid_Amount > highest_Bid:
            highest_Bid = bid_Amount
            winner = bidder

    print(f"The Winner is {winner} with a bid of ${highest_Bid}")


print(hammer)
bid_collection = {}
continue_Bidding = True
while continue_Bidding:
    name = input("What is your name?: ")
    bid_Price = int(input("What is your Bid?: $"))
    bid_collection[name] = bid_Price
    should_Continue = input("Are there any other bidders?Type 'yes' or 'no'.")
    should_Continue.lower()

    if should_Continue == "yes":
        os.system('cls')
        print("\n" * 20)
    else:
        continue_Bidding = False
        highest_Bidder(bid_collection)
