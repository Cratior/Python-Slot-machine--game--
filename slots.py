import random
import time

# Define the possible faces for the slot machine
faces = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

wins = 0
losses = 0
played = 0

def spin():
    global wins, losses, played
    
    # Generate three random faces for the slot machine
    slot1 = random.choice(faces)
    slot2 = random.choice(faces)
    slot3 = random.choice(faces)
    
    # Display the slot machine visuals
    print("----------- Slot Machine -----------")
    print("|   {}   |   {}   |   {}   |".format(slot1, slot2, slot3))
    print("------------------------------------")
    
    # Check for a win
    if slot1 == slot2 == slot3:
        print("Congratulations! You won!")
        wins += 1
        played+=1
    else:
        print("Sorry, you didn't win. Try again!")
        losses += 1
        played+=1
    
    # Calculate and display win percentage
    total_games = wins + losses
    win_percentage = (wins / total_games) * 100 if total_games > 0 else 0
    print("Win Percentage: {:.2f}%".format(win_percentage))
    print(f"games played {played}")

# Game Loop
while True:
    # Clear the console
    print("\033c", end="")
    
    # Emulate spinning animation
    for _ in range(11):
        slot1 = random.choice(faces)
        slot2 = random.choice(faces)
        slot3 = random.choice(faces)
        print("Spinning...")
        print("|   {}   |   {}   |   {}   |".format(slot1, slot2, slot3))
        time.sleep(0.17)  # Delay for 0.5 seconds
        # Clear the console
        print("\033c", end="")
    
    # Final spin
    spin()
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break