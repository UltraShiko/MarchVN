
label intro:

    window hide

    stop music

    scene image "#000"

    pause 2.0

    # nvl clear

    voice "<to 4.08>audio/voice/caius/intro_01_take3.ogg"
    centered "..."

    voice "<from 4.08>audio/voice/caius/intro_01_take3.ogg"
    centered "...I can't believe you did that! You really are a monster!"

    voice "audio/voice/priam/intro_01_take3.ogg"
    centered "Caius, I...I had too! He was going to-"

    voice "audio/voice/caius/intro_02_take3.ogg"
    centered "None of this had to happen!"

    voice "audio/voice/caius/intro_03_take3.ogg"
    extend "\nYour sticky fingers couldn't control themselves! And now a man is dead, and it's all our fault!"

    voice "audio/voice/caius/intro_04_take1.ogg"
    centered "No...it's your fault! You godforsaken Dretchling! They were right about you! You ARE a devil!"

    voice "<to 2.0>audio/voice/priam/intro_01_take3.ogg"
    centered "Caius... I..."

    voice "audio/voice/caius/intro_05_take3.ogg"
    centered "Get the hell away from me! I'll tell the Reverend, so help me!\nI'll see you hanged if you don't get away from me!"

    voice "audio/voice/caius/intro_06_take1.ogg"
    centered "I should've never helped you! I should've left you to starve like the rat you are!"

    voice "audio/voice/caius/intro_07_take3.ogg"
    centered "And now, Yeshua will smite us both..."

    voice "audio/voice/caius/intro_08_take2.ogg"
    extend "\nI could've made something of myself...I didn't want to be a thief my entire life..."

    voice "audio/voice/caius/intro_09_take2.ogg"
    centered "But now I'm a murderer! All because of you!"

    voice "audio/voice/caius/intro_10_take2.ogg"
    centered "I hate you..."

    voice "audio/voice/caius/intro_11_take1.ogg"
    extend " I hate you!!!"

    window hide

    # nvl clear

    jump scene_01

    return
