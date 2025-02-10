import random

def roll_dnd_dice(dice_type='d20', num_rolls=1, modifier=0):
    """Rolls a D&D-style dice (e.g., 'd6', 'd20') a number of times with an optional modifier."""
    
    # Extract the number of sides from the dice type (e.g., 'd6' -> 6)
    sides = int(dice_type[1:])
    
    # Roll the dice the specified number of times and sum the results
    rolls = [random.randint(1, sides) for _ in range(num_rolls)]
    
    # Sum up the rolls and add the modifier
    total = sum(rolls) + modifier
    
    # Display the individual rolls and the total
    print(f"Rolls: {rolls}")
    if modifier != 0:
        print(f"Modifier: {modifier}")
    print(f"Total: {total}")
    return total

# Example: Rolling 2d20 with a +3 modifier
roll_dnd_dice('d20', num_rolls=2, modifier=3)
