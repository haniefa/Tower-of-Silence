# file: script.rpy

define e= Character("???")
define p = Character("[player_name]")
define d = Character("Doherty")
define b = Character("Betelgeuse")
define c = Character("Clara")

image darkenmc = "mc_darken.png"
image darkenc1 = "C1_darken.png"
image darkenc2 = "C2_darken.png"
image darkenc3 = "C3_darken.png"

define left_pos = Position(xalign=0.0, yalign=1.0)
define right_pos = Position(xalign=1.0, yalign=1.0)

# Placeholder images
image bgblack = "#000"
image bgdefault = "BG_Default.png"
image bgdoor = "BG_door.png"
image bgaltar = "BG_door+sign.png"
image final_room = "BG_final_room.png"

image mc neutral = "MC_neutral.png"
image mc confused = "MC_confused.png"
image mc serious = "MC_Serious.png"
image mc smile = "MC_smile.png"
image mc sad = "MC_sad.png"
image mc scared = "MC_scared.png"
image mc shocked = "MC_shocked.png"
image mc worried = "MC_worried.png"
image mc blush = "MC_blush.png"
image mc mad = "MC_mad.png"
image mc cry = "mc_cry.png"
image mc grateful = "mc_grateful.png"

image scenealtar = "scene_sign.png"
image scenepuzzle1 = "scene_puzzle1.png"
image scenepuzzle1solved = "scene_puzzle1_solved.png"

image c1 confused = "C1_confused.png"
image c1 mask1 = "C1_mask1.png"
image c1 mask2 = "C1_mask2.png"
image c1 neutral = "C1_neutral.png"
image c1 sad = "C1_sad.png"
image c1 scared = "C1_scared.png"
image c1 serious = "C1_serious.png"
image c1 shocked = "C1_shocked.png"
image c1 smile = "C1_smile.png"
image c1 worried = "C1_worried.png"

#chapter 2
image bg2door = "BG_2_door.png"
image bg2door_closed = "BG_2_door_closed_1.png"
image braille_1 = "braille_puzzle_1.png"
image braille_2 = "braille_puzzle_2.png"
image hallway_split = "hallway_split.png" #Hall with two separate paths after puzzle 1
image bars = "ironbars_window_no_beet.png" #View between rooms through barred window from room right, without Beet being there
image bars_beet = "ironbars_window_beet.png" #View between rooms through barred window from room right, Beet being there
image room_left = "room_left.png" #View of Beet's POV, a hallway, an iron bar window on the left, the door they came from on the far side of the room. Beet is looking at the camera, the camera is where the puzzle is at

image c2 confused = "C2_confused.png"
image c2mask1 = "C2_mask1.png"
image c2 neutral = "C2_neutral.png"
image c2 sad = "C2_sad.png"
image c2 scared = "C2_scared.png"
image c2 serious = "C2_serious.png"
image c2 shocked = "C2_shocked.png"
image c2 smile = "C2_smile.png"
image c2 worried = "C2_worried.png"
image c2 mad = "C2_mad.png"

image c2 mask neutral = "C2_maskdefault.png"
image c2 mask sad = "C2_masksad.png"
image c2 mask scared = "C2_maskscared.png"
image c2 mask shocked = "C2_maskshocked.png"
image c2 mask smile = "C2_masksmile.png"
image c2 mask worried = "C2_maskworried.png"
image c2 mask confused = "C2_maskconfused.png"

image stone_piece = "stone_piece.png"
image flashbackc1 = "flashbackc1.png"
image flashbackc1bg = "flashbackc1bg.png"

#CH3
image aslchart = "aslchart.png"

image c3 confused = "C3_confused.png"
image c3 neutral = "C3_neutral.png"
image c3 scared = "C3_scared.png"
image c3 serious = "C3_serious.png"
image c3 shocked = "C3_shocked.png"
image c3 smile = "C3_smile.png"
image c3 worried = "C3_worried.png"
image c3 grateful = "C3_grateful.png"

image c3 mask neutral = "C3_maskneutral.png"
image c3 mask scared = "C3_maskscared.png"
image c3 mask serious = "C3_maskserious.png"
image c3 mask shocked = "C3_maskshocked.png"
image c3 mask worried = "C3_maskworried.png"

image cutscenec3 = "cutscenec3.png"

image doherty = "CG_c1_story.png"
image beet = "CG_c2_story.png"
image clara = "CG_c3_story.png"
image player = "CG_mc_story.png"

# Variables
default player_name = "..."
default trust_c1 = 50
default aggression_c1 = 0
default mental_health_c1 = 100

default trust_c2 = 50
default aggression_c2 = 0
default mental_health_c2 = 100

default trust_c3 = 50
default aggression_c3 = 0
default mental_health_c3 = 100

default beet_mask_on = True
default beet_timer = 30.0

default avoided = True

label start:

    scene bgblack

    e "I'm alone, shrouded in darkness. I have no memory of who I am or how long I've been here. Days? Weeks? Months? I have no idea."
    e "I'm not hungry, not thirsty. I just know that I don't belong here. I need to escape."

    $ player_name = renpy.input("What should I call myself?")
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Alex"  # default name

    e "I'll call myself [player_name] from now on."

    scene bgdefault
    show mc neutral

    p "I stand up, looking around for clues, doors, exits, anything."

    show mc confused
    p "Huh?"

    scene bgdoor
    show mc serious at left_pos
    p "I see something, a dim light seeping through the cracks of what I assume is a door outside. I step closer."

    p "It's not locked. I can get out of here."
    
    scene bgblack
    with fade
    pause 0.1

    scene bgaltar
    show mc serious at center
    p "What the hell? Just another room? Wait— that big-ass door might lead me outside!"

    p "Dammit! It's locked. What the hell am I supposed to do now?"
    scene scenealtar
    show mc confused
    p "What the hell is this thing?"
    scene scenealtar
    pause
    p "“Stand not alone, for the gate listens only to unity.”?" 
    show mc serious 
    p "I can't NOT stand alone, there's nobody else in this damn room!"
    scene bgdefault
    show mc sad
    "Getting desperate, I frantically look around the room for keys, hidden buttons, levers, anything."
    show mc serious
    "After losing hope, I look around the altar, trying to see what I could do with or to it."
    scene scenealtar
    scene bgaltar
    show mc shocked
    p "The massive door opened by itself, making a loud noise in the process."

    p "A few moments later, the door I came from aggressively shuts."
    show mc scared
    p "I panic and run straight outside."

    scene bgblack
    p "It's a hallway, dimly lit by candles on the wall. How the hell did I get here? And more importantly, how the hell do I get out?"

    jump chapter1_continue

label chapter1_continue:
    scene bgdefault
    show c1 mask1
    p "As I'm walking, I notice a person chained to the wall. Feminine outfits with a tall body and wide shoulder. A girl? A boy? I can't tell."
    hide c1 mask1
    show mc neutral
    menu:
        "Approach":
            $ avoided = False
            jump approach_doherty
        "Avoid (Will approach later)":
            $ avoided = True
            $ aggression_c1 += 10
            jump avoid_doherty

label avoid_doherty:
    jump altar_poem_room

label approach_doherty:
    scene bgdefault
    show mc serious at left_pos
    show c1 mask2 at right_pos

    show darkenmc at left_pos zorder 10
    e "GET AWAY FROM ME!"
    hide darkenmc

    show darkenc1 at right_pos zorder 10
    show mc shocked at left_pos
    p "Holy shit!"
    hide mc shocked
    show mc serious at left_pos
    menu:
        "What the hell is your problem!?":
            $ trust_c1 -= 10
            $ aggression_c1 += 10
            $ mental_health_c1 -= 5
            show darkenc1 at right_pos zorder 10
            p "What the hell is your problem!?"
            hide darkenc1
            show darkenmc at left_pos zorder 10
            e "What is YOUR problem?"
            hide darkenmc
        "Hey, I'm here to help.":
            $ trust_c1 += 10
            $ aggression_c1 -= 5
            show darkenc1 at right_pos zorder 10
            show mc worried  at left_pos
            p "Hey, I'm here to help."
            hide darkenc1
            show mc worried  at left_pos
            show darkenmc at left_pos zorder 10
            e "Help? Like the others who PUT me in this situation?"
            hide darkenmc

    show mc serious at left_pos
    show darkenc1 at right_pos zorder 10
    p "Look, I have no memory of getting here, but I'm sure as hell would like to leave this god forsaken place."
    p "If you want, I can take you with me, but I need your help in doing so. Look, I can find the keys to unshackle you. It must be around here somewhere, right?"
    hide darkenc1

    show c1 mask2 at right_pos
    show darkenmc at left_pos zorder 10
    e "No thanks. It's better for me here anyway. I don't belong anywhere else."
    hide darkenmc

    if avoided:
        menu:
            "What do you mean by that?":
                $ aggression_c1 -= 5
                show mc serious at left_pos
                show darkenc1 at right_pos zorder 10
                p "What do you mean by that?"
                hide darkenc1
            "But I need your help, come on!":
                $ trust_c1 -= 5
                $ aggression_c1 += 10
                show mc serious at left_pos
                show darkenc1 at right_pos zorder 10
                p "But I need your help, come on!"
                hide darkenc1
        show mc worried at left_pos
        show darkenmc at left_pos zorder 10

    else:
        menu:
            "Okay then, suit yourself.":
                $ trust_c1 -= 10
                $ mental_health_c1 -= 10
                show mc neutral at left_pos
                show darkenc1 at right_pos zorder 10
                p "Okay then, suit yourself."
                hide darkenc1
                jump altar_poem_room
            "What do you mean by that?":
                $ aggression_c1 -= 5
                show mc serious at left_pos
                show darkenc1 at right_pos zorder 10
                p "What do you mean by that?"
                hide darkenc1
            "But I need your help, come on!":
                $ trust_c1 -= 5
                $ aggression_c1 += 10
                show mc serious at left_pos
                show darkenc1 at right_pos zorder 10
                p "But I need your help, come on!"
                hide darkenc1
        show mc worried at left_pos
        show darkenmc at left_pos zorder 10

    if not avoided:
        e "Just go."
        hide darkenmc

        p "..."
        hide c1 mask2
        hide mc worried
        jump altar_poem_room
    
    elif avoided:
        jump second_convo_doherty

label altar_poem_room:
    scene bgdefault
    show mc neutral
    p "I continue, finding another room, eerily similar to the one before. But there's only one thing in that room, another altar."
    scene scenepuzzle1
    show mc confused
    p "On top of it, instead of something glowing, it's a poem, but it looks unfinished."
    hide mc confused
    pause
    show mc serious at left_pos
    p "Masks are made to hide shame"
    p "For someone unable to find themselves"
    p "Though my appearance doesn't match my name"
    p "I am …?"
    show mc confused at left_pos
    p "What the shit is this? This looks like someone deliberately removed the last part. But why? What does this mean?"
    show mc serious
    p "Looking around, I saw nothing. And there's nothing else to check but another big door. I assume the altar is the key to unlocking the big door. Finding no other clues, I walked back to the chained stranger."

if not avoided:
    jump second_convo_doherty

elif avoided:
    jump approach_doherty

define k = Character("Kid")
define m = Character("Lady")

label second_convo_doherty:
    scene bgdefault
    show mc neutral at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos  # MC speaks, darken Doherty

    if not avoided:
        p "Hey, I know you asked me to leave you alone, but I'm quite stuck. Can you please help me out here?"

    elif avoided:
        p "Look, I've been in that room already. There's this weird altar and this huge door but I can't find a way to get it to open. Please help me out."

    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    e "Why ask me? There's nothing someone like me could do to help you."
    hide darkenmc
    show mc confused at left_pos
    show darkenc1 at right_pos  # MC speaks, darken Doherty
    p "(I look at… him? her? I still don't know. Their voice is masculine, but their appearance is very feminine. Wait, 'my appearance doesn't match my name'.)"
    show mc neutral at left_pos
    p "What's your name?"
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    e "Why do you want to know? Is it because it's hard to identify me?"
    hide darkenmc
    show mc neutral at left_pos
    show darkenc1 at right_pos  # MC speaks, darken Doherty
    menu:
        "It's a bit weird talking to someone without knowing their name, you know?":
            $ trust_c1 += 10
            $ aggression_c1 -= 5
        "Yes, actually. You have a very manly voice, yet such a soft and feminine appearance":
            $ mental_health_c1 -= 10
        "I need it for the poem thing in the other room, I guess.":
            $ trust_c1 -= 10
            $ aggression_c1 -= 5
            $ mental_health_c1 -= 5
    hide darkenc1
    e "..."

    menu:
        "Sit down beside them":
            $ trust_c1 += 10
            $ sit_choice = "beside"
        "It's just your name, why can't you answer it?":
            $ trust_c1 -= 10
            $ aggression_c1 += 10
            $ sit_choice = "opposite"

            show darkenmc at left_pos
            e "..."
            e "Screw you."
            hide darkenmc
            show mc confused at left_pos
            show darkenc1 at right_pos
            p "What the hell?"
            hide mc confused
            hide darkenc1

        "It's okay, I don't wanna force you.":
            $ trust_c1 += 10
            $ aggression_c1 -= 5
            $ mental_health_c1 += 5
            $ sit_choice = "beside"
    hide mc
    show mc neutral at left_pos
    show darkenmc at left_pos  # Doherty speaks, darken MC
    show c1 mask1 at right_pos
    d "Doherty. I'm a he."
    hide darkenmc
    show darkenc1 at right_pos  # Doherty speaks, darken MC
    p "Your name is Doherty?"
    hide darkenc1

    if sit_choice == "opposite":
        p "(I stood opposite of him.)"
    elif sit_choice == "beside":
        p "(I sit down beside him.)"

    show darkenc1 at right_pos
    p "Do you know how long you've been here?"
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    d "I don't. I don't care. I want to be here. I hate everything and everyone else."
    hide darkenmc
    show darkenc1 at right_pos  # MC speaks, darken Doherty
    show mc confused at left_pos
    p "What do you mean by ‘everyone else'?"
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    d "I mean everyone else. Everyone made me this way. They built me, and now they throw me out. It's like I'm some heartless doll they play with and discard whenever they please."
    hide darkenmc
    show darkenc1 at right_pos  # MC speaks, darken Doherty    
    p "They… ‘built' you?"
    show darkenmc at left_pos  # Doherty speaks, darken MC
    show stone_piece
    hide darkenmc
    show mc confused at left_pos
    p "Wha-...?"
    "While talking, I noticed the piece from the altar in the other room is right next to Doherty. He then passed me it."
    show mc smile at left_pos
    menu:
        "Thank you.":
            $ aggression_c1 -= 5
        "You had this all this time? Why didn't you tell me?":
            $ aggression_c1 += 10
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    d "..."

    scene bgdefault
    show mc neutral
    p "(I walk back to the other room with the stone in hand. I then place the stone on the missing part of the poem.)"
    scene scenepuzzle1solved
    pause
    p "\"I am more than an empty shell.\""
    p "(The altar moves to the side, behind it lies a key. I take it and rush to the door.)"
    show mc neutral
    menu:
        "Do I check on Doherty?":
            jump going_back_to_doherty
        "Do I just open the door?":
            jump try_key_on_door

label try_key_on_door:
    scene bgdoor
    show mc serious
    p "(I try the key on the doors.)"
    p "Fuck! It doesn't fit the hole."
    jump going_back_to_doherty

label going_back_to_doherty:
    scene bgdefault
    show mc neutral at center
    "I turn back to Doherty."
    hide mc neutral
    show mc smile at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos
    p "I think I found the key to unlocking your shackles."
    hide darkenc1
    show darkenmc at left_pos
    d "Take it away. I don't need it."
    hide darkenmc
    show darkenc1 at right_pos
    show mc worried at left_pos
    p "But—"
    hide darkenc1
    show c1 mask2
    show darkenmc at left_pos
    d "I SAID LEAVE ME BE!"

    scene bgblack
    "(Startled, I got knocked back and hit my head against the wall. I woke up in another room, dizzy.)"
    pause
    scene flashbackc1bg
    "Huh? What the hell? Where am I? Why is everything so… feminine?"

    show flashbackc1
    k "Momma, can I please stop wearing these girl clothes—"
    scene bgblack
    "*SLAP*"
    show flashbackc1
    m "GIRLS WEAR GIRLS' CLOTHING! And you are a girl, aren't you?"
    k "B-but… I'm a—"
    scene bgblack
    "*SLAP*"
    show flashbackc1
    m "YOU ARE A GIRL, AREN'T YOU!?"
    k "Sobbing, Yes, I am."
    m "Good girl. Now, what's your name?"
    k "...Doherty."
    scene bgblack
    "*SLAP*"
    show flashbackc1
    m "DOHERTY IS A BOY'S NAME! Your name is ‘Dorothy', okay?"
    d "Nods"
    m "Good. You'll meet your new father soon enough, my dear."

    "What the fuck am I experiencing?!"
    scene bgdefault
    show mc worried at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos
    "Panting"
    p "Doherty… You never wanted this, did you? To be like this?"
    hide darkenc1
    d "(Shakes head)"
    show darkenc1 at right_pos

    p "So why don't you just… rebel against them?"
    hide darkenc1
    show darkenmc at left_pos
    d "I tried."
    scene bgdefault
    "Doherty begins to unbutton his dress."
    show mc blush
    p "W-what are you??!"
    hide mc blush
    "Doherty shows his bruised back, full with scars."
    d "She won't let me."
    show mc worried at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos
    p "Holy shit…"
    hide darkenc1
    show darkenmc at left_pos
    d "I've always hated the way I am. I can't be a boy because I would get hit by my mother. But every time I put on a dress, my stepfather would touch me. Nothing was ever the right thing. I don't know who I am."
    hide darkenmc
    menu:
        "Let's just get out of here, together. Forget your mother.":
            $ trust_c1 += 10
            $ mental_health_c1 += 10
            $ ending_choice = "good"
            show mc worried at left_pos
            show darkenc1 at right_pos
            p "Let's just get out of here, together. Forget your mother."
            show darkenmc at left_pos
            hide darkenc1
            d "I-"

            hide darkenmc
            d "..."
            show darkenmc

        "I'm so sorry. I could never imagine the pain you've endured…":
            $ trust_c1 += 10
            $ aggression_c1 -= 10
            $ mental_health_c1 += 10
            $ ending_choice = "good"
            show mc sad at left_pos
            show darkenc1 at right_pos
            p "I'm so sorry. I could never imagine the pain you've endured…"
        "The past is in the past. Now let's go!":
            $ mental_health_c1 -= 10
            $ ending_choice = "bad"
            show mc smile at left_pos
            show darkenc1 at right_pos
            p "The past is in the past. Now let's go!"



    if ending_choice == "good":
        show mc worried at left_pos
        show c1 mask1 at right_pos
        show darkenmc at left_pos
        d "I don't have siblings. I don't remember my father. All I know is torture. Everyone treats me like garbage. Like I'm some sort of toy to dress up and humiliate."
        hide darkenmc
        show darkenc1 at right_pos
        p "Oh my god… Doherty, I—"
        hide darkenc1
        show darkenmc at left_pos
        d "It doesn't matter anymore. I'm here, and this is where I want to be."
        hide darkenmc 
        show darkenc1 at right_pos
        show mc smile at left_pos
        p "But we can go away, be free. Be who you are without judgment. Please, join me."
    
    elif ending_choice == "bad":
        d "..."
    
    if trust_c1 > 50 and aggression_c1 < 50 and mental_health_c1 > 60:
        scene bgdefault
        show c1 mask1 at right_pos
        show mc smile at left_pos
        show darkenmc at left_pos
        d "..."
        show c1 sad at right_pos
        "Doherty takes off his mask"
        show c1 smile at right_pos
        d "Let's go."
        "(We both walk to the door. It opens by itself.)"
        jump chapter1_complete

    elif aggression_c1 >= 5:
        scene bgblack
        p "(I waited for an hour, then sat down. Suddenly, I felt a stinging pain in my neck. Doherty with a glass shard in hand, bloody.)"
        scene bgdefault
        show c1 mask2
        d "IT'S SO EASY FOR YOU! YOU DON'T EVEN CARE ABOUT ME!"
        jump bad_ending_1

    elif mental_health_c1 <= 40:
        scene bgblack
        "(I waited for an hour, I then sat down, waiting for Doherty to come. I closed my eyes for a moment.)"
        "(A few moments went by, then Doherty came into the room with a shard of glass in his hand.)"
        scene bgdefault
        show mc worried at left_pos
        show darkenc1 at right_pos
        p "Uh... Doherty? What is that for?"
        show darkenmc at left_pos
        show c1 scared at right_pos
        d "You made me realize why I'm here and why I never wanted to leave. There are only people like you out there. So fuck you!"
        scene bgblack
        "(Doherty then slit his own throat, instantly killing himself. I stood in shock. I am now stuck here for god knows how long.)"
        jump bad_ending_2


label chapter1_complete:
    "-CHAPTER 1 COMPLETE-"
    jump chapter2

label bad_ending_1:
    "-BAD ENDING 1-"
    "Tip: try to approach him with empathy."
    return

label bad_ending_2:
    "-BAD ENDING 2-"
    "Tip: try to approach him with empathy."
    return

#CHAPTER 2
label chapter2:

    scene bgblack with fade
    "After finally unlocking the previous door, Doherty and I continue forward."
    "The hallway we enter is eerily quiet—long, dimly lit by a line of flickering candles. The air feels heavier here."

    p "(Something about this place feels... wrong.)"

    "Eventually, we reach a new chamber. It's different. Two large doors stand on opposite walls. Between them—a strange console embedded into the stone."

    scene bg2door with dissolve
    "Next to the console, we see someone. Just sitting still. Silent. Masked—like Doherty once was."

    scene bgdefault
    show mc worried at left_pos
    show c2 mask neutral at right_pos
    show darkenc2 at right_pos

    p "Hey–"

    show darkenmc at left_pos
    hide darkenc2
    hide c2 mask neutral
    show c2 shocked at right_pos
    show c2mask1 at right onlayer overlay
    
    e "Huh??"

    hide darkenmc
    hide c2 shocked 
    show mc neutral at left_pos
    show c1 neutral at right_pos
    p "I'm [player_name], and this is Doherty. We're not here to hurt you."

    hide c1 neutral
    show c2 smile at right_pos
    show c2mask1 at right onlayer overlay
    show darkenmc at left_pos
    e "Oh… My name is Betelgeus, but you can call me Beet."
    show c2mask1 at right onlayer overlay
    b "What are you doing here? I thought I was the only one left."

    hide darkenmc
    hide mc worried
    hide mc neutral
    show c1 neutral at left_pos
    show c2mask1 at right onlayer overlay
    show darkenc2 at right_pos
    d "We're trying to escape."

    hide darkenc2
    show darkenc1 at left_pos
    show c2mask1 at right onlayer overlay
    b "Escape? From where? To where?"

    hide c1 neutral
    hide darkenc1
    show mc worried at left_pos
    show darkenc2 at right_pos
    show c2mask1 at right onlayer overlay
    p "I don't remember much... but I definitely didn't walk into this dungeon on purpose."

    hide darkenc2
    hide c2
    show darkenmc at left_pos
    show c1 neutral at right_pos
    d "Same. I've been here more days than I could count."

    hide darkenmc
    show darkenc1 at right_pos
    hide c2

    p "Wait... what do you mean, 'the only one left'?"

    hide darkenc1
    hide c1 neutral
    show darkenmc at left_pos
    show c2 smile at right_pos
    show c2mask1 at right onlayer overlay

    b "There used to be others. Three of us, I think. I don't remember names. Maybe I forgot them. But I do remember one of them not speaking, just making noises. Maybe they're deaf?"

    hide darkenmc
    hide mc worried
    show c1 worried at left_pos
    show c2 neutral at right_pos
    show darkenc2 at right_pos
    show c2mask1 at right onlayer overlay

    d "I might've been one of them."

    show darkenc1 at left_pos
    hide darkenc2
    show c2 smile at right_pos
    show c2mask1 at right onlayer overlay

    b "Maybe... It's been so long. But with you two— hearing your voices— it's nice to have company again."

    hide darkenc1
    hide c1 worried
    show mc worried at left_pos
    show darkenc2 at right_pos
    show c2 mask neutral at right_pos 
    p "Yeah, after that long being by yourself, I could imagine."
    
    menu:
        "But we need to get out of here. Do you not want to get out with us?":
            $ trust_c2 += 10
            $ aggression_c2 -= 10
            show darkenmc at left_pos
            hide darkenc2
            show c2mask1 at right onlayer overlay
            b "Haha... yeah. I want out. I don't belong in this place."
            b "But what can I do to help?"

        "But I need to get out of here. So can you please help me?":
            $ aggression_c2 += 10
            show darkenmc at left_pos
            hide darkenc2
            b "..."
            b "Why should I help you again?"

    b "Besides, there's not much a blind guy like me can do."
    hide darkenmc

    hide mc worried
    show c1 worried at left_pos
    show darkenc2 at right_pos
    d "Don't say that. There's a braille puzzle on the console. Maybe you can help."

    show darkenc1 at left_pos
    show c2 worried at right_pos
    hide darkenc2
    show c2mask1 at right onlayer overlay
    b "Braille...? Sorry— I never learned it."

    hide darkenc1
    hide c1 worried

    show mc shocked at left_pos
    show c2 sad at right_pos
    show c2mask1 at right onlayer overlay
    show darkenc2 at right_pos
    p "What?"

    show darkenmc at left_pos
    show c2 neutral at right_pos
    hide darkenc2
    show c2mask1 at right onlayer overlay
    b "Yeah. I only lost my sight recently. At least, I think it was recent. My memory's foggy."

    show mc sad at left_pos
    show darkenc2 at right_pos
    hide darkenmc
    show c2mask1 at right onlayer overlay
    p "What happened?"

    show c2 neutral at right_pos
    hide darkenc2
    hide mc shocked
    show mc worried at left_pos
    show darkenmc at left_pos
    show c2mask1 at right onlayer overlay
    b "I just remember... searing pain. My mother found me afterwards. She said I was just... there."

    show mc sad at left_pos
    show c1 sad at right_pos
    hide darkenmc
    p "..."
    d "...That's rough."

    hide c1 sad
    show mc worried at left_pos
    show c2mask1 at right onlayer overlay
    show darkenmc at left_pos

    b "Since then, life's been a blur. I can't see anything. Not even light. Braille? I never got to learn. Couldn't use it. Never needed to, I guess."
    hide c2
    show c2 sad at right_pos
    show c2mask1 at right onlayer overlay
    b "I guess the fact that I could never understand braille led me to give up. It's frustrating, you know? Everything happened so quick and I'm just forced to adapt to it."
    show c2mask1 at right onlayer overlay
    b "It sucks."

    show darkenmc at left_pos
    show c1 sad at right_pos
    d "That sounds... horrible."

    hide c1 sad
    show darkenmc at left_pos
    show c2 mask smile at right_pos

    b "Heh. You get used to it... or you try."

    hide darkenmc
    menu:
        "We'll figure it out together.":
            $ trust_c2 += 10
            $ aggression_c2 -= 5
            $ mental_health_c2 += 5
            show mc smile at left_pos
            show darkenc2 at right_pos
            show c2mask1 at right onlayer overlay
            p "Even if you don't know braille, we'll figure it out together."
            show darkenmc at left_pos
            show c2 smile at right_pos
            hide darkenc2
            show c2mask1 at right onlayer overlay
            b "Thanks... really."

        "You could've just said you're useless.":
            $ aggression_c2 += 15
            $ trust_c2 -= 15
            $ mental_health_c2 -= 10
            show mc serious at left_pos
            show darkenc2 at right_pos
            show c2mask1 at right onlayer overlay
            p "So you can't help. Great."
            show darkenmc at left_pos
            show c2 sad at right_pos
            hide darkenc2
            show c2mask1 at right onlayer overlay
            b "...I didn't ask for this."

        "Why don't we learn braille together?":
            $ trust_c2 += 20
            $ aggression_c2 -= 5
            $ mental_health_c2 += 15
            show mc neutral at left_pos
            show darkenc2 at right_pos
            show c2mask1 at right onlayer overlay
            p "No use arguing. Let's learn braille together."
            show darkenmc at left_pos
            show c2 neutral at right_pos
            show c2mask1 at right onlayer overlay
            hide darkenc2
            b "You mean it?"
            show mc smile at left_pos
            hide darkenmc
            show c2mask1 at right onlayer overlay
            show darkenc2 at right_pos
            p "Yeah. We'll learn together."

    hide mc
    hide darkenmc
    hide darkenc2
    hide c2
    show c2 mask neutral at right_pos
    show mc serious at left_pos
    show darkenc2 at right_pos
    p "We can describe it to you. You might notice something we miss."

    show darkenmc at left_pos
    show c1 smile at right_pos
    hide c2mask1
    d "Totally worth a shot."

    show mc neutral at left_pos
    show darkenc2 at right_pos
    hide darkenmc
    p "Alright, let's give it a try."

    show darkenmc at left_pos
    hide c1
    hide c2
    hide darkenc2
    show c2 mask smile at right_pos

    b "Alright. Where is this thing?"

    jump braille_puzzle_1

label braille_puzzle_1:
    scene braille_puzzle_1
    pause
    show mc neutral at left_pos
    show c1 neutral at right_pos
    hide darkenmc

    p "Looks like this console uses braille to display a four-digit code. There's a hint carved into the sign below."

    d "It's a number sequence. Should be easy if we follow the guide."

    hide c1
    hide c2
    show darkenmc at left_pos
    show c2 smile at right_pos
    show c2mask1 at right onlayer overlay

    b "Alright... I'll try to feel it out too."
    
    hide c2
    hide mc
    hide darkenmc


    $ braille_answer = renpy.input("What's the 4-digit pin?", length=4)
    $ braille_answer = braille_answer.strip()

    if braille_answer == "0101":
        show c2 mask smile at right_pos
        p "That worked!"
        $ mental_health_c2 += 5
        scene bg2door
        hide mc neutral
        hide c1 neutral
        show mc smile at left_pos
        show c1 smile at right_pos

        p "The doors… they're opening."
        hide mc smile
        hide c1
        show c2 mask smile
        b "Did we do it?"
        jump hallway_split
    else:
        hide c2
        show c2 sad at right_pos
        show c2mask1 at right onlayer overlay
        p "That's not right..."
        jump braille_puzzle_1_retry

label braille_puzzle_1_retry:
    show c2mask1 at right onlayer overlay
    menu:
        "Try again":
            jump braille_puzzle_1
        "Give up":
            hide mc neutral
            hide c1 neutral
            show mc sad at left_pos
            show darkenmc at left_pos
            show c2mask1 at right onlayer overlay
            p "(We'll never get out like this...)"
            $ mental_health_c2 -= 10
            return

label hallway_split:
    scene hallway_split
    show mc serious at left_pos
    show c2 mask worried at right_pos
    p "There's two paths now…"

    show darkenmc at left_pos

    b "Let's not split up. I'll stay close."

    "The group steps toward the right door."

    scene bgblack
    hide mc serious
    hide c1 worried

    "A sudden slam echoes. The door slams shut behind [player_name] and Doherty—Beet is left on the other side."

    scene bars
    show mc shocked at left_pos
    show c1 shocked at right_pos
    p "Beet!?"

    scene bg2door_closed
    hide mc shocked
    hide c1
    show c2 mask confused

    b "What the—!? The door just slammed on me!"

    scene bars
    hide darkenmc
    hide c2
    show c1 worried at right_pos
    show mc worried at left_pos
    show darkenc1 at right_pos
    p "Damn it!"

    hide darkenc1
    show c1 serious at right_pos
    show darkenmc at left_pos
    d "There's an iron window in this room that connects to the other!"

    scene bars
    show mc worried at left_pos
    show c1 worried at right_pos
    p "Beet! You good?"

    scene bg2door_closed
    hide mc worried
    hide c1 worried
    show c2 mask smile

    b "Yeah… just shaken."
    show c2mask1 onlayer overlay
    hide c2mask1
    show c2 mask neutral
    b "I feel another door open... I'll check it."
    "Beet goes through the left door"

    scene bars_beet
    show mc serious at left_pos
    show c1 worried at right_pos
    p "We can see you through this iron barred window. I think this room will lead to the same exit as ours!"

    scene room_left
    hide mc serious
    hide c1 worried
    show c2 mask smile

    b "Heh. Guess I can't see you back."

    scene bgblack
    hide c2mask1
    hide c2 neutral
    "Another heavy slam. The left room's door shuts tight behind him."

    scene bars_beet
    show mc shocked at left_pos
    show c1 shocked at right_pos
    p "...Wait."

    scene room_left
    show c2 mask worried

    b "...Did you hear that?"

    "Metal creaks above."

    scene bars_beet
    show mc shocked at left_pos
    show c1 shocked at right_pos
    show darkenc1 at right_pos
    p "The ceiling! It's moving!"

    show darkenmc at left_pos
    show c1 scared at right_pos
    hide darkenc1
    d "Both rooms are closing in!"

    scene room_left
    show c2 mask shocked

    b "Oh shit! I need to move—now!"

    jump beet_solo_puzzle

label beet_solo_puzzle:

    if trust_c2 >= 50 and aggression_c2 <= 5:
        scene braille_2
        pause
        show c2 mask scared
        b "(You know what... I trust them now.)"
        b "(If I'm going to survive this... I want to do it as me.)"

        b "Here goes nothing."
        show c2 mask neutral
        ""
        show c2 neutral with dissolve

        "For the first time, you see him—not as a prisoner or a stranger, but as a person."
        hide c2 serious
        show c2 serious
        b "Okay... Let's do this."
        hide c2 serious

    else:
        scene braille_2
        pause

        b "(Okay… I'm on my own now. No hints. Just me and this panel.)"

        show c2 mad
        show c2mask1 onlayer overlay
        b "...You know what? No."
        show c2mask1 onlayer overlay
        b "And you know what else? I'm keeping the mask on."
        show c2mask1 onlayer overlay
        b "You never saw me—not really—and I think I prefer it that way."
        show c2mask1 onlayer overlay
        b "You guys aren't nice at all. I don't think I'm gonna help you."
        show c2mask1 onlayer overlay
        b "Figure it out yourselves!"
        show c2mask1 onlayer overlay

        scene bars_beet
        show mc shocked at left_pos
        show c1 shocked at right_pos
        d "Wait—Beet!"

        scene bgblack
        "Without Beet's help, the console stayed locked. The ceiling kept falling..."
        "And we couldn't escape."

        jump bad_ending_beet_refuses

    $ attempt_left = 3

    label beet_input_loop:
        $ beet_input = renpy.input("Enter the 4-digit code:", length=4)
        $ beet_input = beet_input.strip()

        if beet_input == "0314":
            hide c2
            show c2 smile
            b "I did it!"
            $ trust_c2 += 10
            $ mental_health_c2 += 10
            scene bgdefault
            show c2 smile
            b "The door opened... I'm safe."
            jump beet_survives
        else:
            $ attempt_left -= 1
            b "Dammit! It's wrong!"
            if attempt_left <= 0:
                scene bgblack
                "The ceiling crushed down before he could try again."
                jump bad_ending_beet_crushed
            else:
                b "I have [attempt_left] tries left!"
                jump beet_input_loop

label beet_survives:
    scene bgdefault
    show mc smile at left_pos
    show c1 smile at right_pos
    hide c2
    "[player_name] & Doherty" "Beet! You're okay!"
    hide mc smile
    hide c1
    show c2 smile
    b "Heh… barely."

    "-GOOD ENDING-"
    jump chapter3

label bad_ending_beet_refuses:
    "-BAD ENDING: YOU LOST HIS TRUST-"
    return

label bad_ending_beet_crushed:
    "-BAD ENDING: BEET WAS CRUSHED-"
    return

# Chapter 3

label chapter3:

    scene bgblack
    "We finally managed to escape those death puzzle room things. Makes me wonder what this place actually is and what it's for."
    "As we continue to walk towards what I assume are the exits, things seem to calm down a bit. No traps, no puzzles, nothing. Just stairs and hallways."
    "Another floor... When will this end?"
    "Oh well, at least I'm not alone"


    scene bgdefault
    show c1 smile
    with fade
    "I got an unexpected friend in Doherty"

    hide c1
    show c2 smile
    with fade
    "And Beet trusts me now, too."

    scene bgblack
    with fade
    "My job now is, not just to find and exit out of this place, but to make them feel comfortable with who they are, in the real world once we get there."

    scene bgdefault
    show c1 neutral at left_pos
    show c2 neutral at right_pos
    show darkenc1 at left_pos
    with fade
    b "-Sigh- Another floor."
    hide darkenc1
    show darkenc2 at right_pos
    d "Look. There's something on the floor."
    hide darkenc2
    hide c1 neutral
    hide c2 neutral
    show mc serious
    p "..."

    scene aslchart
    pause

    show mc serious at left_pos
    show c2 neutral at right_pos
    show darkenc2 at right_pos
    p "Looks like... an ASL alphabet guide. Neatly drawn and easy to understand."
    hide darkenc2
    show darkenmc at left_pos
    hide c2
    show c2 smile at right_pos
    b "Oh? Remember someone I mentioned before? Yeah, the deaf one. Maybe this belonged to them."
    hide darkenmc
    hide mc serious
    show darkenc2 at right_pos
    show c1 neutral at left_pos
    d "Throw it away. It's probably just trash."
    hide darkenc2
    show darkenc1 at left_pos
    b "Better to memorize a few. Who knows, it might be useful later."
    hide darkenc1
    hide c1 neutral
    hide c2 neutral
    call screen asl_chart_screen

    screen asl_chart_screen():
        add "aslchart.png"
        text "Did you memorize it?" xalign 0.5 yalign 0.9
        textbutton "Yes" action Return("yes") xalign 0.4 yalign 0.95
        textbutton "No" action Return("no") xalign 0.6 yalign 0.95

label after_asl_chart:
    $ result = renpy.call_screen("asl_chart_screen")
    if result == "no":
        jump asl_chart_screen  # restart the ASL scene
    else:
        jump continue_ch3


label continue_ch3:

    scene bgdoor
    with fade

    show c3 mask neutral
    e "..."
    hide c3 mask neutral
    show mc smile
    p "Excuse me?"
    hide mc smile
    show c3 mask neutral
    "..."
    hide c3 mask neutral
    show mc confused
    p "Hello?"
    hide mc confused
    menu:
        "What do you do?"
        "Shout into her ear":
            $ trust_c3 -= 10
            $ aggression_c3 += 10
            $ mental_health_c3 -= 5
            show mc mad at left_pos
            hide c3
            show c3 mask neutral at right_pos
            show darkenc3 at right_pos
            p "HEY!"
            hide mc
            show mc serious at left_pos
            show darkenmc at left_pos
            hide c3
            show c3 mask scared at right_pos
            e "!!!"
            hide c3
            hide darkenc3
            hide mc
            show mc scared at left_pos
            show darkenmc at left_pos
            show c2 mad at right_pos
            b "Why the hell would you do that!?"
            hide c2
            hide darkenmc
            hide mc
            jump wrong_approach
        "Tap her shoulder":
            $ trust_c3 += 10
            $ aggression_c3 -= 5            
            jump right_approach
        "Forcefully remove her earmuffs":
            $ trust_c3 -= 10
            $ aggression_c3 += 10
            $ mental_health_c3 -= 5
            hide c3
            show c3 mask scared
            e "!!!"
            hide c3
            show mc neutral at left_pos
            show darkenmc at left_pos
            show c2 neutral at right_pos
            b "What'd you do?"
            hide darkenmc
            show darkenc2 at right_pos
            p "I took her earmuffs off."
            hide darkenc2
            show darkenmc at left_pos
            show c2 neutral at right_pos
            b "Forcefully?"
            hide darkenmc
            show darkenc2 at right_pos
            p "Uhh... yeah?"
            hide mc
            show mc scared at left_pos
            show darkenmc at left_pos
            hide darkenc2
            hide c2
            show c2 mad at right_pos
            b "Why the hell would you do that!?"
            b "Give it back to them!"
            scene bgblack
            "I gave them back to her just like Beet asked."
            scene bgdoor
            jump wrong_approach

label right_approach:
    $ trust_c3 += 10
    $ aggression_c3 -= 5
    show c3 mask worried at left_pos
    show darkenc3 at left_pos
    show c1 serious at right_pos
    d "Maybe she's the one Beet mentioned... the deaf one?"
    show darkenc1 at right_pos
    hide darkenc3
    hide c3 mask worried
    show c2 confused at left_pos
    b "I guess so. I could only sense someone was nearby. Without sound, I can't really tell."
    show darkenc2 at left_pos
    hide darkenc1
    hide c1 serious
    show c1 worried at right_pos
    d "Damn... I don't have a pen to talk to her."
    show c2 serious at left_pos
    hide darkenc2
    show darkenc1 at right_pos
    b "That's why I told you to memorize that guide earlier. Well, [player_name]? Try using it."
    scene bgdefault
    jump deafmenu

label wrong_approach:
    $ trust_c3 -= 5
    $ aggression_c3 += 15
    show c3 mask worried at left_pos
    show darkenc3 at left_pos
    show c1 serious at right_pos
    d "Maybe she's the one Beet mentioned... the deaf one?"
    show darkenc1 at right_pos
    hide darkenc3
    hide c3 mask worried
    show c2 confused at left_pos
    b "I guess so. I could only sense someone was nearby. Without sound, I can't really tell."
    show darkenc2 at left_pos
    hide darkenc1
    hide c1 serious
    show c1 worried at right_pos
    d "Damn... I don't have a pen to talk to her."
    show c2 serious at left_pos
    hide darkenc2
    show darkenc1 at right_pos
    b "That's why I told you to memorize that guide earlier. Well, [player_name]? Try using it."
    scene bgdefault
    jump deafmenu
    
label deafmenu:
    menu:
        "What will you do?"
        "Are you the deaf person he mentioned?":
            $ trust_c3 -= 10
            $ mental_health_c3 -= 5
            jump girl_unresponsive
        "Can you not hear us or speak at all?":
            $ trust_c3 -= 10
            $ mental_health_c3 -= 5
            jump girl_unresponsive
        "Start signing using ASL":
            $ trust_c3 += 10
            $ aggression_c3 -= 5 
            jump girl_understands

label girl_unresponsive:

    show c3 mask neutral
    "She stares at you without a word."
    jump deafmenu

label girl_understands:

    show c3 mask neutral

    call screen asl_dialogue

screen asl_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 15

        imagebutton:
            idle "opsi1.png"
            action Return("right")

        imagebutton:
            idle "opsi2.png"
            action Return("angry")

        imagebutton:
            idle "opsi3.png"
            action Return("confused")

label asl_response:
    $ response = renpy.call_screen("asl_dialogue")
    if response == "right":
        show c3 mask neutral
        d "She seems fine.."
        p "Yeah it says 'Can we ask you something?'"
        $ trust_c3 += 10
        $ aggression_c3 -= 5 
        jump claraconvo
    elif response == "angry":
        show c3 mask serious
        d "She seems angry.."
        p "Maybe I was too rude.. I was saying 'Say something, are you deaf?"
        $ trust_c3 -= 10
        $ aggression_c3 += 10
        $ mental_health_c3 -= 5
        jump girl_understands
    else:
        show c3 mask worried
        d "Is that even a language..."
        p "It's 'oiiaiaoiiiai'"
        b "...What?"
        $ trust_c3 -= 10
        $ mental_health_c3 -= 5
        jump girl_understands

#di sini masih perlu if else kalo trust dan aggression di titik tertentu, bikin label baru bad ending dibunuh atau clara bunuh diri
# Tapi aku cape :')
# yawes gini aja
label claraconvo:
    scene bgdefault
    show mc smile at right_pos
    show c3 mask neutral at left_pos
    "Since then, they started to communicate in sign language, with Doherty speaking in words to make sure Beet still in the same boat."
    show darkenc3 at left_pos
    p "So.. What's your name?"
    hide darkenc3
    show darkenmc at right_pos
    c "I'm Clara."
    show darkenc3 at left_pos
    hide darkenmc
    p "So.. Clara. We're trying to get to the top of the tower in hopes we could find an exit. Can you help us?"
    "She nods softly."
    hide mc smile
    show c1 confused at right_pos
    d "I'm sorry but.. Can I ask... Are you just deaf or you...?"

    "..."
    "She lowers her head. Then slowly, she opens her mouth."

    hide darkenc3
    show darkenc1 at right_pos
    c "...m-my.. v-voice.. is weird..."

    hide c1
    show darkenc3 at left_pos
    show c1 smile at right_pos
    d "(laughs) Haha! What the hell's that supposed to be? You sound like a comedian played back on a broken radio!"

    menu:
        "How do you respond?"
        "Ask Doherty to stop":
            $ trust_c3 += 10
            $ aggression_c3 -= 5
            hide mc
            hide c1
            hide c2
            hide c3
            hide darkenc1
            hide darkenc2
            hide darkenc3
            show mc serious at left_pos
            show c1 sad at right_pos
            show darkenc1 at right_pos
            p "Hey quit it!"
            hide mc
            hide c1
            hide c2
            hide c3
            hide darkenc1
            hide darkenc2
            hide darkenc3
        "Let Doherty make fun of her":
            $ trust_c3 -= 10
            $ aggression_c3 += 10
            $ mental_health_c3 -= 15
            hide mc
            hide c1
            hide c2
            hide c3
            hide darkenc1
            hide darkenc2
            hide darkenc3
            show c2 serious at left_pos
            show c1 sad at right_pos
            show darkenc1 at right_pos
            b "Hey quit it!"
            hide c2
            hide c1
            hide darkenc1
            show c2 serious at right_pos
            show mc sad at left_pos
            show darkenmc at left_pos
            b "You're seriously not gonna do anything about that?"
            hide mc
            hide c2
            hide darkenmc

    show c3 mask worried
    "Her expression fades. She pulls out her small notebook."

    p "Wait..."

    scene bgblack
    with fade
    "As she pulled out her notebook, I got transported again, just like how it was with Doherty."
    "I started hearing unfamiliar voices again."

    scene cutscenec3

    e "Haha what is this? Are you expecting us to learn all of those? For YOU? Get a grip!"
    p "Is this her past?"

    scene bgblack

    "*Scrap*"

    scene cutscenec3

    c "n-no.. p-p.. plea--...zh..."
    e "What the hell is that voice? It's so weird and ugly hahaha!"
    e "Someone grab some tape and tape her mouth shut! Her voice is gonna make me puke!"
    p "No, please stop it! Stop bullying that poor girl!"

    scene bgblack
    pause
    
    "As Clara shows more and more, it became even clearer how her past was."
    "All those bullying, all of her spent tears."
    "Poor girl..."
    "This world is too mean to her."
    show mc serious
    with fade
    "We have to help her!"

    scene bgdefault
    show mc worried at left_pos
    show c3 mask worried at right_pos
    with fade

    "I sign to her"
    show darkenc3 at right_pos

    "Clara, I'm so sorry you went through all of that."

    hide darkenc3

    "Clara begins to sob."

    menu:
        "I offer her a hug":
            hide c3
            hide mc
            show mc smile at left_pos
            show c3 mask neutral at right_pos
            "I reached out to her, offering her a hug."
            "She came to me and hugged me back."
            "I feel like she only needed company, someone who understands her"
            hide c3
            hide mc
        "I signed her to please stop crying":
            hide c3
            hide mc
            show mc neutral at left_pos
            show c3 mask worried at right_pos
            show darkenc3 at right_pos
            "I sign to her"
            p "Clara, please stop crying."
            "A few moments later, Clara stopped."
            hide c3
            hide mc

    
    jump ending_scene

label ending_scene:
    if aggression_c3 >= 5 or mental_health_c3 <= 60:
        jump bad_ending_clara

    else:
        scene bgdefault

        show mc smile at left_pos
        show c3 mask worried at right_pos
        show darkenc3 at right_pos

        "I sign to her again, still looking at the ASL sheet we found previously."
        p "Hey, you are no longer alone. We are friends. Your friends."

        show darkenmc at left_pos
        hide darkenc3
        hide c3
        show c3 mask neutral at right_pos

        "She then takes off her mask."
        hide c3
        hide mc
        hide darkenmc
        show c3 mask neutral
        ""
        hide c3
        show c3 smile
        with dissolve
        ""
        hide c3
        show mc blush at left_pos
        show c1 scared at right_pos
        "[player_name] & Doherty" "!!!"

        hide mc
        hide c1
        show c3 grateful
        "Sh-angk... yiu--!"

        hide c3
        show c1 smile
        d "Wow, she looks prettier than I could've ever been."

        hide c1
        show c1 smile at left_pos
        show c2 confused at right_pos
        b "What happened? Did she take of her mask? Dammit I wish I could see her!"

        hide c1
        hide c2
        show mc smile at left_pos
        show c3 smile at right_pos
        show darkenc3 at right_pos
        "I sign to her again"
        p "So, do you want to find a way out of here, with us?"
        hide c3
        show c3 serious at right_pos
        "She wrote down on her notebook, which I then read out."
        hide mc
        hide darkenc3
        show mc confused at left_pos
        show darkenmc at left_pos
        c "There is no exit for me. I am stuck here. Maybe there is an exit for you. I will help you three!"
        hide mc
        hide darkenmc
        hide c3
        show c2 confused at left_pos
        show c1 confused at right_pos
        show mc confused
        "Everyone " "Huh?"
        hide c1
        hide c2
        p "What do you mean by that, Clara?"

        hide mc
        show c2 serious
        b "Could it be that she knew why she's here in the first place?"

        hide c2
        show c1 serious

        "Doherty starts to sign to her"
        d "Do you remember anything about your past or how you got here?"

        hide c1
        show c3 neutral
        "Clara nods"
        
        scene bgblack
        "Before we could ask any more questions, the door opened."
        "Fearing it might close in just a few moments, I grab Clara's hand, Doherty grabs Beet's hand, and the four of us rush towards the door."
        ""
        "As expected, the door closed behind us."
        "We barely managed to escape."

        jump final_chapter



label bad_ending_clara:
    scene bgdefault
    show c3 mask neutral
    with fade

    "Clara wrote something in her notebook."
    "She then passed the notebook to us."

    hide c3
    show mc sad at left_pos
    show c1 serious at right_pos
    p "\"I'm... sorry..?\" Why?"
    "We then look back towards Clara, her pen in her hand, up against her neck."
    hide mc
    hide c1
    show mc shocked at left_pos
    show c1 shocked at right_pos
    "[player_name] & Doherty" "CLARA NO!"

    scene bgblack
    "We were too late. She stabbed herself in the throat. It didn't kill her instantly, she died painfully and slowly. There was nothing we could've done. There were no medical equipment nearby."

    b "What happened?"

    "-BAD ENDING-"
    "Tip: Try to be nicer to Clara"

    jump continue_ch3


label final_chapter:
    scene bgdefault
    with dissolve
    "While walking, I asked her about the details of her memories. What brought us here."
    
    show c3 neutral
    "Clara signed while also struggling to say what she's signing out loud."
    c "You know my story, right? All that bullying never stopped. I gave up."
    hide c3
    
    show c2 neutral at right_pos
    show c1 neutral at left_pos
    c "After that, here I am. I suddenly woke up, with him and her in the same room."
    
    show mc shocked
    p "Holy shit!"

    hide mc
    "I then turn towards Doherty and Beet who doesn't seem that suprised."

    hide c1
    hide c2

    show mc worried
    "Both of you knew?"

    show darkenmc
    show c1 worried at left_pos
    show c2 neutral at right_pos
    show darkenc2 at right_pos

    d "Maybe I just forgot. But that doesn't seem unbelievable. I've always wanted to end my suffering. I just... don't recall it ever happening. I guess it happened already."

    hide darkenc2
    show darkenc1 at left_pos

    b "What? So we're here because we died? Ohh thank makes sense now, how we're never hungry or thirsty, how it feels like it's been a long time, and yet nothing seemed to have changed."

    show darkenc2 at right_pos
    hide mc
    show mc cry 
    hide darkenmc

    p "...No...There's no way. I haven't died yet! I'm sure of it."

    hide c1
    hide c2
    hide mc
    hide darkenc1
    hide darkenc2

    show c3 worried

    c "Hey, it's okay. Maybe you're brought here to help us find peace."

    hide c3
    show c1 smile at left_pos
    show c2 smile at right_pos
    show darkenc2 at right_pos

    d "Yeah, look at me. I didn't trust you, or anyone else before for what they've done to me. And yet, here we are. You've helped me overcome my struggles."

    hide darkenc2
    show darkenc1 at left_pos
    b "That's right! You helped me go through my frustration of not being able to accept my newfound disability. Well, even if it was because our lives were on the line. Or \"lives\" I should say."

    hide darkenc1
    hide c2
    show c3 smile at right_pos
    d "And I'm sure you've shown Clara that there are people who will still care and be there for her, even if her voice is weird or whatever."
    hide c3
    hide c1
    show c1 smile
    d "You're the only one who showed us all of that."
    
    hide c1
    show mc grateful 
    "Sobbing."
    p "You guys... Thank you."

    scene final_room
    with fade

    "We arrived at what looks to be the final room in this tower. There are no more doors, no more stairs. Just an altar and a strange symbol on the floor. This might be the way out."

    show mc serious

    p "This looks like the end. That altar is similar to the one I found when I first started moving."
    p "This states \"true friends surround those who yearn to reach some place greater than this\"."

    hide mc
    show c2 smile
    b "I'm guessing we hold hands and surround you, and then you'll just... teleport back to the real world?"

    hide c2
    show c2 smile at right_pos
    show darkenc2 at right_pos
    show mc worried at left_pos

    p "...But I just made friends in you guys... I don't want to leave you here."

    hide c2
    hide darkenc2
    show c1 smile at right_pos
    show darkenmc at left_pos

    d "I hope when you die of old age, or whatever natural causes that will cause your death, you have the chance to go back here with us. And don't worry, we'll always be here anyway."

    scene bgblack
    with fade
    "Doherty, Betelgeuse and Clara hold hands and surrounds me. A few moments later, a bright beam appeared from the ground, engulfing me."

    scene final_room
    show mc grateful
    with dissolve

    "Sobbing"
    p "I will miss you guys"

    show c3 smile
    show c1 smile at left_pos
    show c2 smile at right_pos
    "..."
    "Everyone " "We will miss you too. May we meet again some day."

    show darkenc3
    show darkenc1 at left_pos
    b "But not too soon, I hope!"

    hide c1
    hide c2
    hide c3
    hide darkenc1
    hide darkenc3
    show mc grateful

    "We have a little giggle."
    show mc grateful at left_pos 
    show c3 grateful at right_pos
    "As I was about to teleport, Clara suddenly gave me a hug"

    hide mc
    hide c3
    show c1 smile at left_pos
    show c2 smile
    show c3 grateful at right_pos
    "Everyone else followed."
    "These people..."

    scene bgblack
    with dissolve
    scene doherty
    with dissolve
    "Doherty, gave up by slicing his throat with a shard of broken glass from a mirror in his room."

    scene bgblack
    with dissolve
    scene beet
    with dissolve
    "Betelgeuse, gave up by jumping off of his office building's highest floor."
    
    scene bgblack
    with dissolve
    scene clara
    with dissolve
    "And Clara, gave up by puncturing her neck with her pen in front of her bullies at school."

    scene bgblack
    with dissolve
    "Nobody helped them."
    "Nobody cared for them."

    scene player
    with dissolve
    "What am I doing?"
    "Why am I giving up?"
    "My life still has meaning."
    "I can help people like them."
    "I won't let my bi-polar disorder get the best of me!"

    jump credits
    return