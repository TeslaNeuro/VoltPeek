# Toggling neo-pixel rainbow colours on a RP2040 development board
# Creator: Arshia Keshvari
# Date: 25th of May 2025

import machine
import neopixel
import time

# Setup: 1 LED on GPIO 16
pin = machine.Pin(16)
np = neopixel.NeoPixel(pin, 1)

# List of RGB colors to cycle through
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 255, 255) # White
]

try:
    while True:
        for color in colors:
            np[0] = color       # Set the color
            np.write()          # Send data to the LED
            time.sleep(0.4)     # Wait 400ms
except KeyboardInterrupt:
    # Turn off the LED on exit
    np[0] = (0, 0, 0)
    np.write()
    print("Stopped by user.")
