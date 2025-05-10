# file: script.rpy

define e = Character("???")
define p = Character("[player_name]")
define d = Character("Doherty")
define b = Character("Betelgeuse")

image darkenmc = "mc_darken.png"
image darkenc1 = "C1_darken.png"
image darkenc2 = "C2_darken.png"

define left_pos = Position(xalign=0.0, yalign=1.0)
define right_pos = Position(xalign=1.0, yalign=1.0)

# Placeholder images
image bgblack = "#000"
image bgdefault = "BG_Default.png"
image bgdoor = "BG_door.png"
image bgaltar = "BG_door+sign.png"

image mcneutral = "MC_neutral.png"
image mcconfused = "MC_confused.png"
image mcserious = "MC_Serious.png"
image mcsmile = "MC_smile.png"
image mcsad = "MC_sad.png"
image mcscared = "MC_scared.png"
image mcshocked = "MC_shocked.png"
image mcworried = "MC_worried.png"
image mcblush = "MC_blush.png"

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
image braille_1 = "braille_puzzle_1.png"
image braille_2 = "braille_puzzle_2.png"
image hallway_split = "hallway_split.png" #Hall with two separate paths after puzzle 1
image bars = "ironbars_window_no_beet.png" #View between rooms through barred window from room right, without Beet being there
image bars_beet = "ironbars_window_beet.png" #View between rooms through barred window from room right, Beet being there
image room_left = "room_left.png" #View of Beet's POV, a hallway, an iron bar window on the left, the door they came from on the far side of the room. Beet is looking at the camera, the camera is where the puzzle is at

image c2 confused = "C2_confused.png"
image c2 mask1 = "C2_mask1.png"
image c2 neutral = "C2_neutral.png"
image c2 sad = "C2_sad.png"
image c2 scared = "C2_scared.png"
image c2 serious = "C2_serious.png"
image c2 shocked = "C2_shocked.png"
image c2 smile = "C2_smile.png"
image c2 worried = "C2_worried.png"

image stone_piece = "stone_piece.png"
image flashbackc1 = "flashbackc1.png"
image flashbackc1bg = "flashbackc1bg.png"

# Variables
default player_name = "..."
default trust_c1 = 50
default aggression_c1 = 0
default mental_health_c1 = 100

default trust_c2 = 50
default aggression_c2 = 0
default mental_health_c2 = 100

default beet_mask_on = True
default beet_timer = 30.0

default avoided = True

label start:

    scene bgblack

    e "I’m alone, shrouded in darkness. I have no memory of who I am or how long I’ve been here. Days? Weeks? Months? I have no idea."
    e "I’m not hungry, not thirsty. I just know that I don’t belong here. I need to escape."

    $ player_name = renpy.input("What should I call myself?")
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Alex"  # default name

    e "I’ll call myself [player_name] from now on."

    scene bgdefault
    show mcneutral

    p "I stand up, looking around for clues, doors, exits, anything."

    show mcconfused
    p "Huh?"

    scene bgdoor
    show mcserious at left
    p "I see something, a dim light seeping through the cracks of what I assume is a door outside. I step closer."

    p "It’s not locked. I can get out of here."
    
    scene bgblack
    with fade
    pause 0.1

    scene bgaltar
    show mcserious at center
    p "What the hell? Just another room? Wait— that big-ass door might lead me outside!"

    p "Dammit! It’s locked. What the hell am I supposed to do now?"
    scene scenealtar
    show mcconfused
    p "What the hell is this thing?"
    scene scenealtar
    pause
    p "“Stand not alone, for the gate listens only to unity.”?" 
    show mcserious 
    p "I can’t NOT stand alone, there’s nobody else in this damn room!"
    scene bgdefault
    show mcsad
    "Getting desperate, I frantically look around the room for keys, hidden buttons, levers, anything."
    show mcserious
    "After losing hope, I look around the altar, trying to see what I could do with or to it."
    scene scenealtar
    scene bgaltar
    show mcshocked
    p "The massive door opened by itself, making a loud noise in the process."

    p "A few moments later, the door I came from aggressively shuts."
    show mcscared
    p "I panic and run straight outside."

    scene bgblack
    p "It’s a hallway, dimly lit by candles on the wall. How the hell did I get here? And more importantly, how the hell do I get out?"

    jump chapter1_continue

label chapter1_continue:
    scene bgdefault
    show c1 mask1
    p "As I’m walking, I notice a person chained to the wall. Feminine outfits with a tall body and wide shoulder. A girl? A boy? I can’t tell."
    hide c1 mask1
    show mcneutral
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
    show mcserious at left_pos
    show c1 mask2 at right_pos

    show darkenmc at left_pos zorder 10
    e "GET AWAY FROM ME!"
    hide darkenmc

    show darkenc1 at right_pos zorder 10
    show mcshocked at left_pos
    p "Holy shit!"
    hide mcshocked
    show mcserious at left_pos
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
        "Hey, I’m here to help.":
            $ trust_c1 += 10
            $ aggression_c1 -= 5
            show darkenc1 at right_pos zorder 10
            show mcworried  at left_pos
            p "Hey, I’m here to help."
            hide darkenc1
            show mcworried  at left_pos
            show darkenmc at left_pos zorder 10
            e "Help? Like the others who PUT me in this situation?"
            hide darkenmc

    show mcserious at left_pos
    show darkenc1 at right_pos zorder 10
    p "Look, I have no memory of getting here, but I’m sure as hell would like to leave this god forsaken place."
    p "If you want, I can take you with me, but I need your help in doing so. Look, I can find the keys to unshackle you. It must be around here somewhere, right?"
    hide darkenc1

    show c1 mask2 at right_pos
    show darkenmc at left_pos zorder 10
    e "No thanks. It’s better for me here anyway. I don’t belong anywhere else."
    hide darkenmc

    if avoided:
        menu:
            "What do you mean by that?":
                $ aggression_c1 -= 5
                show mcserious at left_pos
                show darkenc1 at right_pos zorder 10
                p "What do you mean by that?"
                hide darkenc1
            "But I need your help, come on!":
                $ trust_c1 -= 5
                $ aggression_c1 += 10
                show mcserious at left_pos
                show darkenc1 at right_pos zorder 10
                p "But I need your help, come on!"
                hide darkenc1
        show mcworried at left_pos
        show darkenmc at left_pos zorder 10

    else:
        menu:
            "Okay then, suit yourself.":
                $ trust_c1 -= 10
                $ mental_health_c1 -= 10
                show mcneutral at left_pos
                show darkenc1 at right_pos zorder 10
                p "Okay then, suit yourself."
                hide darkenc1
                jump altar_poem_room
            "What do you mean by that?":
                $ aggression_c1 -= 5
                show mcserious at left_pos
                show darkenc1 at right_pos zorder 10
                p "What do you mean by that?"
                hide darkenc1
            "But I need your help, come on!":
                $ trust_c1 -= 5
                $ aggression_c1 += 10
                show mcserious at left_pos
                show darkenc1 at right_pos zorder 10
                p "But I need your help, come on!"
                hide darkenc1
        show mcworried at left_pos
        show darkenmc at left_pos zorder 10

    if not avoided:
        e "Just go."
        hide darkenmc

        p "..."
        hide c1 mask2
        hide mcworried
        jump altar_poem_room
    
    elif avoided:
        jump second_convo_doherty

label altar_poem_room:
    scene bgdefault
    show mcneutral
    p "I continue, finding another room, eerily similar to the one before. But there’s only one thing in that room, another altar."
    scene scenepuzzle1
    show mcconfused
    p "On top of it, instead of something glowing, it’s a poem, but it looks unfinished."
    hide mcconfused
    pause
    show mcserious at left
    p "Masks are made to hide shame"
    p "For someone unable to find themselves"
    p "Though my appearance doesn’t match my name"
    p "I am …?"
    show mcconfused at left
    p "What the shit is this? This looks like someone deliberately removed the last part. But why? What does this mean?"
    show mcserious
    p "Looking around, I saw nothing. And there’s nothing else to check but another big door. I assume the altar is the key to unlocking the big door. Finding no other clues, I walked back to the chained stranger."

if not avoided:
    jump second_convo_doherty

elif avoided:
    jump approach_doherty

define k = Character("Kid")
define m = Character("Lady")

label second_convo_doherty:
    scene bgdefault
    show mcneutral at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos  # MC speaks, darken Doherty

    if not avoided:
        p "Hey, I know you asked me to leave you alone, but I’m quite stuck. Can you please help me out here?"

    elif avoided:
        p "Look, I've been in that room already. There's this weird altar and this huge door but I can't find a way to get it to open. Please help me out."

    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    e "Why ask me? There’s nothing someone like me could do to help you."
    hide darkenmc
    show mcconfused at left_pos
    show darkenc1 at right_pos  # MC speaks, darken Doherty
    p "(I look at… him? her? I still don’t know. Their voice is masculine, but their appearance is very feminine. Wait, 'my appearance doesn’t match my name'.)"
    show mcneutral at left_pos
    p "What’s your name?"
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    e "Why do you want to know? Is it because it’s hard to identify me?"
    hide darkenmc
    show mcneutral at left_pos
    show darkenc1 at right_pos  # MC speaks, darken Doherty
    menu:
        "It’s a bit weird talking to someone without knowing their name, you know?":
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
        "It’s just your name, why can’t you answer it?":
            $ trust_c1 -= 10
            $ aggression_c1 += 10
            $ sit_choice = "opposite"

            show darkenmc at left_pos
            e "..."
            e "Screw you."
            hide darkenmc
            show mcconfused at left_pos
            show darkenc1 at right_pos
            p "What the hell?"
            hide mcconfused
            hide darkenc1

        "It’s okay, I don’t wanna force you.":
            $ trust_c1 += 10
            $ aggression_c1 -= 5
            $ mental_health_c1 += 5
            $ sit_choice = "beside"
    show darkenmc at left_pos  # Doherty speaks, darken MC
    show c1 mask1 at right_pos
    d "Doherty. I’m a he."
    hide darkenmc
    show darkenc1 at right_pos  # Doherty speaks, darken MC
    p "Your name is Doherty?"
    hide darkenc1

    if sit_choice == "opposite":
        p "(I stood opposite of him.)"
    elif sit_choice == "beside":
        p "(I sit down beside him.)"

    show darkenc1 at right_pos
    p "Do you know how long you’ve been here?"
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    d "I don’t. I don’t care. I want to be here. I hate everything and everyone else."
    hide darkenmc
    show darkenc1 at right_pos  # MC speaks, darken Doherty
    show mcconfused at left_pos
    p "What do you mean by ‘everyone else’?"
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    d "I mean everyone else. Everyone made me this way. They built me, and now they throw me out. It’s like I’m some heartless doll they play with and discard whenever they please."
    hide darkenmc
    show darkenc1 at right_pos  # MC speaks, darken Doherty    
    p "They… ‘built’ you?"
    show darkenmc at left_pos  # Doherty speaks, darken MC
    show stone_piece
    hide darkenmc
    show mcconfused at left_pos
    p "Wha-...?"
    "While talking, I noticed the piece from the altar in the other room is right next to Doherty. He then passed me it."
    show mcsmile at left_pos
    menu:
        "Thank you.":
            $ aggression_c1 -= 5
        "You had this all this time? Why didn’t you tell me?":
            $ aggression_c1 += 10
    hide darkenc1
    show darkenmc at left_pos  # Doherty speaks, darken MC
    d "..."

    scene bgdefault
    show mcneutral
    p "(I walk back to the other room with the stone in hand. I then place the stone on the missing part of the poem.)"
    scene scenepuzzle1solved
    pause
    p "\"I am more than an empty shell.\""
    p "(The altar moves to the side, behind it lies a key. I take it and rush to the door.)"
    show mcneutral
    menu:
        "Do I check on Doherty?":
            jump going_back_to_doherty
        "Do I just open the door?":
            jump try_key_on_door

label try_key_on_door:
    scene bgdoor
    show mcserious
    p "(I try the key on the doors.)"
    p "Fuck! It doesn’t fit the hole."
    jump going_back_to_doherty

label going_back_to_doherty:
    scene bgdefault
    show mcneutral at center
    "I turn back to Doherty."
    hide mcneutral
    show mcsmile at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos
    p "I think I found the key to unlocking your shackles."
    hide darkenc1
    show darkenmc at left_pos
    d "Take it away. I don’t need it."
    hide darkenmc
    show darkenc1 at right_pos
    show mcworried at left_pos
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
    m "GIRLS WEAR GIRLS’ CLOTHING! And you are a girl, aren’t you?"
    k "B-but… I’m a—"
    scene bgblack
    "*SLAP*"
    show flashbackc1
    m "YOU ARE A GIRL, AREN’T YOU!?"
    k "Sobbing, Yes, I am."
    m "Good girl. Now, what’s your name?"
    k "...Doherty."
    scene bgblack
    "*SLAP*"
    show flashbackc1
    m "DOHERTY IS A BOY’S NAME! Your name is ‘Dorothy’, okay?"
    d "Nods"
    m "Good. You’ll meet your new father soon enough, my dear."

    "What the fuck am I experiencing?!"
    scene bgdefault
    show mcworried at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos
    "Panting"
    p "Doherty… You never wanted this, did you? To be like this?"
    hide darkenc1
    d "(Shakes head)"
    show darkenc1 at right_pos

    p "So why don’t you just… rebel against them?"
    hide darkenc1
    show darkenmc at left_pos
    d "I tried."
    scene bgdefault
    "Doherty begins to unbutton his dress."
    show mcblush
    p "W-what are you??!"
    hide mcblush
    "Doherty shows his bruised back, full with scars."
    d "She won’t let me."
    show mcworried at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos
    p "Holy shit…"
    hide darkenc1
    show darkenmc at left_pos
    d "I’ve always hated the way I am. I can’t be a boy because I would get hit by my mother. But every time I put on a dress, my stepfather would touch me. Nothing was ever the right thing. I don’t know who I am."
    hide darkenmc
    menu:
        "Let’s just get out of here, together. Forget your mother.":
            $ trust_c1 += 10
            $ mental_health_c1 += 10
            $ ending_choice = "good"
            show mcworried at left_pos
            show darkenc1 at right_pos
            p "Let’s just get out of here, together. Forget your mother."
            show darkenmc at left_pos
            hide darkenc1
            d "I-"

            hide darkenmc
            d "..."
            show darkenmc

        "I’m so sorry. I could never imagine the pain you’ve endured…":
            $ trust_c1 += 10
            $ aggression_c1 -= 10
            $ mental_health_c1 += 10
            $ ending_choice = "good"
            show mcsad at left_pos
            show darkenc1 at right_pos
            p "I’m so sorry. I could never imagine the pain you’ve endured…"
        "The past is in the past. Now let’s go!":
            $ mental_health_c1 -= 10
            $ ending_choice = "bad"
            show mcsmile at left_pos
            show darkenc1 at right_pos
            p "The past is in the past. Now let’s go!"



    if ending_choice == "good":
        show mcworried at left_pos
        show c1 mask1 at right_pos
        show darkenmc at left_pos
        d "I don’t have siblings. I don’t remember my father. All I know is torture. Everyone treats me like garbage. Like I’m some sort of toy to dress up and humiliate."
        hide darkenmc
        show darkenc1 at right_pos
        p "Oh my god… Doherty, I—"
        hide darkenc1
        show darkenmc at left_pos
        d "It doesn’t matter anymore. I’m here, and this is where I want to be."
        hide darkenmc 
        show darkenc1 at right_pos
        show mcsmile at left_pos
        p "But we can go away, be free. Be who you are without judgment. Please, join me."
    
    elif ending_choice == "bad":
        d "..."
    
    if trust_c1 > 50 and aggression_c1 < 50 and mental_health_c1 > 60:
        scene bgdefault
        show c1 mask1 at right_pos
        show mcsmile at left_pos
        show darkenmc at left_pos
        d "..."
        show c1 sad at right_pos
        "Doherty takes off his mask"
        show c1 smile at right_pos
        d "Let’s go."
        "(We both walk to the door. It opens by itself.)"
        jump chapter1_complete

    elif aggression_c1 >= 5:
        scene bgblack
        p "(I waited for an hour, then sat down. Suddenly, I felt a stinging pain in my neck. Doherty with a glass shard in hand, bloody.)"
        scene bgdefault
        show c1 mask2
        d "IT’S SO EASY FOR YOU! YOU DON’T EVEN CARE ABOUT ME!"
        jump bad_ending_1

    elif mental_health_c1 <= 40:
        scene bgblack
        "(I waited for an hour, I then sat down, waiting for Doherty to come. I closed my eyes for a moment.)"
        "(A few moments went by, then Doherty came into the room with a shard of glass in his hand.)"
        scene bgdefault
        show mcworried at left_pos
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

    "Eventually, we reach a new chamber. It’s different. Two large doors stand on opposite walls. Between them—a strange console embedded into the stone."

    scene bg2door with dissolve
    "Next to the console, we see someone. Just sitting still. Silent. Masked—like Doherty once was."

    scene bgdefault
    show mcworried at left
    show c2 neutral at right
    if beet_mask_on:
        show c2 mask1 at right
    show darkenc2 at right

    p "Hey–"

    show darkenmc at left
    show c2 shocked at right
    

    e "Huh??"

    show mcneutral at left
    show c1 neutral at right
    p "I’m [player_name], and this is Doherty. We’re not here to hurt you."

    hide c1 neutral
    show darkenmc at left
    show c2 smile at right
    if beet_mask_on:
        show c2 mask1 at center

    e "Oh… My name is Betelgeus, but you can call me Beet."
    b "What are you doing here? I thought I was the only one left."

    hide darkenmc
    hide mcworried
    hide mcneutral
    show c1 neutral at left
    d "We’re trying to escape."

    b "Escape? From where? To where?"

    hide c1 neutral
    show mcworried at left
    p "I don’t remember much... but I definitely didn’t walk into this dungeon on purpose."

    hide darkenc2
    show darkenmc at left
    show c1 neutral at right
    d "Same. I’ve been here longer than I can count."

    hide darkenmc
    show darkenc1 at right

    p "Wait... what do you mean, 'the only one left'?"

    hide darkenc1
    hide c1 neutral

    b "There used to be others. Three of us, I think. I don’t remember names. Maybe I forgot them."

    hide darkenmc
    hide mcworried
    show c1 worried at left
    show c2 neutral at right
    show darkenc2 at right

    d "I might’ve been one of them."

    show darkenc1 at left
    hide darken c2

    b "Maybe... It’s been so long. But you two—hearing your voices—it’s nice."

    hide darkenc1
    hide c1 worried
    show mcworried at left
    show darkenc2 at right
    p "Yeah, after that long being by yourself, I could imagine."

    menu:
        "But we need to get out of here. Do you not want to get out with us?":
            $ trust_c2 += 10
            $ aggression_c2 -= 10
            show darkenmc at left
            b "Haha... yeah. I want out. I don’t belong in this place."
            b "But what can I do to help?"

        "But I need to get out of here. So can you please help me?":
            $ aggression_c2 += 10
            show darkenmc at left
            b "..."
            b "Why should I help you again?"

    b "Besides, there’s not much a blind guy like me can do."
    hide darkenmc

    hide mcworried
    show c1 worried at left
    show darkenc2 at right
    d "Don’t say that. There’s a braille puzzle on the console. Maybe you can help."

    show darkenc1 at left
    show c2 neutral at right
    b "Braille...? Sorry—I never learned it."

    hide darkenc1
    hide c1 worried

    show mcshocked at left
    show darkenc2 at right
    p "What?"

    show darkenmc at left
    show c2 neutral at right
    b "Yeah. I only lost my sight recently. At least, I think it was recent. My memory’s foggy."

    show mcsad at left
    show darkenc2 at right
    p "What happened?"

    show darkenmc at left
    show c2 neutral at right
    b "I just remember... searing pain. My mother found me afterwards. She said I was lying in a pool of blood."

    show mcsad at left
    show c1 sad at right
    p "..."
    d "...That’s rough."

    hide c1 sad

    b "Since then, life’s been a blur. I can’t see anything. Not even light. Braille? I never got to learn. Couldn’t use it. Never needed to."

    show darkenmc at left
    show c1 sad at right
    d "That sounds... horrible."

    hide c1 sad
    show darkenmc at left
    show c2 neutral at right
    if beet_mask_on:
        show c2 mask1 at center

    b "Heh. You get used to it... or you try."

    menu:
        "We’ll figure it out together.":
            $ trust_c2 += 10
            $ aggression_c2 -= 5
            $ mental_health_c2 += 5
            show mcsmile at left
            show darkenc2 at right
            p "Even if you don’t know braille, we’ll figure it out together."
            show darkenmc at left
            show c2 smile at right
            if beet_mask_on:
                show c2 mask1 at center
            b "Thanks... really."

        "You could’ve just said you’re useless.":
            $ aggression_c2 += 15
            $ trust_c2 -= 15
            $ mental_health_c2 -= 10
            show mcserious at left
            show darkenc2 at right
            p "So you can’t help. Great."
            show darkenmc at left
            show c2 sad at right
            if beet_mask_on:
                show c2 mask1 at center
            b "...I didn’t ask for this."

        "Why don’t we learn braille together?":
            $ trust_c2 += 20
            $ aggression_c2 -= 5
            $ mental_health_c2 += 15
            show mcneutral at left
            show darkenc2 at right
            p "No use arguing. Let’s learn braille together."
            show darkenmc at left
            show c2 neutral at right
            if beet_mask_on:
                show c2 mask1 at center
            b "You mean it?"
            show mcsmile at left
            p "Yeah. We’ll learn together."

    show mcserious at left
    show darkenc2 at right
    p "We can describe it to you. You might notice something we miss."

    show darkenmc at left
    show c1 smile at right
    d "Totally worth a shot."

    show mcneutral at left
    show darkenc2 at right
    p "Alright, let’s give it a try."

    show darkenmc at left
    show c2 thinking at right
    if beet_mask_on:
        show c2 mask1 at center

    b "Alright. Where is this thing?"

    jump braille_puzzle_1

label braille_puzzle_1:
    scene braille_puzzle_1
    show mcneutral at left
    show c1 neutral at right
    if beet_mask_on:
        show c2 mask1 at center
    else:
        show c2 neutral at center

    p "Looks like this console uses braille to display a four-digit code. There’s a hint carved into the stone wall nearby."

    d "It's a number sequence. Should be easy if we follow the guide."

    b "Alright... I’ll try to feel it out too."

    $ braille_answer = renpy.input("What’s the 4-digit pin?", length=4)
    $ braille_answer = braille_answer.strip()

    if braille_answer == "7302":
        p "That worked!"
        $ trust_c2 += 10
        $ mental_health_c2 += 5
        scene bg2door
        hide mcneutral
        hide c1 neutral
        if beet_mask_on:
            hide c2 mask1
        else:
            hide c2 neutral
        show mcsmile at left
        show c1 smile at right
        if beet_mask_on:
            show c2 mask1 at center
        else:
            show c2 smile at center

        p "The doors… they’re opening."
        b "Did we do it?"
        jump hallway_split
    else:
        p "That’s not right..."
        jump braille_puzzle_1_retry

label braille_puzzle_1_retry:
    menu:
        "Try again":
            jump braille_puzzle_1
        "Give up":
            hide mcneutral
            hide c1 neutral
            if beet_mask_on:
                hide c2 mask1
            else:
                hide c2 neutral
            p "(We’ll never get out like this...)"
            $ mental_health_c2 -= 10
            jump stuck_scene

label hallway_split:
    scene hallway_split
    show mcserious at left
    show c1 worried at right
    p "There’s two paths now…"

    show darkenmc at left
    if beet_mask_on:
        show c2 mask1 at right
    else:
        show c2 neutral at right

    b "Let’s not split up. I’ll stay close."

    "The group steps toward the right door."

    scene bgblack
    hide mcserious
    hide c1 worried
    if beet_mask_on:
        hide c2 mask1
    else:
        hide c2 neutral

    "A sudden slam echoes. The door slams shut behind [player_name] and Doherty—Beet is left on the other side."

    scene bars
    show mcshocked at left
    show c1 shocked at right
    p "Beet!?"

    show darkenmc at left
    if beet_mask_on:
        show c2 mask1 at right
    else:
        show c2 shocked at right

    b "What the—!? The door just slammed on me!"

    hide darkenmc
    show mcworried at left
    show darkenc2 at right
    p "Damn it!"

    hide darkenc2
    show c1 serious at right
    d "There’s a window—there!"

    scene bars
    show mcshocked at left
    show c1 scared at right
    p "Beet! You good?"

    scene bg2door
    hide mcshocked
    hide c1 scared
    if beet_mask_on:
        show c2 mask1 at center
    else:
        show c2 neutral at center

    b "Yeah… just shaken."
    b "I feel another door open... I’ll check it."

    scene bars_beet
    show mcserious at left
    show c1 worried at right
    p "We can see you through this window. It’s barred."

    scene room_left
    hide mcserious
    hide c1 worried
    if beet_mask_on:
        show c2 mask1 at center
    else:
        show c2 neutral at center

    b "Heh. Guess I can’t see you back."

    scene bgblack
    hide c2 mask1
    hide c2 neutral
    "Another heavy slam. The left room’s door shuts tight behind him."

    scene bars_beet
    show mcshocked at left
    show c1 shocked at right
    p "...Wait."

    scene room_left
    if beet_mask_on:
        show c2 mask1 at center
    else:
        show c2 neutral at center

    b "...Did you hear that?"

    "Metal creaks above."

    scene bars_beet
    show mcshocked at left
    show c1 shocked at right
    show darkenc1 at right
    p "The ceiling! It’s moving!"

    show darkenmc at left
    show c1 scared at right
    hide darkenc1
    d "Both rooms are closing in!"

    scene room_left
    if beet_mask_on:
        show c2 mask1 at center
    else:
        show c2 scared at center

    b "Oh shit! I need to move—now!"

    jump beet_solo_puzzle

label beet_solo_puzzle:

    if trust_c2 >= 30 and aggression_c2 <= 40:
        scene braille_2
        if beet_mask_on:
            show c2 mask1 at center
        else:
            show c2 serious at center

        b "(You know what... I trust them now.)"
        b "(If I'm going to survive this... I want to do it as me.)"

        b "Here goes nothing."
        $ beet_mask_on = False
        hide c2 mask1
        show c2 neutral at center

        "For the first time, you see him—not as a prisoner or a stranger, but as a person."

        b "Okay... Let’s do this."

    else:
        scene braille_2
        if beet_mask_on:
            show c2 mask1 at center
        else:
            show c2 serious at center

        b "(Okay… I’m on my own now. No hints. Just me and this panel.)"

        if trust_c2 < 30 or aggression_c2 > 40:
            b "...You know what? No."
            b "And you know what else? I'm keeping the mask on."
            b "You never saw me—not really—and I think I prefer it that way."
            b "You guys aren’t nice at all. I don’t think I’m gonna help you."
            b "Figure it out yourselves."

            d "Wait—Beet!"

            scene bgblack
            "Without Beet’s help, the console stayed locked. The ceiling kept falling..."
            "And we couldn’t escape."

            jump bad_ending_beet_refuses

        b "(Focus. Breathe. You can do this.)"

    $ attempt_left = 3

    label beet_input_loop:
        $ beet_input = renpy.input("Enter the 4-digit code:", length=4)
        $ beet_input = beet_input.strip()

        if beet_input == "9581":
            b "I did it!"
            $ trust_c2 += 10
            $ mental_health_c2 += 10
            scene bg2door
            show mcsmile at left
            show c1 smile at right
            show c2 smile at center
            b "The door opened... I’m safe."
            jump beet_survives
        else:
            $ attempt_left -= 1
            b "Dammit! It’s wrong!"
            if attempt_left <= 0:
                scene bgblack
                "The ceiling crushed down before he could try again."
                jump bad_ending_beet_crushed
            else:
                b "I have [attempt_left] tries left!"
                jump beet_input_loop

label beet_survives:
    scene bgdefault
    show mcsmile at left
    show c1 smile at right
    show c2 smile at center
    p "Beet! You’re okay!"
    b "Heh… barely."
    return

label bad_ending_beet_refuses:
    "-BAD ENDING: YOU LOST HIS TRUST-"
    return

label bad_ending_beet_crushed:
    "-BAD ENDING: BEET WAS CRUSHED-"
    return