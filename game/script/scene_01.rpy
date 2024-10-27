
label scene_01:

    pause 0.5

    play music bgm.VillageAmbienceLoop fadein 1.5

    scene background slums with Dissolve(1.0)

    pause 2.0

    window show

    voice "audio/voice/caius/scene_01_01_take2.ogg"
    c "Ngh..."

    "Damn it, my mind wandered off again. I’m supposed to be preparing for my trial."
    "It's been five years...and those memories still haunt me."
    extend " No matter how much I've repented, I still haven’t been able to shake their hold over me. I can't forgive myself, no matter what I do to atone."
    "Five years... I wonder how he's doing..."
    extend " It wasn't his fault. The whole thing was just a big mistake. We were cornered, he didn’t have any other choice..."
    "Once I become an Emissary though, I'll change everything. I'll make things right."

    voice "audio/voice/jory/scene_01_01_take3.ogg"
    v "Hey, how are you holding up?"

    window hide

    show Jory happy at center with dissolve

    window show

    "I shudder as the giant approaches me."
    extend " I never understood how a man so big could be so quiet."

    voice "audio/voice/caius/scene_01_02_take2.ogg"
    c smile "I'm managing, thanks for asking, sir."

    voice "audio/voice/jory/scene_01_02_take3.ogg"
    j "...You're not going to stop calling me that, are you?"
    voice "audio/voice/jory/scene_01_03_take2.ogg"
    extend " We're family! We don't need formalities!"

    voice "audio/voice/caius/scene_01_03_take1.ogg"
    c smile "I prefer them. You did adopt me, I want to show my respect."

    voice "audio/voice/jory/scene_01_04_take2.ogg"
    j "Respect? I don't care about that. I'm proud of you, Caius! You've grown into a fine man!"

    show Jory neutral with dissolve

    voice "audio/voice/jory/scene_01_05_take3.ogg"
    extend " And now, you're going away..."

    "As jovial as he was trying to be, I read him like a book."
    extend " Jory supports me, but I know he doesn't want me to leave. Like he said, we're family."

    $ unlockCompendionEntry("EmissaryLore")

    extend " That and the mortality rate for Emissaries is high."
    "They say death is a daily occurrence in their ranks. I've heard tales that some of the recruits are criminals forced to join them or face execution."
    extend " Apparently, many prefer the noose..."
    "The Emissaries aren't like Celestials. They aren't guards. Instead, they go out and confront problems directly."
    extend " Whether it be outlaws, spies from Jorunderfell, witches, or devils, they hunt down every last one of them."
    "I don't blame Jory for worrying. I might not be the same person when - if - I return..."
    extend " Still, I had to go. I only met Jory because the Reverend took pity on me. I had to make things right."

    voice "audio/voice/caius/scene_01_04_take1.ogg"
    c "You've taught me well, sir."
    voice "audio/voice/caius/scene_01_05_take1.ogg"
    extend " From combat, to controlling mana, to keeping my mind pure. I'm ready!"

    show Jory happy with dissolve

    voice "audio/voice/jory/scene_01_06_take3.ogg"
    j "Oh of course you are, it's just..."

    show Jory neutral with dissolve

    voice "audio/voice/jory/scene_01_07_take2.ogg"
    extend " A lot of people join the Emissaries, and it breaks them."
    voice "audio/voice/jory/scene_01_08_take1.ogg"
    j " I'm not trying to trample on your dream, but are you sure there's no other way?"

    show Jory happy with dissolve

    voice "audio/voice/jory/scene_01_09_take2.ogg"
    extend " I mean, look at me! I never joined the Emissaries, and I'm the Reverend's right hand man!"
    voice "audio/voice/jory/scene_01_10_take3.ogg"
    j "It's not just about what you accomplish Caius. It's about who you know and the impressions you make."
    voice "audio/voice/jory/scene_01_11_take3.ogg"
    extend " I mean, that's why we met. The Reverend plopped you at my doorstep, remember?"

    window hide

    stop music fadeout 0.8

    scene image "#000" with iris_in_out_reverse_slow_8

    window show

    "How could I not?"
    extend " When he found me, crying over that Celestial's corpse so many years ago, I thought my fate was sealed...."
    "From what I hear, the Reverend is a tyrant. But that's what I saw..."
    extend "\nI mean, I took the blame. I told them that the bloody dagger was mine and I was the murderer."
    "He didn't believe me. I could tell..."
    extend " Rather than executing me though, he said something that I'll never forget..."

    voice "audio/voice/hale/scene_01_01_take1.ogg"
    hale "Blessed are the peacekeepers. Blessed are those who relinquish themselves for the sake of others."
    voice "audio/voice/hale/scene_01_02_take1.ogg"
    hale "I do not know what really transpired, but I'm thankful I met someone as noble as you. You remind me of why I took up the mantle."
    voice "audio/voice/hale/scene_01_03_take3.ogg"
    hale "Although the crime committed is great, his end was his own doing."
    voice "audio/voice/hale/scene_01_04_take1.ogg"
    extend " As your reverend, I command you to rise. Your friend will not face retribution."

    "...I haven't seen him since. I've been too ashamed, too afraid to face him."

    $ unlockCompendionEntry("DretchlingLore")

    "The Dretchlings are a race feared, hated, and even attacked because of their fiendish blood."
    extend " Once I rise up through the ranks, putting in laws to protect them will be the first change I implement."
    "After all, devils don't need our help harvesting souls. And I hear they flock to Dretchlings like moths to a flame..."

    window hide

    play music bgm.VillageAmbienceLoop fadein 1.5

    scene background slums

    show Jory happy at center

    with iris_in_out_8

    pause 1.2

    window show

    voice "audio/voice/caius/scene_01_06_take3.ogg"
    c neutral "Sir, I'm aware of the danger. I've been preparing myself all week."
    voice "audio/voice/caius/scene_01_07_take3.ogg"
    c neutral "How can I change this country if I don't have the courage to face the evils I want to abolish? Devils lurk not just in Hell but also in the ears and minds of our leaders."
    voice "audio/voice/caius/scene_01_08_take3.ogg"
    c angry "If I don't learn how to deal with them, I'll run the risk of making the same mistake The Third did."

    show Jory sad with dissolve

    voice "audio/voice/jory/scene_01_12_take2.ogg"
    j "Hmmm, he was a terrible man indeed..."

    $ unlockCompendionEntry("HaleLore")

    "The now deceased Reverend Hale III, or The Third as we call him, held more executions than any other reverend."

    $ unlockCompendionEntry("ReckoningLore")

    "They say his cruelty was so atrocious that he caused The Reckoning, where the sky tore open and an agent of the Archfiend Hecate dragged him into Hell..."

    voice "audio/voice/caius/scene_01_09_take3.ogg"
    c angry "He abused you. He abused everyone! His pride and arrogance caused the Reckoning, and now our country is divided!"

    show Jory neutral with dissolve

    voice "audio/voice/jory/scene_01_13_take2.ogg"
    j "Caius, hear me out..."
    voice "audio/voice/jory/scene_01_14_take2.ogg"
    extend " That man's vices weren't because of a fiend. He walked into that fire himself."
    voice "audio/voice/jory/scene_01_15_take3.ogg"
    extend " Not every act of malice has a devil behind it. We're capable of making decisions, both good and bad..."

    show Jory sad with dissolve

    voice "audio/voice/jory/scene_01_16_take2.ogg"
    j "I know your guilt is heavy, and I know that you want to make things right."
    voice "audio/voice/jory/scene_01_17_take1.ogg"
    extend " But you can't let your past blind you. You need to think about the here and now."

    voice "audio/voice/jory/scene_01_18_take2.ogg"
    j "If I hadn't done so, Caius, I would've been burnt alive just like her... And we wouldn't be having this conversation."

    "I cringe along with him."
    extend " It takes a lot to get under Jory's skin, and when something does, it’s always about a woman he once cared for..."

    voice "audio/voice/caius/scene_01_10_take2.ogg"
    c neutral "...But you've made amends. I mean, you took me in despite the fact I...you know."

    show Jory happy with dissolve

    voice "audio/voice/jory/scene_01_19_take1.ogg"
    j "I sure did, and I have no regrets!"

    show Jory angry with dissolve

    voice "audio/voice/jory/scene_01_20_take3.ogg"
    extend " Still, a day doesn't go by when I don't think about her or how I wanted to avenge her...!"

    "The sight of his fists clenching makes me shudder."
    extend " I still can't believe The Third had the courage to bully Jory or his friends."

    show Jory happy with dissolve

    voice "audio/voice/jory/scene_01_21_take2.ogg"
    j "Uh whoops! Lost myself there!"

    voice "audio/voice/jory/scene_01_22_take1.ogg"
    extend " You get what I mean though, right?"

    voice "audio/voice/caius/scene_01_11_take1.ogg"
    c smile "I do, sir. And I appreciate your concern, but my mind is made up."

    show Jory neutral with dissolve

    voice "audio/voice/jory/scene_01_23_take1.ogg"
    j "Oh, I see..."

    voice "<to 4.10>audio/voice/caius/scene_01_12_take1.ogg"
    c angry "I will make things right, for my friend and Aurielle."
    voice "<from 4.7>audio/voice/caius/scene_01_12_take1.ogg"
    extend " I won't let anyone make the same mistakes we did!"

    show Jory sad with dissolve

    voice "audio/voice/jory/scene_01_24_take1.ogg"
    j " But...you know what you're getting yourself into, right?"
    voice "audio/voice/jory/scene_01_25_take1.ogg"
    extend " These rogues are very strict. I bet your recruiter has some sort of test cooked up for you."

    show Jory neutral with dissolve

    voice "audio/voice/jory/scene_01_26_take1.ogg"
    j "And even if - no when, you complete it - there's not guarantee they'll let you join."
    voice "audio/voice/jory/scene_01_27_take3.ogg"
    j "It's one thing when a condemned criminal is admitted, but another when someone wants to impress them. Their work isn't for everyone..."

    voice "audio/voice/caius/scene_01_13_take2.ogg"
    c neutral "I'll manage. I'm not sure how, but I'll figure it out!"

    show Jory happy with dissolve

    voice "audio/voice/jory/scene_01_28_take3.ogg"
    j "Shoot, guess I can't complain then, can I?"

    play sound light_grapple

    "His meaty hand pats my shoulder."
    extend " Well... more like engulfs it."

    voice "audio/voice/jory/scene_01_29_take1.ogg"
    j "Just come back in one piece, alright?"

    voice "audio/voice/caius/scene_01_14_take3.ogg"
    c smile "I promise!"

    voice "audio/voice/griswyr/scene_01_01.ogg"
    v "Hmmm... I knew you took a vow of poverty, but I still expected better lodgings..."

    window hide

    hide Jory with dissolve

    show Griswyr neutral at center with dissolve

    pause 0.75

    window show

    "We turn, and there stands a gaunt man."
    extend " His pale complexion rivals that of snow, and his hair is just as white."
    extend " He is almost as skinny as mye, but his arms and legs are chiseled with muscle."
    "Despite him being an elite, he wears only a leather vest and breeches."
    extend " On one hip rests a shortsword, on the other...a grisly-edged hatchet."
    "Then there are his eyes. I feel like I'm peering into an abyss when our gazes meet."
    "This man has to be my recruiter."
    extend " The stories depict Emissaries as dark, brooding individuals. He fits that description perfectly."
    "He puts away his notebook and looks towards us, disinterested..."

    voice "audio/voice/griswyr/scene_01_02.ogg"
    v "You are Caius, correct?"

    voice "audio/voice/caius/scene_01_15_take2.ogg"
    c "Yes, sir."

    voice "audio/voice/griswyr/scene_01_03.ogg"
    g "I am Griswyr Alucard. I have come to claim you."

    window hide

    show Jory sad at center_left
    show Griswyr neutral at center_right

    with dissolve

    window show

    voice "audio/voice/jory/scene_01_30_take4.ogg"
    j "So late in the day? It'll be night within the hour..."

    voice "audio/voice/griswyr/scene_01_04_take2.ogg"
    g "That's right, it's the perfect time to be on the move. Our foes will strike when we are most vulnerable."
    voice "audio/voice/griswyr/scene_01_05.ogg"
    extend " That's not a problem, is it?"

    voice "audio/voice/caius/scene_01_16_take1.ogg"
    c angry "No sir..."

    "Oh, but it is a BIG problem! I'm not prepared for a nocturnal expedition..."
    extend "\nI thought the trial would test my skills in combat, not my endurance...."

    voice "audio/voice/griswyr/scene_01_06.ogg"
    g "If you are ready, then let's go. Our enemy has already begun their machinations."

    voice "audio/voice/caius/scene_01_17_take3.ogg"
    c neutral "Who are we going after?"

    voice "audio/voice/griswyr/scene_01_07.ogg"
    g "You're familiar with the Thorns, correct?"

    voice "audio/voice/caius/scene_01_18_take1.ogg"
    c neutral "Hmm, that name doesn't ring a bell..."

    $ unlockCompendionEntry("ThornLore")

    voice "audio/voice/griswyr/scene_01_08_take2.ogg"
    g "They call themselves the {i}Agents of the Rose{/i}. Hecate's cultists, to be precise."

    "Jory grimaces."
    extend " I don't blame him. I expected to face a vagabond, an apostate, or a weaker devil, but not an entire cult?!"
    extend " With just the two of us?!"
    "Griswyr's eyes narrow."
    extend " On top of being unprepared, now I've earned his ire..."

    voice "audio/voice/griswyr/scene_01_09_take1.ogg"
    g "...I'm sorry, did you expect this mission to be simple?"

    voice "audio/voice/caius/scene_01_19_take1.ogg"
    c neutral "No, I'm ready for anything."

    voice "audio/voice/griswyr/scene_01_10_take2.ogg"
    g "Many fools have run to their end believing such nonsense."
    voice "audio/voice/griswyr/scene_01_11_take1.ogg"
    extend " It is alright to be intimidated, how you follow through is what matters."
    voice "audio/voice/griswyr/scene_01_12_take3.ogg"
    g "Now let's be off. Time is of the essence."

    voice "audio/voice/caius/scene_01_20_take5.ogg"
    c neutral "Yes, sir..."

    window hide

    hide Griswyr with dissolve

    pause 0.5

    show Jory neutral with dissolve

    window show

    "As we depart, Jory waves me off, but the enthusiasm has vanished from his face..."
    "My blood freezes as the sun sets."

    window hide

    stop music fadeout 1.2

    scene image "#000" with dissolve

    window show

    "Jory just might be onto something, but it's too late for me to back out now..."
    "I suppose it's only natural that the trials of the Emissaries are just as dangerous as the work they do, and Griswyr has a point."
    extend " I wonder why he chose me for this particular task... I'm as green as they come."

    window hide

    stop music

    pause 0.5

    jump scene_02

    return
