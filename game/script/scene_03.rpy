
label scene_03:

    #scene background cave entrance
    play music night-ambience 
    queue music night-ambience loop

    "As we brush past the thickets, we come upon a cave."
    extend " It has crude, wooden doors at the entrance, much like you'd expect from hovels owned by brigands."
    "What catches my eye, however, are the roses."
    extend " The outskirts of the area are decorated with bushes of purple roses: Hecate's symbol."
    "To be so bold as to place your beliefs out in the open, especially when growing purple roses is forbidden..."
    extend " Does their faith inspire that arrogance, or do they have reason to be so open?"
    "To the side of the door stands a man cloaked in purple robes, nodding off."
    extend " If he's on watch, he's doing a poor job..."
    "Griswyr and I crouch beneath the bushes. The Thorn continues his daydreaming, mumbling to himself."

    nvl clear

    #show cultist silhouette at center with dissolve
    cu "Oh man, tonight's the night! We can finally take back what's ours!"
    extend " Those damned Celestials chased us out of the city, and for what?! I baked bread! Worshiping mother wasn't hurtin' nobody!"
    cu "But damn, why did I get stuck outside? I wanna see her emerge on that altar. Gotta make sure she's given a warm welcome!"
    cu "Well, she'll be out soon enough. There's no sign of any Celestials, guess I can take it easy until then. After all, chanting is hard work..."

    "He really enjoys talking to himself..."
    extend " Was he trying to summon the Archfiend herself? It can't be that simple..."
    hide Cultist
    #show Griswyr neutral at center with dissolve
    "I shudder, spotting Griswyr on all fours."
    extend " He leers at the cultist like a wolf would at a deer!"

    nvl clear

    #show Griswyr neutral at center with dissolve
    g "Alright, recruit, deal with him."

    c "Wh-What?! Just by myself?!"

    g "Did I stutter?"

    c "Shouldn't we move together? We don't have much time..."

    g "There's no guarantee that we'll make it. And I wish to see what you're capable of. Now go!"

    c "Ugh, yes sir..."

    hide Griswyr with dissolve
    play sound forestfootsteps loop
    "I stumble out from the bushes. I was prepared to fight, but not by myself..."
    "Alright, what's my plan?"
    extend " Perhaps I could rush him. If I'm quick, I could knock him out and slip inside."
    "But what if there are others watching from behind the door?"
    extend " I can't see anyone from the other side, yet I would still be risking getting swamped by an ambush."
    "Hmm, maybe I could convince them to let me inside? Many have called me a monk, so I could claim I'm a pilgrim of Hecate.."
    extend "But I don't know anything about Hecate's faith. If they test me, I won't-"

    nvl clear

    stop sound
    
    cu "Who the hell are you?!" with vpunch

    "Ah no..."
    #show cultist silhouette with dissolve
    "He draws his kukri and strides towards me."
    extend " I toss my hands in the air, stammering like a child."

    nvl clear

    c "Ah! I-I mean no harm! I-I'm just a m-monk, and I was-was just going for a walk!"

    cu "Out here, in the depths of the forest, near midnight?"

    c "Yes...I was enjoying myself a bit too much and got a little lost."
    extend " Um, would you happen to know the way back to Jubilee?"

    cu "...Hmm."

    "It takes all my self control not to attack as he draws closer."
    "My heart races! Is he going to cut me?"
    extend " A broad smile answers my worries. It's as if he's forgotten he's upset."
    "Hold on, did my plan actually work?!"

    nvl clear

    cu "Just keep heading straight, and you'll find the road." 
    extend " If you got this far, you should be okay on your own."

    c "Ahh! Is it that simple?! I made so many twists and turns..."

    cu "It is a nice night. That full moon is splendid!"

    c "Yes, sir...!"

    cu "Wait, you said you were a monk?"

    c "Uh huh..."

    cu "Who do you worship?"

    c "Ummm, Yeshua!"

    cu "Ha, I never would've guessed."

    "Why is he being so nice to me...? Especially after I said Yeshua?"
    extend " If memory serves, Hecate detests Yeshua specifically. I believe she's still vengeful about her banishment"

    nvl clear

    cu "You monks are a dime a dozen! Can't believe you'd come this far without an escort."

    c "Well haha, I have faith in my lord..."

    cu "Ahh, I can relate. So do I!"

    play sound sfx.weaponswing
    queue sound sfx.bam
    queue sound sfx.thud

    #hide Cultist moveoutbottom

    "Within a blink of an eye, he swings the knife and I strike his chest."
    "I tremble. So he was just leading me on? How could I be so naive...?"
    extend " Had I been a second slower..."

    nvl clear

    show griswyr at center with dissolve

    g "So what was your strategy, there?"

    c "I have no idea..."

    g "Well, you got him away from the door... I suppose some praise is in order."

    c "We can hide him in the rose bushes. When he wakes up, being tangled up in there will slow him down."

    g "..."
    extend "You think he's going to wake up?"

    c "Huh?"

    play sound sfx.blood_splatter
    with bloodflash

    "Did Griswyr just..."
    extend "cut that man's throat?!"
    "The Thorn's gurgled chokes ring through my ears, and Griswyr licks his sword."
    extend " My stomach grows nauseous... What is the point of this...? He's not scaring anyone but me..."
    "Time stands still. The body wriggles slightly before going stiff..."
    extend " I close my eyes multiple times, just to open them to the same carnage..."

    nvl clear
    
    g "If any cultists are on patrol, I say we leave the body in the open."
    extend " It'll give them a taste of what awaits them."

    c "...Why?"

    g "Oh? Do you feel sorry for him?"

    c "That's...not how we do things. He should have been tried by the Law, not us..."

    g "I don't see the problem. He would've been killed either way."
    extend " If anything, he got off easy. I doubt he even knows he's dead."

    c "Griswyr...!"

    g "What? Are you going to tell me he could've been redeemed?"
    extend " He didn't think twice when he tried to remove your head."

    c "..."
    extend "I don't like this. We're Emmisaries. We protect people, not butcher them..."

    g "Yes, we should give a man who wanted to plunge our world into Hell another chance."
    extend " Why? So he could give us lip service and try again?"

    c "You're assuming again, Griswyr."
    extend " Devils prey on weakness. Not all of their worshipers are malicious. A lot of them didn't have a choice..."

    g "And I'm supposed to care?"
    extend " The road to Hell is paved with good intentions. If you try to bring a fiend into this world, you are an enemy of humanity no matter your reasons."

    c "And if they were deceived?"

    g "If a devil tricks you, that is a failure on your end. Even a simpleton knows not to believe those monsters."
    extend " People aren't blameless. That man knew what he was signing up for. And now he is with his wretched goddess."

    c "And has become another asset for her ranks..."
    g "So be it. He's locked in Hell and no longer our concern."
    extend " If you're done preaching, can we resume our objective?"

    c "...Yes sir."

    "I'm heartbroken. I knew he would be cold, but not heartless..."
    extend " I understand his fears, but I don't agree with his methods. I hope that he doesn't expect me to take someone's life so..."
    extend "callously."
    "Perhaps I care because of my guilt."
    extend " Dretchlings are prime targets for Devils. Their bitter mistreatment by others pushes those poor souls straight into their hands."
    "I only hoped that a saint would give {i}him{/i} the compassion I couldn't..."

    nvl clear

    hide griswyr
    stop music fadeout 1.5
    scene image "#000" with dissolve

    jump scene_04

    return
