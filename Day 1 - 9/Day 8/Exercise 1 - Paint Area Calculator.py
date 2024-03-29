# Theodoro Bertol Dev (Abeelha) #
# || Day 8 of #100DaysOfCode || #

# number of cans = (wall height x wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5

# = 1.6

# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

def paint_calc(height, width, cover):
    number_of_cans = round((height * width) / cover)
    
    print(f"You'll need {number_of_cans} cans of paint.")

# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

