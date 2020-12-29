# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pg = Character("PG")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg homepage

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pg smug at right

    # These display lines of dialogue.

    pg "So I've heard you wanted to learn using Notify?"

    pg "You're in luck, I know quite a few good tips."

    pg "I call them PG tips, hahah :D"

    # This ends the game.

    return
