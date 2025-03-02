# Scroller Text 
# Adapted from Kevin McAleer May 2022

from scroller import Scroller

from time import sleep

# create a message to display

message = "HELLO WORLD"
# message = "abdefghijklmnopqrstuvwxyz0123456789"
# message = "? / \ < > ( ) ~ ' | . , "

# create a scroller 0bject
scroll = Scroller()

# set the hue colour (0 is red etc)
hue = 0

scroll.clear()

while True or KeyboardInterrupt:
    for position in range(16,-len(message*(5+1)),-1):
        if hue <=1 or hue == 0:
            hue += 0.01
        else: hue = 0
        
        # uncomment the next section to make the brightness pulse
        if scroll.brightness ==1 or scroll.brightness >= 0.1:
            scroll.brightness -= 0.1
        else: scroll.brightness = 1
        scroll.show_message(message, position, hue)
        sleep(0.09)

scroll.clear()