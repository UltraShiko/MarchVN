
label scene_05:

    pause 0.4

    scene background cult altar with dissolve

    play music bgm.altar_ambience volume 0.35

    window show

    "The sanctum isn't too far away, and the sounds of prayer grow louder as we advance."
    "When we approach, my eyes scan the room."
    "On top of what you'd expect from a summoning circle, there is a corpse entangled in rose bushes."
    extend " It's an elderly woman, and her pink eyes paint her as a hag. Is this her lair?"
    "An altar takes up the back portion of the room."
    extend " Three bronze statuettes rest atop the podium. Each is of a woman, aging from one statuette to the next."
    "The sickly-sweet smell of roses overtakes the room, and the crimson aura of Malice was thicker than the swamps in Jorunderfell."

    window hide

    show cultist at left as cultist4 with dissolve
    show cultist at center_left as cultist2 with dissolve:
        xoffset 100
    show cultist at center as cultist1 with dissolve
    show cultist at center_right as cultist3 with dissolve:
        xoffset -100
    show cultist at right as cultist5 with dissolve

    window show

    "Five acolytes stand at each position of the pentagram, too engrossed in their trance to notice us."
    "There's no way they didn't hear the racket of our fight. They must have decided to continue the ritual and are now close to finishing."

    window hide

    show Griswyr blood_on at center with dissolve

    window show

    voice "audio/voice/griswyr/scene_05_01_take1.ogg"
    g "Looks like we made it in time."

    voice "audio/voice/caius/scene_05_01_take1.ogg"
    c "I suppose we...just attack?"

    voice "audio/voice/griswyr/scene_05_02_take1.ogg"
    g "If they're going to make it that easy."
    voice "audio/voice/griswyr/scene_05_03_take1.ogg"
    extend " Stay back, wouldn't want you to stain your conscience."

    voice "audio/voice/caius/scene_05_02_take3.ogg"
    c snide "No no, please, after you."

    window hide

    scene image "#000" with iris_in_out_reverse

    window show

    "I cover my eyes, and he goes to work."

    play sound heavyslash
    pause 0.6
    queue sound sfx.thud

    extend " Much like with the group of Thorns we just faced, the bodies here also fall like rain..."

    play sound heavyslash
    pause 0.6
    queue sound sfx.thud

    "I can feel the aura beginning to wane. I've had enough bloodshed for one night, maybe for a lifetime..."

    play sound heavyslash
    pause 0.6
    queue sound sfx.thud

    extend " Jory wasn't wrong about the brutality of the Emissaries. I doubt that gentle giant would stand any of this..."

    window hide

    scene background cult altar

    show Griswyr blood_on at center

    with iris_in_out_8

    window show

    "When I open my eyes, Griswyr cuts down the final Thorn."
    extend " Yet the woman doesn't whimper. She grins menacingly as Griswyr towers over her."

    voice "audio/voice/cultist_mage/scene_05_01_take_1.ogg"
    cu "Ngh...hehehe! You have my thanks! Blood was the last thing we needed, and you spilled more than enough!"

    "Griswyr twitches."
    extend " Is it my imagination, or do I spot veins bulging from his head."

    voice "audio/voice/griswyr/scene_05_04_take1.ogg"
    g "Grrr...!"

    voice "<to 2.870>audio/voice/cultist_mage/scene_05_02_take_1.ogg"
    cu "Go on, cut me down!"

    voice "<from 2.870>audio/voice/cultist_mage/scene_05_02_take_1.ogg"
    extend " Mother will avenge us! You're as good as dead!"

    voice "audio/voice/griswyr/scene_05_04_take3.ogg"
    g "Graaaahhhh!!!" with vpunch

    play sound sfx.heavyslash
    with bloodflash

    "The cultist's severed head soars through the air."
    extend " That swing wasn't nearly as graceful as usual. It was crude, brutish, and wild."
    "When he turns, his face is twisted into a scowl."

    voice "audio/voice/griswyr/scene_05_06_take1.ogg"
    g "Goddamn it! We played right into their hands!"

    voice "audio/voice/caius/scene_05_03_take2.ogg"
    c "They needed blood? Was this a suicide pact?"
    voice "audio/voice/caius/scene_05_04_take3.ogg"
    extend " That hag has been dead for awhile, and I see no one tied to the altar."

    voice "audio/voice/griswyr/scene_05_07_take1.ogg"
    g "It doesn't matter! Our objective has changed!"

    window hide

    play sound sfx.bubble1 volume 0.5
    queue sound sfx.bubble2 loop volume 0.5

    hide Griswyr with dissolve

    stop music fadeout 1.5

    #play music bgm.lethal_suspense #TODO: Add this after jam release

    pause 3.5

    window show

    "The blood begins bubbling, and we retreat behind a pillar."
    extend " A caustic scene fills the air, burning my nose."

    stop sound

    play sound sfx.magic_charge
    with maliceflash

    "The circle glows purple, and a red mist rises from the blood."

    scene image "#cb4a4a" with dissolve

    extend " It shrouds us, obscuring our vision and surrounding us in a crimson fog."

    # play sound sfx.weapon_draw

    window hide

    scene background cult altar

    show persephone sillhouette at center

    with Dissolve(1.2)

    window show

    "Griswyr and I ready ourselves as a curvaceous silhouette comes into view."
    extend " My mind races. Will she attack? Will she try to bewitch us? The suspense is unnerving..."

    voice "audio/voice/caius/scene_05_05_take4.ogg"
    c snide "Ngh..."

    "My heart pounds. I swear I can {i}feel{/i} her presence..."
    extend " It's soothing, alluring, and at same time, suffocating..."
    "I sense both a welcoming and a frightening presence from her..."
    extend " I've never been so relaxed, yet afraid for my life at the same before."

    voice "audio/voice/griswyr/scene_05_08_take2.ogg"
    g "That devil.... Why do I recognize her?"

    voice "audio/voice/caius/scene_05_06_take1.ogg"
    c "You can see through the mist?"

    voice "audio/voice/griswyr/scene_05_09_take1.ogg"
    g "My eyes are more precise than most. This is a succubus."
    voice "audio/voice/griswyr/scene_05_10_take2.ogg"
    extend " Pfft, these people gave their lives to summon that? What a waste."

    voice "audio/voice/caius/scene_05_07_take3.ogg"
    c "But why?"

    voice "audio/voice/griswyr/scene_05_11_take2.ogg"
    g "I have no clue."
    voice "audio/voice/griswyr/scene_05_12_take3.ogg"
    extend " Time to adapt."

    play sound sfx.melee_swing

    window hide

    hide persephone with dissolve

    window show

    #we'd zoom in on the silhouette here

    "I yelp as he shoves me forward."
    extend " I turn in protest, only to see no one."

    window hide

    scene background cult altar with dissolve

    window show

    "I fidget as the veil starts to disperse. What does he want me to do?!"
    extend " Wait, succubi aren't very strong. They're spies more than anything else, so he must be testing me."
    "Ok, Caius..."
    extend " Breathe in...breath out..."
    extend " You have the advantage. She's vulnerable to Grace like any other devil, and you know her tricks."
    "I tremble with each step I take."
    extend " I must resemble a scared child who is in over his head. She won't expect much, and it will be her demise."

    window hide

    play music bgm.altar_ambience volume 0.35

    # TODO: will be lethal_suspense after jam
    #hide persephone silhouette

    pause 0.8

    show persephone smirk at center with Dissolve(1.0)

    pause 1.8

    window show

    "I gulp when her true form appears."
    extend " I sense no threat from her. Her eyes aren't cross, and there isn't disgust or bloodlust in them."
    "Careful, Caius, eyes above the chest. Stare too long, and you'll become enthralled..."
    "My mouth opens, but no words leave. I feel breathless."
    extend " If I enter any stance, my guise will be blown. If she lunges first though, I'll be defenseless..."
    "Ugh, to hell with duplicity! I'll engage her before she can-"

    v "...Did you kill her children?"

#########################

    voice "audio/voice/caius/scene_05_08_take2.ogg"
    c snide "Uhh..!"

    "Oh no! We're surrounded by corpses! There's no way she won't suspect anything now..."
    "Damn it! How could I be so careless?! All I've done is give her an opening!"
    extend " Wait...no reaction. She isn't drawing a weapon or anything..."
    "Hell, she's smiling! It's one of amusement, not malevolence."

    v "Hehehe! Relax! They're in a better place now."
    extend " Besides, there's no blood on {i}your{/i} hands. Looks like I'm outnumbered."

    voice "audio/voice/caius/scene_05_09_take6.ogg"
    c "Ugh, right..."

    v "So, what am I dealing with here?"
    extend " Celestial?"
    extend " Exorcist?"
    extend " Adventurer who's in over his head?"

    voice "audio/voice/caius/scene_05_10_take3.ogg"
    c neutral "Emissary."

    v "Really? You, one of those cutthroats?"
    extend " Ohhh, it's your first day isn't it?"

    "She carries on like a waitress in a tavern."
    extend " Had she hidden her horns and wings, I might've forgotten she was a fiend..."

    voice "audio/voice/caius/scene_05_11_take2.ogg"
    c "It's been quite an experience...one I would like to put to bed."

    v "So, are you going to kill me?"

    voice "audio/voice/caius/scene_05_12_take3.ogg"
    c "Or send you back to Hell. I prefer the latter, to be honest."

    v "Aww, how thoughtful!"
    extend " Buuut...."

    play sound sfx.charm
    with charmflash

    voice "audio/voice/caius/scene_05_13_take1.ogg"
    c snide "Gnnnghhh...!" with vpunch

    "Her eyes flash pink, and my head throbs."
    extend " It feels like a hand is squeezing my head, forcing my mind to bend to her will..."
    extend " Except it won't work!"
    "She caught me off guard, but my mind won't bend so easily."
    extend " I faced many temptations when I took my vow, her magic is pitiful in comparison."
    "I'll let her think she has the upper hand...for now."
    extend " Besides, compulsion magic has a fatal flaw: it cannot force its victim to channel mana nor harm themself."
    "My stance relaxes. As long as her spell persists, I'll have to act like her most devoted companion."
    extend " I'm not too experienced with acting, but I can at least give Griswyr a show."

    v "See? Isn't that better? You can call me Persephone, what's your name?"

    voice "audio/voice/caius/scene_05_14_take1.ogg"
    c neutral "...Caius."

    p "Hmmm, that doesn't sound familiar... Where are you from?"

    # TODO: Replace with correct pronunciation.
    voice "audio/voice/caius/scene_05_15_take3.ogg"
    c "...Thrycia?"

    p "That mound of dirt? Wow! That place is older than me!"
    extend " Though I haven't been around that long..."

    voice "audio/voice/caius/scene_05_16.ogg"
    c "...How old are you?"

    p "Rude! We just met! Don't you know not to ask a lady her age?"

    voice "audio/voice/caius/scene_05_17_take2.ogg"
    c "...My apologies. ...It appears your magic is working too well."

    p "Pfft! I softened you up, I didn't remove your manners..."
    p "I've been around for...twenty years? I'm unsure... Time flows differently in Hell."
    extend " Don't worry, I'm very mature for my age, hehehehe!"

    "Devils are immortal, so twenty years was hardly a drop in the bucket for them."
    extend " Her soul must not have fallen too long ago. So in tandem with being alone, she's also not as experienced."

    p "I don't have any intention of hurting you or whoever is lurking in the corner. I just have an \"errand\" to run."
    extend " You won't even know I was here!"

    voice "audio/voice/caius/scene_05_18_take1.ogg"
    c "...What kind of errand?"

    p "Nothing special, I just need to touch base with a certain someone."
    p "Would you happen to know a man named Jory? He's a giant! You couldn't have missed him! I think he's still living in Jubilee..."

    "My heart accelerates!"

    voice "<to 0.84>audio/voice/caius/scene_05_20_take3.ogg"
    c angry "Wh-What do you want-"

    "Calm down, Caius...you're supposed to be pulling her leg."

    voice "<from 0.86>audio/voice/caius/scene_05_20_take3.ogg"
    c neutral "I-uh, I mean...I think he left several years ago."

    $ unlockCompendionEntry("MeropianLore")

    voice "audio/voice/caius/scene_05_21_take2.ogg"
    extend " Poor man was wrought with grief. They say he fell in love with a Meropian."
    voice "audio/voice/caius/scene_05_22_take1.ogg"
    c "I never believed the rumors, but he wasn't the same after one was executed."
    voice "audio/voice/caius/scene_05_23_take1.ogg"
    extend " I prayed for his soul, but that was the only interaction I ever had with him."

    "Her smile curls into a frown, and her eyes widen."
    extend " Every mention of Jory pains her. But why? He never worshiped Hecate, did he?"

    p "Oh, that's...too bad."
    extend " And where did you say he was headed?"

    voice "audio/voice/caius/scene_05_24_take3.ogg"
    c "...A small village to the west of Jubilee. ...I guess he wanted to get away from everything."

    p "Huh, I see."

    voice "audio/voice/caius/scene_05_25_take2.ogg"
    c "Right."

    p "Right..."

    voice "audio/voice/caius/scene_05_26_take4.ogg"
    c snide "Mhm..."

    p "Mm...hm."

    c "..."

    p "..."

    hide persephone
    show persephone angry at center

    extend "You lying piece of shit!"

    # Raagyuo: If possible, I would like to make this scene work without any narration.
    # So I'm thinking, maybe the screen zooms in to emulate Caius attacking, and then darts back as he's shunted backwards
    # In summary, the screen will demonstrate Caius attacking, than being slammed backwards

    window hide

    camera:
        subpixel True xzoom 1.0
        pos (0, 0) zoom 1.0
        ease 0.20 pos (-531, -180) zoom 1.52
        ease 0.33 pos (0, 0) zoom 1.0
    with Pause(0.63)

    camera:
        pos (0, 0) zoom 1.0

    play sound sfx.lunge

    window show

    "I lunge!"

    play sound sfx.whoosh

    voice "audio/voice/caius/scene_05_27_take4.ogg"
    c "Wh-Whoooa..!"

    play sound sfx.heavy_crash
    with hpunch

    "I collide with the wall, knocking the wind out of me..."
    "What was that....?"
    extend " It felt like leaping into a tornado. I got shunted backwards as if I were a toy...!"
    "I didn't see her conjure any mana...though she hasn't wielded any while charming me either."
    extend " If no mana is used, it must be innate. But I don't recall succubi being able to manipulate the wind."

    p "You thought you could pull a fast one on me?! I'm a devil, goddamn it!"
    p "All things considered, I thought your little act was adorable."
    extend " Until you lied about HIM!"

    play sound sfx.magic_charge
    with maliceflash

    "When she snarls, Malice oozes from her eyes."
    extend " She must notice because she shakes her head and resumes her smirk."

    hide persephone
    show persephone smirk at center

    p "So...let's try this again."
    extend " Where's Jor-"

    play sound sfx.slash

    #Ragyuo: I'm thinking Griswyr would come in from the top and appear at the left / right of Persephone
    #Normally I'd use a moveintop command, but maybe you have a better idea?
    hide persephone

    window hide

    show Griswyr neutral:
        subpixel True
        ypos -0.18
        easein_bounce 0.27 ypos 1.0
    with Pause(0.37)
    show Griswyr neutral:
        ypos 1.0

    window show

    #will be combat later

    "Gryswyr jumps down from the ceiling, grazing her cheek with his blade."

    play sound sfx.thud

    "He lands then swings at her neck..."

    #Maybe zoom Persephone back? Or to the opposite direction?

    window hide

    camera:
        subpixel True xzoom 1.0
        xpos 0 zoom 1.0
        ease_expo 0.33 xpos -366 zoom 1.21
    with Pause(0.43)

    camera:
        xpos -366 zoom 1.21

    window show

    extend " only for her to float out of the way."

    p "Hehehe, finally showed yourself, huh? I take it you're his boss?"

    voice "audio/voice/griswyr/scene_05_13_take4.ogg"
    g "Now I've figured you out."

    p "Eh?"

    voice "audio/voice/griswyr/scene_05_14_take2.ogg"
    g "Your cult was very adamant about bringing you here, so adamant that they were ready to die."
    voice "audio/voice/griswyr/scene_05_15_take1.ogg"
    extend " And for a lowly sex devil? That made no sense."

    p "Oh, so we're going there..."
    extend " Sorry, Snowflake, but you aren't my type."
    p "Here's some advice: you should reaaally learn what the sun is. You're looking a little pale~."

    voice "audio/voice/griswyr/scene_05_16_take1.ogg"
    g "Then you brought up Jory, a man surrounded in rumors." # Changed "shrouded" to "surrounded" to match the voice line.
    voice "audio/voice/griswyr/scene_05_17_take3.ogg"
    extend " They say many things about him. How he knew {i}The Reckoning{/i} would happen. How he fell in love with a gar who worshiped Hecate."

    p "Gar...?"

    voice "audio/voice/griswyr/scene_05_18_take2.ogg"
    g "They say her death throes shook The Third so much that he hired double the protection, and they also say a succubus was the one who dragged him into Hell."
    voice "audio/voice/griswyr/scene_05_19_take2.ogg"
    extend " Which means..."
    voice "audio/voice/griswyr/scene_05_20_take1.ogg"
    g "You're the banshee who caused the Reckoning!" with vpunch

    "I shudder. Could she have been that SAME monster who caused so much chaos?!"
    "She sighs grumpily and claps her hands slowly."

    p "Look at that... you blew my case wide open... So much for the surprise..."
    extend " You must be fun at parties, Snowflake. A reeeeal crowd pleaser..."

    voice "audio/voice/griswyr/scene_05_21_take3.ogg"
    g "It was hardly a secret. Even the boy would've figured it out eventually."

    play sound sfx.weapon_draw volume 0.5

    "He draws his hatchet and throws an arm in front of me."

    voice "audio/voice/griswyr/scene_05_22_take2.ogg"
    g "Stay back. You are no match for her."

    voice "audio/voice/caius/scene_05_28_take2.ogg"
    c "But-"

    voice "audio/voice/griswyr/scene_05_23_take2.ogg"
    g "I've pushed you into danger twice tonight, but only because I knew you could overcome it."
    voice "audio/voice/griswyr/scene_05_24_take2.ogg"
    extend " This fiend is much stronger than a succubus. You'll only get in the way."

    voice "audio/voice/caius/scene_05_29_take1.ogg"
    c "Griswyr, she'll just revive in Hell if I don't-"

    voice "audio/voice/griswyr/scene_05_25_take2.ogg"
    g "You talk too much! Do you forget that the enemy is right there?!"

    "What does he mean?"
    extend " Oh wait, she might not know I can wield Grace. By Yeshua, this is not my night..."

    voice "audio/voice/caius/scene_05_30_take1.ogg"
    c neutral "Alright then, I'll watch for any more Thorns."

    voice "audio/voice/griswyr/scene_05_26_take3.ogg"
    g "That's the smartest thing you've done all night."
    voice "audio/voice/griswyr/scene_05_27_take2.ogg"
    extend " As for you..."
    voice "audio/voice/griswyr/scene_05_28_take3.ogg"
    g "I will have those wings, banshee! Scream if you must!"

    stop music
    play music bgm.reckoning_I volume 0.5
    play sound sfx.lunge volume 0.5

    #Ragyuo: If an animation is needed, maybe Griswyr would zoom in towards her?

    window hide

    show Griswyr neutral:
        subpixel True xpos 0.0
        parallel:
            zoom 1.0
            linear 0.21 zoom 1.0
            linear 0.19 zoom 0.74
        parallel:
            alpha 1.0
            linear 0.17 alpha 1.0
            linear 0.21 alpha 0.0
        parallel:
            blur 0.0
            linear 0.17 blur 8.35
    with Pause(0.50)
    show Griswyr neutral:
        zoom 0.74 alpha 0.0 blur 8.35

    window show

    "He leaps towards her, and she shakes her head."

    hide Griswyr
    show persephone smirk at center with dissolve

    p "Good grief, did you learn nothing from your friend?"

    "She waves her hand, and a gust of wind shields her."
    #show Griswyr behind Persephone
    extend " Griswyr lands and skirts behind her."

    window hide

    show persephone smirk:
        subpixel True
        xpos 0.5
        linear 0.23 xpos -0.5
    with Pause(0.33)
    show persephone smirk:
        xpos -0.5

    play sound sfx.weapon_draw volume 0.5

    hide persephone
    show Griswyr neutral at center

    window show

    extend " She gasps as his sword hisses through the air."

    voice "audio/voice/griswyr/scene_05_29_take1.ogg"
    g "Die!"

    #Ragyuo: So the idea is that she used aeromancy as a launching pad
    #Currently unsure as to how to make this work. Maybe move her out quickly? We'll see
    "He cleaves, only to cut air."
    "That wasn't a hover... She {i}propelled{/i} herself out of his reach."
    "To move so gracefully, I think I get it now."
    extend " I'm not too experienced with magic, but considering that mana is involved, it should function the same."
    "The more you practice wielding it, the less mana you consume. Much like exercising a muscle, mana needs to be nurtured."
    extend " She must've incorporated Aeromancy into her fighting style. Impressive!"
    "I suppose it was unwise of me to try and generalize about how devils fight..."

    hide Griswyr
    show persephone smirk at center

    p "Fine, fine... You wanna play rough?"

    play sound sfx.dagger_draw

    "Five, razor-sharp claws spring from her fingertips."
    "She hunches forward, mimicking Griswyr's stance."
    extend " He does not appreciate that."

    voice "audio/voice/griswyr/scene_05_30_take1.ogg"
    g "...Are you mocking me?"

    p "What?"

    voice "audio/voice/griswyr/scene_05_31_take2.ogg"
    g "You copied my stance!"

    p "..."
    extend "Snowflake, I just met you. Never heard of you either."
    extend " Guess you're not that important~."

    voice "audio/voice/griswyr/scene_05_32_take3.ogg"
    g "Hmph!"

    play sound sfx.parry
    #Ragyuo: Not sure how to animate this. Maybe using hpunch alongside the sfx will be enough?
    #The upcoming scene is basically Griswyr trying and failing to cut Persephone. What are your thoughts?

    window hide

    camera:
        subpixel True
        xpos 0
        linear 0.04 xpos 18
        linear 0.07 xpos -20
        linear 0.11 xpos 39
        linear 0.02 xpos 0
    with Pause(0.34)
    camera:
        xpos 0

    window show

    "They both spring forward, claws dragging across steel when they clash."
    "While their stances are similar, their techniques aren't."

    window hide

    camera:
        subpixel True
        parallel:
            xpos 0
            linear 0.07 xpos -18
            linear 0.08 xpos -18
            linear 0.08 xpos -324
            linear 0.10 xpos -60
            linear 0.10 xpos 0
        parallel:
            zoom 1.0
            linear 0.07 zoom 1.23
            linear 0.05 zoom 1.23
            linear 0.31 zoom 1.0

    show persephone smirk:
        subpixel True
        xpos 0.5
        linear 0.07 xpos 0.41
        linear 0.13 xpos 0.51
        linear 0.03 xpos 0.39
        linear 0.10 xpos 0.5
        linear 0.10 xpos 0.5
    with Pause(0.53)

    camera:
        xpos 0 zoom 1.0
    show persephone smirk:
        xpos 0.5

    window show

    extend " As Griswyr spins in a flurry of swings, Persephone keeps evading his efforts before retaliating."
    "Griswyr attacks viciously, but Persephone appears more relaxed."
    extend " She might just be trying to lure him into lowering his guard, or trying to antagonize him..."

    window hide

    camera:
        subpixel True
        parallel:
            xpos 0
            linear 0.07 xpos -18
            linear 0.08 xpos -18
            linear 0.08 xpos -324
            linear 0.10 xpos -60
            linear 0.10 xpos 0
        parallel:
            zoom 1.0
            linear 0.07 zoom 1.23
            linear 0.05 zoom 1.23
            linear 0.31 zoom 1.0

    show persephone smirk:
        subpixel True
        xpos 0.5
        linear 0.07 xpos 0.41
        linear 0.13 xpos 0.51
        linear 0.03 xpos 0.39
        linear 0.10 xpos 0.5
        linear 0.10 xpos 0.5
    with Pause(0.53)

    camera:
        xpos 0 zoom 1.0

    show persephone smirk:
        xpos 0.5

    window show

    "Strike after strike comes from Griswyr, but not one lands on Persephone."

    window hide

    camera:
        subpixel True
        parallel:
            xpos 0
            linear 0.07 xpos -18
            linear 0.08 xpos -18
            linear 0.08 xpos -324
            linear 0.10 xpos -60
            linear 0.10 xpos 0
        parallel:
            zoom 1.0
            linear 0.07 zoom 1.23
            linear 0.05 zoom 1.23
            linear 0.31 zoom 1.0

    show persephone smirk:
        subpixel True
        xpos 0.5
        linear 0.07 xpos 0.41
        linear 0.13 xpos 0.51
        linear 0.03 xpos 0.39
        linear 0.10 xpos 0.5
        linear 0.10 xpos 0.5
    with Pause(0.53)

    camera:
        xpos 0 zoom 1.0
    show persephone smirk:
        xpos 0.5

    window show

    "Griswyr snarls and repeats the same maneuvers.... He is the same whirling cyclone of death he was earlier, yet even his skill and fury are no match for Persephone’s otherworldly evasions."
    "They dance around the room as I do my best to follow their movements and not get swept up in the battle."
    "My heart pounds as she begins evading with growing ease."

    #we'd probably show Persephone behind him here?

    # NOTE: Commented the following two lines as they did nothing.
    # hide Griswyr with moveoutright
    # show persephone smirk at center

    extend " After a wide swing, Griswyr stumbles forward. He's wide open!"

    voice "audio/voice/caius/scene_05_31_take2.ogg"
    c angry "Griswyr, look out!"

    p "Good night~!"

    # No audio file here.
    g "..."
    voice "audio/voice/griswyr/scene_05_33_take2.ogg"
    g "{i}Blood Lance{/i}."

    play sound sfx.bloodlance

    "A spear of blood erupts from his blade."

    p "W-wait..."

    window hide

    play sound sfx.blood_splatter
    with bloodflash

    show persephone smirk:
        subpixel True additive 0.0
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.09 matrixcolor InvertMatrix(4.25)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.07 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    with Pause(0.47)

    show persephone smirk:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

    show persephone smirk:
        subpixel True
        parallel:
            ypos 1.0
            ease_bounce 0.27 ypos 0.89
        parallel:
            zoom 1.0
            ease_bounce 0.30 zoom 0.86
    with Pause(0.40)

    show persephone smirk:
        ypos 0.89 zoom 0.86

    window show

    extend " Gnnnnggggghhh!!!!" with vpunch

    "It pierces her chest like a dagger."
    extend " Had she not backpedaled at the last moment, it would've impaled her."

    window hide

    hide persephone with dissolve
    show Griswyr neutral with dissolve

    window show

    "Meanwhile, Griswyr's arm reddens violently."
    extend " I cringe. He is showing no reaction to it, but it looks painful..."

    play sound sfx.hurl

    "He throws his hatchet at her."

    #move Persephone slightly, than have Griswyr hide

    extend " She sidesteps, and Griswyr...vanishes?!"

    #show griswyr behind Persephone

    "He reappears behind her, alarming Persephone as he takes his hatchet in hand once again."

    #might want to find a sfx for his flurry...
    #Ragyuo: This is a similar situation as before where he's swinging madly and she's dodging

    window hide

    camera:
        subpixel True
        parallel:
            xpos 0
            linear 0.07 xpos -18
            linear 0.08 xpos -18
            linear 0.08 xpos -324
            linear 0.10 xpos -60
            linear 0.10 xpos 0
        parallel:
            zoom 1.0
            linear 0.07 zoom 1.23
            linear 0.05 zoom 1.23
            linear 0.31 zoom 1.0

    show persephone smirk:
        subpixel True
        xpos 0.5
        linear 0.07 xpos 0.41
        linear 0.13 xpos 0.51
        linear 0.03 xpos 0.39
        linear 0.10 xpos 0.5
        linear 0.10 xpos 0.5
    with Pause(0.53)

    camera:
        xpos 0 zoom 1.0
    show persephone smirk:
        xpos 0.5

    window show

    extend " Again comes his flurry of deadly strikes, but Persephone isn't amused."
    "Her wound isn't deep, but Griswyr has her on the run."
    extend " She can't just float around anymore, or else he might catch her off guard again!"
    "He feints and as Persephone braces herself..."

    # TODO: show Griswyr behind Persephone

    p "Ah shit...!" with vpunch

    voice "audio/voice/griswyr/scene_05_34_take2.ogg"
    g "You should've stayed in Hell, banshee!"

    play sound sfx.heavyslash volume 0.5

    "With his sword, Griswyr gouges her waist!"
    extend " Yet Persephone smiles."

    p "And you should've brought silver!"

    window hide

    play sound sfx.galeblast

    pause 0.6

    queue sound sfx.crash
    with hpunch

    #Ragyuo: Griswyr would be send off screen and the screen shakes. He got punted just like Caius did

    hide Griswyr with moveoutleft

    window show

    "A gale blast sends Griswyr crashing into the wall."
    "I watch in horror! She hit him point blank!"
    extend " She wanted him to get close... Why else would she have relied so heavily on evasion?"

    window hide

    #Ragyuo: Griswyr would ease back in here

    hide persephone with dissolve
    show Griswyr neutral at center with easeinbottom
    #combat

    window show

    "Griswyr snarls and recovers."
    extend " He may seem unharmed, but his breaths are heavy as he clutches his chest."

    voice "audio/voice/caius/scene_05_32_take1.ogg"
    c angry "That's enough, Griswyr! Let me handle this!"

    voice "audio/voice/griswyr/scene_05_35_take2.ogg"
    g "Nnngh..."
    voice "audio/voice/griswyr/scene_05_36_take2.ogg"
    extend " Just who do you think you are?! I'm your superior!"

    voice "audio/voice/caius/scene_05_33_take3.ogg"
    c "And as my superior, you must test me. Consider this another trial."

    voice "audio/voice/griswyr/scene_05_37_take1.ogg"
    g "Grrr..."

    p "By Yeshua, you're pious, I'll give you that..."

    "Griswyr's temperament is much more aggressive than before."
    extend " He isn't cool and collected anymore, and he eyes me as if I were his foe."
    "And now that I think about it, he did lose his temper earlier, when he beheaded that cultist..."

    voice "audio/voice/griswyr/scene_05_38_take3.ogg"
    g "...Very well. She is yours. Do not disappoint me."

    p "Hehehe, you ought to watch your mouth, Snowflake. Someone might get the wrong idea~."

    voice "audio/voice/caius/scene_05_34_take2.ogg"
    c smile "Thank you, Griswyr. I won't let you down!"

    window hide

    hide Griswyr with dissolve
    show persephone smirk with dissolve

    window show

    #Ragyuo Maybe she would zoom in a little? Or have the screen shake slightly to simulate him approaching her?
    "I ready my stance then slowly walk towards her."
    #Idk how we'd simulate them circling each other, though if you got any ideas let me know

    "We circle each other, our eyes not breaking contact."
    extend " She could pounce at any moment, yet all I continue to get from her is that scheming grin."
    "Even now, she's still choosing to toy with us. Something tells me she's a lot stronger than what she's letting on..."

    p "So..."
    extend "what did they tell you about me?"

    voice "audio/voice/caius/scene_05_35_take2.ogg"
    c angry "Nothing much. Just that you dragged The Third into Hell..."

    p "Are you sure that was me? It could've been one of my sisters. We all look alike, after all~."
    p "Come on... This is all a misunderstanding! I didn't do anything...I just want to check up on an old friend..."

    "My blood freezes with anger."

    # No voice.
    c angry "..."
    voice "audio/voice/caius/scene_05_36_take5.ogg"
    extend " You mean my friend?!"

    p "Well..."
    extend " If his name's Jory, then-"

    play sound sfx.jab
    with graceflash

    show persephone angry at center

    extend "Grrrr!!!" with vpunch

    "Too slow!"
    extend " She recoils heavily from that blow, even more than when she got stabbed!"
    "The mana flows in me alongside my fury."
    extend " I don't know what she wants with him, but I don't care."
    "Jory has only wanted to help others. He doesn't deserve to be pestered by the likes of her!"

    voice "audio/voice/caius/scene_05_37_take4.ogg"
    c "Keep my friend's name...out of your mouth!" with vpunch

    play sound sfx.jab
    pause 0.6
    queue sound sfx.jab
    pause 0.6
    queue sound sfx.jab

    #Ragyuo: For reference if you're familiar with Wing Chun, or Kung Lao from Mortal Kombat, Caius is jabbing her like them.
    #If not, think of something like gatling fists or something. We can discuss later
    #His hands are also glowing blue from his mana. I'd rather not make the screen flash with every punch.
    #Animation wise, I leave it up to you if you want to add anything

    play sound sfx.rapidfirepunch

    #shake Persephone if anything

    "She twitches and staggers with each consecutive blow to her chest."
    extend " My strikes fly as quickly as Griswyr's swipes, maybe even faster!"

    play sound sfx.rapidfirepunch

    #maybe push her back a bit?
    "I manage to back her into a corner. I have to finish this fight quickly before she can hurt Griswyr or Jory or anyone else."

    play sound sfx.magic_charge
    with maliceflash

    "Eventually, she musters her Malice and retaliates!"

    #maybe zoom in closer to simulate their clench?

    play sound sfx.magic_charge
    #with whiteflash

    extend " I block the blow with my own, the clashing manas dispersing whilst our palms are clenched."
    "Our brows furrow, eyes locked onto one another."
    extend " Her whimsical smile twists into a scowl. Looks like she's not having fun anymore."

    p "Grrr...so that's why he picked you."
    extend " Snowflake's soul is too black to ever wield Grace. He needed a proxy, how clever..."

    voice "audio/voice/caius/scene_05_38_take2.ogg"
    c "Why are you surprised?"
    voice "audio/voice/caius/scene_05_39_take4.ogg"
    extend " I can't be the only Emissary who channels Grace."

    hide persephone
    show persephone smirk at center

    p "Hahaha! If you only knew!"

    play sound sfx.weapon_swing

    "She breaks out of our hold and slashes."
    extend " I breathe deeply..."

    play sound sfx.block

    "And catch her clawed wrists mid-swing."

    hide persephone with moveoutright

    play sound sfx.potterycrash volume 0.15
    with vpunch

    "She gasps as I spin and hurl her onto the altar."
    extend " She lies splayed among the fractured statuettes."

    show persephone angry at center with moveinbottom

    #zoomed out Ragyuou

    "She pushes herself up, furious, as I waggle my finger."

    voice "audio/voice/caius/scene_05_40_take1.ogg"
    c angry "Blasphemer! Mother will be displeased!"

    p "Wise ass, huh...?!"

    play sound sfx.galeblast volume 0.5
    pause 0.5
    play sound sfx.potterycrash volume 0.15
    pause 0.5

    "She summons the wind and blasted the table, sending debris my way."

    #Ragyuo: Not sure how to go about this. Debris is flying at him. Maybe a screen shake and a sfx will be enough?
    #Or zoom out, and shake the screen?

    play sound sfx.lunge
    pause 0.6
    queue sound sfx.block
    pause 0.6
    queue sound sfx.block
    pause 0.6
    queue sound sfx.block

    extend " I jump out of the way and managed to block the projectiles."
    "I land, trying to regain my bearings, but my pause leaves me open."

    play sound sfx.galeblast
    pause 0.6
    play sound sfx.heavy_bam

    voice "audio/voice/caius/scene_05_41_take6.ogg"
    c snide "Gahhh!" with vpunch

    "Her second gale that hits me hard... It feels like getting kicked by a mule!"

    #have her zoom in

    # show persephone smirk at center

    play sound sfx.lunge

    "She springs at me, but I block her attack and throw her a second time."
    extend " She lands hard again but recovers quickly and braces herself against the wall."
    "Again she lunges."
    #maybe her sprite would hop to simulate the pounce
    extend " And feints, her flapping wings frightening me and nearly causing me to stumble. What is she going to do now?! I don't have the time to-"

    voice "<to 0.8>audio/voice/griswyr/scene_05_39_take2.ogg"
    g "What are you doing?!" with vpunch
    voice "<from 1.0>audio/voice/griswyr/scene_05_39_take2.ogg"
    extend " Attack!!!" with vpunch

    "I obey."

    play sound sfx.jab
    with graceflash

    hide persephone
    show persephone angry at center

    p "Nuagh...!" with vpunch

    "I understand now. I can do more than harm her with my attacks - I can also block her attacks with my own!"

    #Ragyuo: Gatling punch spam again.
    play sound sfx.rapidfirepunch

    "I double down on my efforts, both striking blows and preventing her attacks as they come. A barrage of my strikes batters her chest."

    p "Nnnnnnggghhhh....!"

    "I'm using a lot of mana and energy, but I can't let up!"
    extend " I can't risk giving her another opening! Our lives are on the line, and the lives of others as well."

    play sound sfx.galeblast

    #Have her zoom out, than back in to simulate Caius chasing her
    "She tries to retreat by blasting the ground, but I continue to pursue her."

    play sound sfx.magic_charge
    with graceflash

    extend " As strong as she might be, my Grace tore through her like a venom."
    "I keep going."
    extend " I've trained my arms and legs to ceaselessly land consecutive blows. Stamina isn't an issue!"
    #have her zoom out
    "She finally manages to break away, but she writhes in damage and pain."
    #have the sprite move slightly to simulate her writing
    extend " I see my mana taking its toll. Each blow makes her twitch and shiver. I almost pity her."

    #zoom in slightly

    "I step towards her, ready to end this."
    extend " Yeshua knows how mangled her soul must've been after Hecate got her hands on it..."
    extend " It saddens me..."

    play sound sfx.magic_charge
    with graceflash

    "I close my eyes and clasp my hands."
    extend " She should have enough of my Grace within her. With a flex of my hands, it'll explode."
    "She won't feel a thing."

    voice "audio/voice/caius/scene_05_42_take1.ogg"
    c "...Farewell."

    p "...Is that pity in your eyes?"

    show persephone smirk

    extend " Aww, how noble! Though not showing kindness to your friend? That's pretty cold..."

    voice "audio/voice/caius/scene_05_43_take4.ogg"
    c neutral "...?"

    p "Oh no, I'm not talking about Snowflake. Though you're probably the only friend he has ehehehehe!"

    hide persephone
    show persephone smirk at center

    extend " I can read it in your eyes. You're not motivated by zeal; you're motivated by regret."

    voice "audio/voice/caius/scene_05_44_take3.ogg"
    c angry "So what?"

    p "So what? You know that we fiends can peer into your past, right?"

    voice "audio/voice/caius/scene_05_45_take1.ogg"
    c angry "Huh?!"

    p "Uh oh, guess not~."
    extend " Well I can understand Jory not knowing, but Snowflake? Tsk tsk, how irresponsible~!"

    voice "audio/voice/griswyr/scene_05_41_take2.ogg"
    g "Do not humor her, Caius!"

    voice "audio/voice/caius/scene_05_46_take5.ogg"
    c angry "You lie!"

    p "Ahahahaha! Why else would people sell their souls?"
    extend " It's because we see everything! Your regrets, what you care about, and what haunts you. It's all an open book!"
    p "Aww, what's with the long face? You were looking so high-and-mighty just a moment ago..."
    extend " I'm guessing I lost your sympathy?"

    "If Griswyr knowing about my past unnerved me, Persephone knowing about it took the cake!"
    "How could I not realize?! I'm no scholar, but I've looked far and wide for knowledge about devils, and yet I’ve never heard of this power!"
    extend " More importantly, she knows about HIM!!!!"

    p "Ah yes, you let someone down."
    extend " How else would you have made it this far? You were a nobody until you threw him to the wolves!"
    p "That's pretty wicked! And now you starve yourself to get pity from everyone."
    extend " Hahaha, you holier-than-thou types always have the darkest secrets! Watching your souls fall is soooo delicious~!"

    voice "audio/voice/griswyr/scene_05_42_take2.ogg"
    g "Strike her down, goddamn it!"

    voice "audio/voice/caius/scene_05_47_take7.ogg"
    c angry "Be quiet, devil!" with vpunch

    #have Persephone zoom out and back in

    play sound sfx.melee_swing

    p "Whoa, whoa....what's swatting at me going to do? I'm not the one who abandoned him..."

    voice "<to 0.6>audio/voice/caius/scene_05_48_take3.ogg"
    c angry "You... "
    voice "<from 1.3>audio/voice/caius/scene_05_48_take3.ogg"
    extend " You leave him alone, monster!" with vpunch

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    p "Oh, your friend? Hmm, I'm sure he's much different now. People change when their hearts are ripped out."

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    voice "audio/voice/caius/scene_05_49_take1.ogg"
    c angry "Tell me, Persephone!"

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    voice "audio/voice/caius/scene_05_49_take2.ogg"
    c angry "Hecate calls herself the mother of outcasts, a protector of the damned!"

    #have Persephone zoom out and back in

    play sound sfx.melee_swing

    voice "<to 6.2>audio/voice/caius/scene_05_49_take3.ogg"
    extend " But you're just like any other devil! You'd corner and bewitch the same people you claim to care about!"
    voice "<from 6.7>audio/voice/caius/scene_05_49_take3.ogg"
    c angry "The Dretchlings suffer enough without your poison!"

    voice "audio/voice/griswyr/scene_05_43_take1.ogg"
    g "Stop talking, Caius-"

    p "Ohohoho! You have it backwards!"
    extend " We don't corrupt people, we {i}save{/i} them from the lies of your absent Archlords."

    #have Persephone zoom out and back in

    play sound sfx.melee_swing

    voice "audio/voice/caius/scene_05_50_take3.ogg"
    c angry "Damn you!!!" with vpunch

    #zoom in, they're locked again

    play sound sfx.magic_charge
    with whiteflash

    "Our manas clash as we clench again."
    "My eyes beam at that grinning monster!"

    play sound sfx.magic_charge
    with graceflash

    extend " My Grace spikes. It must sting her severely, yet she only grins more."

    voice "<to 3.0>audio/voice/caius/scene_05_51_take1.ogg"
    c angry "You and that goddamned archfiend aren't any different!"
    voice "<from 3.1>audio/voice/caius/scene_05_51_take1.ogg"
    extend " Why else would she reside in Hell?!"

    show persephone angry

    p "Right, because your god's any better?"
    extend " Who were the Celestials founded under? Oh, he must've been cruel to allow his followers to imprison Dretchlings like cattle."
    p "Yet we're the bad guys for coming to their rescue? How is that fair?"
    extend " Face it, your precious Archlords don't care about you!."
    extend " Now that I think about it, looks I have TWO errands to run!"

    voice "<to 0.86>audio/voice/caius/scene_05_52_take1.ogg"
    c angry "I'll end you-"

    play sound sfx.grapple

    voice "audio/voice/caius/scene_05_52_2_take2.ogg"
    extend " Agh!" with vpunch

    #have her increase in y-axis?

    "A hand grabs my throat, and she hoists me above her."
    "My mana vanishes alongside my breathing! I can't channel it if I can't breathe...!"

    show persephone smirk

    p "Though while we're talking about fibbing, I wasn't entirely honest with you."
    extend " You see, we devils can't read people's pasts. So I appreciate the information~."

    voice "audio/voice/caius/scene_05_53_take3.ogg"
    c snide "Gngh!!!" with vpunch

    "My heart skips, and she giggles darkly."

    p "You mortals will believe anything. Just like false seers, we only need to paint a picture broad enough to apply to anyone, and suddenly you're spilling your guts for us."
    p "And now you've failed him twice..."
    extend " Nah! You did him a favor!"

    play sound sfx.magic_charge
    with maliceflash

    "Wind blasts me from her grip, and she channels Malice and winds in her other hand."

    p "I'll take good care of him, you can die now."
    extend " Buh-bye~!"

    #Ragyuo: Not sure how to animate her here. She basically dropped Caius and leapt backwards

    play sound sfx.weapon_swing
    queue sound sfx.thud
    pause 0.6

    show persephone angry

    p "Shit!" with hpunch

    hide persephone with moveoutright
    show Griswyr neutral at left with moveinleft
    #combat

    "She drops me, narrowly slipping past Griswyr's slash."
    "I don't have the strength nor the courage to stand..."
    extend " She played me like a harp... So easily too!"
    "Griswyr turns to me, his eyes as stoic as ever."

    voice "audio/voice/griswyr/scene_05_44_take1.ogg"
    g "...I thought I told you not to disappoint me."

    p "Aww, did I break your friend-"

    #have Persephone zoom out and back in
    play sound sfx.weapon_swing

    extend " Whoa Snowflake! Lighten up, will ya?!"
    $ unlockCompendionEntry("JinxLore")
    extend " I mean, isn't being jinxed bad enough?"

    # No voice.
    g "..."
    voice "audio/voice/griswyr/scene_05_45_take2.ogg"
    extend " It'll be worth it when I feast on your blood!"

    "Wh-what?! What does he mean-"
    extend " Oh right, he licked his sword after it got coated in gore. He's not trying to scare her, he MEANS what he's saying..."
    "Persephone looks as dumbfounded as I do."

    hide Griswyr
    show persephone smirk at center with dissolve

    p "Oh, oh wow..."
    extend " You've completely lost it... I knew you were into some weird stuff, but-"

    #have Persephone zoom out and back in

    play sound sfx.weapon_swing

    extend " Whoops! You're going to have to do better if you want my neck, you leech~."

    play sound sfx.parry
    with vpunch

    "I watch them clash, my mind blank."
    "How can I help Griswyr when I can't even help myself? I'll just be in the way..."
    #Queue in similar animation where Griswyr flurries, and she dodges
    "All the blows I landed were because she let me... Now she's dodging and weaving past Griswyr's swipes just like before..."
    "She rears back."

    hide Persephone
    show Griswyr neutral at right

    extend " And Griswyr ducks behind her, readying his ax."

    voice "<to 0.7>audio/voice/griswyr/scene_05_46_take1.ogg"
    g "And now you-"

    play sound sfx.slash
    with bloodflash

    voice "<from 1.49>audio/voice/griswyr/scene_05_46_take3.ogg"
    extend "Ngh! What the-?!" with vpunch

    "Wounds tear open in his arms. They seem to surprise him more than hurt him."
    extend " I can't blame him for his shock. I didn't even see her claws land. So how did she get him?"

    voice "audio/voice/griswyr/scene_05_47_take4.ogg"
    g "Tch...just a flesh wound!"

    play sound sfx.hurl

    "He siphons some of the blood and flings his hatchet."
    extend " Persephone turns around, but he teleports in front of her, sword at the ready."

    play sound sfx.parry

    "She catches his sword in two fingers, the blade causing blood to trickle down her hand."
    extend " Griswyr winces."

    hide Griswyr
    show persephone smirk at center

    p "Ooh, looks like you grazed me..."
    extend " Go on, have a taste."

    #Compared to last animation, Griswyr is slowing down.

    "She releases his blade and holds out her fingers."
    extend " Griswyr cringes but follows through with his swing."

    #have Persephone zoom out and back in

    play sound sfx.weapon_swing

    p "Hey now, don't be greedy..."

    voice "audio/voice/griswyr/scene_05_48_take2.ogg"
    g "You think taunting me is going to work?"
    voice "audio/voice/griswyr/scene_05_49_take3.ogg"
    extend " I've had this curse my whole life. I am not enslaved to it!"

    #show persephone combatS #smile expression

    p "Then why did you flinch? You might've had my head if you were faster~."

    #have Persephone zoom out to simulate evasion

    play sound sfx.weapon_swing
    pause 0.6
    queue sound sfx.bloodlance
    with bloodflash

    "Persephone darts backwards, and he fires another Blood Lance."
    extend " She swats it away with her wings."
    "Griswyr's body hunches over, his breaths weighty."
    extend " Every time he uses one of those attacks, he injures himself..."

    #have Persephone zoom in

    play sound sfx.lunge

    p "Wake up, Snowflake!"

    hide persephone with moveoutright
    show Griswyr neutral at right with moveinright

    play sound sfx.slash
    with bloodflash

    "He evades her pounce and hisses as more wounds rip open on his body."
    extend " It was subtle, but I finally spot the source of her attack. She's channeling wind through her hands."
    "So even if he dodges her blows, the gusts will still cut him."

    #have Persephone zoom in
    hide Griswyr with moveoutright
    show persephone smirk at center with moveinright

    play sound sfx.lunge

    "She launches herself again!"

    voice "audio/voice/caius/scene_05_54_take1.ogg"
    c angry "Don't dodge, Griswyr, or you'll be cut by her wind!"

    voice "audio/voice/griswyr/scene_05_50_take1.ogg"
    g "Grr! No shit!!!" with vpunch

    window hide

    #move his sprite to the left and right

    hide Persephone
    show Griswyr neutral at left with moveinright

    window show

    "He spins."

    play sound sfx.parry
    pause 0.6
    queue sound sfx.slash
    with bloodflash

    extend " His hatchet parries her claws, and his blade sinks into her side."

    #move his sprite down x-axis slighty

    play sound sfx.grapple
    with bloodflash

    "He digs the steel more deeply into her as his leg ensnares hers."

    play sound sfx.thud
    with hpunch

    #move griswyr down more

    extend " She slams into the floor, and he plants his knees atop her back."
    "He leers down at her, her body resting on the bloody floor beneath them."
    extend " I blink. I'm not crazy. Fangs have emerged where his canines once were."
    "I shiver. The look of ferocity in his eyes...he doesn't see her as his target."
    extend " He sees her as his food!"

    voice "audio/voice/griswyr/scene_05_51_take4.ogg"
    g "I told you I'd have your wings, but I'll start with your neck."
    voice "audio/voice/griswyr/scene_05_52_take3.ogg"
    extend " Even if you revive in Hell, you'll have to find your way back to our plane, and you'll become my prey again!"

    p "Ngh...not bad! You're {i}actually{/i} starting to scare me, Snowflake!"

    voice "audio/voice/griswyr/scene_05_53_take3.ogg"
    g "Even now, you joke?!"

    play sound sfx.slash
    with bloodflash

    p "Gngh...!" with vpunch

    voice "audio/voice/griswyr/scene_05_54_take3.ogg"
    g "What will it take for you to stay down?!"
    voice "audio/voice/griswyr/scene_05_55_take1.ogg"
    extend " You're like a cockroach! You sever its head, yet it still crawls!"

    p "Ohh, don't let me stop you. If you want my neck, go for it."
    extend " I am your snack after all. I'm powerless to stop you. What good would any resistance do?"

    play sound sfx.slash
    with bloodflash

    voice "audio/voice/griswyr/scene_05_56_take3.ogg"
    g "Shut up!!!" with vpunch

    "By Yeshua...fiends are something else."
    extend " Despite all her injuries, Persephone still keeps going."
    "Griswyr pauses, finding both of his hands drenched in blood..."
    extend " He just sits there...something has gripped his heart."

    play sound sfx.slash
    with bloodflash

    "He drives the shortsword into her again...and he pauses a second time."
    extend " Try as he might, he can't seem to break her smile."

    p "They say a predator takes the easiest approach to hunting. Even if a wolf could kill any human, it will only target the weakest link."
    p "Matter of fact, wolves only hunt when they {i}know{/i} they can win. But I prefer cats."
    extend " They are an exception. They hunt for sport as well as food. A cat will even choose to torment its prey before killing it."
    p "They're very sadistic - at a glance."
    extend " Truth is, that cat isn't torturing for fun. It's tiring the prey out to ensure that it can't retaliate."
    p "Is that why you're frozen? Is it because I'm laughing off your little cuts?"
    extend " Or is it because your instincts won't allow you to move?" with vpunch

    voice "audio/voice/griswyr/scene_05_57_take3.ogg"
    g "...Enough of this!"
    voice "audio/voice/griswyr/scene_05_58_take3.ogg"
    extend " I am not enslaved by my hunger!"
    voice "audio/voice/griswyr/scene_05_59_take3.ogg"
    extend " It is enslaved by me!!!" # with vpunch

    "His jaw expands as he dives!"

    p "Oof..."
    extend " Should've listened to your gut."

    play sound grapple
    with vpunch

    hide Griswyr with moveoutbottom
    show persephone smirk at center with moveinbottom

    "Her arms lash out and hold his head still."
    extend " Her head springs forward, and my heart stops."

    play sound sfx.kiss

    extend " She plants her lips onto his!"

    voice "audio/voice/caius/scene_05_55_take1.ogg"
    c "Griswyr!"

    "A second wind lifts me back onto my feet, and I dash toward them!"

    play sound sfx.kiss

    extend " Her kiss is lethal! She's sapping his mana with every twist of her lips."

    play sound sfx.kiss

    "His body wrinkles, and her wounds begin to close."

    #zoom in

    extend " She pulls away as I charge."

    p "...Oh, you're still with us?"

    play sound sfx.thud

    "Griswyr collapses to the floor as we engage."

    window hide

    play sound sfx.bam
    pause 0.6
    play sound sfx.magic_charge
    with whiteflash
    with hpunch

    show persephone angry at center

    play sound sfx.bam
    pause 0.6
    play sound sfx.magic_charge
    with whiteflash
    with hpunch
    play sound sfx.bam
    pause 0.6
    play sound sfx.magic_charge
    with whiteflash
    with hpunch

    window show

    "Sounds of hissing rattle the room. The mana screams just as violently as our blows."
    extend " Yet, she suffers more than I do. Looking more closely, I see her body tremble."

    #Ragyou more gatling fist Kung lao barrage

    play sound sfx.rapidfirepunch
    with hpunch

    "My blows from earlier weren't in vain after all, but I need to keep injecting more mana into her."
    extend " If this explosion doesn't kill her, I don't know if I'll get another chance!"

    show persephone angry at center

    p "Ugh, you're so annoying! Go away!"

    #zoom in Persephone

    play sound sfx.galeblast
    pause 0.6
    queue sound sfx.jab

    "I weave past her gale and jab her chest."
    "I gnash my teeth whilst my palms assail her like a barrage of arrows."

    play sound sfx.weapon_swing
    pause 0.6
    queue sound sfx.jab

    extend " She swipes, but I duck and slam my heel into her sternum."

    #shake persephone with each blow
    play sound sfx.jab

    "Her hisses devolve to growls the more I strike her."
    extend " Her eye twitches. She's reaching her limit."

    #zoom in and out of Persephone

    "She keeps trying to float backwards, but I keep stepping forward."
    extend " My arms are growing heavy...I'm starting to run low on mana. I can't continue much longer..."
    "I need to land one good strike."

    voice "audio/voice/caius/scene_05_56_take4.ogg"
    c angry "Fall, monster!" with vpunch

    #zoom out Persephone

    play sound sfx.melee_swing

    "I kick and hit nothing but air..."
    "She flies backwards, digging her claws into the wall. She glowers, ready to attack again."

    play sound sfx.magic_charge
    with maliceflash

    extend " Malice and wind engulf her! I can't stop this...and even if I dodge..."

    voice "audio/voice/griswyr/scene_05_60_take2.ogg"
    g "You goddamned fool! What are you doing?!"
    voice "audio/voice/griswyr/scene_05_61_take1.ogg"
    extend " This battle is yours! DO - NOT - FALTER!!!" with vpunch

    "..."
    extend " I know, Griswyr."

    #zoom in Persephone

    play sound sfx.lunge
    pause 0.5
    play sound heavy_bam
    pause 0.3

    voice "audio/voice/caius/scene_05_57_take6.ogg"
    c "Gnnnnngggggghhhh!!!" with vpunch

    "I dodge, and her intense gusts bludgeon my body. I felt like I’ve slammed straight into a wall of pure force!"
    "Blood sputters from my mouth as several of my ribs collapse...."
    extend " The only reason the rest of me doesn't follow suit is because Grace protects me from most of the pain..."
    "It takes all of my concentration not to be swept away..."
    extend " And now..."

    play sound sfx.jab

    voice "audio/voice/caius/scene_05_58_take1.ogg"
    c angry "HAAAA!!!!" with vpunch

    "I deliver a mighty blow to her chest and..."
    extend "nothing."

    p "...Was that your last stand?"
    extend " WEAK!!!" with vpunch

    #zoom out Persephone

    play sound sfx.heavy_bam

    "Her Roundhouse kick sends me flying. Time stands still as I float away..."
    extend " I turn to her, that insipid grin peering into my soul."
    "I breathe heavily, coughing up blood as I clasp my hands."

    # hide persephone
    # scene image "#000" with dissolve

    # No voice.
    c angry "..."
    voice "audio/voice/caius/scene_05_59_take5.ogg"
    extend "Shine!" with vpunch

    # scene background cult altar with dissolve
    stop music fadeout 1.5

    p "Huh...?"

    window hide

    play sound sfx.manaexplosion
    stop music

    scene image "#fff" with iris_in_out

    window show

    "My Grace pours from her body and explodes."
    extend " I can't see a thing, but this battle has ended."
    "That blast tore her apart from the inside out."
    extend " Against a mortal, it would just render them paralyzed, but against a devil? There's no way she survived."
    "A hand caught me. It must've been Griswyr's."

    voice "audio/voice/caius/scene_05_60_take4.ogg"
    c snide "Ngh..."

    voice "audio/voice/griswyr/scene_05_62_take3.ogg"
    g "Impressive. What was that?"

    voice "audio/voice/caius/scene_05_61_take2.ogg"
    c "Agh...well each of my blows injects my mana into my opponent, disrupting their own..."
    voice "audio/voice/caius/scene_05_62_take1.ogg"
    extend " And once it consumes most of their body, I can cause it to tear itself out..."
    voice "audio/voice/caius/scene_05_63_take3.ogg"
    extend " Agh... It hurts to talk..."

    voice "audio/voice/griswyr/scene_05_63_take3.ogg"
    g "That's...violent. Color me impressed."

    voice "audio/voice/caius/scene_05_64_take1.ogg"
    c "Well, it doesn't kill mortals..."

    voice "<to 0.7>audio/voice/griswyr/scene_05_64_take7.ogg"
    g "Of course it-"
    voice "<from 0.85>audio/voice/griswyr/scene_05_64_take7.ogg"
    extend " Gngh!" with hpunch

    voice "audio/voice/caius/scene_05_65_take3.ogg"
    c "What's the matter...?"

    voice "audio/voice/griswyr/scene_05_65_take2.ogg"
    g "I still smell her!"

    scene background cult altar with dissolve

    "As the radiance dies down, the first thing I spot are two, red eyes glaring at me..."
    extend " My teeth chatter. My body feels cold, exhausted, and afraid. That was my strongest technique, how did she survive it?!"

    window hide

    show persephone angry at center with dissolve

    play sound sfx.magic_charge
    with maliceflash

    window show

    "Malice's crimson hue shrouds her. Her stance is unsteady, however she appears more than capable to continue..."
    extend "I try to stand only to stumble. A stabbing pain pierces my waist..."
    "I could conjure Grace to numb it, but I wanted to reserve what little I had left..."

    p "You know, I tried to be nice... I tried to make your death quick and painless BUT now I don't really care!"
    p "I'll give you credit, that might've killed me. Good thing Snowflake topped me off hehehe...!"

    play sound sfx.dagger_draw

    "She hisses as her talons spring from her fingers."

    play sound sfx.magic_charge
    with maliceflash

    extend " Her Malice spikes. In hindsight, she didn't use up as much mana as I expected..."

    window hide

    hide persephone with dissolve
    show Griswyr neutral at center with dissolve

    window show

    "Griswyr seems more upset than afraid as he looks to the ground."

    play sound sfx.weapon_draw

    extend " He spits and readies his weapons."

    voice "audio/voice/griswyr/scene_05_66_take2.ogg"
    g "Looks like this mission is a failure! Out of all the monsters, we had to get matched up against that goddamned banshee!"

    voice "audio/voice/caius/scene_05_66_take1.ogg"
    c snide "Griswyr...?"

    voice "audio/voice/griswyr/scene_05_67_take3.ogg"
    g "I'll hold her off while you crawl away. Don't worry about me, because I'm not coming back."

    "He crosses his throat and speaks gravely "

    voice "audio/voice/griswyr/scene_05_68_take3.ogg"
    g "This is my final lesson to you, Caius. Even in death, we Emissaries leave no trace. We'll face annihilation if that's what it takes!"
    voice "audio/voice/griswyr/scene_05_69_take3.ogg"
    extend " Do not let any information fall into the hands of the enemy! To the end!"

    #zoom in Griswyr

    play sound sfx.lunge

    "He charges."
    extend " He startles Persephone, but she meets his advance."
    "He isn't dodging..."

    voice "audio/voice/caius/scene_05_67_take2.ogg"
    c snide "Griswyr, don't..!"

    play sound sfx.heavyslash
    with bloodflash

    "Her claws tear into his chest, ripping blood and flesh from his body."
    extend " Yet he doesn't so much as wince."

    play sound sfx.slash
    with bloodflash
    pause 0.6
    queue sound sfx.grapple

    "He drives his sword into her leg and wraps his arm around her waist."

    #should we show Persephone's sprite?

    p "What the hell are you-?!"

    play sound sfx.grapple

    "He drops his hatchet before getting behind her and hooking his arms around hers, pulling up and restraining her."
    extend " He clings to her like a monkey. Try as she might, Persephone can’t shake him."

    p "Grr! Snowflake, I'm not in the mood!"
    extend " Let go!!!"

    voice "audio/voice/griswyr/scene_05_70_take4.ogg"
    g "Ngggh...what are you doing, idiot?! Run!"

    p "Who are you calling an idiot?! You're the one who-"
    extend " Wait a minute..."

    "I wish I had the strength to flee..."
    extend " My heart weeps for him. My eyes might also weep if it didn't hurt so much to breathe..."
    "Even if I start crawling away, there's no way she's going to let me go."
    extend " I don't know what Griswyr is planning, but if it involves his blood magic, she'll just chase me and we'll all be collateral damage."
    "Best I can do is stay here and see him off..."
    "Persephone turns to him. I can't see what happened, but I have a bad feeling in my stomach..."

    p "...Hehehe, so that's what you're up to? How naughty~."
    extend " Isn't suicide frowned upon by the Celestials?"

    voice "audio/voice/caius/scene_05_68_take2.ogg"
    c "Suicide?!"

    voice "audio/voice/griswyr/scene_05_71_take1.ogg"
    g "Too late...!"

    play sound sfx.magic_charge
    with maliceflash

    "Griswyr's own Malice erupts, causing a whirring sound to hum from within him."

    with graceflash

    extend " Blue glyphs appear on the studs in his armor, growing brighter by the second."
    "I try to call to him, try to move towards him, but my body still refuses to budge..."
    extend " This is horrible! Why is he dying for me?! I'm a novice, I'd be much easier to replace than him."
    "After all, I can't even save myself, let alone anyone else..."

    voice "audio/voice/griswyr/scene_05_72_take1.ogg"
    g "See you in Hell, banshee!" with hpunch

    window hide

    hide Griswyr
    show persephone angry at center
    with dissolve

    window show

    p "Ngh..."

    show persephone smirk at center

    extend " Yep, but not in the way you're thinking!"

    play sound sfx.slash
    pause 0.6
    queue sound sfx.grapple
    with hpunch

    "She slits her wrist and shoves it into his maw."
    "Griswyr's eyes widen and runes on his chest begin flickering."
    extend " His grip loosens as his eyes shut. I hear faint sounds of suckling."
    "At first he clings to her. Then slowly his grip relaxes, and she begins to cradle him."

    p "I can't have you exploding on me. I'll be taking this."

    play sound sfx.heavyslash

    "She tears off his vest and tosses it to the side."
    "Griswyr stirs and groans. He tries to pull away."

    play sound sfx.grapple

    extend " But her palm around his maw clenches."

    p "Now now, I'm still playing with you. Besides, you've had a long day~."

    play sound sfx.heavy_bam
    with vpunch

    extend " So go to sleep!"

    "She slams her knee into his chest, knocking the wind and consciousness out of him."

    #move Persephone to the left/right

    "I watch helplessly while she drags him towards the hanging corpse."
    extend " She tears the grizened woman from the bushes and pins him there."
    "What does she have in store for-"

    show persephone angry at center

    p "Hey, shithead! We're not finished!"

    #should we have an animation for this? Maybe Caius's perspective shifts up by the y-axis?

    "I have to use the wall just to stand..."
    extend "My body twitches with every movement. My lungs are on fire, and these shattered ribs are all too eager to feed me pain..."
    "I breathe heavily, knowing that I only have one way out of this."

    stop music
    play music bgm.reckoning_II volume 0.3
    play sound sfx.magic_charge
    with graceflash

    "Grace surges from my body."
    extend " With this much pouring out, I'll run out of mana in no time. However I need Grace just so I can move..."
    "On the flip side, expending this much mana will inject more into her body. I need to blow her up again..."
    "Who will burn out first? Will I be able to hold up long enough to defeat her? Only one way to find out."

    p "Still have some fight left in you?"

    show persephone smirk at center

    extend " Good! I wasn't satisfied!"

    play sound sfx.magic_charge
    with maliceflash

    p "Even if you don't feel it now, your body is in agony."
    extend " And that pales in comparison to what I have in store for you!"
    p "There's no way Jory raised someone so blind! If the Third lived, you'd kiss his boots like every other slave!"
    extend " You self-righteous idiots are what's wrong with this world!!!" with vpunch

    voice "audio/voice/caius/scene_05_69_take2.ogg"
    c "Ngh...maybe. Maybe I am too pious... And I don't know what you went through..."
    voice "audio/voice/caius/scene_05_70_take3.ogg"
    extend " But I'd sooner believe in myself than an Archfiend...!"

    p "That's not the first time I've heard those words, and it won't be the last..."

    show persephone angry

    extend " Doesn't mean this won't hurt like a bitch!!!" with vpunch

    play sound sfx.block
    with vpunch

    "I breathe deeply and block her swipe."
    extend " She retreats before lunging for my legs!"

    play sound sfx.melee_swing

    "I drive my heel into her jaw."

    play sound sfx.slash
    with bloodflash

    extend " And she counters by scratching my chest. Praise Yeshua that I step back when I do..."

    #have her sprite move around to left and right

    "We dance, blocking and countering each other's blows."
    extend " The manas screech. Our motives are personified and continue to clash!"

    window hide

    scene image "#000" with dissolve

    show Jory happy at center with dissolve

    window show

    "With each punch, visions of Jory enter my mind..."
    extend " Is my life flashing before my eyes...?"

    voice "audio/voice/jory/scene_05_01_take3.ogg"
    j "{i}Relax, Caius, you're always so uptight.{/i}"
    voice "audio/voice/jory/scene_05_02_take1.ogg"
    extend " {i}Take a load off and breathe once in a while, yeah?{/i}"

    window hide

    hide Jory with dissolve

    scene background cult altar
    show persephone angry at center
    with dissolve

    play sound sfx.heavy_bam
    with vpunch

    show persephone angry at center

    p "Gaaaaahhhh!!!" with vpunch

    #zoom out Persephone

    "That attack sends her reeling. If I can just land a few more strikes like that one..."

    #zoom her out and up y-axis

    play sound sfx.galeblast
    pause 0.5
    play sound sfx.galeblast
    pause 0.5
    play sound sfx.galeblast
    pause 0.5
    play sound sfx.galeblast
    pause 0.5
    play sound sfx.galeblast

    "She blasts herself airborne, screeching before launching a volley of gusts towards me."
    extend " I lack the agility to dodge... I walk forward, blocking, deflecting, and even enduring gust after gust..."

    play sound sfx.bam
    with vpunch

    "Even with Grace protecting me, my body rattles with every blast..."

    #zoom in on her

    "I breathe deeply before jumping up to attack her"

    play sound sfx.grapple
    pause 0.4
    play sound sfx.crash
    pause 0.2
    with hpunch

    #move screen downwards

    extend " She dodges and grabs me, and I drive my mana into her as we plummet to the floor."

    window hide

    scene image "#000" with dissolve

    show Griswyr at center with dissolve

    # play sound sfx.heavy_bam
    # with vpunch

    #show griswyr silhouette at center with dissolve

    voice "audio/voice/griswyr/scene_05_73_take2.ogg"
    g "{i}How do you expect to be an Emissary when you're so weak?!{/i}"
    voice "audio/voice/griswyr/scene_05_74_take2.ogg"
    g "{i}I was ready to die for the mission, yet here you are, ready to surrender everything you stand for.{/i}"
    voice "audio/voice/griswyr/scene_05_75_take1.ogg"
    g "{i}Fight goddamn it, even if it kills you!{/i}"

    window hide

    hide Griswyr with dissolve

    scene background cult altar
    show persephone angry at center
    with dissolve

    play sound sfx.grapple
    with bloodflash

    window show

    "My fractured arm latches onto her face, my fingernails and Grace digging into her flesh!"
    extend " A shrill yelp meets my ears. More of her blood trickles down my hands as I hold on for dear life."

    play sound sfx.jab

    #zoom her out a bit

    "She pries my palm from her head, and I kick her off of me."
    extend " I rise, my teeth bared and my eyes seeing red."

    #zoom in

    "Her gaze wavers when I sprint towards her."

    play sound sfx.grapple
    pause 0.4
    play sound sfx.heavy_bam
    pause 0.2
    with hpunch

    extend " Her wings flap, and I grab her foot before clobbering her face."

    #move sprite slightly

    play sound sfx.weapon_swing

    "She squirms and slashes."
    extend " Her nails graze me. I spit up blood and keep attacking."
    "She isn't nearly as dangerous when you have her pinned!"

    p "Grrrrr!!!" with vpunch

    # No voice
    c "..."

    p "Ngh...struggle all you want! In the end...you'll still-"

    window hide

    play sound sfx.hurl

    hide persephone with moveoutright

    queue sound sfx.potterycrash volume 0.5

    window show

    "I shove her jaw shut and hurl her into the table."

    window hide

    show persephone angry at center with easeinbottom

    window show
    #zoomed in slightly Ragyuou

    extend " She leaps to her feet and I approach, walking slowly."

    #zoom in slighty

    "She lunges but flinches."

    #move her sprite from side to side

    extend " She staggers more and more with each step I take towards her."

    window hide

    show image "#00000088" as hider zorder 5 with dissolve

    window show
    # TODO: Change music or decrease volume,

    voice "audio/voice/priam/scene_05_01_take1.ogg"
    priam "...You hate me, huh?"

    voice "audio/voice/priam/scene_05_02_take3.ogg"
    extend " Man...I knew I messed up, but did you have to tell her about me...?"

    "...You're right."

    window hide

    hide hider with dissolve

    window show

    play sound sfx.heavy_bam

    p "AHHHH!!!!!" with vpunch

    window hide

    show image "#00000088" as hider zorder 5 with dissolve

    window show

    voice "audio/voice/priam/scene_05_03_take4.ogg"
    priam "I was just trying to protect us..."

    "I know..."

    window hide

    hide hider with dissolve

    window show

    play sound sfx.heavy_bam
    with hpunch

    p "Gah...damn you! Ngh...!"

    window hide

    show image "#00000088" as hider zorder 5 with dissolve

    window show

    voice "audio/voice/priam/scene_05_04_take2.ogg"
    priam "Why did you abandon me, Caius?! I thought we were friends..."

    "...We are."

    window hide

    hide hider with dissolve

    window show

    #show persephone combat at center with dissolve

    play sound sfx.grapple

    "She catches my last strike, deflecting it."

    play sound sfx.magic_charge
    with whiteflash

    "A hand presses against my chest, with Malice hissing against my Grace..."

    play sound sfx.jab

    #shake Persephone sprite

    "I jab her throat, causing her to spit and her breath to fly from her maw."

    play sound galeblast
    pause 0.6
    queue sound sfx.heavy_bam
    with hpunch

    extend " Yet I still get blasted..."

    #zoom out screen

    "I fly backwards, doing my best to brace my fall as I land."
    extend " With an eldritch calm, I peer back at her."

    window hide

    show image "#00000088" as hider zorder 5 with dissolve

    window show

    voice "audio/voice/priam/scene_05_05_take6.ogg"
    priam "You're coming back, right?"

    "...I am."

    window hide

    hide hider with dissolve

    play sound sfx.magic_charge
    with graceflash

    window show

    "I lift my hands and clasp them together."
    "With an unsteady breath, I speak"

    voice "audio/voice/caius/scene_05_71_take2.ogg"
    c "Rest in peace..."

    stop music

    voice "audio/voice/caius/scene_05_72_take3.ogg"
    extend " Ngh!!!" with vpunch

    play sound sfx.thud
    with vpunch

    #move screen down y-axis

    "Suddenly, I fall to my knees."
    extend " Intense pain floods through my veins, wracking my entire body!"
    "The strain prevents my hands from reaching her...I've run out of mana."

    voice "audio/voice/caius/scene_05_73_take1.ogg"
    c snide "No...not now!"

    window hide

    show image "#00000088" as hider zorder 5 with dissolve

    window show

    voice "audio/voice/priam/scene_05_06_take8.ogg"
    priam "I knew I couldn't trust you..."

    window hide

    hide hider with dissolve

    window show

    "Tears well in my eyes. There isn't anything I can do anymore..."
    "It looks like I've reached my limit first..."

    show persephone smirk

    extend " My adversary laughs triumphantly."

    voice "audio/voice/caius/scene_05_74_take3.ogg"
    c "Priam...I'm sorry. I tried my best..."

    p "Your best FAILED you!" with hpunch

    window hide

    show persephone:

        parallel:
            ease 0.35 zoom 1.5
        parallel:
            ease 0.35 yoffset 450

    play sound sfx.lunge

    scene image "#000" with Dissolve(0.3)

    window show

    "She pounces, and I close my eyes..."
    extend " So be it. Someone, anyone, help him..."

    play sound sfx.heavyslash volume 0.5

    "..."

    voice "audio/voice/griswyr/scene_05_76_take2.ogg"
    g "Caught you!"

    play music bgm.reckoning_II volume 0.3

    scene background cult altar
    show Griswyr neutral at center
    with vpunch
    #combat

    "Griswyr jumps down from the ceiling, his body engulfed by his Malice."
    "She clutches her slashed arm, and her body convulses."

    voice "audio/voice/griswyr/scene_05_77_take6.ogg"
    g "Even if he couldn't finish the job, there's still a lot of Grace inside you."
    voice "audio/voice/griswyr/scene_05_78_take3.ogg"
    extend " Seeing as how both manas repel each other, I wonder what will happen when my Malice is added?"

    hide Griswyr
    show persephone angry at center
    with dissolve

    p "...Oh shit!"

    window hide

    stop music fadeout 1.5
    play sound sfx.magic_charge
    with graceflash
    play sound sfx.manaexplosion

    scene image "#faf7f7" with iris_in_out

    window show

    "Before exploding just like before."

    window hide

    scene background cult altar with Dissolve(2.0)

    pause 0.5

    window show

    "I can't believe it...I survived! We won!"
    extend " I don't care about the buzzing pain coursing through me. Now everyone is safe from her..."
    "Better yet, I never realized before that Malice could also set off such an explosion..."

    voice "audio/voice/caius/scene_05_75_take3.ogg"
    c "Griswyr..."
    voice "audio/voice/caius/scene_05_76_take3.ogg"
    extend " How did you know that would happen...?"

    window hide

    show Griswyr at center with dissolve

    window show

    voice "audio/voice/griswyr/scene_05_79_take4.ogg"
    g "I didn't."
    voice "audio/voice/griswyr/scene_05_80_take3.ogg"
    extend " It was a theory at best. Either way, her blood gave me the second wind I needed."
    voice "audio/voice/griswyr/scene_05_81_take6.ogg"
    g "Even if that didn't kill her, she was more than enough..."
    voice "audio/voice/griswyr/scene_05_82.ogg"
    extend " WHAT THE FUCK?!" with vpunch

    "The lingering effects of the explosion dissipate and Griswyr stomps furiously."
    extend " Persephone was defeated, so what is setting him off?"

    voice "audio/voice/griswyr/scene_05_83_take1.ogg"
    g "HOW THE HELL DID SHE ESCAPE?!" with vpunch

    voice "audio/voice/caius/scene_05_77_take2.ogg"
    c snide "Wh-wha...?"

    "I look to the floor and gasp. There are no remains, no body, no sign of her. Persephone is gone!"

    voice "audio/voice/griswyr/scene_05_84_take4.ogg"
    g "Goddamn it! She was a nuisance before, Yeshua forbid how hard she's going to be to track now!" with vpunch

    voice "audio/voice/caius/scene_05_78_take1.ogg"
    c "How...how do you know she escaped...?"

    voice "audio/voice/griswyr/scene_05_85_take2.ogg"
    g "DON'T YOU THINK I'D TELL YOU IF I KNEW?!" with vpunch
    voice "audio/voice/griswyr/scene_05_86_take2.ogg"
    extend " Damn it to hell! That Banshee will cause a panic if people learn she's back in our plane..."
    voice "audio/voice/griswyr/scene_05_87_take3.ogg"
    g "Yeshua knows what she's plotting! A second reckoning?! Summoning that Archfiend..."
    # NOTE: This line wasn't recorded.
    # voice "audio/voice/griswyr/scene_05_87_take3.ogg"
    # extend " GRAAAAH!!! THIS IS HORRIBLE!!!" with vpunch

    "A voice booms into my ear."

    p "...Looks like you win this time."
    extend " Don't worry, I'll leave Jory be, just as you wished. Anything to get away from you..."
    p "If you see me again, do a girl a favor, and just keep walking!"

    voice "audio/voice/caius/scene_05_79_take1.ogg"
    c "...Griswyr."

    voice "audio/voice/griswyr/scene_05_88_take1.ogg"
    g "What is it?!"

    voice "<to 0.6>audio/voice/caius/scene_05_80_take1.ogg"
    c "Don't..."
    voice "<from 1.30 to 2.5>audio/voice/caius/scene_05_80_take1.ogg"
    extend "tell..."
    voice "<from 3.1>audio/voice/caius/scene_05_80_take1.ogg"
    extend "Jo-"

    window hide
    
    play sound sfx.thud

    scene image "#000" with Dissolve(1.0)

    pause 3.0

    jump scene_06

    return
