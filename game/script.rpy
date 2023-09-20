# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define J = Character("Jacob")

default TestVar = True

# The game starts here.

label start:

    jump notStart

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    J "this is a pretty funny test"

    menu: #NEEDS a label to jump to

        "this is a choice with text underneath"

        "Turn on Test variable":
            $ TestVar = True
            jump LabelTest

        "Keep Test variable off":
            jump LabelTest

label LabelTest:

    J "the test variable is now..."

    if TestVar: #the start is assuming is already on
        J "True!"
    else:
        J "False!"

    J "NOW FUCKING LEAVE."

    # This ends the game.

    return


label notStart:

    # add voice here

    "Riley is dead. They put her in a dirty grinder."
    "I saw The Family eating her parts, or at least what I assumed were her parts."
    show kitchen
    "I was locked in a cage beforehand, although when they took Riley away I was able to hide in a nearby closet."
    "They don’t know I left."
    "While they were gone I was able to collect a bunch of things and make a Noisemaker."
    "Basically a small ball where when it hits the ground a bunch of stuff will pop out and make a ton of noise."
    "Although I think I’m having second thoughts."
    "What should I do?"

    menu:

        "Continue hiding":
            #
            jump LabelTest

        "Throw Noisemaker":
            #
            jump LabelTest

    return
