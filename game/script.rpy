# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define J = Character("Jacob")
define K = Character("Kimberly")
define P = Character("Policeman")

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

    show blackbg with fade
    stop music fadeout 1.0
    "I tense up as the realization enters my mind..."
    "They found me."

    play sound "blood.mp3"
    show red
    show overwatch with fade
    ""

    return

label notStart:

    play sound "new33-2.mp3"
    pause 35.0

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

    play music "forest amb.mp3"
    show forest with fade
    "But the outside wasn’t what I thought it was going to look like."
    "It looks like it’s early afternoon."
    "The Family’s murmurs turn into full on yelps and screams of frustration."
    "I need to make a decision soon..."
    "Where should I go?"

    menu:

        "Continue in the forest":

            "There are more hiding spots in the forest if they keep trying to find me, that’s gotta be the better option."
            "I walk forward, being as quiet as I could be."
            hide forest with dissolve
            jump ForestRoute

        "Try to find the road":

            "If I go on the road then I’m sure I’ll be able to find someone to help."
            stop music fadeout 1.0
            "I ran as quietly as I could’ve."
            hide forest with dissolve
            jump RoadRoute



label ForestRoute:

    show forest2 with fade
    "As I follow a path, it slowly becomes more and more rocky."
    "I hear more and more noises around the forest, it terrifies me."
    "With every bush rustle and tree branch snap, I spin around."
    "I need to push forward... If not then I’ll end up just like Riley...!"
    play sound "branch.mp3"
    "..."
    "What was that noise?"
    "My mind is going everywhere... What should I do?"

    menu:

        "Try to find a place to hide":

            "I hold my breath and sneak into a nearby bush."
            show bush with fade
            play sound "branch.mp3"
            "Something pushes against me."
            "Probably just some rock."
            "I pushed it aside and heard a grunt."
            "..."
            "It took me a moment to realize what I did."
            "I turn around and see a man with gross and sweaty hair."
            "He turns to me with cut up skin on his face..."
            jump GameOver

        "Keep going down the path":

            "I need to hurry up, I think they’re watching..."
            "I hear strange noises behind me and I start to speed up."
            "The noises... They get closer and closer..."
            "I get faster and faster..."
            "Soon enough I start to run as fast as I can, with branches breaking all around me."
            "Are they after me? Are they close? How far are they?"
            "My thoughts are interrupted by something peculiar..."
            hide hallway with dissolve
            show house with fade
            "An old house, the path seems to continue a bit before being blocked off by some logs."
            "I turn around to see some bushes moving."
            "I'm scared..."
            "I think if I go inside of the house I could trick the Family following me."
            "I think that’s them following me at least..."
            "I need to go in...{w} Now."
            stop music fadeout 1.0
            hide house with dissolve
            show inside with fade
            "I enter the house and I can’t help but cough from all the dust."
            "Thankfully the floor isn’t crowded so there’s no way I’d be making any kind of noise."
            "Although there’s a strange doll that looks so realistic..."
            "It’s so drab..."
            "What should I try to do now?"
            if TestVar:
                jump HouseEnding1
            else:
                jump HouseEnding2

label HouseEnding1:

    "...Wait..."
    "I have an idea...!"
    "I reach into my pocket and look at my Noisemaker."
    "If I use this then I could hide and make them think I ran off..."
    "I have a bad feeling about this, but I need to do it!"
    "I threw it as hard as I could and hid underneath a staircase that the doll was laying on."
    "I hear them stumbling inside with groans."
    "It’s almost as if they’re trying to talk to each other..."
    "I held my breath for as long as I could’ve."
    "Dread builds inside of me..."
    play sound "noises2.mp3"
    pause 20.0
    "..."
    "Are they gone?"
    "I wasn’t really planning on what to do now..."

    menu:

        "Leave":

            jump HouseEnding11

        "Wait longer":

            "Can never be too sure..."
            "I wait until I see the sunset and the area dim."
            jump HouseEnding12

label HouseEnding11:

    hide inside with dissolve
    show outsidenoon with fade
    jump HouseEnding13

label HouseEnding12:

    hide inside with dissolve
    show outsidenight with fade
    jump HouseEnding13

label HouseEnding13:

    "I turn up to the sky and have a realization..."
    "It’s so beautiful... Not only that but I survived..."
    "At least I think..."
    "I look all around and see some marks on the ground."
    "I crouch down to inspect it more and notice that they’re footprints going off in another direction."
    "I’m safe. I’m free."
    pause 2.0
    "Ending 1 - Distracted Nightmares"
    return

label HouseEnding2:

    "I start looking around and searching my pockets. I have nothing to work with..."
    "As my mind starts to race I hear moans and groans outside. I start sweating with no plan."
    "Without thinking I ran behind the stairs with the strange doll."
    "The door slams open as I see figures entering."
    "It’s almost as if they’re trying to talk to each other..."
    "I held my breath for as long as I could’ve."
    "Dread builds inside of me..."
    play sound "noises.mp3"
    pause 13.0
    "..."
    "Are they gone? What should I do?"

    menu:

        "Leave":

            "I peek my head out, scanning the room, when all of a sudden."
            "My hair is pulled very tightly."
            "I try to fight back, run away, push their arm away, anything...{w} But nothing worked..."
            jump GameOver

        "Wait longer":

            "Can never be too safe..."
            "I stay as quiet as I can while still trying to look around the room."
            "I hear their strange breathing, the noise feeling so alien."
            "Drool falls down to the floor. I can’t help but look at them, they have such a dirty yellow color to it..."
            play sound "noises2.mp3"
            pause 20.0
            "..."
            "Are they gone? What should I do?"
            "Can never be too sure..."
            "I wait a while before emerging from my hiding spot."
            "The inside of the house is completely dark."
            "I guess now would be a better time than ever to leave..."
            jump HouseEnding22

label HouseEnding22:

    hide inside with dissolve
    show outsidenight with fade
    "I turn up to the sky and have a realization..."
    "It’s so beautiful... Not only that but I survived..."
    "At least I think..."
    "I look all around and see some marks on the ground."
    "I crouch down to inspect it more and notice that they’re footprints going off in another direction."
    "I’m safe. I’m free."
    pause 2.0
    "Ending 2 - Death’s Doorway"
    return

label RoadRoute:

    hide forest with dissolve
    show road with fade
    "The road stretches almost infinitely."
    "The bright sky starts to dim as it’s getting late."
    "I struggle  making things known in my own mind as everything starts to shake around me."
    "I see small animals come out of bushes, trees start to shake and I start to hear strange noises..."
    "What should I do?"

    menu:

        "Hide":

            "I calm myself down and go into a bush nearby."
            show bush with fade
            play sound "branch.mp3"
            "Soon enough I see a figure walk extremely close to me."
            "It gets closer... and closer... and closer..."
            "Until eventually stopping and a strange sniffing sound starts to emerge."
            "Are they trying to sniff me out?"
            "I need to stay silent for a moment."
            play sound "noises3.mp3"
            pause 12.0
            "..."
            "Are they gone?"
            "I peek my head out for a moment only to notice footprints leading back into the forest."
            "I did it...? Do they think I’m still in the forest now?"
            "I would love to jump in joy right now if I wasn’t so terrified..."
            "I start to quicken my pace again."
            "My vision gets more and more blurry until I notice something..."
            jump NotPolice

        "Start running":

            "I start to quicken my pace. My mind starts to race looking all around me."
            "My view shaking from running makes me feel so dizzy..."
            show daddy with fade
            "I keep on going as fast as I can until I see someone..."
            hide daddy with dissolve
            show daddy2 with fade
            "They slowly approach me and I can’t help but try to run backwards."
            hide daddy2 with dissolve
            show daddy3 with fade
            "I do until I bump into someone else."
            jump GameOver

label NotPolice:

    hide road with dissolve
    show police with fade
    "A police station...?"
    "A society..."
    "Real people! That can help!!"
    "I ran inside to tell them all..."
    "I’ll get justice for Riley..."
    hide police with dissolve
    show police2 with fade
    K "HELP MY FRIEND IS DEAD TO A BUNCH OF CANNIBALS WHO WERE JUST AFTER ME! YOU GOTTA HELP ME!!"
    "The man behind the glass looks at me with a strange look."
    "Dropping a pen he moves his chair to be facing me."
    P "Alright then... How about we take this one thing at a time."
    P "You’re safe now, you’re in our custody."
    P "Now tell us what’s going on."
    K "M-Me and my friend Riley went on a trip to the forest and all of a sudden this weird ass family with axes kidnapped us into this small and dirty house!"
    K "We were locked in a closet and they dragged Riley away before shoving her in a grinder..."
    P "Holy shit... You’re Kimberly Pearl... The news was about you just now!"
    K "Jeez, already? Well, whatever!"
    K "Can you help me?!"
    P "Well I would love to but you see..."
    P "It’s a bit difficult to just say ‘Hey! Someone said there’s something weird over there, let’s check it out!’"
    K "Why the hell not?!"
    P "Well, false reports happen all the time. We need some kind of hard proof evidence that something weird is over there."
    P "Do you have anything like that?"
    if TestVar:
        jump PoliceEnding1
    else:
        jump PoliceEnding2

label PoliceEnding1:

    K "I have this... Does that count?"
    P "What the hell is it?"
    K "It’s a noisemaker I made trying to distract the family. I ended up never using it."
    P "...Works out for me."
    hide police2 with dissolve
    play sound new33-3
    pause 43.0
    "Ending 3 - Evident"
    return

label PoliceEnding2:

    K "I got... Nothing."
    P "Then... I’m sorry..."
    K "But-"
    P "Here on file it says that you’re below the age of 18, would you like us to contact an adult? A parent or guardian?"
    K "Um... Yea... My mom’s phone number is 305-555-7820..."
    "Nothing in return for my survival."
    "Other than my life, I guess..."
    "Everyday I sleep terrified of what I saw."
    "I wish I could’ve more."
    "I’m sorry, Riley..."
    "I’m sorry for not giving you more..."
    "I think this might be the worst way this could’ve gone..."
    "...I'm sorry..."
    pause 2.0
    "Ending 4 - Justice Craven"
    return
