import random

def roll_dice(num_dice=1, num_sides=6):
    """Simulates rolling 'num_dice' dice with 'num_sides' sides."""
    return [random.randint(1, num_sides) for _ in range(num_dice)]

# Example: Rolling 2 six-sided dice
rolls = roll_dice(num_dice=2)
print("Rolled dice:", rolls)