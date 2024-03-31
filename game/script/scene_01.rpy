
label scene_01:

    pause 0.5

    play music bgm.VillageAmbienceLoop fadein 1.5

    scene background slums with Dissolve(1.0)

    window show

    c "Ngh..."

    "Damn it, my mind wandered off again. I’m supposed to be preparing for my trial."
    "It's been five years...and those memories still haunt me."
    extend " No matter how much I've repented, I still haven’t been able to shake their hold over me. I can't forgive myself, no matter what I do to atone."
    "Five years... I wonder how he's doing..."
    extend " It wasn't his fault. The whole thing was just a big mistake. We were cornered, he didn’t have any other choice..."
    "Once I become an Emmisary though, I'll change everything. I'll make things right."

    # nvl clear

    v "Hey, how are you holding up?"

    window hide

    show Jory happy at center with dissolve

    window show

    "I shudder as the giant approaches me."
    extend " I never understood how a man so big could be so quiet."

    # nvl clear

    c smile "I'm managing, thanks for asking, sir."

    j "...You're not going to stop calling me that, are you?"
    extend " We're family! We don't need formalities!"

    c smile "I prefer them. You did adopt me, I want to show my respect."

    j "Respect? I don't care about that. I'm proud of you, Caius! You've grown into a fine man!"

    extend " And now, you're going away..."

    "As jovial as he was trying to be, I read him like a book."
    extend " Jory supports me, but I know he doesn't want me to leave. Like he said, we're family."
    $ unlockCompendionEntry("EmissaryLore")
    extend " That and the mortality rate for Emissaries is high."
    "They say death is a daily occurrence in their ranks. I've heard tales that some of the recruits are criminals forced to join them or face execution."
    extend " Apparently, many prefer the noose..."
    "The Emmisaries aren't like normal Celestials. They aren't guards. Instead, they go out and confront problems directly."
    extend " Whether it be outlaws, spies from Jorunderfell, witches, or devils, they hunt down every last one of them."
    "I don’t blame Jory for worrying. I might not be the same person when – if – I return..."
    extend " Still, I had to go. I only met Jory because the Reverend took pity on me. I had to make things right."
    "I could enlist as a Celestial, but the Emissaries often work alongside the Reverend, or at least closely with him."
    extend " Even if Jory knows him well, I would still rather impress the Reverend with my own deeds instead of relying on Jory buttering him up."

    # nvl clear

    c "You've taught me well, sir."
    extend " From combat, to controlling mana, to keeping my mind pure. I'm ready!"

    # TODO:
    show Jory neutral with dissolve

    j "Oh of course you are, it's just..."
    extend " A lot of people join the Emmisaries, and it breaks them."
    j " I'm not trying to trample on your dream, but are you sure there's no other way?"

    # TODO:
    show Jory happy with dissolve

    extend " I mean, look at me! I never joined the Emmisaries, and I'm the Reverend's right hand man!"
    j "It's not just about what you accomplish Caius, it's about who you know and the impressions you make."
    extend " I mean, that's why we met. The Reverend plopped you at my doorstep, remember?"

    "How could I not?"
    extend " When he found me, crying over that Celestial's corpse so many years ago, I thought my fate was sealed...."
    "From what I hear, the Reverend is a tyrant. But that's what I saw..."
    extend " I mean, I took the blame. I told them that the bloody dagger was mine and I was the murderer."
    "He didn't believe me. I could tell..."
    extend " Rather than executing me though, he said something that I'll never forget..."

    # nvl clear

    v "Blessed are the peacekeepers. Blessed are those who relinquish themselves for the sake of others."
    extend " I do not know what really transpired, but I'm thankful I met someone as noble as you. You remind me of why I took up the mantle."
    v "Although the crime committed is great, his end was his own doing."
    extend " As your reverend, I command you to rise. Your friend will not face retribution."

    "...I haven't seen him since. I’ve been too ashamed, too afraid to face him."
    extend " He was spared, but that didn't erase the horrible things I said to him... I treated him no differently than anyone else that day, like a Dretchling whose life had no value."
    extend " So I cannot squander the chance he has given me. I owe my life to Yeshua, and I want to prevent others from making the same mistakes I’ve made."
    #$ unlockCompendionEntry("DretchlingLore")
    "The Dretchlings are a race feared, hated, and even attacked because of their fiendish blood."
    extend " Their horns, hooves, and complexion paint targets on their backs. They resemble the monsters that came before them."
    "Once I rise up through the ranks, putting in laws to protect them will be the first change I implement."
    extend " After all, devils don't need our help harvesting souls. And I hear they flock to Dretchlings like moths to a flame..."

    # nvl clear

    c neutral "Sir, I'm aware of the danger. I've been preparing myself all week."
    c neutral "How can I change this country if I don't have the courage to face the evils I want to abolish? Devils lurk not just in Hell but also in the ears and minds of our leaders."
    c angry "If I don't learn how to deal with them, I'll run the risk of making the same mistake The Third did."

    # TODO:
    show Jory sad with dissolve

    j "Hmmm, he was a terrible man indeed..."

    $ unlockCompendionEntry("HaleLore")

    "The current Reverend is the fourth of his lineage. Jory has told me many stories of how cruel his uncle was."
    "Reverend Hale III, or The Third as we call him, held more executions than any other reverend."
    extend " They say his antics were so atrocious that he caused The Reckoning, where the sky tore open and an agent of the Archfiend Hecate dragged him into Hell..."

    # nvl clear

    c angry "He abused you. He abused everyone! His pride and arrogance caused the Reckoning, and now our country is divided!"

    # TODO:
    show Jory neutral with dissolve

    j "Caius, hear me out..."
    extend " That man's vices weren't because of a fiend. He walked into that fire himself."
    j "Not every act of malice has a devil behind it. We're capable of making decisions, both good and bad..."

    # TODO:
    show Jory sad with dissolve

    j "I know your guilt is heavy, and I know that you want to make things right."
    extend " But you can't let your past blind you. You need to think about the here and now."
    j "If I hadn't done so, Caius, I would've been burnt alive just like her... And we wouldn't be having this conversation."

    "I cringe along with him."
    extend " It takes a lot to get under Jory's skin, and when something does, it’s always about a woman he once cared for..."

    # nvl clear

    c snide "...But you've made amends. I mean, you took me in despite the fact I...you know."

    # TODO:
    show Jory neutral with dissolve

    j "I sure did, and I have no regrets!"
    extend " Still, a day doesn't go by when I don't think about her or how I wanted to avenge her...!"

    "The sight of his fists clenching makes me shudder."
    "I still can’t believe the earlier reverend had the courage to bully Jory or his friends."
    extend " Jory always holds back when we spar, yet his blows still hurt more than anything I’ve ever endured. Yeshua forbid what damage he could cause if he ever got angry enough..."

    # nvl clear

    # TODO:
    show Jory happy with dissolve

    j "Uh whoops! Lost myself there!"

    # TODO:
    show Jory neutral with dissolve

    extend " You get what I mean though, right?"

    c smile "I do, sir. And I appreciate your concern, but my mind is made up."

    j "Oh, I see..."

    c angry "I will make things right, for my friend and Aurielle."
    extend " I won't let anyone make the same mistakes we did!"

    # TODO:
    show Jory sad with dissolve

    j " But...you know what you're getting yourself into, right?"
    extend " These rogues are very strict. I bet your recruiter has some sort of test cooked up for you."
    j "And even if, no when, you complete it, there's not guarantee they'll let you join."
    extend " It's one thing when a condemned criminal is admitted, but another when someone wants to impress them. Their work isn't for everyone..."

    c "I'll manage. I'm not sure how, but I'll figure it out!"

    # TODO:
    show Jory happy with dissolve

    j "Shoot, guess I can't complain then, can I?"

    play sound light_grapple
    "His meaty hand pats my shoulder."
    extend " Well... more like engulfs it."

    # nvl clear

    j "Just come back in one piece, alright?"

    c smile "I promise!"

    v "Hmmm... I knew you took a vow of poverty, but I still expected better lodgings..."

    window hide

    hide Jory with dissolve

    show Griswyr neutral at center with dissolve

    pause 0.75

    window show

    "We turn, and there stands a gaunt man."
    "His pale complexion rivals that of snow, and his hair is just as white."
    "He is almost as skinny as myself, but his arms and legs are chiseled with muscle."
    extend " Despite him being taller than me, he wears only a leather vest and breeches."
    "On one hip rests a shortsword, on the other...a grisly-edged hatchet."
    extend " Then there are his eyes. I feel like I’m peering into an abyss when our gazes meet."
    "This man has to be my recruiter."
    extend " The stories depict Emmisaries as dark, brooding individuals. He fits that description perfectly."
    "He puts away his notebook and looks towards us, emotionless..."

    # nvl clear

    v "You are Caius, correct?"

    c "Yes, sir."

    g "I am Griswyr Alucard. I have come to claim you."

    window hide

    show Jory sad at center_left
    show Griswyr neutral at center_right

    with dissolve

    window show

    j "So late in the day? It'll be night within the hour..."

    g "That's right, it's the perfect time to be on the move. Our foes will strike when we are most vulnerable."
    extend  " That's not a problem, is it?"

    c angry "No sir..."

    "Oh, but it is a BIG problem! I'm not prepared for a nocturnal expedition..."
    extend " I thought the trial would test my skills in combat, not my endurance...."

    # nvl clear

    g "If you are ready, then let's go. Our enemy has already begun their machinations."

    c neutral "Who are we going after?"

    g "You're familiar with the Thorns, correct?"

    c neutral "Hmm, that name doesn't ring a bell..."

    $ unlockCompendionEntry("ThornLore")
    g "They call themselves the {i}Agents of the Rose{/i}, Hecate's cultists, to be precise."

    #show jory silhouete at left flip
    "Jory grimaces audibly."
    extend " I don't blame him. I expected to face a vagabond, an apostate, or a weaker devil, but not an entire cult?!"
    extend " With just the two of us?!"
    "Griswyr's eyes narrow."
    extend " On top of being unprepared, now I’ve earned his ire..."

    # nvl clear

    g "...I'm sorry, did you expect this mission to be simple?"

    c neutral "No, I'm ready for anything."

    g "Many fools have run to their end believing such nonsense."
    extend " It is alright to be intimidated, how you follow through is what matters."
    g "Now let's be off. Time is of the essence."

    c neutral "Yes, sir..."

    window hide

    hide Griswyr with dissolve

    pause 0.5

    show Jory neutral with dissolve

    window show

    "As we depart, Jory waves me off, but the enthusiasm has vanished from his face..."
    "My blood freezes as the sun sets."

    window hide

    scene image "#000" with dissolve

    window show

    extend " Jory just might be onto something, but it's too late for me to back out now..."
    "I suppose it's only natural that the trials of the Emmisaries are just as dangerous as the work they do, and Griswyr has a point."
    extend " I wonder why he chose me for this particular task... I'm as green as they come."

    # nvl clear

    window hide

    stop music
    jump scene_02

    return
