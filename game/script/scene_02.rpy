
label scene_02:

    scene background forest with dissolve

    play music bgm.night_ambience

    play sound sfx.forestfootsteps loop # TODO: Using placeholder track. Replace with correct one.

    window show

    "A choir of crickets chirps as we leave Jubilee's outskirts."
    "I feel dismayed. The moon's radiance is telling me it's time for bed, but we've only just started our journey..."

    window hide

    show Griswyr neutral at center with dissolve

    window show

    extend " Meanwhile, Griswyr moves like he's in his element, under the cover of night..."
    "Now that I think about it, something is...different about him."
    extend " He can't be a Dretchling. They're pale, but not to his degree. And his eyes don’t share their crimson pupils."
    "Yet the way he carries himself, feels unnatural somehow."
    extend " He looks human, but..."

    # nvl clear

    g "You aren't getting tired already, are you?"

    c "N-No! I'm just...usually in bed by this time."

    g "You'll wake up soon enough. Their cave isn't far from here."

    c angry "R-Right!"
    extend " So, can you tell me about these uhh, \"Thorns\"?"

    g "...It's a band of heretics worshiping an Archfiend. What more do you need to know?"

    c neutral "I mean, their numbers? Their weapons? If there's anyone among them who can cast spells or utilize mana?"

    g "Hmm, I wasn't expecting you to be so resourceful."
    extend " It's a small sect. I doubt there's more than ten of them. I'd imagine their leader can wield magic."

    c smile "Ah! I was expecting something more organized! That eases my mind!"

    g "And they're on the cusp of summoning a devil."

    c neutral "..."
    extend "Tonight?"

    g "Tonight."
    g "If one pops out, this mission becomes much deadlier. Even I will have to be careful.."
    extend " Not like it'll change the outcome, of course."

    c neutral "Hmm..."

    g "I wouldn't have picked someone who was incapable. I have high expectations for you, and I expect to see them met."
    extend " I don't think I need to explain the consequences of a devil escaping."

    c angry "O-Of course not. Not like I'd let them finish summoning it."

    g "How do you intend to stop it?"

    c neutral "Well, if we move together, we can dispatch them  one-by-one."
    extend " I assume this ritual requires a lot of mana. The fewer men they have, the more mana will be needed from each of them."

    g "And you don't think their leader has mana in spades? He's devout, after all. His fervor alone is likely all that's needed."

    c neutral "Well then, we can sneak in, take him out, and-"

    g "Are you so quick to abandon your plans?"

    c snide "But you said-"

    g "So what? One weak point doesn't make a plan fallible."
    extend " If anything, your next suggestion may as well be suicide. What cult would be foolish enough to allow us to assassinate their leader?"
    g "These people are aware of the danger; from us, from rival cults, and from the wrath of their deity."
    extend " If anything, they already know we're coming. Hecate's followers are excellent at blending in."

    c neutral "If I recall correctly, Hecate favors deception. I've heard that even beggars worship her in secret."

    g "Why do you think we have Celestials guarding every orphanage? They're breeding grounds for her acolytes. No one ever suspects caregivers."
    g "I was lucky to locate this cult. Normally they are just as elusive as succubi, but I guess someone got sloppy. Or arrogant."

    c neutral "Alright, then let's discuss tactics."
    extend " I'm good at fighting hand-to-hand, and I have great control of my mana."

    g "You, a fighter? With arms that spindly?"

    c "Yes..."

    "I took a vow of poverty to atone for what I said to my friend."
    extend " I chose to live in poverty, much like he and I were living in before the incident."
    #$ unlockCompendionEntry("CircleLore")
    "It would've been very easy for me to establish a comfortable life. Had I joined the Celestials, I've could've bought a house in the Enlighted Circle."
    "But I wouldn't be able to forgive myself. My friend shouldn't continue to starve while I enjoy myself. Especially when my mistake got me where I am."
    extend " I'm no snake. I'm grateful for where I am, but I will indulge myself once I've changed how Dretchlings are treated."
    "This vow limits my nutrition and spending activities. I only eat enough to sustain myself, and purchase items that are absolutely necessary."
    extend " Jory believes I would have been taller had I eaten a normal diet. But I care little about my appearance."
    "Besides, this vow has forced me to look within myself, to master every thought that passes through."
    extend " And it has made me stronger!"

    # nvl clear

    g "How pious..."
    extend " Too pious! You expect such flimsy arms to have an impact?"

    c smile "That's what my mana is for."

    g "What mana do you wield?"

    $ unlockCompendionEntry("GraceLore")
    c "Grace."
    extend " Normally it doesn't empower its wielder like other mana, but I've learned to manipulate it to my advantage."
    c smile "Grace will be paramount if this monster is summoned."
    $ unlockCompendionEntry("MaliceLore")
    extend " Devils are beings of the dark mana, Malice. Seeing how Grace repels that mana, I'm certain even my jabs will be lethal to it."

    g "It might, assuming you get the chance to use it."

    c "Well as you said, I am feeble. I doubt the fiend will expect much of a fight from me."

    g "Or, it'd take you out first to even the odds."
    extend " Let's say it barrels towards you, wanting to kill you as quickly as possible. What then?"

    c "..."
    extend "Then I'll-"

    g "Too late, you're dead!"
    extend " You hesitated, and it tore your throat out."

    c snide "Oh..."

    g "You don't hesitate. Not for a second. If it attacks, you fight back."
    extend " If it chases after me, you pursue it. If it casts a spell, you dodge. Whatever happens, you adapt!"
    g "I can tell that you spend way too much time thinking, and not enough time acting."
    extend " On a good day, the best plans fail. We're dealing with schemers from Hell itself, what makes you think that you can outwit them?"

    c snide "..."

    g "Humor me. Why do you think I picked you?"

    c "Hmm, I was wondering that myself..."

    g "Two reasons."
    extend " One, for your mana. If this monster is summoned, I need someone to exploit its weakness. I don't channel Grace, nor do I plan on it."

    c snide "So you knew all along?"

    g "Of course I did."
    extend " I know who you are, your abilities, your nature, and more importantly, your origins."

    $ unlockCompendionEntry("ThryciaLore")
    c snide "That means...you know I'm from Thrycia."

    g "I also know about your run-in with the law."

    "I gasp."
    extend " I should've expected no less from an Emissary... Why wouldn't they research their applicants?"
    "Though I had hoped that the reverend and Jory had kept what happened a secret amongst themselves..."

    # nvl clear

    c snide "...How much do you know?"

    g "Enough."
    extend " I know about the Dretchling, and I know about the dead Celestial."
    extend " I also understand that you and the Dretchling were cutpurses at one point."

    c snide "...We were."
    extend " You don't have...plans to arrest my friend, do you?"

    g "That decision is not mine to make."
    extend " I've partnered with murderers, arsonists, champions of Yeshua, fallen champions, it makes no difference to me."
    g "I only care about results."
    extend " Morals mean nothing in the grand scheme of things. If Yeshua felt so obliged, he would get off his lofty throne and solve everything himself."
    g "But he doesn't, so his opinion means nothing to me."
    extend " If principles give you faith, so be it. As long as the mission is accomplished, I don't care."

    c "That's..."
    extend "cold."

    g "Consider it a taste of being an Emissary."
    extend " We aren't heroes, Caius. We're exterminators."
    extend " Those Celestials, or Luminaries as we call them, only serve to assuage the public."
    g "The Celestials that truly care about defending our country join our ranks. Anyone else is just a pretender."

    c "I believe you had a second reason for picking me?"

    "He snarls softly, but quickly recovers his stoicism."

    # nvl clear

    g "Indeed. I picked you because I believe you are driven by regret."
    g "I'm not a fan of the \"righteous crusaders\", or anyone with a savior complex. They may as well be infants."

    "The more he belittles others, the uneasier I grow."
    extend " He's very condescending... I understand that his work is treacherous, yet I can't imagine myself ever becoming so cynical."
    "Is this attitude what Jory meant by the life as an Emissary \"breaking\" people?"

    # nvl clear

    c angry "...With all due respect sir, you are very judgemental."

    g "And?"

    c angry "What's wrong with wanting to protect other people? Would you prefer people to join for money alone?"

    g "Yes, it's a realistic and achievable goal."

    c angry "Well, I hate to upset you, but my motivation isn't too far off from the former."
    extend " Regret is a big part of it, but I want to reform our country into something better."
    c angry "That Dretchling and Jory were victims of oppression."
    extend " I used to be a cutthroat, but I had a choice. My friend...no one would pay a \"mongrel\" to shine their shoes."

    g "Fear - it drives the weak. How unfortunate for him."

    "Hmm, Griswyr still remains unfazed."
    extend " Whenever I bring up my friend being a Dretchling, people always scowl, grimace, or become disgusted. I figured an Emissary would react no differently..."
    "Then again, Griswyr doesn't strike me as normal either."

    # nvl clear

    g "It's a pious goal, but at least it has direction."

    c "Sir, I must know..."
    extend " Are you human?"

    "He blinks at me, as if I'm asking him if the sky was blue."

    # nvl clear

    g "...What makes you think otherwise?"

    c snide "I-I don't mean to be rude-"

    g "Save it. It's not the first time I've been asked that."
    extend " Let's just say a whimsical creature thought it'd be humorous to mangle with my soul when I was a child. The end."

    "He doesn't appear insulted, though that response seems rehearsed."
    extend " Not like it changes the way I see him. Though he's definitely growing \"more alive\", the darker it gets."
    "Griswy wasn't this outspoken when we met. I can understand being a night owl, but it's like the night is his element."
    extend " Though if he sleeps during the day, I guess it makes sense. Much like how I'm an early riser, and rely on the sun to keep me going."

    # nvl clear

    g "Enough questions, we're almost there."

    window hide

    hide Griswyr with dissolve

    stop music
    stop sound

    pause 0.5

    scene image "#000" with dissolve

    #I think here would be a good place to ask the player if they want to save their game.
    #We can place these "intermissions" to let the player know they can take a break.
    #I'm thinking we could put a prompt here, one after scene_01, and one after scene_04

    jump scene_03

    return
