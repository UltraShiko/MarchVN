
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    frame:

        pos (0,0)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background "gui/title_screen/background.png"

        add "gui/title_screen/logo.png":

            xsize 1300
            ysize 392
            xalign 0.45
            ypos 50

        vbox:

            xalign 0.5
            yalign 0.96

            spacing 13

            imagebutton auto "gui/title_screen/start_%s.png" action Start()

            imagebutton auto "gui/title_screen/load_%s.png" action ShowMenu("load")

            imagebutton auto "gui/title_screen/option_%s.png" action ShowMenu("preferences")

            imagebutton auto "gui/title_screen/codex_%s.png" action ShowMenu("codex_default")

            imagebutton auto "gui/title_screen/credits_%s.png" action ShowMenu("about")

            imagebutton auto "gui/title_screen/quit_%s.png" action Quit(confirm=not main_menu)
