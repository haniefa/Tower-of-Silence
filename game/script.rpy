# file: script.rpy

define e = Character("???")
define p = Character("[player_name]")
define d = Character("Doherty")

image darkenmc = "mc_darken.png"
image darkenc1 = "c1_darken.png"

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

image stone_piece = "stone_piece.png"
image flashbackc1 = "flashbackc1.png"
image flashbackc1bg = "flashbackc1bg.png"

# Variables
default player_name = "..."
default trust = 50
default aggression = 0
default mental_health = 100

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
    show mcserious
    p "I see something, a dim light seeping through the cracks of what I assume is a door outside. I step closer."

    p "It’s not locked. I can get out of here."

    scene bgaltar
    show mcserious
    p "What the hell? Just another room? Wait— that big-ass door might lead me outside!"

    p "Dammit! It’s locked. What the hell am I supposed to do now?"
    scene scenealtar
    show mcconfused
    p "What the hell is this thing?"
    scene scenealtar
    pause
    p "“Stand not alone, for the gate listens only to unity.”?" 
    show mcserious 
    p "I can’t not stand alone, there’s nobody else in this damn room!"
    scene bgdefault
    show mcsad
    p "Getting desperate, I frantically look around the room for keys, hidden buttons, levers, anything."
    show mcserious
    p "After losing hope, I look around the altar, trying to see what I could do with or to it."
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
            jump approach_doherty
        "Avoid (Will approach later)":
            $ aggression += 10
            jump avoid_doherty

label avoid_doherty:
    scene bgdefault
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
            $ trust -= 10
            $ aggression += 10
            $ mental_health -= 5
            show darkenc1 at right_pos zorder 10
            p "What the hell is your problem!?"
            hide darkenc1
            show darkenmc at left_pos zorder 10
            e "What is YOUR problem?"
            hide darkenmc
        "Hey, I’m here to help.":
            $ trust += 10
            $ aggression -= 5
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

    menu:
        "Okay then, suit yourself.":
            $ trust -= 10
            $ mental_health -= 10
            show mcneutral at left_pos
            show darkenc1 at right_pos zorder 10
            p "Okay then, suit yourself."
            hide darkenc1
        "What do you mean by that?":
            $ aggression -= 5
            show mcserious at left_pos
            show darkenc1 at right_pos zorder 10
            p "What do you mean by that?"
            hide darkenc1
        "But I need your help, come on!":
            $ trust -= 5
            $ aggression += 10
            show mcserious at left_pos
            show darkenc1 at right_pos zorder 10
            p "But I need your help, come on!"
            hide darkenc1
    show mcworried at left_pos
    show darkenmc at left_pos zorder 10
    e "Just go."
    hide darkenmc

    p "..."
    hide c1 mask2
    hide mcworried
    jump altar_poem_room

label altar_poem_room:
    scene bgdefault
    show mcneutral
    p "I continue, finding another room, eerily similar to the one before. But there’s only one thing in that room, another altar."
    scene scenepuzzle1
    show mcconfused
    p "On top of it, instead of something glowing, it’s a poem, but it looks unfinished."
    hide mcconfused
    pause
    show mcserious
    p "Masks are made to hide shame"
    p "For someone unable to find themselves"
    p "Though my appearance doesn’t match my name"
    p "I am …?"
    show mcconfused
    p "What the shit is this? This looks like someone deliberately removed the last part. But why? What does this mean?"
    show mcserious
    p "Looking around, I saw nothing. And there’s nothing else to check but another big door. I assume the altar is the key to unlocking the big door. Finding no other clues, I walked back to the chained stranger."

    jump second_convo_doherty

define k = Character("Kid")
define m = Character("Lady")

label second_convo_doherty:
    scene bgdefault
    show mcneutral at left_pos
    show darkenc1 at right_pos  # MC speaks, darken Doherty
    show c1 mask1 at right_pos

    p "Hey, I know you asked me to leave you alone, but I’m quite stuck. Can you please help me out here?"
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
            $ trust += 10
            $ aggression -= 5
        "Yes, actually. You have a very manly voice, yet such a soft and feminine appearance":
            $ mental_health -= 10
        "I need it for the poem thing in the other room, I guess.":
            $ trust -= 10
            $ aggression -= 5
            $ mental_health -= 5
    hide darkenc1
    e "..."

    menu:
        "Sit down beside them":
            $ trust += 10
            $ sit_choice = "beside"
        "It’s just your name, why can’t you answer it?":
            $ trust -= 10
            $ aggression += 10
            $ sit_choice = "opposite"
        "It’s okay, I don’t wanna force you.":
            $ trust += 10
            $ aggression -= 5
            $ mental_health += 5
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
    show mcsmile at left_pos
    menu:
        "Thank you.":
            $ aggression -= 5
        "You had this all this time? Why didn’t you tell me?":
            $ aggression += 10
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
    p "I turn back to Doherty."
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
    p "(I got knocked back and hit my head against the wall. I woke up in another room, dizzy.)"
    pause
    scene flashbackc1bg
    p "Huh? What the hell? Where am I? Why is everything so… feminine?"

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
    d "nods"
    m "Good. You’ll meet your new father soon enough, my dear."

    p "What the fuck am I experiencing?!"
    scene bgdefault
    show mcworried at left_pos
    show c1 mask1 at right_pos
    show darkenc1 at right_pos
    p "Panting, Doherty… You never wanted this, did you? To be like this?"
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
    "W-what are you??!"
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
            $ trust += 10
            $ mental_health += 10
            $ ending_choice = "good"
            show mcworried at left_pos
            show darkenc1 at right_pos
            p "Let’s just get out of here, together. Forget your mother."
        "I’m so sorry. I could never imagine the pain you’ve endured…":
            $ trust += 10
            $ aggression -= 10
            $ mental_health += 10
            $ ending_choice = "good"
            show mcsad at left_pos
            show darkenc1 at right_pos
            p "I’m so sorry. I could never imagine the pain you’ve endured…"
        "The past is in the past. Now let’s go!":
            $ mental_health -= 10
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


    

    if trust > 50 and aggression < 50 and mental_health > 60:
        scene bgdefault
        show c1 smile at right_pos
        show mcsmile at left_pos
        d "Let’s go."
        p "(We both walk to the door. It opens by itself.)"
        jump chapter1_complete

    elif aggression >= 5:
        scene bgblack
        p "(I waited for an hour, then sat down. Suddenly, I felt a stinging pain in my neck. Doherty with a glass shard in hand, bloody.)"
        scene bgdefault
        show c1 mask2
        d "IT’S SO EASY FOR YOU! YOU DON’T EVEN CARE ABOUT ME!"
        jump bad_ending_1


label chapter1_complete:
    "-CHAPTER 1 COMPLETE-"
    return

label bad_ending_1:
    "-BAD ENDING 1-"
    "Tip: try to approach him with empathy."
    return
