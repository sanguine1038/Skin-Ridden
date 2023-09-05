# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define J = Character("Jacob")

default TestVar = False

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

    J "s"



    show Space at right
    #pos (961, 1078) 

    J "e"

    return