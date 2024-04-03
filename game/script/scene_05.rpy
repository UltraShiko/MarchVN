
label scene_05:

    scene background cult altar with dissolve

    play music bgm.altar_ambience

    window show

    "The sanctum isn't too far away, and the sounds of prayer grow louder as we advance."
    "When we approach, my eyes scan the room."
    "On top of what you'd expect from a summoning circle, there is a corpse entangled in rose bushes."
    extend " It's an elderly woman, and her pink eyes paint her as a hag. Is this her lair?"
    "An altar takes up the back portion of the room."
    extend " Three bronze statuettes rest atop the podium. Each is of a woman, aging from one statuette to the next."
    "The sickly-sweet smell of roses overtakes the room, and the crimson aura of Malice was thicker than the swamps in Jorunderfell."
    show cultist at center as cultist1 with dissolve
    show cultist at center_left as cultist2 with dissolve
    show cultist at center_right as cultist3 with dissolve
    "Five acolytes stand at each position of the pentagram, too engrossed in their trance to notice us."
    extend " There's no way they didn't hear the racket of our fight. They must have decided to continue the ritual and are now close to finishing."

    # nvl clear

    g "Looks like we made it in time."

    c "I suppose we...just attack?"

    g "If they're going to make it that easy."
    extend " Stay back, wouldn't want you to stain your conscience."

    c smide "No please, after you."

    scene image "#000" with dissolve
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
    scene background cult altar with dissolve
    show Griswyr neutral at center with dissolve
    "When I open my eyes, Griswyr cuts down the final Thorn."
    extend " Yet the man doesn't whimper. He grins menacingly as Griswyr towers over him."

    # nvl clear

    cu "Ngh...hehehe! You have my thanks! Blood was the last thing we needed, and you spilled more than enough!"

    "Griswyr twitches."
    extend " Is it my imagination, or do I spot veins bulging from his head."

    # nvl clear

    g "Grrr...!"

    cu "Go on, cut me down!"
    extend " Mother will avenge us! You're as good as dead!"

    g "Graaaahhhh!!!" with vpunch

    play sound sfx.heavyslash
    with bloodflash

    "The cultist's severed head soars through the air."
    extend " That swing wasn't nearly as graceful as usual. It was crude, brutish, and wild."
    "When he turns, his face is twisted into a scowl."

    # nvl clear

    g "Goddamn it! We played right into their hands!"

    c "They needed blood? Was this a suicide pact?"
    extend " That hag has been dead for awhile, and I see no one tied to the altar."

    g "It doesn't matter! Our objective has changed!"

    stop music fadeout 1.5
    #play music bgm.lethal_suspense #TODO: Add this after jam release
    play sound sfx.bubble1
    queue sound sfx.bubble2 loop
    "The blood begins bubbling, and we retreat behind a pillar."
    extend " A caustic scene fills the air, burning my nose."
    stop sound
    play sound sfx.magic_charge
    with maliceflash
    "The circle glows purple, and a red mist rises from the blood."
    hide Griswyr
    scene image "#cb4a4a" with dissolve
    extend " It shrouds us, obscuring our vision and surrounding us in a crimson fog."
    play sound sfx.weapon_draw
    #show Persephone silhouette at center with dissolve #might want to zoom her out a bit
    "Griswyr and I ready ourselves as a curvaceous silhouette comes into view."
    extend " My mind races. Will she attack? Will she try to bewitch us? The suspense is unnerving..."

    # nvl clear

    c snide "Ngh..."

    "My heart pounds. I swear I can {i}feel{/i} her presence..."
    extend " It's soothing, alluring, and at same time, suffocating..."
    "I sense both an welcoming and a frightening presence from her..."
    extend " I've never been so relaxed, yet afraid for my life at the same before."

    # nvl clear

    g "That devil.... Why do I recognize her?"

    c "You can see through the mist?"

    g "My eyes are more precise than most. This is a succubus."
    extend " Pfft, these people gave their lives to summon that? What a waste."

    c "But why?"

    g "I have no clue."
    extend " Time to adapt."

    play sound sfx.melee_swing
    #we'd zoom in on the silhouette here
    "I yelp as he shoves me forward."
    extend " I turn in protest, only to see no one."
    "I fidget as the veil starts to dispers. What does he want me to do?!"
    extend " Wait, succubi aren't very strong. They're spies more than anything else, so he must be testing me."
    "Ok, Caius..."
    extend " Breathe in...breath out..."
    extend " You have the advantage. She's vulnerable to Grace like any other devil, and you know her tricks."
    "I tremble with each step I take."
    extend " I must resemble a scared child who is in over his head. She won't expect much, and it will be her demise."

    # nvl clear

    scene background cult altar with dissolve
    play music bgm.altar_ambience fadein 1.5
    #will be lethal_suspense after jam
    #hide persephone silhouette
    show persephone smirk at center with dissolve

    "I gulp when her true form appears."
    extend " I sense no threat from her. Her eyes aren't cross, and there isn't disgust or bloodlust in them."
    "Careful, Caius, eyes above the chest. Stare too long, and you'll become enthralled..."
    "My mouth opens, but no words leave. I feel breathless."
    extend " If I enter any stance, my guise will be blown. If she lunges first though, I'll be defenseless..."
    "Ugh, to hell with duplicity! I'll engage her before she can-"

    # nvl clear

    v "...Did you kill her children?"

    c snide "Uhh..!"

    "Oh no! We're surrounded by corpses! There's no way she won't suspect anything now..."
    "Damn it! How could I be so careless?! All I've done is give her an opening!"
    extend " Wait...no reaction. She isn't drawing a weapon or anything..."
    "Hell, she's smiling! It's one of amusement, not malevolence."

    # nvl clear

    v "Hehehe! Relax! They're in a better place now."
    extend " Besides, there's no blood on {i}your{/i} hands. Looks like I'm outnumbered."

    # nvl clear

    c "Ugh, right..."

    v "So, what am I dealing with here?"
    extend " Celestial?"
    extend " Exorcist?"
    extend " Adventurer who's in over his head?"

    c "Emissary."

    v "Really? You, one of those cutthroats?"
    extend " Ohhh, it's your first day isn't it?"

    "She carries on like a waitress in a tavern."
    extend " Had she hidden her horns and wings, I might've forgotten she was a fiend..."

    # nvl clear

    c "It's been quite an experience...one I would like to put to bed."

    v "So, are you going to kill me?"

    c "Or send you back to Hell. I prefer the latter to be honest."

    v "Aww, how thoughtful!"
    extend " Buuut...."

    play sound sfx.charm
    with charmflash

    c snide "Gnnnghhh...!" with vpunch

    "Her eyes flash pink, and my head throbs."
    extend " It feels like a hand is squeezing my head, forcing my mind to bend to her will..."
    extend " Except it won't work!"
    "She caught me off guard, but my mind won't bend so easily."
    extend " I faced many temptations when I took my vow, her magic is pitiful in comparison."
    "I'll let her think she has the upper hand...for now."
    extend " Besides, compulsion magic has a fatal flaw: it cannot force it's victim to channel mana nor harm themself."
    "My stance relaxes. As long as her spell persists, I'll have to act like her most devoted companion."
    extend " I'm not too experienced with acting, but I can at least give Griswyr a show."

    # nvl clear

    v "See? Isn't that better? You can call me Persephone, what's your name?"

    c "...Caius."

    p "Hmmm, that doesn't sound familiar... Where are you from?"

    c "...Thrycia?"

    p "That mound of dirt? Wow! That place is older than me!"
    extend " Though I haven't been around that long..."

    c "...How old are you?"

    p "Rude! We just met! Don't you know not to ask a lady her age?"

    c "...My apologies. ...It appears your magic is working too well."

    p "Pfft! I softened you up, I didn't remove your manners..."
    p "I've been around for...twenty years? I'm unsure... Time flows differently in Hell."
    extend " Don't worry, I'm very mature for my age, hehehehe!"

    "Devils are immortal, so twenty years was hardly a drop in the bucket for them."
    extend " Her soul must not have fallen too long ago. So in tandem with being alone, she's also not as experienced."

    # nvl clear

    p "I don't have any intention of hurting you or whoever is lurking in the corner. I just have an \"errand\" to run."
    extend " You won't even know I was here!"

    c "...What kind of errand?"

    p "Nothing special, I just need to touch base with a certain someone."
    p "Would you happen to know a man named Jory? He's a giant! You couldn't have missed him! I think he's still living in Jubilee..."

    "My heart accelerates!"

    c angry "Wh-What do you want-"

    "Calm down, Caius...you're supposed to be pulling her leg."

    # nvl clear

    c "I-uh, I mean...I think he left several years ago."
    $ unlockCompendionEntry("MeropianLore")
    extend " Poor man was wrought with grief. They say he fell in love with a Meropian."
    c "I never believed the rumors, but he wasn't the same after one was executed."
    extend " I prayed for his soul, but that was the only interaction I ever had with him."

    "Her smile curls into a frown, and her eyes widen."
    extend " Every mention of Jory pains her. But why? He never worshiped Hecate, did he?"

    # nvl clear

    p "Oh, that's...too bad."
    extend " And where did you say he was headed?"

    c "...A small village to the west of Jubilee. ...I guess he wanted to get away from everything."

    p "Huh, I see."

    c "Right."

    p "Right..."

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
    play sound sfx.lunge
    "I lunge!"

    # nvl clear

    play sound sfx.whoosh

    c "Wh-Whoooa..!"

    play sound sfx.heavy_crash
    with hpunch

    "I collide with the wall, knocking the wind out of me..."
    "What was that....?"
    extend " It felt like leaping into a tornado. I got shunted backwards as if I were a toy...!"
    "I didn't see her conjure any mana...though she hasn't wielded any while charming me either."
    extend " If no mana is used, it must be innate. But I don't recall succubi being able to manipulate the wind."

    # nvl clear

    p "You thought you could pull a fast one on me?! I'm a devil, goddamn it!"
    p "All things considered, I thought your little act was adorable."
    extend " Until you lied about HIM!"

    play sound sfx.magic_charge
    with maliceflash
    "When she snarls, Malice oozes from her eyes."
    extend " She must notice because she shakes her head and resumes her smirk."

    # nvl clear

    hide persephone
    show persephone smirk at center
    p "So...let's try this again."
    extend " Where's Jor-"

    play sound sfx.slash

    #Ragyuo: I'm thinking Griswyr would come in from the top and appear at the left / right of Persephone
    #Normally I'd use a moveintop command, but maybe you have a better idea?
    hide persephone
    show Griswyr neutral at left with moveinleft
    #will be combat later
    "Gryswyr jumps down from the ceiling, grazing her cheek with his blade."
    play sound sfx.thud
    "He lands then swings at her neck..."
    #Maybe zoom Persephone back? Or to the opposite direction?
    extend " only for her to float out of the way."

    # nvl clear

    p "Hehehe, finally showed yourself, huh? I take it you're his boss?"

    g "Now I've figured you out."

    p "Eh?"

    g "Your cult was very adamant about bringing you here, so adamant that they were ready to die."
    extend " And for a lowly sex devil? That made no sense."

    p "Oh, so we're going there..."
    extend " Sorry, Snowflake, but you aren't my type."
    p "Here's some advice: you should reaaally learn what the sun is. You're looking a little pale~."

    g "Then you brought up Jory, a man shrouded in rumors."
    #$ unlockCompendionEntry("ThornLore")
    extend " They say many things about him. How he knew {i}The Reckoning{/i} would happen. How he fell in love with a gar who worshiped Hecate."

    p "Gar...?"

    g "They say her death throes shook The Third so much that he hired double the protection, and they also say a succubus was the one who dragged him into Hell."
    extend " Which means..."
    g "You're the banshee who caused the Reckoning!" with vpunch

    "I shudder. Could she have been that SAME monster who caused so much chaos?!"
    "She sighs grumpily and claps her hands slowly."

    # nvl clear

    p "Look at that... you blew my case wide open... So much for the surprise..."
    extend " You must be fun at parties, Snowflake. A reeeeal crowd pleaser..."

    g "It was hardly a secret. Even the boy would've figured it out eventually."

    play sound sfx.weapon_draw
    "He draws his hatchet and throws an arm in front of me."

    # nvl clear

    g "Stay back. You are no match for her."

    c "But-"

    g "I've pushed you into danger twice tonight, but only because I knew you could overcome it."
    extend " This fiend is much stronger than a succubus. You'll only get in the way."

    c "Griswyr, she'll just revive in Hell if I don't-"

    g "You talk too much! Do you forget that the enemy is right there?!"

    "What does he mean?"
    extend " Oh wait, she might not know I can wield Grace. By Yeshua, this is not my night..."

    # nvl clear

    c "Alright then, I'll watch for any more Thorns."

    g "That's the smartest thing you've done all night."
    extend " And as for you..."

    g "I will have those wings, banshee! Scream if you must!"

    stop music
    play music bgm.reckoning_I
    play sound sfx.lunge
    #Ragyuo: If an animation is needed, maybe Griswyr would zoom in towards her?
    "He leaps towards her, and she shakes her head."

    # nvl clear

    hide Griswyr
    show persephone smirk at center with dissolve
    p "Good grief, did you learn nothing from your friend?"

    "She waves her hand, and a gust of wind shields her."
    #show Griswyr behind Persephone
    extend " Griswyr lands and skirts behind her."
    play sound sfx.weapon_draw
    hide persephone
    show Griswyr neutral at center
    extend " She gasps as his sword hisses through the air."

    # nvl clear

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

    # nvl clear

    hide Griswyr
    show persephone smirk at center
    p "Fine, fine... You wanna play rough?"

    play sound sfx.dagger_draw

    "Five, razor-sharp claws spring from her fingertips."
    "She hunches forward, mimicking Griswyr's stance."
    extend " He does not appreciate that."

    # nvl clear

    g "...Are you mocking me?"

    p "What?"

    g "You copied my stance!"

    p "..."
    extend " Snowflake, I just met you. Never heard of you  either."
    extend " Guess you're not that important~."

    g "Hmph!"

    play sound sfx.parry
    #Ragyuo: Not sure how to animate this. Maybe using hpunch alongside the sfx will be enough?
    #The upcoming scene is basically Griswyr trying and failing to cut Persephone. What are your thoughts?
    "They both spring forward, claws dragging across steel when they clash."
    "While their stances are similar, their techniques aren't."
    extend " As Griswyr spins in a flurry of swings, Persephone keeps evading his efforts before retaliating."
    "Griswyr attacks viciously, but Persephone appears more relaxed."
    extend " She might just be trying to lure him into lowering his guard, or trying to antagonize him..."
    "Strike after strike comes from Griswyr, but not one lands on Persephone.."
    extend " Griswyr snarls and repeats the same maneuvers.... He is the same whirling cyclone of death he was earlier, yet even his skill and fury are no match for Persephone’s otherworldly evasions. They dance around the room as I do my best to follow their movements and not get swept up in the battle."
    "My heart pounds as she begins evading with growing ease."
    #we'd probably show Persephone behind him here?
    hide Griswyr with moveoutright
    show persephone smirk at center
    extend " After a wide swing, Griswyr stumbles forward. He's wide open!"

    # nvl clear

    c "Griswyr, look out!"

    p "Good night~!"

    g "..."
    g "{i}Blood Lance{/i}."

    play sound sfx.bloodlance
    "A spear of blood eupts from his blade."

    # nvl clear

    p "W-wait..."

    play sound sfx.blood_splatter
    with bloodflash
    extend " Gnnnnggggghhh!!!!" with vpunch

    #Ragyuo: If you think some movement is pertinent here, maybe have her zoom out?
    "It pierces her chest like a dagger."
    extend " Had she not backpedaled at the last moment, it would've impaled her."
    hide persephone
    show Griswyr neutral with dissolve
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
    extend " Again comes his flurry of deadly strikes, but Persephone isn't amused."
    "Her wound isn't deep, but Griswyr has her on the run."
    extend " She can't just float around anymore, or else he might catch her off guard again!"
    "He feints and as Persephone braces herself..."

    # nvl clear

    # TODO: show Griswyr behind Persephone

    p "Ah shit...!" with vpunch

    g "You should've stayed in Hell, banshee!"

    play sound sfx.heavyslash

    "With his sword, Griswyr gouges her waist!"
    extend " Yet Persephone smiles."

    # nvl clear

    p "And you should've brought silver!"

    play sound sfx.galeblast
    pause 0.6
    queue sound sfx.crash
    with hpunch
    #Ragyuo: Griswyr would be send off screen and the screen shakes. He got punted just like Caius did
    hide Griswyr with moveoutright
    "A gale blast sends Griswyr crashing into the wall."
    "I watch in horror! She hit him point blank!"
    extend " She wanted him to get close... Why else would she have relied so heavily on evasion?"
    #Ragyuo: Griswyr would ease back in here
    hide persephone
    show Griswyr neutral at center with easeinbottom
    #combat
    "Griswyr snarls and recovers."
    extend " He may seem unharmed, but his breaths are heavy as he clutches his chest."

    # nvl clear

    c angry "That's enough, Griswyr! Let me handle this!"

    g "Nnngh..."
    extend " Just who do you think you are?! I'm your superior!"

    c "And as my superior, you must test me. Consider this another trial."

    g "Grrr..."

    p "By Yeshua, you're pious, I'll give you that..."

    "Griswyr's temperament is much more aggressive than before."
    extend " He isn't cool and collected anymore, and he eyes me as if I were his foe."
    "And now that I think about it, he did lose his temper earlier, when he beheaded that cultist..."

    # nvl clear

    g "...Very well. She is yours. Do not disappoint me."

    p "Hehehe, you ought to watch your mouth, Snowflake. Someone might get the wrong idea~."

    c smile "Thank you, Griswyr. I won't let you down!"

    #Ragyuo Maybe she would zoom in a little? Or have the screen shake slightly to simulate him approaching her?
    "I ready my stance then slowly walk towards her."
    #Idk how we'd simulate them circling each other, though if you got any ideas let me know
    hide Griswyr
    show persephone smirk with dissolve
    "We circle each other, our eyes not breaking contact."
    extend " She could pounce at any moment, yet all I continue to get from her is that scheming grin."
    "Even now, she's still choosing to toy with us. Something tells me she's a lot stronger than what she's letting on..."

    # nvl clear

    p "So..."
    extend "what did they tell you about me?"

    c "Nothing much. Just that you dragged The Third into Hell..."

    p "Are you sure that was me? It could've been one of my sisters. We all look alike, after all~."
    p "Come on... This is all a misunderstanding! I didn't do anything...I just want to check up on an old friend..."

    "My blood freezes with anger."

    # nvl clear

    c angry "..."
    extend " You mean my friend?!"

    p "Well..."
    extend " If his name's Jory, then-"

    play sound sfx.jab
    with graceflash
    hide persephone
    show persephone angry at center
    extend "Grrrr!!!" with vpunch

    "Too slow!"
    extend " She recoils heavily from that blow, even more than when she got stabbed!"
    "The mana flows in me alongside my fury."
    extend " I don't know what she wants with him, but I don't care."
    "Jory has only wanted to help others. He doesn't deserved to be pestered by the likes of her!"

    # nvl clear

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

    # nvl clear

    p "Grrr...so that's why he picked you."
    extend " Snowflake's soul is too black to ever wield Grace. He needed a proxy, how clever..."

    c "Why are you surprised?"
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
    play sound sfx.potterycrash
    with vpunch
    "She gasps as I spin and hurl her onto the altar."
    extend " She lies splayed among the fractured statuettes."
    show persephone angry at center with moveinbottom
    #zoomed out Ragyuou
    "She pushes herself up, furious, as I waggle my finger."

    # nvl clear

    c angry "Blasphemer! Mother will be displeased!"

    p "Wise ass, huh...?!"

    play sound sfx.galeblast
    pause 0.6
    queue sound sfx.potterycrash
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

    # nvl clear

    play sound sfx.galeblast
    pause 0.6
    play sound sfx.heavy_bam
    c snide "Gahhh!" with vpunch

    "Her second gale that hits me hard... It feels like getting kicked by a mule!"
    #have her zoom in
    hide persephone
    show persephone smirk at center
    play sound sfx.lunge
    "She springs at me, but I block her attack and throw her a second time."
    extend " She lands hard again but recovers quickly and braces herself against the wall."
    "Again she lunges."
    #maybe her sprite would hop to simulate the pounce
    extend " And feints, her flapping wings frightening me and nearly causing me to stumble. What is she going do now?! I don't have the time to-"

    # nvl clear

    g "What are you doing?!" with vpunch
    extend " Attack!!!" with vpunch

    "I obey."

    # nvl clear
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

    extend " I'm using a lot of mana and energy, but I can't let up!"
    "I can't risk giving her another opening! Our lives are on the line, and the lives of others as well."

    play sound sfx.galeblast

    #Have her zoom out, than back in to simulate Caius chasing her
    "She tries to retreat by blasting the ground, but I continue to pursue her."
    with graceflash
    extend " As strong as she might be, my Grace tore through her like a venom."
    "I keep going."
    extend " I've trained my arms and legs to ceaselessly land consecutive blows. Stamina isn't an issue!"
    #have her zoom out
    "She finally manages to break away, but she writhes in damage and pain."
    #have the sprite move slightly to simulate her writing
    extend " I see my mana taking its toll. Each blow makes her twitch and shiver. I almost pity her."

    # nvl clear

    #zoom in slightly
    "I step towards her, ready to end this."
    extend " Yeshua knows how mangled her soul must've been after Hecate got her hands on it..."
    extend " It saddens me..."

    play sound sfx.magic_charge
    with graceflash

    "I close my eyes and summon Grace. I will put her to rest with this next strike."

    # nvl clear

    c "...Farewell."

    p "...Is that pity in your eyes?"
    extend " Aww, how noble! Though not showing kindness to your friend? That's pretty cold..."

    c "...?"

    p "Oh no, I'm not talking about Snowflake. Though you're probably the only friend he has ehehehehe!"
    hide persephone
    show persephone smirk at center
    extend " I can read it in your eyes. You're not motivated by zeal; you're motivated by regret."

    c "So what?"

    p "So what? You know that we fiends can peer into your past, right?"

    c angry "Huh?!"

    p "Uh oh, guess not~."
    extend " Well I can understand Jory not knowing, but Snowflake? Tsk tsk, how irresponsible~!"

    g "Do not humor her, Caius!"

    c angry "You lie!"

    p "Ahahahaha! Why else would people sell their souls?"
    extend " It's because we see everything! Your regrets, what you care about, and what haunts you. It's all an open book!"
    p "Aww, what's with the long face? You were looking so high-and-mighty just a moment ago..."
    extend " I'm guessing I lost your sympathy?"

    "If Griswyr knowing about my past unnerved me, Persephone knowing about it took the cake!"
    extend " How could I not realize?! I'm no scholar, but I've looked far and wide for knowledge about devils, and yet I’ve never heard of this power!"
    extend " More importantly, she knows about HIM!!!!"

    # nvl clear

    p "Ah yes, you let someone down."
    extend " How else would've you have made it this far? You were a nobody until you threw him to the wolves!"
    p "That's pretty wicked! And now you starve yourself to get pity from everyone."
    extend " Hahaha, you holier-than-thou types always have the darkest secrets! Watching your souls fall is soooo delicious~!"

    g "Strike her down, goddamn it!"

    c angry "Grrr! Be quiet, devil!" with vpunch

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    p "Whoa, whoa....what's swatting at me going to do? I'm not the one who abandoned him..."

    c angry "You... "
    extend " You leave him alone, monster!" with vpunch

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    p "Oh, your friend? Hmm, I'm sure he's much different now. People change when their hearts are ripped out."

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    c angry "Tell me, Persephone!"

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    c angry "Hecate calls herself the mother of outcasts, a protector of the damned!"
    #have Persephone zoom out and back in
    play sound sfx.melee_swing
    extend " But you're just like any other devil! You'd corner and bewitch the same people you claim to care about!"
    c angry "The Dretchlings suffer enough without your poison!"

    g "Stop talking, Caius-"

    p "Ohohoho! You have it backwards!"
    extend " We don't corrupt people, we {i}save{/i} them from the lies of your absent Archlords."

    #have Persephone zoom out and back in
    play sound sfx.melee_swing

    c angry "Damn you!!!" with vpunch

    #zoom in, they're locked again
    play sound sfx.magic_charge
    with whiteflash

    "Our manas clash as we clench again."
    "My eyes beam at that grinning monster!"
    play sound sfx.magic_charge
    with graceflash
    extend " My Grace spikes. It must sting her severely, yet she only grins more."

    # nvl clear

    c angry "You and that goddamned archfiend aren't any different!"
    extend " Why else would she reside in Hell?!"

    p "Right, because your god's any better?"
    extend " Who were the Celestials founded under? Oh, he must've been cruel to allow his followers to imprison Dretchlings like cattle."
    p "Yet we're the bad guys for coming to their rescue? How is that fair?"
    extend " Face it, your precious Archlords don't care about you!."
    extend " Now that I think about it, looks I have TWO errands to run!"

    c angry "I'll end you-"

    play sound sfx.grapple
    extend " Agh!" with vpunch

    #have her increase in y-axis?
    "A hand grabs my throat, and she hoists me above her."
    "My mana vanishes alongside my breathing! I can't channel it if I can't breathe...!"

    # nvl clear

    p "Though while we're talking about fibbing, I wasn't entirely honest with you."
    extend " You see, we devils can't read people;s pasts. So I appreciate the information~."

    c snide "Gngh!!!" with vpunch

    "My heart skips, and she giggles darkly."

    # nvl clear

    p "You mortals will believe anything. Just like false seers, we only need to paint a picture broad enough to apply to anyone, and suddenly you're spilling your guts for us."
    p "And now you've failed him twice..."
    extend " Nah! You did him a favor!"

    play sound sfx.magic_charge
    with maliceflash
    "Wind blasts me from her grip, and she channels Malice and winds in her other hand."

    # nvl clear

    p "I'll take good care of him, you can die now."
    extend " Buh-bye~!"

    #Ragyuo: Not sure how to animate her here. She basically dropped Caius and leapt backwards
    play sound sfx.weapon_swing
    pause 0.6
    queue sound sfx.thud
    p "Shit!" with hpunch

    hide persephone with moveoutright
    show Griswyr neutral at left with moveinleft
    #combat
    "She drops me, narrowly slipping past Griswyr's slash."
    "I don't have the strength nor the courage to stand..."
    extend " She played me like a harp... So easily too!"
    "Griswyr turns to me, his eyes as stoic as ever."

    # nvl clear

    g "...I thought I told you not to disaapoint me."

    p "Aww, did I break your friend-"

    #have Persephone zoom out and back in
    play sound sfx.weapon_swing

    extend " Whoa Snowflake! Lighten up, will ya?!"
    $ unlockCompendionEntry("JinxLore")
    extend " I mean, isn't being jinxed bad enough?"

    g "..."
    extend " It'll be worth it when I feast on your blood!"

    "Wh-what?! What does he mean-"
    extend " Oh right, he licked his sword after it got coated in gore. He's not trying to scare her, he MEANS what he's saying..."
    "Persephone looks as dumbfounded as I do."

    # nvl clear
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

    # nvl clear

    g "And now you-."
    play sound sfx.slash
    with bloodflash
    extend "Ngh! What the-?!" with vpunch

    "Wounds tear open in his arms. They seem to surprise him more than hurt him."
    extend " I can't blame him for his shock. I didn't even see her claws land. So how did she get him?"

    # nvl clear

    g "Tch...just a flesh wound!"

    play sound sfx.hurl
    "He siphons some of the blood and flings his hatchet."
    extend " Persephone turns around, but he teleports in front of her, sword at the ready."
    play sound sfx.parry
    "She catches his sword in two fingers, the blade causing blood to trickle down her hand."
    extend " Griswyr winces."

    # nvl clear

    hide Griswyr
    show persephone smirk at center with dissolve
    p "Ooh, looks like you grazed me..."
    extend " Go on, have a taste."

    #Compared to last animation, Griswyr is slowing down.
    "She releases his blade and holds out her fingers."
    extend " Griswyr cringes but follows through with his swing."

    # nvl clear

    #have Persephone zoom out and back in
    play sound sfx.weapon_swing

    p "Hey now, don't be greedy..."

    g "You think taunting me is going to work?"
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
    extend " Every time he uses one of those attacks, he injurs himself..."

    # nvl clear

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

    # nvl clear

    c angry "Don't dodge, Griswyr, or you'll be cut by her wind!"

    g "Grr! No shit!!!" with vpunch

    #move his sprite to the left and right
    hide Persephone
    show Griswyr neutral at left with moveinright
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

    # nvl clear

    g "I told you I'd have your wings, but I'll start with your neck."
    extend " Even if you revive in Hell, you'll have to find your way back to our plane, and you'll become my prey again!"

    p "Ngh...not bad! You're {i}actually{/i} starting to scare me, Snowflake!"

    g "Even now, you joke?!"

    play sound sfx.slash
    with bloodflash
    p "Gngh...!" with vpunch
    g "What will it take for you to stay down?!"
    extend " You're like a cockroach! You sever its head, yet it still crawls!"

    p "Ohh, don't let me stop you. If you want my neck, go for it."
    extend " I am your snack after all. I'm powerless to stop you. What good would any resistance do?"

    play sound sfx.slash
    with bloodflash
    g "Shut up!!!" with vpunch

    "By Yeshua...fiends are something else."
    extend " Despite all her injuries, Persephone still keeps going."
    "Griswyr pauses, finding both of his hands drenched in blood..."
    extend " He just sits there...something has gripped his heart."
    play sound sfx.slash
    with bloodflash

    "He drives the shortsword into her again...and he pauses a second time."
    extend " Try as he might, he can't seem to break her smile."

    # nvl clear

    p "They say a predator takes the easiest approach to hunting. Even if a wolf could kill any human, it will only target the weakest link."
    p "Matter of fact, wolves only hunt when they {i}know{/i} they can win. But I prefer cats."
    extend " They are an exception. They hunt for sport as well as food. A cat will even choose to torment its prey before killing it."
    p "They're very sadistic - at a glance."
    extend " Truth is, that cat isn't torturing for fun. It's tiring the prey out to ensure that it can't retaliate."
    p "Is that why you're frozen? Is it because I'm laughing off your little cuts?"
    extend " Or is it because your instincts won't allow you to move?" with vpunch

    g "...Enough of this!"
    extend " I am not enslaved by my hunger..."
    extend " It is enslaved by me!!!" with vpunch

    "His jaw expands as he dives!"

    # nvl clear

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

    # nvl clear

    c "Griswyr!"

    "A second wind lifts me back onto my feet, and I dash toward them!"
    play sound sfx.kiss
    extend " Her kiss is lethal! She's sapping his mana with every twist of her lips."
    play sound sfx.kiss
    "His body wrinkles, and her wounds begin to close."
    #zoom in
    extend "She pulls away as I charge."

    # nvl clear

    p "...Oh, you're still with us?"

    play sound sfx.thud
    "Griswyr collapses to the floor as we engage."
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
    play sound sfx.bam
    pause 0.6
    play sound sfx.magic_charge
    with whiteflash
    with hpunch
    "Sounds of hissing rattle the room. The mana screams just as violently as our blows."
    extend " Yet, she suffers more than I do. Looking more closely, I see her body tremble."
    #Ragyou more gatling fist Kung lao barrage
    play sound sfx.rapidfirepunch
    with hpunch
    "My blows from earlier weren't in vain, my mana still wracks her body!"
    extend " Which means I can still strike a killing blow."

    # nvl clear

    hide persephone
    show persephone angry at center
    p "Ugh, you're so annoying! Go away!"

    #zoom in Persephone
    play sound sfx.galeblast
    pause 0.6
    queue sound jab
    "I weave past her gale and jab her chest."
    "I gnash my teeth whilst my palms assail her like a barrage of arrows."
    play sound sfx.weapon_swing
    pause 0.6
    queue sound jab
    extend " She swipes, but I duck and slam my heel into her sternum."
    #shake persephone with each blow
    play sound jab
    "Her hisses devolve to growls the more I strike her."
    extend " Her eye twitches. She's reaching her limit."
    #zoom in and out of Persephone
    "She keeps trying to float backwards, but I keep stepping forward."
    extend " My arms are growing heavy...I'm starting to run low on mana. I can't continue much longer..."
    "I need to land one good strike."

    # nvl clear

    c angry "Fall, monster!" with vpunch

    #zoom out Persephone
    play sound sfx.melee_swing
    "I kick and hit nothing but air..."
    "She flies backwards, digging her claws into the wall. She glowers, ready to attack again."
    play sound sfx.magic_charge
    with maliceflash
    extend " Malice and wind engulf her! I can't stop this...and even if I dodge..."

    # nvl clear

    g "You goddamned fool! What are you doing?!"
    extend " This battle is yours! DO - NOT - FALTER!!!" with vpunch

    "..."
    extend " I know, Griswyr."

    #zoom in Persephone
    play sound sfx.lunge
    pause 0.6
    queue sound heavy_bam
    c "Gnnnnngggggghhhh!!!" with vpunch

    "I dodge, and her intense gusts bludgeon my body. I felt like I’ve slammed straight into a wall of pure force!"
    "Blood sputters from my mouth as several of my ribs collapse...."
    extend " The only reason the rest of me doesn't follow suit is because Grace protects me from most of the pain..."
    "It takes all of my concentration not to be swept away..."
    extend " And now..."

    # nvl clear

    play sound sfx.jab
    c angry "HAAAA!!!!" with vpunch

    "I deliver a mighty blow to her chest and..."
    extend "nothing."

    # nvl clear

    p "...Was that your last stand?"
    extend " WEAK!!!" with vpunch

    #zoom out Persephone
    play sound sfx.heavy_bam
    "Her Roundhouse kick sends me flying. Time stands still as I float away..."
    extend " I turn to her, that insipid grin peering into my soul."
    "I breathe heavily, coughing up blood as I clasp my hands."

    hide persephone
    scene image "#000" with dissolve

    "..."

    extend "Shine!" with vpunch

    # nvl clear

    scene background cult altar with dissolve
    stop music fadeout 1.5
    p "Huh...?"

    play sound sfx.manaexplosion

    scene image "#fff" with iris_in_out

    "My Grace pours from her body and explodes."
    extend " I can't see a thing, but this battle has ended."
    "That blast tore her apart from the inside out."
    extend " Against a mortal, it would just render them paralyzed, but against a devil? There's no way she survived."
    "A hand caught me. It must've been Griswyr's."

    # nvl clear

    c snide "Ngh..."

    g "Impressive. What was that?"

    c "Agh...well each of my blows injects my mana into my opponent, disrupting their own..."
    extend " And once it consumes most of their body, I can cause it to tear itself out..."
    extend " Agh...it hurts to talk..."

    g "That's...violent. Color me impressed."

    c "Well, it doesn't kill mortals..."

    g "Of course it-"
    extend " Gngh!" with hpunch

    c "What's the matter...?"

    g "I still smell her!"

    scene background cult altar with dissolve
    "As the radiance dies down, the first thing I spot are two, red eyes glaring at me..."
    extend " My teeth chatter. My body feels cold, exhausted, and afraid. That was my strongest technique, how did she survive it?!"
    show persephone smirk at center with dissolve
    play sound sfx.magic_charge
    with maliceflash
    "Malice's crimson hue shrouds her. Her stance is unsteady, however she appears more than capable to continue..."
    extend "I try to stand only to stumble. A stabbing pain pierces my waist..."
    "I could conjure Grace to numb it, but I wanted to reserve what little I had left..."

    # nvl clear

    p "You know, I tried to be nice... I tried to make your death quick and painless BUT now I don't really care!"
    p "I'll give you credit, that might've killed me. Good thing Snowflake topped me off hehehe...!"

    hide persephone
    show persephone angry
    play sound sfx.dagger_draw
    "She hisses as her talons spring from her fingers."
    play sound sfx.magic_charge
    with maliceflash
    extend " Her Malice spikes. In hindsight, she didn't use up as much mana as I expected..."
    hide persephone
    show Griswyr neutral at center with dissolve
    "Griswyr seems more upset than afraid as he looks to the ground."
    play sound sfx.weapon_draw
    extend " He spits and readies his weapons."

    # nvl clear

    g "Looks like this mission is a failure! Out of all the monsters, we had to get matched up against that goddamned banshee!"

    c snide "Griswyr...?"

    g "I'll hold her off while you crawl away. Don't worry about me, because I'm not coming back."

    "He crosses his throat and speaks gravely "

    # nvl clear

    g "This is my final lesson to you, Caius. Even in death, we Emissaries leave no trace. We'll face annihilation if that's what it takes!"
    extend " Do not let any information fall into the hands of the enemy! To the end!"

    #zoom in Griswyr
    play sound sfx.lunge
    "He charges."
    extend " He startles Persephone, but she meets his advance."
    "He isn't dodging..."

    # nvl clear

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

    # nvl clear
    #should we show Persephone's sprite?
    p "What the hell are you-?!"

    play sound sfx.grapple
    "He drops his hatchet before getting behind her and hooking his arms around hers, pulling up and restraining her."
    extend " He clings to her like a monkey. Try as she might, Persephone can’t shake him."

    # nvl clear

    p "Grr! Snowflake, I'm not in the mood!"
    extend " Let go!!!"

    g "Ngggh...what are you doing, idiot?! Run!"

    p "Who are you calling an idiot?! You're the one who-"
    extend " Wait a minute..."

    "I wish I had the strength to flee..."
    extend " My heart weeps for him. My eyes might also weep if it didn't hurt so much to breathe..."
    "Even if I start crawling away, there's no way she's going to let me go."
    extend " I don't know what Griswyr is planning, but if it involves his blood magic, she'll just chase me and we'll all be collateral damage."
    "Best I can do is stay here and see him off..."
    "Persephone turns to him. I can't see what happened, but I have a bad feeling in my stomach..."

    # nvl clear

    p "...Hehehe, so that's what you're up to? How naughty~."
    extend " Isn't suicide frowned upon by the Celestials?"

    c "Suicide?!"

    g "Too late...!"

    play sound sfx.magic_charge
    with maliceflash
    "Griswyr's own Malice erupts, causing a whirring sound to hum from within him."
    with graceflash
    extend " Blue glyphs appear on the studs in his armor, growing brighter by the second."
    "I try to call to him, try to move towards him, but my body still refuses to budge..."
    extend " This is horrible! Why is he dying for me?! I'm a novice, I'd be much easier to replace than him."
    "After all, I can't even save myself, let alone anyone else..."

    # nvl clear

    g "See you in Hell, banshee!" with hpunch

    hide Griswyr
    show persephone angry at center
    p "Ngh..."
    hide persephone
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

    # nvl clear

    p "I can't have you exploding on me. I'll be taking this."

    play sound sfx.heavyslash
    "She tears off his vest and tosses it to the side."
    "Griswyr stirs and groans. He tries to pull away."

    play sound sfx.grapple

    extend " But her palm around his maw clenches."

    # nvl clear

    p "Now now, I'm still playing with you. Besides, you've had a long day~."

    play sound sfx.heavy_bam
    with vpunch
    extend " So go to sleep!"

    "She slams her knee into his chest, knocking the wind and consciousness out of him."
    #move Persephone to the left/right
    "I watch helplessly while she drags him towards the hanging corpse."
    extend " She tears the grizened woman from the bushes and pins him there."
    "What does she have in store for-"

    # nvl clear

    hide persephone
    show persephone angry at center
    p "Hey, shithead! We're not finished!"

    #should we have an animation for this? Maybe Caius's perspective shifts up by the y-axis?
    "I have to use the wall just to stand..."
    extend "My body twitches with every movement. My lungs are on fire, and these shattered ribs are all too eager to feed me pain..."
    "I breathe heavily, knowing that I only have one way out of this."

    stop music
    play music bgm.reckoning_II
    play sound sfx.magic_charge
    with graceflash
    "Grace surges from my body."
    extend " With this much pouring out, I'll run out of mana in no time. hHowever I need Grace just so I can move..."
    "On the flip side, expending this much mana will inject more into her body. I need to blow her up again..."
    "Who will burn out first? Will I be able to hold up long enough to defeat her? Only one way to find out."

    # nvl clear

    p "Still have some fight left in you?"
    extend " Good! I wasn't satisfied!"

    play sound sfx.magic_charge
    with maliceflash
    hide persephone
    show persephone smirk at center
    p "Even if you don't feel it now, your body is in agony."
    extend " And that pales in comparison to what I have in store for you!"
    p "There's no way Jory raised someone so blind! If the Third lived, you'd kiss his boots like every other slave!"
    extend " You self-righteous idiots are what's wrong with this world!!!" with vpunch

    c "Ngh...maybe. Maybe I am too pious... And I don't know what you went through..."
    extend " But I'd sooner believe in myself than an Archfiend...!"

    p "That's not the first time I've heard those words, and it won't be the last..."
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
    hide persephone
    show Jory happy at center with dissolve
    "With each punch, visions of Jory enter my mind..."
    extend " Is my life flashing before my eyes...?"

    # nvl clear

    j "{i}Relax, Caius, you're always so uptight.{/i}"
    extend " {i}Take a load off and breathe once in a while, yeah?{/i}"
    hide jory with dissolve
    play sound sfx.heavy_bam
    with vpunch
    hide Jory
    show persephone angry at center
    p "Gaaaaahhhh!!!" with vpunch
    #zoom out Persephone
    "That attack sends her reeling. If I can just land a few more strikes like that one..."
    #zoom her out and up y-axis
    play sound sfx.galeblast
    pause 0.6
    queue sound sfx.galeblast
    pause 0.6
    queue sound sfx.galeblast
    pause 0.6
    queue sound sfx.galeblast
    pause 0.6
    queue sound sfx.galeblast
    "She blasts herself airborne, screeching before launching a volley of gusts towards me."
    extend " I lack the agility to dodge... I walk forward, blocking, deflecting, and even enduring gust after gust..."
    play sound bam
    with vpunch
    "Even with Grace protecting me, my body rattles with every blast..."
    #zoom in on her
    "I breathe deeply before jumping up to attack her"
    play sound sfx.grapple
    #move screen downwards
    queue sound crash
    with hpunch
    extend " She dodges and grabs me, and I drive my mana into her as we plummet to the floor."

    # nvl clear

    hide Persephone
    play sound sfx.heavy_bam
    with vpunch
    #show griswyr silhouette at center with dissolve
    g "{i}How do you expect to be an Emissary when you're so weak?!{/i}"
    g "{i}I was ready to die for the mission, yet here you are, ready to surrender everything you stand for!{/i}"
    g "{i}Fight goddamn it, even if it kills you!{/i}"

    hide Griswyr with dissolve
    show persephone angry at center
    play sound sfx.grapple
    with bloodflash
    "My fractured arm latches onto her face, my fingernails and Grace digging into her flesh!"
    extend " A shrill yelp meets my ears. More of her blood trickles down my hands as I hold on for dear life."
    play sound sfx.jab
    #zoom her out a bit
    "She pries my palm from her head, and I kick her off of me."
    extend " I rise, my teeth bared and my eyes seeing red."
    #zoom in
    "Her gaze wavers when I sprint towards her."
    play sound sfx.grapple
    pause 0.6
    queue sound sfx.heavy_bam
    with hpunch
    extend " Her wings flap, and I grab her foot before clobbering her face."
    #move sprite slightly
    play sound sfx.weapon_swing
    "She squirms and slashes."
    extend " Her nails graze me. I spit up blood and keep attacking."
    "She isn't nearly as dangerous when you have her pinned!"

    # nvl clear

    p "Grrrrr!!!" with vpunch

    c "..."

    p "Ngh...struggle all you want! In the end...you'll stll-"

    hide persephone with moveoutright
    play sound sfx.hurl
    pause 0.6
    queue sound sfx.potterycrash
    "I shove her jaw shut and hurl her into the table."
    show persephone at center with easeinbottom
    #zoomed in slightly Ragyuou
    extend " She leaps to her feet and I approach, walking slowly."
    #zoom in slighty
    "She lunges but flinches."
    #move her sprite from side to side
    extend " She staggers more and more with each step I take towards her."

    # nvl clear

    #hide persephone
    #show Priam sprite at center with dissolve
    vi "...You hate me, huh?"
    extend " Man...I knew I messed up, but did you have to tell her about me...?"

    "...You're right."

    # nvl clear

    play sound sfx.heavy_bam

    p "AHHHH!!!!!" with vpunch

    vi "I was just trying to protect us..."

    "I know..."

    # nvl clear

    play sound sfx.heavy_bam
    with hpunch
    p "Gah...damn you! Ngh...!"

    vi "Why did you abandon me, Caius?! I thought we were friends..."

    "...We are."
    # nvl clear

    #hide Priam
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

    # nvl clear

    vi "You're coming back, right?"

    "...I am."
    # nvl clear

    play sound sfx.magic_charge
    with graceflash
    "I lift my hands and clasp them together."
    "With an unsteady breath, I speak"

    # nvl clear

    c "Rest in peace..."
    extend " Ngh!!!" with vpunch

    play sound sfx.thud
    with vpunch
    #move screen down y-axis
    "Suddenly, I fall to my knees."
    extend " Intense pain floods through my veins, wracking my entire body!"
    "The strain prevents my hands from reaching her...I've run out of mana."

    # nvl clear

    c snide "No...not now!"

    vi "I knew I couldn't trust you..."

    "Tears well in my eyes. There isn't anything I can do anymore..."
    "It looks like I've reached my limit first..."
    extend " My adversary laughs triumphantly."

    # nvl clear

    c "Priam...I'm sorry. I tried my best..."

    p "Your best FAILED you!" with hpunch

    hide persephone
    play sound sfx.lunge
    scene image "#000" with dissolve

    "She pounces, and I close my eyes..."
    extend " So be it. Someone, anyone, help him..."

    play sound sfx.heavyslash

    "..."

    # nvl clear

    g "Caught you!"

    scene background cult altar
    show Griswyr neutral at center
    #combat
    "Griswyr jumps down from the ceiling, his body engulfed by his Malice."
    "She clutches her slashed arm, and her body convulses."

    # nvl clear

    g "Even if he couldn't finish the job, there's still a lot of Grace inside you."
    extend " Seeing as how both manas repel each other, I wonder what will happen when my Malice is added."

    hide Griswyr
    show persephone angry at center with dissolve
    p "...Oh shit!"

    stop music fadeout 1.5
    play sound sfx.magic_charge
    with graceflash
    play sound sfx.manaexplosion
    hide persephone
    scene image "#faf7f7"

    " Before exploding just like before."

    pause 3.0

    "I can't believe it...I survived! We won!"
    extend " I don't care about the buzzing pain coursing through me. Now everyone is safe from her..."
    "Better yet, I never realized before that Malice could also set off such an explosion..."

    # nvl clear

    c "Griswyr..."
    extend " How did you know that would happen...?"

    g "I didn't."
    extend " It was a theory at best. Either way, her blood gave me the second wind I needed."

    g " Even if that didn't kill her, she was more than injured enough to..."
    extend " WHAT THE FUCK?!" with vpunch

    scene background cult altar with dissolve
    show Griswyr neutral at center with dissolve
    #combat
    "The lingering effects of the explosion dissipate and Griswyr stomps furiously."
    extend " Persephone was defeated, so what is setting him off?"

    # nvl clear

    g "HOW THE HELL DID SHE ESCAPE?!" with vpunch

    c snide "Wh-wha...?"

    "I look to the floor and gasp. There are no remains, no body, no sign of her. Persephone is gone!"

    # nvl clear

    g "GODDAMN IT! SHE WAS A NUISANCE BEFORE, YESHUA FORBID HOW HARD SHE'S GOING TO BE TO TRACK NOW!!!" with vpunch

    c "How...how do you know she escaped..."

    g "DON'T YOU THINK I'D TELL YOU IF I KNEW?!" with vpunch
    extend " Damn it to hell! That Banshee will cause a panic if people learn she's back in our plane..."
    g " Yeshua knows what she's plotting! A second reckoning?! Summoning that Archfiend..."
    extend " GRAAAAH!!! THIS IS HORRIBLE!!!" with vpunch

    "A voice booms into my ear."

    # nvl clear

    p "...Looks like you win this time."
    extend " Don't worry, I'll leave Jory be just as you wished. Anything to get away from you..."
    p "If you see me again, do a girl a favor, and just keep walking!"

    c "...Griswyr."

    g "What is it?!"

    c "Don't..."
    extend "tell..."
    extend "Jo-"

    play sound sfx.thud

    scene image "#000" with Dissolve(1.0)

    pause 3.0

    jump scene_06

    #ask player to save game

    return
