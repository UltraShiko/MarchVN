
label scene_06:

    v "By Yeshua, I knew I shouldn't have let him leave!"
    v "Enough. He needs rest. You can't treat all injuries with mana."
    v "Damn you, Emissary!"
    v "I'll accept your insults. I should be dead myself." 
    extend " In fact, I'd prefer death over the position we're in now..."
    v "Oh! He's waking up! Thank goodness!"

    scene background slums

    show Jory sad at center
    show griswyr at left

    with dissolve(0.8)

    "I stir wearily, wrapped in bandages in more places than I can fathom..."
    "I find myself in Jory's arms... It still hurts to move, but it looks like I've pulled through."
    "Griswyr stands in the corner, at a distant as always."

    nvl clear

    j "By Yeshua, are you alright?!"

    c "Ngh....well, I'm still breathing so..."

    g "Luckily most of his injuries weren't deep. Those broken ribs are going to need some time, not like you can move anyways."
    g "You nearly burnt all of your mana, Caius. A drop more, and you would be a corpse."

    j "It shouldn't have ended this way!"
    j "What came of this?! All you did was put my friend in bandages! You didn't even kill the devil!"

    g "I know, and I'm very upset... She's going to be a problem."
    extend " Caius was the only reason we lived. This won't make you feel better, but I believe he'll make a fine Emissary."
    g "If he wants to, that is."

    play sound sfx.heavybam
    with vpunch
    "The ground quakes from Jory's stomp!"
    "I know he didn't mean to, but damn that hurts my ribs..."
    extend " Of course Griswyr hardly cares..."

    nvl clear

    j "Get out! We're done here!"
    extend " It may be his choice, but I don't want to see you or your kind ever again!"

    g "As you wish."
    extend " I'll find Caius when my superior makes a decision. I won't blame him if he wants to reconsider joining after last night."
    g " Until next time."

    hide griswyr with dissolve

    j "Grr... Damn it! Why does this keep happening my friends?!"

    c "Hey...it's not your fault, sir."
    extend " I couldn't stop thinking about you... I kept pushing myself for your sake..."

    j "Oh right, you made that promise..."
    extend " But I'm not the one who needs to be protected!"

    c "On that, we'll have to agree to disagree..."

    j "By Yeshua, you're as stubborn as always..."

    c "Hey Jory, when I'm better..."
    extend " Can we visit Thrycia?"

    j "I...thought you wanted to become an Emissary first."

    c "I did, but after last night, I'm ready to go back now."
    extend " I may not be able to change anything yet, but I can still see him..."

    "Jory sighs deeply and closes his eyes."

    nvl clear

    j "Caius...there's something you need to know."
    extend " While you were gone, word hit Jubilee, and..."
    c "And...?"

    "He gulps hard and speaks slowly."

    nvl clear

    j "Thrycia..."
    extend "is no more."

    c "Huh...?"

    j "No one is sure of what happened, but the rumors say a devil was involved..."

    c "A devil...?!"

    j "Two... Apparently, a dretchling summoned it. I'm sorry..."

    c "Gngh!" with vpunch

    "I swear I hear Persephone's words in my mind again."

    nvl clear

    p "Don't worry, I'll leave Jory be, just as you wished. Anything to get away from you..."

    "My mouth falls agape. I stare at Jory in utter denial."
    "My heart races, tears fall from my cheeks, but all I can do is remain paralyzed in shock..."
    "Yet again, I was too weak...and now."
    extend " There's nothing I can do to save him...!"

    nvl clear

    c "...Priam?!"

    play sound magic_charge
    with graceflash

    j "Woah!"

    c "PRRRRRRRIIIIIIIIIAAAAAAAAMMMMMM!!!" with vpunch

    $ quick_menu = False

    window hide

    scene image "#fff" with iris_in_out_slow

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
    return

    #### Game ends
