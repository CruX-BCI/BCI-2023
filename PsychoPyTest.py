# Import necessary libraries
from psychopy import visual, core
import random

# Create a window for the experiment
win = visual.Window(size=(800, 600), fullscr=False)

# Define the stimuli
tongue_image = visual.ImageStim(win, image='tongue_image.png')
feet_image = visual.ImageStim(win, image='feet_image.png')
instruction_text = visual.TextStim(win, text='clench jaw')

# Define the timing parameters
iti_min = 3.0  # minimum inter-trial interval in seconds
iti_max = 5.0  # maximum inter-trial interval in seconds
stim_duration = 5.0  # duration of image presentation in seconds

# Set up the experiment
for trial in range(10):
    # Display a blank screen for a semi-random inter-trial interval
    iti_duration = random.uniform(iti_min, iti_max)
    core.wait(iti_duration)

    # Display the "clench jaw" instruction for 1 second
    instruction_text.draw()
    win.flip()
    core.wait(1.0)

    # Display a random image for 5 seconds
    if random.randint(0, 1) == 0:
        tongue_image.draw()
    else:
        feet_image.draw()

    win.flip()
    core.wait(stim_duration)

# Clean up and exit the experiment
win.close()
core.quit()