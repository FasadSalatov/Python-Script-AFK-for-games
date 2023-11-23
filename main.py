import sys
sys.path.insert(0, '\\modules')
import pyautogui
import random
import time
from pynput import keyboard

# Set seed for reproducibility
random.seed()

# Get screen size
screen_width, screen_height = pyautogui.size()

# Flag to track script execution status
script_running = True

# Flag to track pause state
paused = False

# Function for slow mouse movement
def move_mouse_slowly(target_x, target_y):
    current_x, current_y = pyautogui.position()
    steps = 50  # Number of steps for slow movement

    for i in range(steps):
        if not script_running or paused:
            break  # Exit the loop if the flag is changed
        intermediate_x = current_x + (target_x - current_x) * i / steps
        intermediate_y = current_y + (target_y - current_y) * i / steps

        pyautogui.moveTo(intermediate_x, intermediate_y)
        time.sleep(0.001)

# Function to handle key events
def on_key_press(key):
    global script_running, paused

    if key == keyboard.Key.space:
        if not paused:
            paused = True
            print("Script paused.")
        else:
            paused = False
            print("Script resumed.")

# Create a keyboard listener object
listener = keyboard.Listener(on_press=on_key_press)

# Start the listener in a separate thread
listener.start()

try:
    # Main script loop
    while script_running:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        move_mouse_slowly(x, y)

finally:
    # Stop the keyboard listener in the finally block to ensure execution even if an exception occurs
    listener.stop()
