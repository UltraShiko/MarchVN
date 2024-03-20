
### Auxiliar animations.

transform credits_text_fade(pause_time, fadein_time, hold_time, fadeout_time):

    alpha 0.0

    pause pause_time

    ease fadein_time alpha 1.0

    pause hold_time

    ease fadeout_time alpha 0.0

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

#
# define gui.about = _p("""

# {b}{/b}
#
#  ({a=https://yoruuta.itch.io}Itch.io{/a})
#
# {b}{/b}
#
#  ({a=https://twitter.com/mediamonochrome}Twitter{/a})


### Screen definition

screen cinematic_credits_screen():

    timer 20.0 action Return()

    frame:

        pos (0,0)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background "#000"

        ### Credit page 1
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Director & Lead Writer", "TotalLeeAwesome")

            null height 150 width 0

            use credits_screen_role_and_name("Script Editor", "Jenna Rose")

            at credits_text_fade(0.0, 1.0, 2.0, 1.0)

        ### Credit page 2
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Background artist", "Lynnasaurus")

            null height 150 width 0

            use credits_screen_role_and_name("Sprite Artist", "Kate")

            at credits_text_fade(5.0, 1.0, 2.0, 1.0)

        ### Credit page 3
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Cinematography", "ragyuo")

            null height 150 width 0

            use credits_screen_role_and_name("GUI & Logo Designer, UI coding, Marketing Assets", "senchousan")

            at credits_text_fade(10.0, 1.0, 2.0, 1.0)

        ### Credit page 4
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Coding", "YoruUta")

            null height 150 width 0

            use credits_screen_role_and_name("Sound Composer", "Monochrome")

            at credits_text_fade(15.0, 1.0, 2.0, 1.0)


screen credits_screen_role_and_name(role, name):

    text role:

        style "credits_text_role_style"

    null height 15 width 0

    text name:

        style "credits_text_name_style"
