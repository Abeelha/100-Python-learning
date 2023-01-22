# Theodoro Bertol Dev (Abeelha) #
# || Day 4 of #100DaysOfCode || #

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_Y = int(position [0]) -1
position_X =  int(position [1]) - 1

if position_X == 0:
    if position_Y == 0:
        row1[0] = "X"
    if position_Y == 1:
        row1[1] = "X"
    if position_Y == 2:
        row1[2] = "X"
if position_X == 1:
    if position_Y == 0:
        row2[0] = "X"
    if position_Y == 1:
        row2[1] = "X"
    if position_Y == 2:
        row2[2] = "X"
if position_X == 2:
    if position_Y == 0:
        row3[0] = "X"
    if position_Y == 1:
        row3[1] = "X"
    if position_Y == 2:
        row3[2] = "X"

print(f"{row1}\n{row2}\n{row3}")

