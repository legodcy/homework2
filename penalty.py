import random

dirs = ["Left", "Center", "Right"]
you = 0
cpu = 0

for r in range(1, 6):
    print("\n--- Round", r, "---")

    # You shoot, the computer keeper dives randomly
    shot = int(input("Your shot (1-Left 2-Center 3-Right): ")) - 1
    dive = random.randrange(3)
    print("Keeper dived", dirs[dive])
    if shot == dive:
        print("Saved!")
    else:
        print("GOAL!")
        you += 1

    # The computer shoots randomly, you dive
    dive = int(input("Your dive (1-Left 2-Center 3-Right): ")) - 1
    shot = random.randrange(3)
    print("Computer shot", dirs[shot])
    if shot == dive:
        print("You saved it!")
    else:
        print("Computer scored!")
        cpu += 1

    print("Score: You", you, "-", cpu, "Computer")

print("\n=== Final Result ===")
print("You", you, "-", cpu, "Computer")

if you > cpu:
    print("You win!")
elif cpu > you:
    print("Computer wins!")
else:
    print("Draw!")
