
label scene_04:

    scene background cave with dissolve

    play music bgm.dungeon_ambience

    window show

    "We slither inside and are greeted by a luminous path."
    "Torches with purple flames light the corridor, and the pleasant aroma of roses enters our noses."
    extend " Their dedication to that single flower astonishes me. I expected something more elaborate..."

    window hide

    show Griswyr neutral at center with dissolve

    window show

    "Griswyr moves so lightly. There are times when I have to double check if he's still beside me."

    play sound sfx.light_grapple

    voice "audio/voice/caius/scene_04_01.ogg"
    c snide "Ngh..."

    voice "audio/voice/griswyr/scene_04_01_take2.ogg"
    g "Watch your step. We are in enemy territory."

    play sound weapon_draw volume 0.15

    "He draws his hatchet and kneels."
    extend " Ah, a tripwire! Of course, I should've expected that..."

    voice "audio/voice/griswyr/scene_04_02_take2.ogg"
    g "Brace yourself."

    play sound sfx.kathunk
    with vpunch

    "I leap backwards, only for a loud noise to follow!"
    extend " We turn to and fro but hear nothing heading our way except footsteps."

    voice "audio/voice/griswyr/scene_04_03_take2.ogg"
    g "Damn! I should've expected something crude... These people aren't living in a fortress."

    voice "audio/voice/caius/scene_04_02.ogg"
    c "We're caught in a corridor. There won't be much room to maneuver."

    # TODO: show griswyr combat at center with dissolve

    voice "audio/voice/griswyr/scene_04_04_take1.ogg"
    g "Stand back. I'll take care of them."

    voice "audio/voice/caius/scene_04_03.ogg"
    c "B-By yourself?!"

    voice "audio/voice/griswyr/scene_04_05_take1.ogg"
    g "Watch and learn, and don't interfere."

    # TODO: If we have a combat sprite with black pupils, they'll shift to red here

    voice "audio/voice/griswyr/scene_04_06_take2.ogg"
    extend " They're mine!"

    # TODO: they'll change back to black now

    window hide

    hide Griswyr with dissolve

    window show

    "It's momentary, but I think I see a glimmer in his eyes."
    extend " It irks me. I know Emissaries hunted down apostates, but I fear he might be taking that role too seriously..."
    "Several disciples rush forward, weapons drawn."
    extend " Just like the first guard though, no one notices us at first."

    show cultist at center_left as cultist1
    show cultist at center_right as cultist2

    with dissolve

    voice "audio/voice/cultist_b/scene_04_01.ogg"
    cu_b "The hell? Did Oakley set off the tripwire again?! How many times do we have to spell it out for him?!"

    voice "audio/voice/cultist_c/scene_04_01.ogg"
    cu_c "Where is Oakley anyways? I get being embarrassed, but he'll have to face us eventually."

    voice "audio/voice/cultist_c/scene_04_02.ogg"
    cu_c "Wait, Oakley is as stubborn as a mule! He wouldn't cower like that, so that means-"

    play sound sfx.heavyslash
    with bloodflash

    voice "audio/voice/cultist_c/scene_04_03.ogg"
    cu_c "GAAAAAAAAHHHHHH!!!!" with vpunch

    window hide

    show cultist at center_left as cultist1:

        xoffset 0

        ease 0.3 yoffset 150

    pause 0.1

    play sound sfx.thud

    hide cultist1 with Dissolve(0.2)

    show Griswyr neutral at center with dissolve # TODO: will be griswyr combat later

    window show

    "Griswyr doesn't strike from behind - no, he plants himself at the center of the group!"
    "His victim collapses, his throat cut wide open. I didn't even see the slash."

    voice "audio/voice/cultist_b/scene_04_02.ogg"
    cu_b "Agh...!"

    voice "audio/voice/cultist_b/scene_04_03.ogg"
    extend " Intruder-"

    voice "audio/voice/griswyr/scene_04_07_take3.ogg"
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
    "His stance is wide, and he spirals with ferocity AND dexterity! No matter how they try to fight him, none of the cultists stand a chance."

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

    play sound sfx.heavyslash
    with bloodflash

    voice "audio/voice/cultist_d/scene_04_01_take1.ogg"
    cu_d "AAAAAHHHH!!!!" with vpunch

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

    window hide

    show Griswyr neutral blood_on at center with dissolve

    window show

    voice "audio/voice/griswyr/scene_04_08_take3.ogg"
    g "As expected, they were pathetic."
    voice "audio/voice/griswyr/scene_04_09_take2.ogg"
    extend " Were you paying attention, Caius?"

    voice "audio/voice/caius/scene_04_04_take1.ogg"
    c snide "Ngh..."

    "The hallway, AND Griswyr are painted crimson!"
    extend " The metallic stench leaves me dizzy. The gore, the carnage, the corpses littered across the floor, it all taxes me greatly..."

    play sound sfx.blood_splatter

    "Worst of all, the man with the hatchet inside his forehead is still alive and {i}still{/i} screaming..."

    voice "audio/voice/cultist_d/scene_04_02_take4.ogg"
    cu_d "Please! I surrender! Just get this thing out of my head!" with vpunch

    voice "audio/voice/caius/scene_04_05_take2.ogg"
    c snide "By Yeshua, I'm going to be ill..."

    voice "audio/voice/griswyr/scene_04_05_take2.ogg"
    g "Swallow it! This is nothing compared to the horrors we face!"

    "Griswyr strolls up to the man, not granting him any mercy."
    extend " The poor Thorn scurries away, until he has nowhere left to go."
    "Griswyr shakes his head. He appears bored, of all things..."

    voice "audio/voice/griswyr/scene_04_11_take1.ogg"
    g "Surrender is cheap, I want information."

    voice "audio/voice/cultist_d/scene_04_03_take3.ogg"
    cu_d "Right, right! Just get this thing out of my head!"

    voice "audio/voice/griswyr/scene_04_12_take4.ogg"
    g "I'll remove it AND your head if you don't start talking!"

    voice "audio/voice/cultist_d/scene_04_04_take3.ogg"
    cu_d "Alright! Please, just don't kill me..."

    voice "audio/voice/griswyr/scene_04_13_take1.ogg"
    g "Tch..."
    voice "audio/voice/griswyr/scene_04_14_take3.ogg"
    extend " Quit cowering, Caius. Get over here."

    voice "audio/voice/griswyr/scene_04_06.ogg"
    c "...Right."

    play sound sfx.bloodfootsteps

    "Each of my steps squelches as I walk..."
    extend " The blood has formed puddles across the ground. Moving through the carnage sends shivers down my spine..."
    "It feels like I'm wading through a sticky, red mud... By Yeshua, I hope this will wash out."

    voice "audio/voice/cultist_d/scene_04_05_take3.ogg"
    cu_d "So there's...five people leading the ritual. They've already begun chanting..."
    voice "audio/voice/cultist_d/scene_04_06_take3.ogg"
    extend "\nI doubt you have much longer. If you're here to stop us, then you best\nhurry..."

    voice "audio/voice/griswyr/scene_04_15_take2.ogg"
    g "What kind of devil are you summoning?"

    voice "audio/voice/cultist_d/scene_04_07_take3.ogg"
    cu_d "Wh-what...?"

    voice "audio/voice/griswyr/scene_04_16_take3.ogg"
    g "Don't be coy. You worship an Archfiend. There's no way you're unfamiliar with her kin."

    voice "audio/voice/cultist_d/scene_04_08_take5.ogg"
    cu_d "I...I don't know! Our leader kept it under-"

    voice "audio/voice/griswyr/scene_04_17_take3.ogg"
    g "I hope for your sake you are not lying!"

    play sound sfx.heavyslash
    with hpunch

    voice "audio/voice/cultist_d/scene_04_09_take5.ogg"
    "As Griswyr presses his boot into the hatchet, I spring forward."
    extend " I run on air, or at least that's what it feels like."

    voice "audio/voice/caius/scene_04_07.ogg"
    c angry "Stop it, Griswyr!"

    "I shield the man, placing my body between him and his tormentor."
    "My breaths accelerate, and a cold sweat breaks out on my brow. I can’t allow this torture to continue!"
    extend " Superior or otherwise, he has gone too far! There's no way the reverend would stand for this cruelty!"

    voice "audio/voice/caius/scene_04_08.ogg"
    c angry "That's enough! He's already down!"

    voice "audio/voice/griswyr/scene_04_18_take2.ogg"
    g "So what?"

    voice "audio/voice/caius/scene_04_09.ogg"
    c angry "So what?! You can't treat people like this!"
    voice "audio/voice/caius/scene_04_10.ogg"
    extend " You're supposed to be protecting people, not torturing them! I can understand the grim reality of our job, but this is too much!"

    voice "audio/voice/griswyr/scene_04_19_take2.ogg"
    g "I thought I made it clear we were exterminators, not heroes."

    voice "audio/voice/caius/scene_04_11.ogg"
    c angry "That might be true, but it doesn't mean we have to behave like brutes!"
    voice "audio/voice/caius/scene_04_12.ogg"
    extend " How can we stop the devils when we behave no differently? We'll just become the same monsters we vowed to destroy!"

    voice "audio/voice/griswyr/scene_04_20_take2.ogg"
    g "...You choose now to make a stand?"

    "I nod fiercely."

    voice "audio/voice/caius/scene_04_13.ogg"
    c angry "You may not follow Yeshua, but I know Ahriman won't stand for what you are doing!"

    voice "audio/voice/griswyr/scene_04_21_take2.ogg"
    g "You forget your place, and I care not for what Ahriman or any Archlord has to say."
    voice "audio/voice/griswyr/scene_04_22_take2.ogg"
    extend " I wear his symbol out of formality, nothing more."

    voice "audio/voice/caius/scene_04_14.ogg"
    c angry "But I care, and I will not let this treatment continue!"

    "He sighs."

    voice "audio/voice/griswyr/scene_04_23_take1.ogg"
    g "...We don't have time for this."

    "He moves past me. Before I can react..."

    play sound sfx.heavyslash
    with bloodflash

    voice "audio/voice/cultist_d/scene_04_09_take1.ogg"
    extend " The cultist wheezes as the ax is yanked out of his head."

    voice "audio/voice/griswyr/scene_04_24_take1.ogg"
    g "Get out of my sight. Consider it an act of your false goddess that I don't flay you like a fish!"

    "The man, with the gash in his head streaming blood, scrambles to his feet and barrels to the exit."
    "I sigh in relief."
    extend " If I accomplish anything tonight, I have at least given that man another chance at life."
    "Griswyr turns to me, his gaze just as disinterested as usual."
    extend " I don't flinch. After my actions, I might not end up becoming an Emissary, but at least I'll still have my humanity!"

    voice "audio/voice/griswyr/scene_04_25_take3.ogg"
    g "You understand he's going to bleed out, correct?"

    voice "audio/voice/caius/scene_04_15.ogg"
    c "...He might find a healer."

    voice "audio/voice/griswyr/scene_04_26_take2.ogg"
    g "Who would tend to a Thorn?"

    voice "audio/voice/caius/scene_04_16.ogg"
    c angry "If healers are true to their oath, someone will."

    "He scoffs and turns forward."

    voice "audio/voice/griswyr/scene_04_27_take2.ogg"
    g "Let's move. I've had enough preaching for a lifetime."

    voice "audio/voice/caius/scene_04_17.ogg"
    c smile "Fair enough."

    "Though Griswyr manifesting Malice concerns me. No wonder he’s so cold."
    extend " Malice doesn't morph people into monsters, it erodes their character. No one wakes up and decides to be a villain. It's a slope..."
    "How long has he been channeling it? Why does he rely on it?"
    extend " He looks more than capable of fighting on his own. What would drive him to such ends?"
    "That is a question for after the mission."

    window hide

    hide Griswyr with dissolve

    pause 0.3

    scene image "#000" with dissolve

    stop music fadeout 1.5

    jump scene_05

    return
