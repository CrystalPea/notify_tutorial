# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pg = Character("Pidgey")  # noqa

init python:
    intro = True


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

    pg "I call them Pidgey tips :)"

    jump main_menu


label main_menu:
    scene bg homepage
    show pg smug at right

    if intro:
        pg "So I've heard you wanted to learn using Notify?"
        pg "You're in luck, I know quite a few good tips."
        pg "I call them Pidgey tips :)"

    python:
        intro = False
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

    pg "Do you have a Notify Template ready?"
    menu:
        "Yes":
            jump template_ready

        "No":
            jump create_template

    label create_template:
        scene template create
        show pg smug at right
        pg "If you don't have a template yet, you will have to create one. To do it, just click \"New Template\" button." # noqa

        scene template type
        show pg smug at right
        pg "Choose template type. I will go for email here."

        scene template edit
        show pg smug at right
        pg "Now add the content to your template. Formatting options are listed below the input areas. I have added a \"daily tip\" placeholder, to dynamically insert my daily tips. This way I can enter a different one each time I send, how neat !"  # noqa

    label template_ready:
        scene template send
        show pg smug at right
        "ok, time to send our messages out."

    jump main_menu


label send_one_email:
    scene bg homepage
    show pg smug at right

    pg "Let's send one email."
    jump main_menu


label end:
    scene bg homepage
    show pg smug at right
    pg "Okay, bye then!"
    $ renpy.quit()
