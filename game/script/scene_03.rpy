
label scene_03:

    scene background cave entrance with fade

    play music bgm.night_ambience volume 0.25

    window show

    "As we brush past the thickets, we come upon a cave."
    extend " There's an eerie, pink radiance leering at me from within."
    "What catches my eye, however, are the roses."
    extend " The outskirts of the area are decorated with bushes of purple roses: Hecate's symbol."
    "To be so bold as to place your beliefs out in the open, especially when growing any type of rose is forbidden..."
    extend " Does their faith inspire that arrogance, or do they have reason to be so open?"

    window hide

    show Cultist at center with dissolve

    window show

    "To the side of the entrance stands a man cloaked in purple robes, nodding off."
    extend " If he's on watch, he's doing a poor job..."
    "Griswyr and I crouch beneath the bushes. The Thorn continues his daydreaming, mumbling to himself."

    voice "audio/voice/cultist_a/scene_03_01_take2.ogg"
    cu_a "Oh man, tonight's the night! We can finally take back what's ours!"

    voice "audio/voice/cultist_a/scene_03_02_take6.ogg"
    extend " Those damned Celestials chased us out of the city, and for what?! I baked bread! Worshiping mother wasn't hurtin' nobody!"

    voice "audio/voice/cultist_a/scene_03_03_take2.ogg"
    cu_a "But damn, why did I get stuck outside? I wanna see her emerge on that altar. Gotta make sure she's given a warm welcome!"

    voice "audio/voice/cultist_a/scene_03_04_take2.ogg"
    cu_a "Well, she'll be out soon enough. There's no sign of any Celestials, guess I can take it easy until then. After all, chanting is hard work..."

    "He really enjoys talking to himself..."
    extend " Was he trying to summon the Archfiend herself? It can't be that simple..."

    window hide

    hide Cultist with dissolve

    show Griswyr neutral at center with dissolve

    window show

    "I shudder, spotting Griswyr on all fours."
    extend " He leers at the cultist like a wolf would at a deer!"

    voice "audio/voice/griswyr/scene_03_01_take3.ogg"
    g "Alright, recruit, deal with him."

    voice "audio/voice/caius/scene_03_01_take1.ogg"
    c snide "Wh-What?! Just by myself?!"

    voice "audio/voice/griswyr/scene_03_02_take1.ogg"
    g "Did I stutter?"

    voice "audio/voice/caius/scene_03_02_take3.ogg"
    c "Shouldn't we move together? We don't have much time..."

    voice "audio/voice/griswyr/scene_03_03_take1.ogg"
    g "There's no guarantee that we'll make it back. And I wish to see what you're capable of. Now go!"

    voice "audio/voice/caius/scene_03_03_take4.ogg"
    c snide "Ugh, yes sir..."

    window hide

    hide Griswyr with dissolve

    play sound sfx.forestfootsteps loop

    window show

    "I stumble out from the bushes. I was prepared to fight, but not by myself..."
    "Alright, what's my plan?"
    extend " Perhaps I could rush him. If I'm quick, I could knock him out and slip inside."
    "But what if there are others watching from deeper inside?"
    extend " I can't see anyone from the other side, yet I would still be risking getting swamped by an ambush."
    "Hmm, maybe I could convince them to let me inside? Many have called me a monk, so I could claim I'm a pilgrim of Hecate.."
    extend "But I don't know anything about Hecate's faith. If they test me, I won't-"

    stop sound

    show Cultist at center

    voice "audio/voice/cultist_a/scene_03_05_take1.ogg"
    cu_a "Who the hell are you?!" with vpunch

    "Ah no..."

    play sound sfx.dagger_draw

    "He draws his kukri and strides towards me."
    extend " I toss my hands in the air, stammering like a child."

    voice "audio/voice/caius/scene_03_04_take2.ogg"
    c snide "Ah! I-I mean no harm! I-I'm just a m-monk, and I was-was just going for a walk!"

    voice "audio/voice/cultist_a/scene_03_06_take9.ogg"
    cu_a "Out here, in the depths of the forest, near midnight?"

    voice "audio/voice/caius/scene_03_05_take1.ogg"
    c "Yes! I was enjoying myself a bit too much and got a little lost."
    voice "audio/voice/caius/scene_03_06_take4.ogg"
    extend " Um, would you happen to know the way back to Jubilee?"

    voice "audio/voice/cultist_a/scene_03_07_take6.ogg"
    cu_a "...Hmm."

    "It takes all my self control not to attack as he draws closer."
    "My heart races! Is he going to cut me?"
    extend " A broad smile answers my worries. It's as if he's forgotten he's upset."
    "Hold on, did my plan actually work?!"

    voice "audio/voice/cultist_a/scene_03_08_take6.ogg"
    cu_a "Just keep heading straight, and you'll find the road."

    voice "audio/voice/cultist_a/scene_03_09_take6.ogg"
    extend " If you got this far, you should be okay on your own."

    # TODO: Missing audio file
    # voice "None"
    c smile "Ahh! Is it that simple?! I made so many twists and turns..."

    voice "audio/voice/cultist_a/scene_03_10_take1.ogg"
    cu_a "It is a nice night. That full moon is splendid!"

    voice "audio/voice/caius/scene_03_08_take2.ogg"
    c "Yes, sir...!"

    voice "audio/voice/cultist_a/scene_03_11_take3.ogg"
    cu_a "Wait, you said you were a monk?"

    # TODO: Missing audio file.
    # voice "NONE"
    c snide "Uh huh..."

    voice "audio/voice/cultist_a/scene_03_12_take2.ogg"
    cu_a "Who do you worship?"

    voice "audio/voice/caius/scene_03_10_take2.ogg"
    c snide "Ummm, Yeshua!"

    voice "audio/voice/cultist_a/scene_03_13_take3.ogg"
    cu_a "Ha, I never would've guessed."

    "Why is he being so nice to me...? Especially after I said Yeshua?"
    extend " If memory serves, Hecate detests Yeshua specifically. I believe she's still vengeful about her banishment."

    voice "audio/voice/cultist_a/scene_03_14_take4.ogg"
    cu_a "You monks are a dime a dozen! Can't believe you'd come this far without an escort."

    voice "audio/voice/cultist_a/scene_03_11_take1.ogg"
    c smile "Well haha, I have faith in my lord..."

    voice "audio/voice/cultist_a/scene_03_15_take2.ogg"
    cu_a "Ahh, I can relate. So do I!"

    window hide

    play sound sfx.weapon_swing

    pause 0.6

    voice "audio/voice/cultist_a/scene_03_16_take9.ogg"

    play sound sfx.jab

    show Cultist:

        ease 0.1 xoffset -10
        ease 0.1 xoffset 10
        ease 0.1 xoffset -10
        ease 0.1 xoffset 0

    pause 0.4

    show Cultist:

        ease 0.3 yoffset 150

    pause 0.1

    play sound sfx.thud

    hide Cultist with Dissolve(0.2)

    stop sound

    window show

    "Within a blink of an eye, he swings the knife and I strike his chest."
    "I tremble. So he was just leading me on? How could I be so naive...?"
    extend " Had I been a second slower..."

    window hide

    show Griswyr neutral at center with dissolve

    window show

    voice "audio/voice/griswyr/scene_03_04_take2.ogg"
    g "So what was your strategy, there?"

    voice "audio/voice/caius/scene_03_12_take5.ogg"
    c snide "I have no idea..."

    voice "audio/voice/griswyr/scene_03_05_take2.ogg"
    g "Well, you got him away from the door... I suppose some praise is in order."

    voice "audio/voice/caius/scene_03_13_take2.ogg"
    c "We can hide him in the rose bushes. When he wakes up, being tangled up in there will slow him down."

    # No voice
    g "..."
    voice "audio/voice/griswyr/scene_03_06_take5.ogg"
    extend "You think he's going to wake up?"

    voice "audio/voice/caius/scene_03_14_take9.ogg"
    c "Huh?"

    play sound sfx.heavyslash
    with bloodflash

    "Did Griswyr just..."
    extend "cut that man's throat?!"
    "The Thorn's gurgled chokes ring through my ears, and Griswyr licks his sword."
    extend " My stomach grows nauseous... What is the point of this...? He's not scaring anyone but me..."
    "Time stands still. The body wriggles slightly before going stiff..."
    extend " I close my eyes multiple times, just to open them to the same carnage..."

    voice "audio/voice/griswyr/scene_03_07_take4.ogg"
    g "If any cultists are on patrol, I say we leave the body in the open."
    voice "audio/voice/griswyr/scene_03_08_take3.ogg"
    extend " It'll give them a taste of what awaits them."

    voice "audio/voice/caius/scene_03_15_take3.ogg"
    c angry "...Why?"

    voice "audio/voice/griswyr/scene_03_09_take2.ogg"
    g "Oh? Do you feel sorry for him?"

    voice "audio/voice/caius/scene_03_16_take4.ogg"
    c angry "That's...not how we do things. He should have been tried by the Law, not us..."

    voice "audio/voice/griswyr/scene_03_10_take2.ogg"
    g "I don't see the problem. He would've been killed either way."
    voice "audio/voice/griswyr/scene_03_11_take1.ogg"
    extend " If anything, he got off easy. I doubt he even knows he's dead."

    voice "audio/voice/caius/scene_03_17_take4.ogg"
    c angry "Griswyr...!"

    voice "audio/voice/griswyr/scene_03_12_take3.ogg"
    g "What? Are you going to tell me he could've been redeemed?"
    voice "audio/voice/griswyr/scene_03_13_take2.ogg"
    extend " He didn't think twice when he tried to remove your head."

    voice "<to 4.0>audio/voice/caius/scene_03_18_take3.ogg"
    c angry "..."
    voice "<from 4.27>audio/voice/caius/scene_03_18_take3.ogg"
    extend "I don't like this. We're Emissaries. We protect people, not butcher them..."

    voice "audio/voice/griswyr/scene_03_14_take2.ogg"
    g "Yes, we should give a man who wanted to plunge our world into Hell another chance."
    voice "audio/voice/griswyr/scene_03_15_take3.ogg"
    extend " Why? So he could give us lip service and try again?"

    voice "audio/voice/caius/scene_03_19_take2.ogg"
    c angry "You're assuming again, Griswyr."
    voice "audio/voice/caius/scene_03_20_take2.ogg"
    extend " Devils prey on weakness. Not all of their worshipers are malicious. A lot of them didn't have a choice..."

    voice "audio/voice/griswyr/scene_03_16_take4.ogg"
    g "And I'm supposed to care?"
    voice "audio/voice/griswyr/scene_03_17_take1.ogg"
    extend " The road to Hell is paved with good intentions. If you try to bring a fiend into this world, you are an enemy of humanity no matter your reasons."

    voice "audio/voice/caius/scene_03_21_take3.ogg"
    c angry "And if they were deceived?"

    voice "audio/voice/griswyr/scene_03_18_take1.ogg"
    g "If a devil tricks you, that is a failure on your end. Even a simpleton knows not to believe those monsters."
    voice "audio/voice/griswyr/scene_03_19_take2.ogg"
    extend " People aren't blameless. That man knew what he was signing up for. And now he is with his wretched goddess."

    voice "audio/voice/caius/scene_03_22_take3.ogg"
    c snide "And has become another asset for her ranks..."

    voice "audio/voice/griswyr/scene_03_20_take1.ogg"
    g "So be it. He's locked in Hell and no longer our concern."
    voice "audio/voice/griswyr/scene_03_21_take2.ogg"
    extend " If you're done preaching, can we resume our objective?"

    voice "audio/voice/caius/scene_03_23_take5.ogg"
    c "...Yes sir."

    "I'm heartbroken. I knew he would be cold, but not heartless..."
    extend " I understand his fears, but I don't agree with his methods. I hope that he doesn't expect me to take someone's life so..."
    extend "callously."
    "Perhaps I care because of my guilt."
    extend " Dretchlings are prime targets for Devils. Their bitter mistreatment by others pushes those poor souls straight into their hands."
    "I only hoped that a saint would give {i}him{/i} the compassion I couldn't..."

    window hide

    hide Griswyr with dissolve

    scene background cave entrance at truecenter:

        zoom 1.0

        easeout 2.0 zoom 1.5

    stop music fadeout 1.5

    pause 1.4

    scene image "#000" with dissolve

    jump scene_04

    return
