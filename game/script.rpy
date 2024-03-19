
label start:

    menu:

        "What do you want to do?"

        "Test credits.":

            window hide

            show screen cinematic_credits_screen()

            pause

            window show

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
