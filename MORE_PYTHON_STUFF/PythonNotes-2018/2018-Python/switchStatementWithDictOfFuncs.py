#!/usr/bin/python3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ever miss the switch statement? As you probably know, Python doesn't
# really have a syntactical equivalent, unless you count repeated elif's.
# What you might not know, though, is that you can replicate the behavior
# (if not the cleanliness) of the switch statement by creating a
# dictionary of functions keyed by the value you want to switch on.
#
# For example, say you're handling keystrokes and you need to call a
# different function for each keystroke. Also say you've already defined
# these three functions:

def key_1_pressed():
    print('Key 1 Pressed')

def key_2_pressed():
    print('Key 2 Pressed')

def key_3_pressed():
    print('Key 3 Pressed')

def unknown_key_pressed():
    print('Unknown Key Pressed')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In Python, you would typically use elif's to choose a function:
#
#        keycode = 2
#        if keycode == 1:
#           key_1_pressed()
#        elif keycode == 2:
#           key_2_pressed()
#        elif number == 3:
#           key_3_pressed()
#        else:
#           unknown_key_pressed()
#
#        output is 'Key 2 Pressed'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# But you could also throw all the functions in a dictionary, and key
# them to the value you're switching on. You could even check see if the
# key exists and run some code if it doesn't:

keycode = 2

functions = {
    1: key_1_pressed,
    2: key_2_pressed,
    3: key_3_pressed,
}

functions.get(keycode, unknown_key_pressed)()

