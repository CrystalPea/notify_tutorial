# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pg = Character("Pidgey")  # noqa

init python:
    intro = True


# The game starts here.

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

        jump template_ready

    label template_ready:
        scene template send
        show pg smug at right
        pg "Ok, time to send our messages out. Click \"Send\" button. Do not worry, it will not send anything yet :)"

        scene send recipient
        show pg smug at right
        pg "Now, if you want to send many messages at once, you have to click the link to upload a list of recipients. For emails the link is called \"Upload a list of email addresses\"."  # noqa

        scene send upload
        show pg smug at right
        pg "Now click \"Choose a file\" and find the list you want to upload"

        show example csv:
            xalign 0.0
            yalign 0.2
        pg "Here is the CSV file we will use. It's pretty basic, but it does the job :)"
        hide example csv

        scene send preview
        show pg smug at right
        pg "Once we upload our list, we are on preview page. Here you can check if everything is correct before sending your messages. Also, if you need to change anything about the file you uploaded, we will inform you about it here. If you are ready, click Send button."  # noqa

        scene send done
        show pg smug at right
        pg "And done. That wasn't too bad, eh? :)\nYou will be able to check status of your sending job in the Uploads section."  # noqa

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
