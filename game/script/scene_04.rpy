
label scene_04:

    #play sound door

    #I doubt we'll find a suitable background in time. I'll look around for a proxy
    scene background cave with dissolve

    play music bgm.dungeon_ambience

    window show

    "We slither inside and are greeted by a luminous path."
    "Torches with purple flames light the corridor, and the pleasant aroma of roses enters our noses."
    "Their dedication to that single flower astonishes me. I expected something more elaborate..."

    window hide

    show Griswyr neutral at center with dissolve

    window show

    "Griswyr moves so lightly. There are times when I have to double check if he's still beside me."

    # nvl clear

    play sound sfx.light_grapple

    c snide "Ngh..."

    g "Watch your step. We are in enemy territory."

    play sound weapon_draw
    "He draws his hatchet and kneels."
    extend " Ah, a tripwire! Of course, I should've expected that..."

    # nvl clear

    g "Brace yourself."

    play sound sfx.kathunk
    with vpunch

    "I leap backwards, only for a loud noise to follow!"
    #play sound fartherfootsteps TODO: find a sfx
    "We turn to and fro but hear nothing heading our way except footsteps."

    # nvl clear

    g "Damn! I should've expected something crude... These people aren't living in a fortress."

    c "We're caught in a corridor. There won't be much room to maneuver."

    #show griswyr combat at center with dissolve

    g "Stand back. I'll take care of them."

    c "B-By yourself?!"

    g "Watch and learn, and don't interfere."

    hide Griswyr with dissolve

    # TODO: If we have a combat sprite with black pupils, they'll shift to red here
    extend " They're mine!"

    #they'll change back to black now
    "It's momentary, but I think I see a glimmer in his eyes."
    extend " It irks me. I know Emissaries hunted down apostates, but I fear he might be taking that role too seriously..."
    "Several disciples rush forward, weapons drawn."
    extend " Just like the first guard though, no one notices us at first."

    # nvl clear

    show cultist at center_left as cultist1
    show cultist at center_right as cultist2

    with dissolve

    cu "The hell? Did Oakley set off the tripwire again?! How many times do we have to spell it out for him?!"
    cu "Where is Oakley anyways? I get being embarrassed, but he'll have to face us eventually."
    cu "Wait, Oakley is as stubborn as a mule! He wouldn't cower like that, so that means-"

    play sound sfx.heavyslash
    with bloodflash

    cu "GAAAAAAAAHHHHHH!!!!" with vpunch

    show cultist at center_left as cultist1:

        xoffset 0

        ease 0.3 yoffset 150

    pause 0.1

    play sound sfx.thud

    hide cultist1 with Dissolve(0.2)

    show Griswyr neutral at center with dissolve #will be griswyr combat later

    "Griswyr doesn't strike from behind - no, he plants himself at the center of the group!"
    "His victim collapses, his throat cut wide open. I didn't even see the slash."

    # nvl clear

    cu "Agh...!"
    extend " Intruder-"

    g "Too slow."

    window hide

    show Griswyr:

        parallel:

            ease 0.25 xoffset 250

        parallel:

            ease 0.25 alpha 0.0

    pause 0.35

    hide Griswyr

    play sound sfx.heavyslash
    with bloodflash

    show cultist at center_right as cultist2:

        ease 0.3 yoffset 150

    pause 0.1

    play sound sfx.thud

    hide cultist2 with Dissolve(0.2)

    window show

    "The cultists realize they are being ambushed and turn their fury on Griswyr. As each one attacks him though, he spins with his weapon, each twirl tearing apart his victims completely."
    extend " His stance is wide, and he spirals with ferocity AND dexterity! No matter how they try to fight him, none of the cultists stand a chance."

    play sound sfx.blood_splatter
    with bloodflash

    "The cave quickly fills with blood and screams."
    extend " The acolytes are panicking now, desperate to stop him or escape. Griswyr won't let them do either."

    play sound sfx.slash
    with bloodflash

    "He may as well be a tornado, cutting down his victims with vicious twirls."
    extend " But he does more than just spinning. Whenever someone runs at him from behind, he pauses and suddenly gouges them with his sword."

    play sound sfx.magic_charge
    with maliceflash

    "At one point, we hear chanting and notice a cultist draped in a red aura."
    extend " He's channeling Malice, the mana that devils wield! It gives unimaginable power to its wielder, but is also known to corrupt them."

    play sound sfx.magic_charge
    with maliceflash

    window show

    "Griswyr pauses his massacre to face the powerful cultist. Unfazed, he scoffs."
    extend " I gasp as the same Malice erupts from Gryswyr's arm as he flings his hatchet."

    # nvl clear

    play sound sfx.heavyslash
    with bloodflash

    cu "AAAAAHHHH!!!!" with vpunch

    "The apostate bellows, the hatchet lodged within his skull!"
    play sound sfx.blood_splatter
    extend " I grow sick, watching blood pour from him like a fountain..."
    "I couldn't believe what I saw. Gryswyr summoned the same, wicked mana as the Thorn!"
    extend " But he's an Emissary, someone who protects people. So why would he use Malice when it corrupts people?"

    "Being down a weapon hardly slows Griswyr."

    play sound sfx.heavyslash
    with bloodflash
    extend " He flourishes his sword  and cuts down the rest of the cultists who are now in disarray and significantly low on numbers."
    "They know they don't have a chance of winning or surviving."
    "Moments later, the cave becomes silent as the final bodies fall. Griswyr merely frowns in disgust as he collects his weapons."

    # nvl clear
    window hide

    show Griswyr neutral blood_on at center with dissolve

    window show

    g "As expected, they were pathetic."
    extend " Were you paying attention Caius?"

    c snide "Ngh..."

    "The hallway, AND Griswyr are painted crimson!"
    extend " The metallic stench leaves me dizzy. The gore, the carnage, the corpses littered across the floor, it all taxes me greatly..."
    play sound sfx.blood_splatter
    "Worst of all, the man with the hatchet inside his forehead is still alive and {i}still{/i} screaming..."

    # nvl clear

    cu "Please! I surrender! Just get this thing out of my head!" with vpunch

    c snide "By Yeshua, I'm going to be ill..."

    g "Swallow it! This is nothing compared to the horrors we face!"

    "Griswyr strolls up to the man, not granting him any mercy."
    extend " The poor Thorn scurries away, until he has nowhere left to go."
    "Griswyr shakes his head. He appears bored, of all things..."

    # nvl clear

    g "Surrender is cheap, I want information."

    cu "Right, right! Just get this thing out of my head!"

    g "I'll remove it AND your head if you don't start talking!"

    cu "Alright! Please, just don't kill me..."

    g "Tch..."
    extend " Quit cowering, Caius. Get over here."

    c "...Right."

    play sound bloodfootsteps
    "Each of my steps squelches as I walk..."
    extend " The blood has formed puddles across the ground. Moving through the carnage sends shivers down my spine..."
    "It feels like I'm wading through a sticky, red mud... By Yeshua, I hope this will wash out."

    # nvl clear

    cu "So there's...five men leading the ritual. They've already begun chanting..."
    extend " I doubt you have much longer. If you're here to stop us, then you best hurry..."

    g "What kind of devil are you summoning?"

    cu "Wh-what...?"

    g "Don't be coy. You worship an Archfiend. There's no way you're unfamiliar with her kin."

    cu "I...I don't know! Our leader kept it under-"

    g "I hope for your sake you aren't lying!"

    play sound sfx.heavyslash
    with hpunch
    "As Griswyr presses his boot into the hatchet, I spring forward."
    extend " I run on air, or at least that's what it feels like."

    # nvl clear

    c angry "Stop it Griswyr!"

    "I shield the man, placing my body between him and his tormentor."
    "My breaths accelerate, and a cold sweat breaks out on my brow. I can’t allow this torture to continue!"
    extend " Superior or otherwise, he has gone too far! There's no way the reverend would stand for this cruelty!"

    # nvl clear

    c angry "That's enough! He's already down!"

    g "So what?"

    c angry "So what?! You can't treat people like this!"
    extend " You're supposed to be protecting people, not torturing them! I can understand the grim reality of our job, but this is too much!"
    g "I thought I made it clear we were exterminators, not heroes."
    c angry "That might be true, but it doesn't mean we have to behave like brutes!"
    extend " How can we stop the devils when we behave no differently? We'll just become the same monsters we vowed to destroy!"
    g "...You choose now to make a stand?"

    "I nod fiercely."

    # nvl clear

    c angry "You may not follow Yeshua, but I know Ahriman won't stand for what you are doing!"

    g "You forget your place, and I care not for what Ahriman or any Archlord has to say."
    extend " I wear his symbol out of formality, nothing more."

    c angry "But I care, and I will not let this treatment continue!"

    "He sighs."

    # nvl clear

    g "...We don't have time for this."

    "He moves past me. Before I can react..."

    play sound sfx.heavyslash
    with bloodflash

    extend " The cultist wheezes as the ax is yanked out of his head."

    g "Get out of my sight. Consider it an act of your false goddess that I don't flay you like a fish!"

    "The man, with the gash in his head streaming blood, scrambles to his feet and barrels to the exit."
    "I sigh in relief."
    extend " If I accomplish anything tonight, I have at least given that man another chance at life."
    "Griswyr turns to me, his gaze just as disinterested as usual."
    extend " I don't flinch. After my actions, I might not end up becoming an Emissary, but at least I'll still have my humanity!"

    # nvl clear

    g "You understand he's going to bleed out, correct?"

    c "...He might find a healer."

    g "Who would tend to a Thorn?"

    c angry "If healers are true to their oath, someone will."

    "He scoffs and turns forward."

    g "Let's move. I've had enough preaching for a lifetime."

    c smile "Fair enough."

    "Though Griswyr manifesting Malice concerns me. No wonder he’s so cold."
    extend " Malice doesn't morph people into monsters, it erodes their character. No one wakes up and decides to be a villain. It's a slope..."
    "How long has he been channeling it? Why does he rely on it?"
    extend " He looks more than capable of fighting on his own. What would drive him to such ends?"
    "That is a question for after the mission."

    window hide

    # nvl clear

    hide Griswyr with dissolve

    pause 0.3

    scene image "#000" with dissolve

    stop music fadeout 1.5
    #Here would be a good place to ask the player to save

    jump scene_05

    return
