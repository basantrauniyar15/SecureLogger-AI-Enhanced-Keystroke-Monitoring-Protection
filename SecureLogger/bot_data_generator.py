import numpy as np
import random

# Generate synthetic bot keystroke timing data
def generate_bot_data(samples=1000):
    bot_keystrokes = []
    
    for _ in range(samples):
        hold_time = round(random.uniform(0.01, 0.05), 3)  # Bots type extremely fast and uniformly
        bot_keystrokes.append([hold_time])

    return np.array(bot_keystrokes)

# Save bot data
bot_data = generate_bot_data(500)  # Generate 500 bot samples
np.save("bot_keystroke_data.npy", bot_data)

print("Bot keystroke data generated and saved!")
