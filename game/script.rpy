﻿
label start:

    menu:

        "What do you want to do?"

        "Test credits.":

            window hide

            $ quick_menu = False

            show screen cinematic_credits_screen()

            pause

            hide screen cinematic_credits_screen

            window show

            $ quick_menu = True

            jump start

        "Unlock compendium entries test.":

            $ clearCompedium()

            $ unlockCompendionEntry("JubileeLore")
            $ unlockCompendionEntry("CelestialLore")
            $ unlockCompendionEntry("NephilimLore")
            $ unlockCompendionEntry("TerraflitLore")

            jump start

        "Play the game.":

            pass

    jump intro

    return
