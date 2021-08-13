
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NEW IN 3.6: f-strings (!)

name='joe'
pi=3.14159
x=4
y=3

print(f"{' '*x*y} {name} ate some {pi}, type of pi is {type(pi)}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Sammy has {} balloons.".format(5))

      # Sammy has 5 balloons.


sammy_string = "Sammy loves {} {}, and has {} {}."
print(sammy_string.format("open-source", "software", 5, "balloons"))

      # Sammy loves open-source software, and has 5 balloons.


print("Sammy is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "blue", "shark"))

      # Sammy is a shark, blue, and smiling happy!


print("Sammy the {0} {1} a {pr}.".format("shark", "made", pr = "pull request"))

      # Sammy the shark made a pull request.


print("Sammy ate {0:.1f} percent of {1:d} pizza(s)!".format(75.765367, 42))

      # Sammy ate 75.8 percent of 42 pizza(s)!


print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))

      # Sammy has    5 red balloons        !


print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))

      # Sammy has 5    red     balloons    !


print("{:*^20s}".format("Sammy"))

      # *******Sammy********


print("Sammy ate {0:5.0f} percent of a pizza!".format(75.765367))

      # Sammy ate    76 percent of a pizza!


nBalloons = 8
print("Sammy has {} balloons today!".format(nBalloons))

      # Sammy has 8 balloons today!


sammy = "Sammy has {} balloons today!"
nBalloons = 8
print(sammy.format(nBalloons))

      # Sammy has 8 balloons today!


for i in range(3,13):
    print("{:6d} {:6d} {:6d}".format(i, i*i, i*i*i))

      #      3      9     27
      #      4     16     64
      #      5     25    125
      #      6     36    216
      #      7     49    343
      #      8     64    512
      #      9     81    729
      #     10    100   1000
      #     11    121   1331
      #     12    144   1728


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               +- Index into the format parameters for the value to be displayed
#               | +- Center the value within the displayed field
#               | |+- Length to be displayed
#               | ||+- We are displaying an integer
#               | |||          +- Index into the format parameters for the value to be displayed
#               | |||          | +- Display leading zeroes
#               | |||          | |+- Length to be displayed
#               | |||          | ||+- (decimal marker)
#               | |||          | |||+- Limit to 1 decimal place
#               | |||          | ||||+- We are displaying a float
#               | |||          | |||||

print("ABCDEF: {3:^8d} VWXYZ: {0:06.3f}\n".format(3.14159, 42, 42, 17, 42, 42, "bogus"))

      # ABCDEF:    17    VWXYZ: 3.141

