# what we do
# store won cards from each round of war
# Compare stored cards for winner of the round give winner a point (for winning the round)
# Compare points (from rounds) to get complete winner
player = "John"
won_cards1 = []
won_cards2 = []
p1_points = []
p2_points = []
card1 = [1]
card2 = [2]


# round 1
# round points
def round_points(cards1, cards2, player1):
    if len(cards1) > len(cards2):
        p1_points.append(1)
        print(f" {player1} win's the round")
        print(f"{player1} has {len(p1_points)} points\n")
    elif len(cards2) > len(cards1):
        p2_points.append(1)
        print("The computer win's the round")
        print(f"computer has {len(p2_points)} points\n")


round_points(won_cards1, won_cards2, player)
# actually giving points here

# round 2
round_points(won_cards1, won_cards2, player)
# giving points

# printing winners
if len(p1_points) != 2:
    pass
else:
    print(f"{player} wins war!")
    quit()
if len(p2_points) != 2:
    pass
else:
    print("Computer wins war!")
    quit()

# round 3 The tie
round_points(won_cards1, won_cards2, player)
# give points

# print the overall winner
if len(p1_points) == 2:
    print(f"{player} wins war!")
elif len(p2_points) == 2:
    print("Computer wins war!")
