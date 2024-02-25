# The script of the game goes in this file.

init python:
    import datetime

define config.developer = True
define config.log = "debug.txt"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Saves created while I go back and forth between happy and sad cause a 'possible infinite loop' exception when loaded."

    $ renpy.suspend_rollback(True)
    label loop:
        $ renpy.log("In the loop!" + str(datetime.datetime.now()))
        show eileen sad
        pause 1
        show eileen happy
        pause 1
        jump loop
        # the actual game has a listener for a button click that jumps to cont that I haven't replicated here.

    label cont:
        $ renpy.suspend_rollback(False)

    # This ends the game.

    return
