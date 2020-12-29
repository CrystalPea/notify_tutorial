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

    jump main_menu


label main_menu:
    scene bg homepage
    show pg smug at right

    pg "So what would you like to do today?"
    menu:
        "Send bulk messages":
            jump send_bulk

        "Send an email":
            jump send_one_email

        "I'd like to quit for now":
            jump end


label send_bulk:
    scene bg homepage
    show pg smug at right

    pg "Let's send many emails."
    jump main_menu


label send_one_email:
    scene bg homepage
    show pg smug at right

    pg "Let's send one email."
    jump main_menu


label end:
    return
