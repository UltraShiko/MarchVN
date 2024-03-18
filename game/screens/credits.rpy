
### Auxiliar animations.

transform credits_text_fade:

    alpha 0.0

    ease 1.0 alpha 1.0

    pause 2.0

    ease 1.0 alpha 0.0

### Auxiliary styles

style credits_text_role_style:

    text_align 0.5
    xalign 0.5

    font "fonts/GARA.TTF"
    size 50
    color "#fff"

    bold True

style credits_text_name_style is credits_text_role_style:

    size 50

    bold False



define credit_text = [

[ ("Director / Lead Writer", "TotalLeeAwesome"), ("Script Editor", "Jenna Rose") ]
[ ("Background Artist", "Lynnesaurus"), ("Sprite Artist", "Kate"), ("Gui Artist & Logo Designer", "senchousan") ]
[ ("Programming", "YoruUta"), ("Sound Composer", "Monochrome") ]

]

### Screen definition

screen credits_screen():

    frame:

        pos (0,0)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background "#000"

        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Director & Lead Writer", "TotalLeeAwesome")

            null height 150 width 0

            use credits_screen_role_and_name("Script Editor", "Jenna Rose")

            # null height 100 width 0
            #
            # use credits_screen_role_and_name("Role 3", "Name 3")

screen credits_screen_role_and_name(role, name):

    text role:

        style "credits_text_role_style"

    null height 15 width 0

    text name:

        style "credits_text_name_style"
