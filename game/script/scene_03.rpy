#
# label scene_03:
#
#     scene background cave entrance
#
#     "As we brush past the thickets, we come upon a cave."
#     extend " It has crude, wooden doors at the entrance, much like you'd expect from hovels owned by brigands."
#     "What catches my eye, however, are the roses."
#     extend " The outskirts of the area are decorated with bushes of purple roses: Hecate's symbol."
#     "To be so bold as to place your beliefs out in the open, especially when growing purple roses is forbidden..."
#     extend " Does their faith inspire that arrogance, or do they have reason to be so open?"
#     "To the side of the door stands a man cloaked in purple robes, nodding off."
#     extend " If he’s on watch, he’s doing a poor job..."
#     "Griswyr and I crouch beneath the bushes. The Thorn continues his daydreaming, mumbling to himself."
#
#     cu "Oh man, tonight's the night! We can finally take back what's ours!"
#     extend " Those damned Celestials chased us out of the city, and for what?! I baked bread! Worshiping mother wasn't hurtin’ nobody!"
#     cu "But damn, why did I get stuck outside? I wanna see her emerge on that altar. Gotta make sure Mother's agent is given a warm welcome!"
#     cu "Well, she'll be out soon enough. There's no sign of any Celestials, guess I can take it easy until then. After all, chanting is hard work..."
#
#     "He really enjoys talking to himself..."
#     "I shudder, spotting Griswyr on all fours...."
#     extend " He leers at the cultist like a wolf would at a deer!"
#     nvl clear
#
#     g "Alright, recruit, deal with him."
#     c "Wh-What?! Just by myself?!"
#     g "Did I stutter?"
#     c "Shouldn't we move together? We don't have much time..."
#     g "There's no guarantee that we'll make it. Besides, I wish to see what you're capable of. Now go!"
#     c "Ugh, yes sir..."
#
#     "I stumble out from the bushes. I was prepared to fight, but not by myself..."
#     "Alright, what’s my plan?"
#     extend " Perhaps I could rush him. If I'm quick, I could knock him out and slip inside."
#     "But what if there are others watching from behind the door?"
#     extend " I can’t see anyone from the other side, yet I would still be risking getting swamped by an ambush."
#     "Hmm, maybe I could convince them to let me inside? Many have called me a monk, so I could claim I’m a pilgrim of Hecate.."
#     extend "But I don't know anything about Hecate's faith. If they test me, I wouldn't-"
#     nvl clear
#
#     cu "Who the hell are you?!" with vpunch
#
#     "Ah no..."
#     "He draws his kukri and scuttles towards me."
#     extend " I toss my hands in the air, stammering like a child.
#
#     c "Ah! I-I mean no harm! I-I'm just a m-monk, and I was-was just going for a walk!"
#     cu "Out here, in the depths of the forest?"
#     c "Yes...I was enjoying myself a bit too much and got a little lost."
#     extend " Um, would you happen to know the way back to Jubilee?"
#     cu "...Hmm."
#
#     "It takes all my self control not to attack as he draws closer."
#     "My heart races! Is he going to cut me?"
#     extend " A broad smile answers my worries. It’s as if he’s forgotten he’s upset."
#     "Hold on, did my plan actually work...?"
#     nvl clear
#
#     cu "Just keep heading straight, and you'll find the road. If you got this far, you should be okay on your own."
#     c "Ahh! Is it that simple?! I made so many twists and turns..."
#     cu "It is a nice night. That full moon is splendid!"
#     c "Yes, sir...!"
#     cu "Wait, you said you were a monk?"
#     c "Uh huh..."
#     cu "Who do you worship?"
#     c "Ummm, Yeshua!"
#     cu "Ha, I never would've guessed."
#
#     "Why is he being so nice to me...? Especially after I said Yeshua?"
#
#     cu "You monks are a dime a dozen! Can't believe you'd come this far without an escort."
#     c "Well haha, I have faith in my lord..."
#     cu "Ahh, I can relate. So do I!"
#
#     #play sound Slash
#     #queue sound Bam
#     #hide Cultist
#     #queue sound Thud
#     "Within a blink of an eye, he swings the knife and I strike his chest."
#     "I tremble. So he was just leading me on? How could I be so naive...?"
#     extend " Had I been a second slower..."
#
#     #show Griswyr at center
#     g "So what was your strategy, there?"
#     c "I have no idea..."
#     g "Well, you got him away from the door. That should help us slip inside."
#     c "We can hide him in the rose bushes. When he wakes up, being tangled up in there will slow him down."
#     g "..."
#     extend "You think he's going to wake up?"
#     c "Huh?"
#
#     #play sound Blood_Splatter with bloodflash
#     "Did Griswyr just..."
#     extend "cut his throat?!"
#     "The Thorn's gurgled chokes ring through my ears, and Griswyr licks his sword."
#     extend " My stomach grows nauseous watching that... What is the point of that..? He's not scaring anyone but me..."
#     "Time stands still. The body wriggles slightly before going stiff..."
#     extend " I close my eyes multiple times, just to open them to the same carnage..."
#
#     g "If any cultists are on patrol, I say we leave the body in the open."
#     extend " It'll give them a taste of what awaits them."
#     c "...Why?"
#     g "Oh? Do you feel sorry for him?"
#     c "That's...not how we do things. He should have been tried by the Law, not us..."
#     g "I don't see the problem. He would've been killed either way."
#     extend " If anything, he got off easy. I doubt he even knows he's dead."
#     c "Griswyr...!"
#     g "What? Are you going to tell me he could've been redeemed?"
#     extend " He didn't think twice when he tried to remove your head."
#     c "..."
#     extend "I don't like this. We're Emmisaries. We protect people, we don’t butcher them..."
#     g "Yes, we should give a man who wanted to plunge our world into Hell another chance."
#     extend " Why? So he could give us lip service and try again?"
#     c "You're assuming again, Griswyr."
#     extend " Devils prey on weakness. Not all of their worshipers are malicious. A lot of them didn't have a choice..."
#     g "And I'm supposed to care?"
#     extend " The road to Hell is paved with good intentions. If you try to bring a fiend into this world, you are an enemy of humanity no matter your reasons."
#     c "And if they were deceived?"
#     g "If a devil tricks you, that is a failure on your end. Everyone knows not to believe those monsters."
#     extend " People aren't blameless. That man knew what he was signing up for. And now he is with his wretched archfiend."
#     c "Another asset for her ranks..."
#     g "So be it. He's locked in Hell and no longer our concern."
#     extend "If you're done preaching, can we resume our objective?"
#     c "...Yes sir."
#
#     "I’m heartbroken. I knew he would be cold, but not heartless..."
#     extend " I understand his fears, but I don’t agree with his methods. I hope that he won’t expect me to take someone's life so..."
#     extend "callously."
#     "Perhaps I care because of my guilt."
#     extend " Dretchlings are prime targets for Devils. Their bitter mistreatment by others pushes Dretchlings straight into the hands of Devils."
#     "I only hoped that a saint would give {i}him{/i} the compassion I couldn't..."
#     nvl clear
#
#     #scene cave
#     #play sound Door_Open
#     "We slither through the door and are greeted by a dim cave."
#     "Torches with purple flames light the corridor, and the pleasant aroma of roses enters our noses.
#     "Their dedication to that single flower astonishes me. I expected something more elaborate..."
#     "Griswyr moves so lightly. There are times when I have to double check if he’s still beside me."
#
#     play sound Lightgrapple
#     c "Ngh..."
#     g "Watch your step. We are in enemy territory."
#
#     "He draws his hatchet and kneels."
#     extend " Ah, a tripwire! Of course, I should've expected that..."
#
#     g "Brace yourself."
#
#     #play sound KaTHUNK
#     "I leap backwards, only for a loud noise to follow!"
#     "We turn to and fro but hear nothing heading our way except footsteps."
#
#     g "Damn. I should've known they lacked the funds for elaborate traps..."
#     c "We're caught in a corridor. There won't be much room to maneuver."
#     #show Griswyr combat
#     g "Stand back. I'll take care of them."
#     c "B-By yourself?!"
#     g "Watch and learn, and don't interfere."
#     #If we have a combat sprite with black pupils, they'll shift to red here
#     extend " They're mine!"
#
#     "It’s momentary, but I think I see a glimmer in his eyes."
#     extend " it irks me. I know Emissaries hunted down apostates, but I fear he might be taking that role too seriously..."
#     "Several disciples rush forward, weapons drawn."
#     extend "Just like the first guard though, no one notices us at first."
#
#     cu "The hell? Did Oakley set off the tripwire again?! How many times do we have to spell it out for him?!"
#     cu "Where is Oakley anyways? I get being embarrassed, but he'll have to face us eventually."
#     cu "Wait, Oakley is as stubborn as a mule! He wouldn't cower like that, so that means-"
#
#     play sound Heavyslash
#     with bloodflash
#     cu "GAAAAAAAAHHHHHH!!!!" with vpunch
#
#     play sound Thud
#     "Griswyr doesn’t strike from behind – no, he plants himself at the center of the group!"
#     "His victim collapses, his throat cut wide open. I didn't even see the slash"
#
#     cu "Agh...!"
#     extend " Intruder-"
#     g "Too slow."
#
#     #some flashy animation or whatever with a lot of blood
#     "The cultists realize they are being ambushed and turn their fury on Griswyr. As each one attacks him though, he spins with his weapon, each twirl  tearing apart his victims completely."
#     extend " His stance is wide, and he spirals with ferocity AND dexterity! No matter how they try to fight him, none of the cultists stand a chance."
#     "The cave quickly fills with blood and screams."
#     extend " The acolytes are panicking now, desperate to stop him or escape. Griswyr won’t let them do either."
#     "He may as well be a tornado, cutting down his victims with vicious twirls."
#     extend " But he does more than just spinning. Whenever someone runs at him from behind, he pauses and suddenly gouges them with his sword."
#     #with maliceflash
#     "At one point, we hear chanting and notice a cultist draped in a red aura."
#     extend " He’s channeling  Malice, the mana that devils wield! It gives unimaginable power to its wielder, but is also known to corrupt them."
#     "Griswyr pauses his massacre to face the powerful cultist. . Unfazed, he scoffs."
#     extend "I gasp as Malice erupts from Gryswyr's arm as he flings his hatchet."
#     nvl clear
#
#     #with bloodflash
#     cu "AAAAAHHHH!!!!" with vpunch
#
#     "The apostate bellows, the hatchet lodged within his skull!"
#     extend "I grow sick, watching blood pour from him like a fountain..."
#     "I couldn't believe what I saw. Gryswyr summoned the same, wicked mana as the Thorn!"
#     extend " But he's an Emissary, someone who protects people. So why would he use Malice when it corrupts people?"
#     "Being down a weapon hardly slows Griswyr."
#     extend " He flourishes his sword as if it’s a knife and cuts down the rest of the cultists who are now in disarray and significantly low on numbers."
#     " They know they don’t have a chance of winning or surviving."
#     extend " Moments later, the cave is silent as the final bodies fall. Griswyr merely frowns in disgust as he collects his weapons."
#
#     g "As expected, they were pathetic."
#     extend " Were you paying attention Caius?"
#     c "Ngh..."
#
#     "The hallway, AND Griswyr are painted crimson!"
#     extend " The metallic stench upsets my stomach. The gore, the carnage, the corpses littered across the floor, it all taxes me greatly..."
#     "Worst of all, the man with the hatchet inside his forehead s still alive and still screaming..."
#
#     cu "Please! I surrender! Just get this thing out of my head!!!"
#     c "By Yeshua, I'm going to be ill..."
#     g "Swallow it! This is only the beginning."
#
#     "Griswyr waltzes up to the man, not granting him any mercy."
#     extend " The poor Thorn scurries away, until he has nowhere left to go."
#     "Griswyr shakes his head. He appears bored, of all things..."
#
#     g "Surrender is cheap, I want information."
#     cu "Right, right! Just get this thing out of my head!"
#     g "I'll remove it AND your head if you don't start talking."
#     cu "Alright! Please, just don't hurt me..."
#     g "Tch..."
#     extend " Quit cowering, Caius! Get over here."
#     c "...Right"
#
#     "Each of my steps squelches as I walk..."
#     extend " The blood has formed puddles across the ground. Moving through the carnage sends shivers down my spine..."
#     "It feels like I’m wading through a sticky, red mud... By Yeshua, I hope this will wash out."
#
#     cu "So there's...five men leading the ritual. They've already begun chanting..."
#     extend " I doubt you have much longer. If you're here to stop us, then you best hurry..."
#     g "What devil are you trying to summon?"
#     cu "Wh-what...?"
#     g "Don't be coy. You worship an archfiend. There's no way you're unfamiliar with her kin."
#     cu "I...I don't know! Our leader kept it under-"
#     play sound HeavySlash
#     cu "Nnnngggghhhh!!!" with vpunch
#     g "I hope you aren't foolish enough to lie to me!"
#
#     "When Griswyr presses his boot into the hatchet, I spring forward."
#     extend " I run on air, or at least that's what it feels like."
#
#     c "Stop it Griswyr!"
#
#     "I shield the man, placing my body between him and his tormentor."
#     "My breaths accelerate, and a cold sweat breaks out on my brow.I can’t allow this torture to continue!"
#     extend " Superior or otherwise, he has gone too far! There's no way the reverend would stand for this cruelty!"
#
#     c "That's enough! He's already down!"
#     g "So what?"
#     c "So what?! You can't treat people like this!"
#     extend " You're supposed to be protecting people, not torturing them! I can understand the grim reality of our job, but this is too much!"
#     g "...You choose now to make a stand?"
#
#     "I nod fiercely."
#
#     c "You may not follow Yeshua, but I know an Archlord wouldn’t stand for what you are doing!"
#     g "You forget your place, and I care not for what Ahriman or any Archlord has to say."
#     extend " I wear his symbol out of formality, nothing more."
#     c "But I care, and I will not let this treatment continue!"
#
#     "He sighs."
#
#     g "...We don't have time for this."
#
#     "He darts past me. Before I can react..."
#     play sound HeavySlash
#     with bloodflash
#     extend "He yanks the ax from the cultist's head."
#
#     g "Get out of my sight. Consider it an act of your false goddess that I don't flay you like a fish!"
#
#     "The man, the gash in his head streaming blood, scrambles to his feet and barrels to the exit."
#     "I sigh in relief."
#     extend " If I accomplish anything tonight, I have at least given that man another chance at life."
#     "Griswyr turns to me, his gaze just as disinterested as usual."
#     extend " I don’t flinch. After my actions,  I might not end up becoming an Emmisary, but at least I’ll still have my humanity!"
#     nvl clear
#
#     g "You understand he's going to bleed out, correct?"
#     c "...He might find a healer."
#     g "Who would tend to a Thorn?"
#     c "If healers are true to their oath, someone will."
#
#     "He scoffs and turns forward."
#
#     g "Let's move. I've had enough preaching for a lifetime."
#     c "Fair enough."
#
#     "Though Griswyr manifesting Malice concerns me. No wonder he’s so cold."
#     extend " Malice doesn’t morph people into monsters, it erodes their character. No one wakes up and decides to be a villain. It's a slope..."
#     "How long has he been channeling it? Why does he rely on it?"
#     extend " He looks more than capable of fighting on his own. What would drive him to such ends?"
#     "That is a question for after the mission."
#     nvl clear
#
#     scene Cult Altar
#     "The sanctum isn’t too far away, and the sounds of prayer grow louder as we advance."
#     "When we approach, my eyes scan the room."
#     "On top of what you'd expect from a summoning circle, there is a corpse entangled in rose bushes."
#     extend " It’s an elderly woman, and her pink eyes paint her as a hag. Is this her lair?"
#     "An altar takes up the back portion of the room."
#     extend " Three bronze statuettes rest atop the podium. Each is of a woman, aging from one statuette to the next."
#     "The sickly-sweet smell of roses overtakes the room, and the crimson aura of Malice is so thick that it could be cut with a knife."
#     "Five acolytes stand at each position of the pentagram, too engrossed in their trance to notice us."
#     extend " There's no way they didn't hear the racket of our fight. They must have decided to continue the ritual and are now close to finishing."
#     nvl clear
#
#     g "Looks like we made it in time."
#     c "I suppose we...just attack?"
#     g "If they're going to make it that easy."
#     extend " Stay back, wouldn't want you to stain your conscience."
#     c "No please, after you." (sarcasm)
#
#     "I cover my eyes, and he goes to work."
#     extend " Much like with the group of Thorns we just faced, the bodies here also fall like rain..." #Should I take this opportunity to introduce Griswyr's hemomancy?
#     "At least the aura is beginning to wane. I've had enough bloodshed for one night, maybe for a week..."
#     extend " Jory wasn't wrong about the brutality of the Emmisaries. I doubt that gentle giant would stand any of this..."
#     "When I open my eyes, Griswyr cuts down the final Thorn."
#     extend " Yet the man doesn’t whimper. He grins menacingly as Griswyr towers over him."
#     nvl clear
#
#     cu "Ngh...hehehe! You have my thanks! Blood was the last thing we needed, and you spilled more than enough!"
#
#     "Griswyr twitches."
#     extend " Is it my imagination, or do I spot veins bulging from his head."
#
#     g "Grrr...!"
#     cu "Go on, cut me down!"
#     extend " Mother will avenge us! You're as good as dead!"
#     g "Graaaahhhh!!!" with vpunch
#
#     play sound HeavySlash
#     with bloodflash
#     "The cultist’s severed head soars through the air."
#     extend " That swing wasn't nearly as graceful as Griswyr’s others. It was crude, brutish, and wild."
#     "When he turns, his face is twisted into a scowl."
#     nvl clear
#
#     g "Goddamn it! We played right into their hands!"
#     c "They needed blood? Was this a suicide pact?"
#     extend " That hag has been dead for awhile, and I see no one tied to the altar."
#     g "It doesn't matter! Our objective has changed!"
#
#     "The blood begins bubbling, and we retreat behind a pillar."
#     extend " The circle glows orange, and a red mist rises from the blood."
#     "Griswyr and I ready ourselves as a curvaceous silhouette comes into view."
#     extend " There are no signs of danger, yet..."
#
#     c "Ngh..."
#
#     "My heart pounds. It’s as if I can {i}feel{/i} her presence..."
#     extend " It’s soothing, almost bewitching, and at same time suffocating..."
#     "I sense both an alluring and a frightening presence from behind that mist..."
#     extend " I look to my comrade. His eyes stare ahead, fixated."
#
#     g "That devil.... Why do I recognize her?"
#     c "You can see through the mist?"
#     g "My eyes are more precise than most. This is a succubus."
#     extend " Pfft, these people gave their lives to summon that? What a waste."
#     c "Why would they risk life and limb for her?"
#     g "Hmmm, I have no clue..."
#     extend " Time to adapt."
#
#     "I yelp as he shoves me forward."
#     extend " I turn to lambast him, only to see no one."
#     "I fidget as the veil disperses. What does he want me to do?!"
#     extend " Wait, succubi aren't very strong. They're spies more than anything else, so he must be testing me."
#     "Ok, Caius..."
#     extend " Breathe in...breath out..."
#     extend " You have the advantage. She's vulnerable to Grace like any other devil, and you know her tricks."
#     "I tremble with each step I take."
#     extend " I must resemble a scared child who is in over his head. She won't expect much, and it will be her demise."
#     nvl clear
#
#     #show Persephone
#     "I gulp when her true form appears."
#     extend " I sense no threat from her. Her eyes aren’t narrowed, there isn’t disgust or bloodlust in her gaze, and I can’t find any malice on her."
#     "Careful, Caius, eyes above the chest. Stare too long, and you'll become enthralled..."
#     "My mouth opens, but no words leave. I feel breathless."
#     extend " If I enter any stance, my guise will be blown. If she lunges first though, I'll be defenseless..."
#     "Ugh, to hell with duplicity! I'll engage her before she can-"
#     nvl clear
#
#     v "Did you kill these people?"
#     c "Uhh..!"
#
#     "Oh no! We're surrounded by corpses! There's no way she won't suspect anything now..."
#     "Damn it! How could I be so careless?! All I've done is give her an opening!"
#     extend " Wait...no reaction. She isn’t drawing a weapon or anything..."
#     "Hell, she’s smiling! It’s one of amusement, not indignation."
#     nvl clear
#
#     v "Hehehe! Relax, they're in a better place now."
#     extend " Besides, there's no blood on {i}your{/i}hands. Looks like I'm outnumbered"
#     c "Ugh, right..."
#     v "So, what am I dealing with here?"
#     extend " Celestial?"
#     extend " Exorcist?"
#     extend " Adventurer who’s in over his head?"
#     c "Emmisary..."
#     v "Really? You, one of those cutthroats?"
#     extend " Ohhh, it's your first day isn't it?"
#
#
#
#
#     "She carries on like a waitress in a tavern."
#     extend " Had she hidden her horns and wings, I might've forgotten she was a fiend..."
#
#     c "It's been quite an experience...one I would like to put to bed."
#     v "So, are you going to kill me?"
#     c "Or send you back to Hell. I have no preference."
#     v "Aww, how thoughtful!"
#     extend " Buuut...."
#
#     with charmflash
#     c "Gnnnghhh...!" with vpunch
#
#     "Her eyes flash pink, and my head throbs."
#     extend " It feels like a hand is squeezing my head, forcing my mind to bend to her will..."
#     extend " Except it won’t work!"
#     "She caught me off guard, but my vow and training have honed my mind."
#     extend " I am aware of every thought and influence in my own head and perfectly in control of all of them."
#     "I'll let her think she has the upper hand...for now."
#     "My stance relaxes. As long as her spell persists, I’ll have to act like her most devoted companion."
#     extend " Besides, she can’t force me to channel mana nor harm myself, so a little roleplay won’t hurt."
#     nvl clear
#
#     v "See? Isn't that better? You can call me Persephone, what's your name?"
#     c "...Caius."
#     p "Hmmm, that doesn't sound familiar... Where are you from?"
#     c "...Thrycia?"
#     p "That mound of dirt? Wow! That place is older than me!"
#     extend " Though I haven’t been around that long...
#     c "...How old are you?"
#     p "Rude! We just met! Don't you know not to ask a lady her age?"
#     c "...My apologies. ...It appears your magic is working too well."
#     p "Pfft! I softened you up, I didn't remove your manners..."
#     p "I've been around for...five years? I'm unsure... Time flows differently in Hell..."
#     extend " Don't worry, I'm very mature for my age, hehehehe!"
#
#     "Five years? Her soul must've fallen not too long ago..."
#     "How odd... Five years ago is when I was adopted by Jory... I hope there aren’t any connection"
#
#     p "I don't have any intention of hurting you or whoever is lurking or any of your precious subjects. I just have an, \"errand\", to run."
#     extend " You won't even know I was here!"
#     c "...What kind of errand?"
#     p "Nothing special, I just need to touch base with a certain someone."
#     extend " Would you happen to know a man named Jory? He's a giant! You couldn't have missed him! I think he's still living in Jubilee..."
#     c "Wh-What do you want-"
#
#     "Calm down, Caius...you're supposed to be pulling her leg."
#
#     c "I-uh, I mean...I think he left several years ago."
#     extend " Poor man was wrought with grief. They say he fell in love with a Meropian."
#     c " i never believed the rumors, but he wasn't the same after one was executed. I prayed for his soul, but that was the only interaction I ever had with him."
#
#     "Her smile curls into a frown, and her eyes widen."
#     extend " Every mention of Jory pains her. But why? He never worshiped Hecate, did he?"
#
#     p "Oh, that's...too bad."
#     extend " And where did you say he was headed?"
#     c "...A small village to the west of Jubilee. ...I guess he wanted to get away from everything."
#     p "Huh, I see..."
#     c "Right..."
#     p "Right..."
#     c "Mhm..."
#     p "Mm...hm."
#     c "..."
#     p "..."
#     extend "You lying piece of shit!"
#
#     "I lunge!"
#
#     #play sound whoosh
#     c "Wh-Whoooa..!"
#
#     play sound HeavyCrash
#     with hpunch
#     "I collide with the wall, knocking the wind out of me..."
#     "What was that....?"
#     extend " It felt like leaping into a tornado. I was shunted backwards as if I were a toy...!"
#     "I didn't see her conjure any mana...though she hadn’t wielded any while charming me either."
#     extend " Is this power she just used against me also innate? I don't recall succubi being able to manipulate the wind."
#     nvl clear
#
#     p "You thought you could pull a fast one on me?! I'm a devil, goddamn it!"
#     p "All things considered, I thought your little act was adorable."
#     extend " Until you lied about HIM!"
#
#     "When she snarls, Malice oozes from her eyes."
#     extend " She must notice because she shakes her head and resumes her smirk."
#
#     p "So...let's try this again."
#     extend " Where's Jor-"
#
#     #play sound Slash
#     "Gryswyr jumps down from the ceiling, grazing her cheek with his blade."
#     "He lands then swings to land a deeper blow against her."
#     extend "But she floats out of the way."
#
#     p "Hehehe, finally showed yourself, huh? I take it you're his superior?"
#     g "Now I've figured you out."
#     p "Eh?"
#     g "Your cult was very adamant about bringing you here, so adamant that they were ready to die.."
#     extend " And for a lowly sex devil? That made no sense."
#     p "Oh, so we're going there, are we...?"
#     extend " Sorry, Snowflake, but you aren't my type."
#     p "Here's some advice. You should reaaally learn what the sun is. You're looking a little pale."
#     g "Then you brought up Jory, a man shrouded in rumors."
#     extend " They say many things about him. How he knew The Reckoning would happen. How he fell in love with a gar who happened to be a heretic."
#     p "Gar...?"
#     c "...Do you mean a Meropian?"
#     g "Whatever they go by..."
#     g "They say her death throes shook The Third so much that he hired double the protection, and they also say a succubus was the one who dragged him into Hell."
#     extend " Which means..."
#     g "You're the banshee who caused the Reckoning!" with vpunch
#
#     "I shudder. Could she have been that SAME monster?!"
#     extend " No wait... If Gryswyr's right, that means..."
#
#     c "You're..."
#     extend " Aurielle, aren't you...?"
#
#     "She sighs grumpily and claps her hands slowly."
#
#     p "Look at that... you blew my case wide open... So much for the surprise..."
#     extend " You must be fun at parties, Snowflake. A reeeeal crowd pleaser..."
#     g "It was hardly a secret. Even the boy would've figured it out eventually."
#
#     "He draws his hatchet and throws an arm in front of me."
#
#     g "Stay back. You are no match for her."
#     c " But-"
#     g "I've pushed you into danger twice tonight, but only because I knew you could overcome it."
#     extend " This fiend is much stronger than a succubus. You'll only get in the way."
#     c "Griswyr, she'll just revive in Hell if you-"
#     g "You talk too much! Do you forget that the enemy is right there?!"
#
#     "What does he mean?"
#     extend " Oh wait, she might not know I can wield Grace. By Yeshua, this is not my night..."
#
#     c "Alright then, I'll watch for any more Thorns."
#     g "That's the smartest thing you've done all night."
#     extend " And as for you..."
#     g "I will have those wings, banshee! Scream if you must!"
#
#     "He leaps towards her, and she shakes her head."
#
#     p "Good grief, did you not learn from your friend?"
#
#     "She waves her hand, and a gust of wind shields her."
#     extend " Griswyr lands and skirts behind her."
#     extend " She gasps as his sword hisses through the air."
#
#     g "Die!"
#
#     "He cleaves, only to cut air."
#     "That wasn't a hover... She {i}propelled{/i} herself out of his reach."
#     "I understand now. She relies on aeromancy. I supposed it was unwise of me to try and generalize about how devils fight..."
#     nvl clear
#
#     p "Fine, fine... You wanna play rough?"
#
#
#
#     play sound DaggerDraw
#     "Five, razor-sharp claws spring from her fingertips."
#     "She hunches forward, mimicking Girswyr's stance."
#     extend " He does not appreciate that."
#
#     g "...Are you mocking me?"
#     p "...What?"
#     g "You copied my stance!"
#     p "..."
#     extend " Snowflake, I just met you. Never heard of you before either."
#     extend " Guess you're not that important~."
#     g "Hmph!"
#
#     "They both spring forward, claws dragging across steel when they clash."
#     "While their stances are similar, their techniques aren’t."
#     extend " As Griswyr spins in a flurry of swings, Persephone keeps evading his efforts before retaliating."
#     "Griswyr attacks viciously, but Persephone appears more relaxed."
#     extend " She might just be trying to lure him into lowering his guard, or trying to antagonize him..."
#     "Strike after strike comes from Griswyr, but not one lands on Persephone.."
#     extend " Griswyr snarls and repeats the same maneuvers.... He is the same whirling machine of death he was earlier, yet even his skill and fury are no match for Persephone’s otherworldly evasions. They dance around the room as I do my best to follow their movements and not get swept up in the battle."
#     "My heart pounds when she suddenly slips away more swiftly than ever."
#     extend " Griswyr can’t stop his momentum as he swings at her, stumbling forward into nothingness. He's left wide open!"
#
#     c "Griswyr, look out!"
#     p "Good night~!"
#     g "..."
#     g "{i}Blood Lance{/i}."
#
#     "A spear of blood appears and extends from his blade, thrusting forward at Persephone."
#
#     p "W-wait..."
#     play sound BloodSplatter"
#     extend " GAAAAHHHH!!!" with vpunch
#
#     "It pierces her chest like a dagger."
#     extend " Had she not backpedaled at the last minute, I imagine it would've impaled her."
#     "Meanwhile, Griswyr's arm reddens violently."
#     extend " I cringe. He is showing no reaction to the change, but it looks painful..."
#     "He throws his hatchet at her."
#     extend " She sidesteps, and Griswyr...vanishes into a red mist?!"
#     "He reappears behind her, alarming Persephone as he takes his hatchet in hand once again."
#     extend " Again comes his flurry of deadly strikes, but Persephone isn’t amused."
#     "Her wound isn’t deep, but Griswyr has her on the run."
#     extend " She can’t just float around anymore, or else he might catch her off guard again!"
#     "He feints and as Persephone braces herself..."
#     nvl clear
#
#     #show Griswyr behind Persephone
#     p "Ah shit...! with vpunch
#     g "You should've stayed in Hell, banshee!"
#
#     #play sound Heavyslash
#     extend " Griswyr darts behind her and impales her waist!"
#     "But Persephone smiles."
#
#     p "And you should've brought silver!"
#
#     "A gale blast sends Griswyr crashing into the wall."
#     "I watch in horror! She hit him point blank!"
#     extend " She wanted him to get close... Why else would she have avoided attacking him in favor of just dodging his blows? And now she knows what he’s capable of..."
#     "Griswyr snarls and recovers."
#     extend " He may seem unharmed, but his breaths are heavy as he clutches his stomach."
#     nvl clear
#
#     c "That's enough, Griswyr! Let me handle this!"
#     g "Nnngh..."
#     extend " Just who do you think you are?! I'm your superior!"
#     c "And as my superior, you must test me. Consider this another trial."
#     g "Grrr..."
#     p "My god, you're pious, I’ll give you that..."
#
#     "Griswyr's temperament is much more aggressive than before."
#     extend " He isn’t cool and collected anymore, and he eyes me as if I were his foe."
#     "Now that I think about it though, he did lose his temper earlier, when he beheaded that cultist..."
#
#     g "...Very well. She is yours, as long as you can handle her."
#     p "Hehehe, you ought to watch your mouth, Snowflake. Someone might get the wrong idea~."
#     c "Thank you, Griswyr. I won't let you down!"
#
#
#
#     "I ready my stance then slowly walk towards her."
#     "I circle her, our eyes not breaking contact."
#     extend " She could pounce at any moment, yet all I continue to get from her is that scheming grin."
#     "Even now, she’s still choosing to toy with us. Something tells me that her blasting power are going to be the least of our worries."
#     nvl clear
#
#     p "So..."
#     extend "what did they tell you about me?"
#     c "Nothing much. Just that you dragged The Third into Hell..."
#     p "Are you sure that was me? It could've been one of my sisters. We all look alike, after all~."
#     p "Come on! This is all a misunderstanding! I didn't do anything...I just want to check up on an old friend..."
#
#     "My blood freezes with anger."
#
#     c "...You mean my mentor?"
#     p "Well..."
#     extend " If his name's Jory, then-"
#     #graceflash
#     extend "Grrrr!!!" with vpunch
#
#     "Too slow!"
#     extend " She recoils heavily from that blow, even more than when she got stabbed.!"
#     "The mana flows in me alongside my fury."
#     extend " Her death caused Jory a lot of heartache, and I won't allow this ghost to haunt him further!"
#
#     c "Keep my friend's name..."
#     extend " Out of your mouth!!!" with vpunch
#     "She twitches and staggers with each consecutive blow to her chest."
#     extend " My strikes fly as quickly as Griswyr's barrage of swipes maybe even faster!"
#     "I manage to back her into a corner. I have to finish this fight quickly before she can hurt Griswyr or Jory or anyone else."
#     "Eventually, she musters her Malice and retaliates!"
#     extend " I block the blow with my own, the clashing manas dispersing whilst our palms are clenched."
#     "Our brows furrow, eyes locked onto one another."
#     extend " Her whimsical smile twists into a scowl. Looks like she’s not having fun anymore."
#     nvl clear
#
#     p "Grrr...so that's why he picked you."
#     extend " His soul is too black to ever wield Grace. Snowflake needed a proxy, how clever..."
#     c "Why are you surprised?"
#     extend " I can't be the only Emmisary who channels Grace."
#     p "Hahaha! If you only knew!"
#
#     "She breaks out of a crouch and lungesagain."
#     extend " I breathe deeply..."
#     "And catch her clawed wrists mid-flight."
#     #heavycrash
#     "She grimaces as I spin and hurl her onto the altar."
#     extend " She is splayed among the fractured statuettes. She pushes herself up, furious, as I wave my hand to release my mana."
#     nvl clear
#
#     c "Blasphemer! Mother will be displeased!"
#     p "Wise ass, huh...?!"
#
#     "She summons the wind and blasted the table, sending debris my way."
#     extend " I jump out of the way and thankfully block and evade it all. I land, trying to regain my bearings, but my pause gives her the opening she needs."
#
#     c "Gahhh!" with vpunch
#
#     "She fires a second gale that hits me hard... It feels like getting kicked by a mule!"
#     "She springs at me, but I block her attack and throw her a second time."
#     extend " She lands hard again but recovers quickly and braces herself against the  wall."
#     "Again she lunges.."
#     extend " And feints, her flapping wings frightening me and nearly causing me to stumble. This battle is wearing us both out. I have to do something soon, but I can’t figure out how to strike the finishing blow."
#     "What is she going do now?! I don't have the time to-"
#
#     g "What are you doing?!"
#     extend " Attack!!!" with vpunch
#
#     "I obey."
#
#     #graceflash
#     p "Nuagh...!"
#
#     "I understand now. I can do more than harm her with my attacks – I can also block her attacks with my own!"
#     "I double down on my efforts, both striking blows and preventing her attacks as they come. A barrage of my strikes batters her chest."
#     "A shrill scream leaves her lips. My frenzy of attacks is starting to rack up damage!"
#     extend " I’m using a lot of mana and energy, but I can’t let up!"
#     "I can’t risk giving her another opening! Our lives are on the line, and the lives of others as well."
#     #galeblast
#     #graceflash
#     "She tries to retreat by blasting the ground to scare me off, but I continue to pursue her."
#     extend " As strong as she might be, Grace can always disrupt a devil's mana."
#     "Since she is born of Malice, my mana is a poison to her."
#     extend " Each of my blows may as well be made of silver!"
#     "I keep going."
#     extend " I’ve trained my arms and legs to ceaselessly land consecutive blows. Stamina isn’t an issue!"
#     "She finally manages to break away, but she writhes in  damage and pain."
#     extend " I can see my mana tearing through her body. Each blow makes her twitch and shiver. I almost pity her."
#     nvl clear
#
#     "I step towards her, ready to end this."
#     extend " Yeshua knows how mangled her soul must've been for her to be contorted into such a hideous form..."
#     "Jory has told me many stories about Aurielle, and seeing her as Persephone saddens me..."
#     #graceflash
#     "I close my eyes and summon Grace. I will put her to rest with this next strike."
#
#     c "Farewell, Aurielle..."
#     p "...Is that pity in your eyes?"
#     extend " Aww, how noble! Though not showing kindness to your friend? That's pretty cold..."
#     c "...?"
#     p "Oh no, I'm not talking about Snowflake. Though you’re probably the only friend he has ehehehehe!"
#     extend " I can read it in your eyes. You're not motivated by zeal; you're motivated by regret."
#     c "...As are you."
#     p "Indeed, and I intend to remedy that situation. I have a plan, a resolution. If only you could say the same..."
#     p "I can read you mortals like a book. Even without my special ability."
#     c "What?"
#     p "Hm, you didn't know?"
#     extend " Well I can understand Jory not knowing, but Snowflake? Tsk tsk, how irresponsible!"
#     c "What the hell are you talking about?"
#     g "Do not humor her, Caius!"
#     p "Ohhh nothing much, just that we devils can see into your past!"
#     c "What?!
#     p "Ahahahaha! Why else would people sell their souls? It's because we see everything! Your regrets, what you care about, and what haunts you. It's all an open book!"
#     p "Aww, what's with the long face? You were looking so high-and-mighty just a moment ago... I'm guessing I lost your sympathy?"
#     "If Griswyr knowing about my past unnerved me, Persephone knowing about it took the cake!"
#     extend " "How could I not realize?! I'm no scholar, but I’ve looked far and wide for knowledge about devils, and yet I’ve never heard of this power!"
#     extend " More importantly, she knows about HIM!!!!"
#
#     p "Ah yes, you threw your friend to the wolves."
#     extend " How else would've you have made it this far? You were a nobody until you exploited their kindness!"
#     p "That's pretty wicked! And now you starve yourself for even MORE sympathy!"
#     extend " Hahaha, you holier-than-thou types always have the darkest secrets! Watching your souls fall is soooo delicious!"
#     g "Strike her down, goddamn it!"
#     c "Grrr! Be quiet!" with vpunch
#     #whoosh
#     p "Whoa, whoa....what's swatting at me going to do? I’m not the one who abandoned him..."
#     c "You...You leave him alone, monster!"
#     #whoosh
#     p "Oh, your friend? Hmm, I'm sure he's much different now. People change when their hearts are torn out."
#     #whoosh
#     c "Tell me, Persephone!"
#     #whoosh
#     c "Hecate calls herself the mother of outcasts, a protector of the damned!"
#     extend " But you're just like any other devil! You'd corner and bewitch the same people you claimed to care about! You only defile people!"
#     c "The Dretchlings suffer enough without your venom!"
#     g "Stop talking, Caius-"
#     p "Ohohoho, what you call defile, we call saving!"
#     #whoosh
#     c "Lies!"
#
#     "Our manas clash as we summon our powers again!"
#     "My eyes shoot daggers at that grinning monster!"
#     extend " My Grace spikes. It must sting her severely, yet she only grins more."
#
#     c "You and that godforsaken archfiend aren't any different! Why else would she reside in Hell?!"
#     p "Right, because your god's any different?"
#     extend " Who were the Celestials founded under? Oh, he must've been cruel to allow his followers to imprison Dretchlings like cattle."
#     p "Yet we're the bad guys for spreading the truth? How is that fair?"
#     extend " Face it, your god doesn't care, and mine does. And now that I think about it, looks I have TWO errands to run!"
#     c "Damn you-"
#     #play sound grapple
#     extend " Agh!"
#
#     "A hand grabs my throat, and she hoists me above her."
#     "My mana vanishes alongside my breathing! I can’t channel it if I can’t breathe. How could I leave my throat defenseless...?!"
#
#     p "Though while we're talking about fibbing, I wasn't entirely honest with you."
#     extend " Ehehehehe, we devils can't read peoples' pasts. So I appreciate the information~."
#     c "Gngh!!!" with vpunch
#
#     "My heart stops, and she giggles darkly."
#
#     p "You mortals will believe anything. Just like false seers, we only need to suggest words and situations that could apply to anyone, and suddenly you’re all suckers spilling your guts for us."
#     p " And now you've failed him twice..."
#     extend " Nah! You did him a favor!"
#
#     "Wind blasts me from her grip, and she channels Malice and winds in her other hand."
#     extend " But I don’t care..."
#
#     p "I'll take good care of him, you can die now."
#     #maliceflash
#     p "Buh-bye!"
#     #weaponslash
#     p " Shit!"
#
#     "I bang into the wall as Griswyr nearly decapitates her."
#     "I don’t have the strength nor the courage to stand..."
#     extend " She played me like a harp... So easily too!
#     "Griswyr turns to me, his eyes as stoic as ever."
#
#     g "Hmph, how disappointing."
#     p "Aww, did I break your friend-"
#     #whoosh
#     extend " Jeez Snowflake! Lighten up, will ya?!"
#     p "I mean, isn't being jinxed bad enough?"
#     g "...?!"
#     extend " It'll be worth it when I feast on your blood!"
#     "Wh-what?! What does he mean-"
#     extend " Oh right, he licked his sword after it got coated in gore. He's not trying to scare her, he MEANS what he's saying..."
#     "Persephone looks as dumbfounded as I do."
#     p "Oh. Oh wow..."
#     extend " You've completely lost it... I knew you were into some weird stuff, but-"
#     #whoosh
#     extend " Whoops! You're going to have to do better if you want my neck, you leech~."
#
#     "I watch them clash, my mind blank."
#     "How can I help Griswyr when I can’t even help myself? I'll just be in the way..."
#     "All the blows I landed were because she let me... Now she’s  dodging and weaving past Griswyr's swipes just like before..."
#     "She rears back."
#     extend " And Griswyr ducks behind her, readying his ax."
#
#     g "And now you-."
#     extend "Ngh! What the-?!" with vpunch
#
#     "Wounds tear open in his arms. They seem to surprise him more than hurt him."
#     extend " I can’t blame him for his shock. I didn’t even see her claws land. So how did those razors inflict such damage?!"
#     g "Tch...just a flesh wound!"
#
#     "He siphons some of the blood and flings his hatchet."
#     extend " Persephone turns around, but he teleports in front of her, sword at the ready."
#     "She catches his sword in two fingers, the blade causing blood to trickle down her hand."
#     extend " Griswyr winces."
#
#     p "Ooh, looks like you grazed me..."
#     extend " Go on, have a taste."
#
#     "She releases his blade and holds out her fingers."
#     extend " Griswyr cringes but follows through with his swing
#
#     #whoosh
#     p "Hey now, don't be greedy..."
#     g "You think taunting me is going to work?"
#     extend " I've had this curse my whole life. I am not enslaved to it!"
#     p "Then why did you flinch? You might've had my head if you were faster~."
#
#     #whoosh
#     "Persephone darts backwards, and he fires another Blood Lance."
#     extend " She swats it away with her wings."
#     "Griswyr's body hunches over, his breaths weighty."
#     extend " Every time he uses one of those attacks, he injurs himself..."
#
#     #lunge
#     p "Wake up, Snowflake!"
#
#     "He evades her pounce and hisses as more wounds rip open on his body."
#     extend " It’s gone in a second, but I finally spot the source of her attack. She wraps wind around her hands. So even if he dodges her blows, the gusts will still cut him."
#     "She launches herself again!"
#
#     c "Don't dodge, Griswyr, or you'll be cut by her wind!"
#     g "Grr! No shit!!!"
#
#     "He spins."
#     extend "His hatchet parries her claws, and his blade sinks into her side."
#     "He digs the steel more deeply into her as his leg ensnares hers."
#     extend " She slams into the floor, and he plants his knees atop her back."
#     "He leers down at her, her body resting on the bloody floor beneath them."
#     extend " I blink. I’m not crazy. Fangs have emerged where his canines once were."
#     "I shiver. The look of ferocity in his eyes...he doesn’t see her as his target."
#     extend " He sees her as his food!"
#     nvl clear
#
#
#
#     g "I told you I'd have your wings, but I'll start with your neck."
#     extend " Even if you revive in Hell, you'll have to find your way back to our plane, and you’ll become my prey again!"
#     p "Ngh...not bad! You're {i}actually{/i} starting to scare me, Snowflake!"
#     g "Even now, you joke?!"
#     #bloodflash
#     p "Gngh...!"
#
#     "His sword sinks into her back like a knife through butter!"
#
#     g "What will it take for you to stay down?! You're like a cockroach! You sever its head, yet it still crawls!"
#     p "Ohh, don't let me stop you. If you want my neck, go for it."
#     extend " I am your snack after all. I'm powerless to stop you. What good would any resistance do?"
#     #bloodflash
#     g "Shut up!!!" with vpunch
#
#     "By Yeshua...fiends are something else."
#     extend " Despite all the injuries she's sustained, Persephone still keeps going."
#     "Griswyr pauses, finding both of his hands drenched in blood..."
#     extend " He just sits there...something has gripped his heart."
#     #bloodflash
#     "He drives the shortsword into her again...and he pauses a second time."
#     extend " Try as he might, he can’t seem to break her smile."
#     nvl clear
#
#     p "They say a predator takes the easiest approach to hunting. Even if a wolf could kill any human, it will only target the weakest link."
#     p "Matter of fact, wolves only hunt when they {i}know{/i} they can win. But I prefer cats."
#     extend " They are an exception. They hunt for sport as well as food. A cat will even  choose to torment its prey before killing it."
#     p "They're very sadistic – at a glance, at least."
#     extend " Truth is, that cat isn't torturing for fun. It's tiring the prey out to ensure that it can't retaliate. Could be nasty if the rat sank its teeth into the cat’s nose, after all."
#     p "Is that why you're frozen? Is it because I'm laughing off your little cuts?
#     extend " Or is it because your instincts won't allow you to move?" with vpunch
#     g "...Enough of this!"
#     extend " I am not enslaved by my hunger..."
#     extend " It is enslaved by me!!!" with vpunch
#
#     "His jaw expands as he dives!"
#
#     p "Should've listened to your friend."
#
#     "Her arms lash out and hold his head still."
#     extend " Her head springs forward, and my heart stops."
#     extend " She plants her lips onto his!"
#
#     c "Griswyr!"
#
#     "A second wind lifts me back onto my feet, and I dash toward them!"
#     extend " Her kiss is lethal! She’s sapping his mana with every twist of her lips."
#     "His body wrinkles, and her wounds begin to close."
#     "She pulls away, and I lunge."
#
#     p "...Oh, you're still with us..."
#
#     "Griswyr collapses to the floor as we engage."
#     "Sounds of hissing rattle the room. The mana screams just as violently as our blows."
#     extend " Yet, she suffers more than I do. Looking more closely, I see her body tremble."
#     "My blows from earlier weren't in vain, my mana still wracks her body!
#     extend " Which means I can still strike a killing blow.
#
#     p "Ugh, you're so annoying! Go away!"
#
#     "I weave past her gale and jab her chest."
#     "I gnash my teeth whilst my palms assail her like a barrage of arrows."
#     extend " She swipes, but I duck and slam my heel into her sternum."
#     "Her hisses devolve to growls the more I strike her."
#     extend " Her eye twitches. She’s reaching her limit."
#     "She keeps trying to float backwards, but I keep stepping forward."
#     extend " My arms are growing heavy...I’m starting to run low on mana. I can’t continue like this..."
#     "I need to land one good strike."
#
#     Caius "Fall, monster!"
#
#     "I kick and hit nothing but air..."
#     "She flies backwards, digging her claws into the wall. She glowers, ready to attack again."
#     extend " Malice and wind engulf her! I can’t stop this...and even if I dodge..."
#
#     g "You goddamned fool! What are you doing?!"
#     extend " This battle is yours! DO - NOT - FALTER!!!" with vpunch
#
#     "..."
#     extend " I know, Griswyr."
#
#     "She zips towards me..."
#     extend " Best I can do is avoid...."
#
#     c "Gnnnnngggggghhhh!!!" with vpunch
#
#     "The intense gusts bludgeon my body! I felt like I’ve slammed straight into a wall of pure force!"
#     "Blood sputters from my mouth as several of my ribs collapse...."
#     extend " The only reason the rest of me doesn’t follow suit is because Grace protects me from most of the pain..."
#     "It takes all of my concentration not to be swept away..."
#     extend " And now..."
#
#     #heavybam
#     c "HAAAA!!!!" with vpunch
#
#     "I deliver a mighty strike to her chest and..."
#     extend "nothing."
#
#
#
#     p "...Was that your last stand?"
#     extend " WEAK!!!" with vpunch
#
#     "Her Roundhouse kick sends me flying. Time stands still as I float away..."
#     extend "I turn to her, that insipid grin peering into my soul."
#     "I breathe heavily, coughing up blood as I clasp my hands."
#
#     scene black
#     "..."
#     extend "Shine!"
#     scene altar
#     p "Huh..."
#     scene white
#     #lightexplosion
#
#     "My Grace pours from her body and consumes her."
#     extend " The mana turns an icy white and explodes."
#     "I can’t see a thing, but this battle has ended."
#     extend " That blast tore her apart from the inside out."
#     "Against a mortal, it would just render them paralyzed, but against a devil? There's no way she survived."
#     "A hand shielded me from the blast. It must've been Griswyr's."
#
#     c "Ngh..."
#     g "Impressive.  What was that?"
#     c "Agh...well each of my blows injects my mana into my opponent, disrupting their own..."
#     extend " And once it consumes most of their body, I can cause it to tear itself out..."
#     extend " Agh...it hurts to talk..."
#     g "That's...violent. Color me impressed."
#     c "Well, it doesn't kill mortals..."
#     g "Of course it doesn't."
#     extend " Gngh!"
#     c "What's the matter...?"
#     g "I still smell her!"
#
#     "As the radiance dies down, the first thing I spot are two, red eyes glaring at me..."
#     extend " My teeth chatter. My body feels cold, exhausted, and afraid. That was my strongest technique, how did she survive it?!"
#     "Malice's crimson hue shrouds her. Her stance is unsteady, however she appears more than capable to continue..."
#     extend "I try to stand only to stumble. A stabbing pain pierces my waist..."
#     "I could conjure Grace to numb it, but I lack the resolve..."
#     nvl clear
#
#     p "You know, I tried to be nice... I tried to make your death quick and painless BUT now I don't really care!"
#     p "I'll give you credit, that might've killed me. Good thing Snowflake offered me some of his mana hehehe...!"
#
#     "She hisses as her talons spring from her fingers."
#     extend " Her Malice spikes. In hindsight, she didn't use up as much mana as I expected..."
#     "Griswyr seems more upset than afraid as he looks to the ground."
#     extend " He spits and readies his weapons."
#
#     g "Well shit, looks like this mission is a failure! Out of all the monsters, we had to get matched up against that goddamned banshee!"
#     c "Griswyr...?"
#     g "I'll hold her off while you crawl away. Don't worry about me, because I'm not coming back."
#
#     "He crosses his throat and speaks gravely "
#
#     g "This is my final lesson to you, Caius. Even in death, we Emmisaries leave no trace. We'll face annihilation if that's what it takes!"
#     extend " Do not let any information fall into the hands of the enemy! To the end!"
#
#     "He charges."
#     extend " He startles Persephone, but she meets his advance."
#     "He isn’t dodging..."
#
#     c "Griswyr, don't...!"
#
#     #bloodflash
#     "Her claws tear into his chest, ripping blood and flesh from his body."
#     extend " Yet he doesn’t so much as wince."
#     #bloodflash
#     "He drives his sword into her leg and wraps his arm around her waist."
#
#     p "What the hell are you-?!"
#
#     "He drops his hatchet before getting behind her and hooking his arms around hers, pulling up and restraining her."
#     extend " He clings to her like a monkey. Try as she might, Persephone can’t shake him."
#
#     p "Grr! Snowflake, I'm not in the mood! Let go!!!"
#     g "Ngggh...what are you doing, idiot?! Run!"
#     p "Who are you calling an idiot?! You're the one who-"
#     extend " Wait a minute..."
#
#     "I wish I had the strength to flee..."
#     extend " My heart weeps for him. My eyes might also weep if it didn't hurt so much to breathe..."
#     "Even if I start crawling away, there's no way she’s going to let me go."
#     extend " I don’t know what Griswyr is planning, but if it involves his blood magic, she'll just chase me and we'll all be collateral damage."
#     "Best I can do is stay here and see him off..."
#     "Persephone turns to him. I can’t see what happened, but I have a bad feeling in my stomach..."
#     nvl clear
#
#
#     p "...Hehehe, so that's what you're up to? How naughty~."
#     extend " Isn't suicide frowned upon by the Celestials?"
#     c "Suicide?!"
#     g "Too late..."
#
#     "Griswyr's own Malice erupts, causing a whirring sound to hum from within him."
#     extend " Blue glyphs appear on the studs in his armor, growing brighter by the second."
#     "I try to call to him, try to move towards him, but my body still refuses to budge..."
#     extend " This is horrible! Why is he dying for me?! I'm a novice, I'd be much easier to replace than him."
#     "After all, I can’t even save myself, let alone anyone else..."
#
#     g "See you in Hell, banshee!"
#     p "Ngh..."
#     extend " Yep, but not in the way you're thinking!"
#
#     "She slits her wrist and shoves it into his maw."
#     "Griswyr's eyes widen and runes on his chest begin flickering."
#     extend " His grip loosens as his eyes shut. I hear faint sounds of suckling."
#     "He may as well have fallen victim to his compulsion for her blood."
#     extend " At first he clings to her. Then slowly his grip relaxes, and she begins to cradle him."
#     nvl clear
#
#     p "I can't have you exploding on me. I'll be taking these."
#
#     "She tears off his vest and tosses it to the side."
#     "Griswyr stirs and groans. He tries to pull away."
#     #grapple
#     extend " But her palm around his maw clenches."
#
#     p "Now now, I’m still playing with you. Besides, you've had a long day~."
#     #heavybam
#     extend " So go to sleep!"
#
#     "She slams her knee into his chest, knocking the wind and consciousness out of him."
#     "I watch helplessly while she drags him towards the hanging corpse."
#     extend " She tears the grizened woman from the bushes and pins him there."
#     "What does she have in store for-"
#     nvl clear
#
#     p "Hey, shithead! We're not finished!"
#
#     "I have to use the wall just to stand..."
#     extend "My body twitches with every movement. My lungs are on fire, and these shattered ribs are all too eager to feed me pain..."
#     "I breathe heavily, knowing that I only have one way out of this."
#     #graceflash
#     "Grace releases from my body."
#     extend " With this much pouring out, I'll run out of mana in no time. hHowever I need Grace just so I can move..."
#     "On the flip side, expending this much mana will inject more into her body. I need to blow her up again..."
#     "Who will burn out first? Will I be able to hold up long enough to defeat her? Only one way to find out."
#     nvl clear
#
#     p "Still have some fight left in you?"
#     extend " Good! I wasn't satisfied!"
#     #maliceflash
#     p "Even if you don't feel it now, your body is in agony."
#     extend " And that pales in comparison to what I have in store for you!"
#     p "There's no way Jory raised someone so blind! If the Third lived, you'd kiss his boots like every other slave!"
#     extend " You self-righteous fools are what's wrong with this world!!!" with vpunch
#     c "Ngh...maybe. Maybe I am too pious... And I don't know what you went through..."
#     extend " But I'd sooner believe in myself than an Archfiend...!"
#     p "That's not the first time I've heard those words, and it won't be the last..."
#     extend " Doesn't mean this won't hurt any less!!!" with vpunch
#
#     "I breathe deeply and block her swipe."
#     extend "She retreats before lunging for my legs!"
#     "I drive my heel into her jaw."
#     extend " And she counters by scratching my chest. Praise Yeshua that I step back when I do..."
#     "We dance, blocking and countering each other's blows."
#     extend " The manas screech. Our motives are personified and continue to clash!"
#     "With each punch, visions of Jory enter my mind..."
#     extend " Is my life flashing before my eyes...?"
#     nvl clear
#
#     j "{i}Relax, Caius, you're always so uptight.{/i}"
#     extend " {i}Take a load off and breathe once in a while, yeah?{/i}"
#
#     #heavybam
#     p "Gaaaaahhhh!!!" with vpunch
#
#     "That attack sends her reeling. If I can just land a few more strikes like that one..."
#     "She blasts herself airborne, screeching before launching a volley of gusts towards me."
#     extend " I lack the agility to dodge... I walk forward, blocking, deflecting, and even enduring gust after gust..."
#     "Even with Grace protecting me, my body rattles with every blast..."
#     "I breathe deeply before jumping up to attack her"
#     extend " She dodges and grabs me, and I drive my mana into her as we plummet to the floor."
#     nvl clear
#
#     #heavybam
#     with vpunch
#     g "{i}How do you expect to be an Emmisary when you're so weak?!{/i}"
#
#     g {i}"I was ready to die for the mission, yet here you are, ready to surrender everything you stand for!{/i}"
#     g "{i}Fight goddamn it, even if it kills you!{/i}"
#
#     "My fractured arm latches onto her face, my fingernails and Grace digging into her flesh!"
#     extend " A shrill yelp meets my ears. More of her blood trickles down my hands as I hold on for dear life."
#     "She pries my palm from her head, and I kick her off of me."
#     extend " I rise, my teeth bared and my eyes seeing red."
#     "Her gaze wavers when I sprint towards her."
#     extend " Her wings flap, and I grab her foot before clobbering her face."
#     'She squirms and slashes."
#     extend " Her nails graze me. I spit up blood and keep attacking."
#     "She isn’t nearly as dangerous when you have her pinned!"
#     nvl clear
#
#     p "Grrrrr!!!" with vpunch
#     c "..."
#     p "Ngh...struggle all you want! In the end...you'll stll-"
#
#     "I shove her jaw shut and hurl her into the table."
#     extend " She leaps to her feet and I approach, walking slowly."
#     "She lunges but flinches."
#     extend " She staggers more and more with each step I take towards her."
#     vi "...You hate me, huh?"
#     extend " Man...I knew I messed up, but did you have to tell her about me...?"
#     "...You're right."
#
#     #heavybam
#     p "AHHHH!!!!!" with vpunch
#
#     vi "I was just trying to protect us..."
#     "I know..."
#
#     #heavybam
#     p "Gah...damn you! Ngh...!"
#
#     vi "Why did you abandon me, Caius?! I thought we were friends..."
#     "...We are."
#
#     "She catches my last strike, deflecting it."
#     "A hand presses against my chest, with Malice hissing against my Grace..."
#     "I jab her throat, causing her to spit and for breath to fly from her maw."
#     extend " Yet I still get blasted..."
#     "I fly backwards, doing my best to brace my fall as I land."
#     extend " With an eldritch calm, I peer back at her."
#     nvl clear
#
#     vi "You're coming back, right?"
#     "...I am."
#
#     "I lift my hands and clasp them together."
#     "With an unsteady breath, I speak"
#     nvl clear
#
#
#     c "Rest in peace..!"
#
#     "Suddenly, I fall to my knees."
#     extend "Intense pain floods through my veins, wracking my entire body!"
#     "The strain prevents my hands from reaching her...I've run out of mana."
#
#     c "No...not now!"
#     vi "...I knew I couldn't trust you."
#
#     "Tears well in my eyes. There isn’t anything I can do anymore..."
#     "It looks like I’ve reached my limit first..."
#     extend " My adversary laughs triumphantly."
#
#     c "Priam...I'm sorry. I tried my best..."
#     p "Your best FAILED you!"
#
#     "She pounces, and I close my eyes..."
#     extend " So be it. Someone, anyone, help him..."
#
#     #heavyslash
#     "..."
#
#     g "Caught you!"
#     p "Eh?! with vpunch
#
#
#     #scene Altar
#     "Griswyr jumps down from the ceiling, driving both his hatchet and his Malice into her arm."
#     "She clutches it, and her body convulses."
#
#     g "Even if he couldn't finish the job, there's still a lot of Grace inside you."
#     extend " Seeing as how both manas repel each other, I wonder what will happen when my Malice comes into play!"
#     p "...Oh shit!"
#
#     "Her jaw clamps shut as my mana begins to violently leave her."
#     "She looks dead at me and narrows her eyes."
#     #explosion
#     extend "Before exploding just like before."
#     "I can’t believe it...I survived! We won!"
#     extend " I don’t care about the buzzing pain coursing through me. Now everyone is safe from her..."
#     "Better yet, I never realized before that Malice could also set off such an explosion..."
#     nvl clear
#
#     c "Griswyr..."
#     extend " How did you know that would happen...?"
#     g "I didn't."
#     extend " It was a theory at best. Either way, her blood gave me the second wind I needed."
#     g " Even if that didn't kill her, she was more than injured enough to..."
#     extend " WHAT THE FUCK?!" with vpunch
#
#     "The lingering effects of the explosion dissipate and Griswyr stomps furiously."
#     extend " Persephone was defeated, so what is setting him off?"
#
#     g "HOW THE HELL DID SHE ESCAPE?!" with vpunch
#     c "Wh-wha...?"
#     "I look to the floor and gasp. There are no remains, no body, no sign of her. Persephone is gone!"
#
#     g "GODDAMN IT! SHE WAS A NUISANCE BEFORE, YESHUA FORBID HOW HARD SHE’S GOING TO BE TO TRACK NOW!!!" with vpunch
#     c "How...how do you know she escaped..."
#
#     "A voice booms into my ear."
#
#     p "...Looks like you win this time."
#     extend " Don't worry, I'll leave Jory be just as you wished. Anything to get away from you..."
#     p "If you see me again, do a girl a favor, and just keep walking!"
#
#     "...You're kidding me."
#
#     c "Griswyr..."
#     g "What is it?!"
#     c "Don't..."
#     extend "tell...:
#     extend "Jo-"
#
#     play sound Thud
#     scene black
#     pause(3.0)
#
#     v "By Yeshua, I knew I shouldn't have let him leave!"
#     v "Enough. He needs rest. Any more of your healing will accomplish nothing.."
#     v "Damn you, Emissary!"
#     v " I'll accept your insults. I should be dead myself. I would prefer it to the position we're in now..."
#     v "Oh! He's waking up! Thank goodness!"
#
#     "My body stirs wearily, wrapped in bandages in more places than I can fathom..."
#     "I find myself in Jory's arms... It still hurts to move, but it looks like I’ve pulled through."
#     "Griswyr stands in the corner, at a distant as always."
#     nvl clear
#
#     j "By Yeshua, are you alright?!"
#     c "Ngh....well, I’m still breathing so..."
#     g "Luckily most of his injuries weren't deep. Those broken ribs are going to need some time, not like you can move anyways."
#     g "You're nearly burnt all of your mana, Caius. A drop more, and you would be a corpse."
#     j "It shouldn't have ended this way!"
#     j "What came of this?! All you did was put my friend in bandages! You didn't even kill the devil!"
#     g "I know, and I'm very upset... She's going to be a problem."
#     extend " Caius was the only reason we lived. This won't make you feel better, but I believe he'll make a fine Emissary."
#     g "If he wants to, that is."
#
#     "Jory's fist slams onto a table and causes the ground to quake!"
#     "I know he didn't mean to, but damn that hurts my ribs..."
#     extend " Of course Griswyr hardly cares..."
#
#     j "Get out! Our business is done!'
#     g "As you wish. It's not our decision to make, it's his."
#     extend " I'll find you once you're ready to decide. I won't blame you if you want to reconsider joining after last night."
#     g " Until next time."
#
#     #hide Griswyr
#     j "Grr... Damn it! I gave the reverend my word I wouldn't let this happen..."
#     c "Hey...it's not your fault, sir."
#     extend " I couldn't stop thinking about you... I kept pushing myself for your sake..."
#     j "Oh right, you made that promise..."
#     extend " But I'm not the one who needs to be protected!"
#     c "On that, we'll have to agree to disagree..."
#     j "By Yeshua, you're as stubborn as always..."
#     c "Hey Jory, when I'm better..."
#     extend " Can we visit Thrycia?"
#     j "I...thought you wanted to become an Emissary first."
#     c "I did, but after last night, I'm ready to back now,"
#     extend "  I may not be able to change anything yet, but I can still see him..."
#
#     "Jory sighs deeply and closes his eyes."
#
#     j "Caius...there's something you need to know."
#     extend " While you were gone, word hit Jubilee, and..."
#     c "And...?"
#
#     "He gulps hard and speaks slowly."
#
#
#
#     j "Thrycia..."
#     extend "is no more."
#     c "Huh...?"
#     j "No one is sure of what happened, but the rumors say a devil was involved..."
#     c "A devil...?!"
#     j "Two... Apparently, a dretchling summoned it. I'm sorry..."
#     c "Gngh!" with vpunch
#
#     "I swear I hear Persephone's words in my mind again."
#
#     p "Don't worry, I'll leave Jory be, just as you wished. Anything to get away from you..."
#
#     "My mouth falls agape. I stare at Jory in utter denial."
#     "My heart races, tears fall from my cheeks, but all I can do is remain paralyzed in shock..."
#     "Yet again, I was too weak...and now."
#     extend " There's nothing I can do to save him...!"
#
#     c "...Priam?!"
#     #graceflash
#     j "Woah!"
#     c "PRRRRRRRIIIIIIIIIAAAAAAAAMMMMMM!!!" with vpunch
#
#     return
#     #game ends
