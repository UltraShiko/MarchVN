
label scene_06:

    voice "audio/voice/jory/scene_06_01_take2.ogg"
    j "By Yeshua, I knew I shouldn't have let him leave!"

    voice "audio/voice/griswyr/scene_06_01_take1.ogg"
    g "Enough. He needs rest. You can't treat all injuries with mana."

    voice "audio/voice/jory/scene_06_02_take1.ogg"
    j "Damn you, Emissary!"

    voice "audio/voice/griswyr/scene_06_02_take2.ogg"
    g "I'll accept your insults. I should be dead myself."
    voice "audio/voice/griswyr/scene_06_03_take2.ogg"
    extend " In fact, I'd prefer death over the position we're in now..."

    voice "audio/voice/jory/scene_06_03_take3.ogg"
    j "Oh! He's waking up! Thank goodness!"

    window hide

    scene background slums

    show Jory sad at center_left #will add in official sprite after jam
    show Griswyr neutral at center_right behind Jory

    with Dissolve(0.8)

    window show

    "I stir wearily, wrapped in bandages in more places than I can fathom..."
    extend " I find myself in Jory's arms... It still hurts to move, but it looks like I've pulled through."
    "Griswyr stands in the corner, at a distant as always."

    voice "audio/voice/jory/scene_06_04_take1.ogg"
    j "By Yeshua, are you alright?!"

    play music bgm.epilogue fadein 1.5 volume 0.35

    voice "audio/voice/caius/scene_06_01_take3.ogg"
    c snide "Ngh....well, I'm still breathing so..."

    voice "audio/voice/griswyr/scene_06_04_take1.ogg"
    g "Luckily most of his injuries weren't deep. Those broken ribs are going to need some time, not like you can move anyways."
    voice "audio/voice/griswyr/scene_06_05_take2.ogg"
    g "You nearly burnt all of your mana, Caius. A drop more, and you would be a corpse."

    show Jory angry with Dissolve(0.25)

    voice "audio/voice/jory/scene_06_05_take3.ogg"
    j "It shouldn't have ended this way!"
    voice "audio/voice/jory/scene_06_06_take2.ogg"
    j "What came of this?! All you did was put him in bandages! You didn't even kill the devil!"

    voice "audio/voice/griswyr/scene_06_06_take3.ogg"
    g "I know, and I'm very upset... She's going to be a problem."
    voice "audio/voice/griswyr/scene_06_07_take1.ogg"
    extend " Caius was the only reason we lived. This won't make you feel better, but I believe he'll make a fine Emissary."
    voice "audio/voice/griswyr/scene_06_08_take2.ogg"
    g "If he wants to, that is."

    play sound sfx.heavy_bam volume 0.5
    with vpunch

    "The ground quakes from Jory's stomp!"
    "I know he didn't mean to, but damn that hurts my ribs..."
    extend " Of course Griswyr hardly cares..."

    voice "audio/voice/jory/scene_06_07_take1.ogg"
    j "Get out! We're done here!"
    voice "audio/voice/jory/scene_06_08_take1.ogg"
    extend " It may be his choice, but I don't want to see you or your kind ever again!"

    voice "audio/voice/griswyr/scene_06_09_take2.ogg"
    g "As you wish."
    voice "audio/voice/griswyr/scene_06_10_take2.ogg"
    extend " I'll find Caius when my superior makes a decision. I won't blame him if he wants to reconsider joining after last night."
    voice "audio/voice/griswyr/scene_06_11_take3.ogg"
    g "Until next time."

    window hide

    hide Griswyr with dissolve

    pause 0.5

    show Jory sad at center with dissolve

    window show

    voice "audio/voice/jory/scene_06_09_take3.ogg"
    j "Grr... Damn it! Why does this keep happening to those I care for?!"

    voice "audio/voice/caius/scene_06_02_take2.ogg"
    c neutral "Hey...it's not your fault, sir."
    voice "audio/voice/caius/scene_06_03_take2.ogg"
    extend " I couldn't stop thinking about you... I kept pushing myself for your sake..."

    voice "audio/voice/jory/scene_06_10_take2.ogg"
    j "Oh right, you made that promise..."

    show Jory angry with dissolve

    voice "audio/voice/jory/scene_06_11_take1.ogg"
    extend " But I'm not the one who needs to be protected!"

    voice "audio/voice/caius/scene_06_04_take3.ogg"
    c neutral "On that, we'll have to agree to disagree..."

    show Jory neutral with dissolve

    voice "audio/voice/jory/scene_06_12_take3.ogg"
    j "By Yeshua, you're as stubborn as always..."

    # TODO: Replace with REDO.
    voice "audio/voice/caius/scene_06_05_take1.ogg"
    c neutral "Hey Jory, when I'm better..."
    # TODO: Replace with REDO.
    voice "audio/voice/caius/scene_06_06_take2.ogg"
    extend " Can we visit Thrycia?"

    voice "audio/voice/jory/scene_06_13_take3.ogg"
    j "I...thought you wanted to become an Emissary first."

    voice "audio/voice/caius/scene_06_07_take3.ogg"
    c neutral "I did, but after last night, I'm ready to go back now."
    voice "audio/voice/caius/scene_06_08_take3.ogg"
    extend " I may not be able to change anything yet, but I can still see him..."

    show Jory sad with dissolve

    voice "audio/voice/jory/scene_06_14_take1.ogg"
    "Jory sighs deeply." # and closes his eyes." # Removed this part to match the sprite.

    stop music fadeout 5.0

    voice "audio/voice/jory/scene_06_15_take3.ogg"
    j "Caius...there's something you need to know."

    voice "audio/voice/jory/scene_06_16_take2.ogg"
    extend " While you were gone, word hit Jubilee, and..."

    voice "audio/voice/caius/scene_06_09_take1.ogg"
    c neutral "And...?"

    "He gulps hard and speaks slowly."

    voice "<to 1.5>audio/voice/jory/scene_06_17_take1.ogg"
    j "Thrycia..."

    stop music

    voice "<from 2.5>audio/voice/jory/scene_06_17_take1.ogg"
    extend "is no more."

    voice "audio/voice/caius/scene_06_10_take4.ogg"
    c snide "Huh...?"

    voice "audio/voice/jory/scene_06_18_take3.ogg"
    j "No one is sure of what happened, but the rumors say a devil was involved..."

    voice "audio/voice/caius/scene_06_11_take2.ogg"
    c snide "A devil...?!"

    voice "audio/voice/jory/scene_06_19_take2.ogg"
    j "Two... Apparently, a dretchling summoned it. I'm sorry..."

    voice "audio/voice/caius/scene_06_12_take2.ogg"
    c angry "Gngh!" with vpunch

    "I swear I hear Persephone's words in my mind again."

    # TODO: Do a flashback.
    # TODO: Missing line!!
    p "Don't worry, I'll leave Jory be, just as you wished. Anything to get away from you..."

    "My mouth falls agape. I stare at Jory in utter denial."
    "My heart races, tears fall from my cheeks, but all I can do is remain paralyzed in shock..."
    "Yet again, I was too weak...and now."
    extend " There's nothing I can do to save him...!"

    voice "audio/voice/caius/scene_06_13_take2.ogg"
    c snide "...Priam?!"

    play sound magic_charge
    with graceflash

    show Jory neutral with dissolve

    voice "audio/voice/jory/scene_06_20_take2.ogg"
    j "Woah!"

    voice "audio/voice/caius/scene_06_14_take6.ogg"
    c snide "PRRRRRRRIIIIIIIIIAAAAAAAAMMMMMM!!!" with vpunch

    $ quick_menu = False

    window hide

    scene image "#92a9f5" with iris_in_out_slow

    pause 2.0

    scene image "#000" with Dissolve(2.0)

    pause 2.0

    ##############################
    ### Roll credits.
    ##############################

    $ quick_menu = False

    call screen cinematic_credits_screen()

    # Update flag used to determine if the ending has been seen once.
    # From this point forward, the credits can be skipped.
    $ persistent.ending_watched =  True

    pause 1.0

    $ unlockCompendionEntry("HecateLore")

    pause 2.0

    return

    #### Game ends
