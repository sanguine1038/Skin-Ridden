# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define J = Character("Jacob")

default TestVar = True #noisemaker
default RegretSwi = False

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

    menu:

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

label GameOver:

    "I tense up as the realization enters my mind..."
    "They found me."


    #change so there's a jumpscare and Game Over text
    return

label notStart:

    # add voice here

    "Riley is dead. {w}They put her in a dirty grinder."
    "I saw The Family eating her parts, or at least what I assumed were her parts."
    show kitchen with fade
    "I was locked in a cage beforehand, although when they took Riley away I was able to hide in a nearby closet."
    "They don’t know I left."
    "While they were gone I was able to collect a bunch of things and make a Noisemaker."
    "Basically a small ball where when it hits the ground a bunch of stuff will pop out and make a ton of noise."
    "Although I think I’m having second thoughts."
    "What should I do?"

    menu:

        "Continue hiding":
            "This might be a bad idea... I’m going to save it."
            "I try to calm down and see the situation fully."
            "My best friend has been killed and I’m hiding from my family."
            "I’m scared..."
            "I readjust my grip on the Noisemaker, the sweat dripping all over me loosening my grip."
            jump Familyback

        "Throw Noisemaker":
            $ TestVar = False
            "I threw the Noisemaker."
            "A pitiful clunk noise happens as it falls down, before everything tied in it shoots outwards."
            "I cover my ears from hearing it, the noise is so awful."
            jump Familyback

label Familyback:
    "I hear the mumbles of the Family getting closer."
    "They notice I’m not in the room and start looking around, making strange noises."
    "One passes by my hiding spot, I see a long string of saliva dripping down."
    "The urge to vomit starts, like a water bottle being squeezed, it goes up my throat."
    "I suppress it however, covering my mouth I gulp it all down."
    "They pass by."
    "What should I do now?"

label RegretDeci:

    menu:

        "Continue hiding":
            "This isn’t safe, they’ll check another room soon enough."
            "I need to stay hidden."
            # add figure standing
            "..."
            "They stand right in front of my hiding spot."
            "I cover my mouth so they don’t hear me breathing."
            "A thick dirty hand comes inside, I see scars and pieces of their skin gone."
            jump GameOver

        "Escape silently":

            if RegretSwi:
                "I rush myself across the room, to a dirty door frame."
                jump Hallway
            else:
                "I open the closet door as quietly as I can."
                "I stop for a moment to look around, they’re all looking away."
                "Is this the right decision?"
                $ RegretSwi = True
                jump RegretDeci

label Hallway:
    hide kitchen with dissolve
    pause 0.9

    show hallway with fade
    "I see a dirty hallway with 4 doorways."
    "I still hear the murmuring from the Family behind me."
    "I hear them get even closer..."
    "I need to make a decision quickly...!"

    menu:

        "Closer Door (Left)":

            jump DeathDoor

        "Closer Door (Right)":

            jump DeathDoor

        "Far Door (Left)":

            "The light shines as I feel the breeze from outside comforts the tense heat I felt."
            "I’m free..."
            hide hallway with dissolve
            jump Outside

        "Far Door (Right)":

            jump DeathDoor

label DeathDoor:
    hide hallway with dissolve
    pause 0.9

    show death room with fade
    "I enter some strange room with trash everywhere."
    "The dampness of the room is matched by the stress I feel hearing the Family behind me."
    "The mumbles and gibberish they speak gives me goosebumps as they get closer."
    "...They’re getting closer..."
    "I start to panic and look around the room."
    "Dry paint buckets and broken wooden planks flood the floor."
    "I knocked one over, very loudly."
    "I turn around to see a figure staring at me..."
    jump GameOver


label Outside:

    "YOUR MOM"

    return
