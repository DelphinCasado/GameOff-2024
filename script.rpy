
#define e = Character("OLD BOOKCASE")

###AUDIO  ##########################################
init python:
    renpy.music.register_channel('ambiance', "music")
define config.default_music_volume = 0.85
define config.default_sfx_volume = 0.85
define config.default_voice_volume = 0.85

###IMAGE DEFINE ##########################################
#backgrounds
image bgroom_01 = "bg/bg_room_01.png"
image bgclassroom = "bg/bg_classroom_01.png"
image bgteacherlounge = "bg/bg_teacherlounge_01.png"
image bgmovie = Movie(size=(1920,1080), play="images/movies/grainy_background_01.webm")

#characters
 ############################################################################
image mc backl:
    "chr/chr_mc_A_01.png"
    pause 0.75
    "chr/chr_mc_A_02.png"
    pause 0.75
    repeat
image mc backr:
    im.Flip("chr/chr_mc_A_01.png", horizontal=True)
    pause 0.75
    im.Flip("chr/chr_mc_A_02.png", horizontal=True)
    pause 0.75
    repeat
image mc frontl:
    "chr/chr_mc_B_01.png"
    pause 0.75
    "chr/chr_mc_B_02.png"
    pause 0.75
    repeat
image mc frontr:
    im.Flip("chr/chr_mc_B_01.png", horizontal=True)
    pause 0.75
    im.Flip("chr/chr_mc_B_02.png", horizontal=True)
    pause 0.75
    repeat
image mc captured = "chr/chr_mc_captured_01.png"
image mcreflection = "chr/chr_mc_reflection_01.png"

#ui
image icon_hlt = "ui/icon_01.png"
image icon_snt = "ui/icon_02.png"
image icon_key = "ui/icon_03.png"
image icon_fir = "ui/icon_04.png"

#
default txt_colo_01 = "#ffad5a"
default check_colo_01 = "#a99e94"
default hlt_colo_01 = "#ab3032"
default snt_colo_01 = "#55c0a8"
default key_colo_01 = "#9094a4"
default fir_colo_01 = "#cb6731"
# SLOTS
##############################################################
transform entrance_slot_01:
    xpos 350
    ypos 580

# VARIABLES DEFINE
##############################################################
default  stat_str = 3
default  stat_mnd = 5
default  stat_dex = 6
default  stat_lck = 6
default  stat_hlt = 10
default  stat_snt = 10
default  stat_key = 0
default  stat_fir = 0
#####################
default event1 = True
default event2 = True
default event3 = True
default event4 = True
default eventstar = True

default  stat_star = 0

########################################################
############### GAME START #############################
########################################################
label start:
    #$ config.rollback_enabled = False
    # scene black
    # pause 2
    #scene bgmovie
    jump firstroom_01

########################################################
############### SUBROUTINES ############################
########################################################

# EVENT RESET
##############################################################
label room_events_reset:
    $ event1 = True
    $ event2 = True
    $ event3 = True
    $ event4 = True
    $ eventstar = True
    return
# DICE ROLLS
##############################################################
label roll_str:
    $ dice = renpy.random.randint(1, 10)
    if dice <= stat_str:
        $ success = True
    else:
        $ success = False
    return
label roll_mnd:
    $ dice = renpy.random.randint(1, 10)
    if dice <= stat_mnd:
        $ success = True
    else:
        $ success = False
    return
label roll_dex:
    $ dice = renpy.random.randint(1, 10)
    if dice <= stat_dex:
        $ success = True
    else:
        $ success = False
    return
label roll_lck:
    $ dice = renpy.random.randint(1, 10)
    if dice <= stat_lck:
        $ success = True
    else:
        $ success = False
    return

# HEALTH LOSS
##############################################################
label hlt_loss:
    play audio "sfx/sfx_health_01.mp3"
    pause 0.1
    play audio "sfx/sfx_hurt_01.mp3"
    show screen stat_overlay_hlt
    pause 0.01
    hide screen stat_overlay_hlt
    with Dissolve(0.5)
    if stat_hlt < 0:
            $stat_hlt = 0
    if stat_hlt <= 0:
        jump gameover
    return
label snt_loss:
    play audio "sfx/sfx_sanity_01.mp3"
    show screen stat_overlay_snt
    pause 0.01
    hide screen stat_overlay_snt
    with Dissolve(0.5)
    if stat_snt < 0:
            $stat_snt = 0
    if stat_snt <= 0:
        jump gameover
    return
label choice_selected:
    play audio "sfx/sfx_ui_click_01.mp3"
    return

label stat_increase:
    play audio "sfx/sfx_stat_increase_01.mp3"
    show screen stat_overlay_01
    pause 0.01
    hide screen stat_overlay_01
    with Dissolve(0.5)
    return

label star_found:
    play audio "sfx/sfx_ui_star_01.mp3"
    $ eventstar = False
    $ stat_star += 1
    return

##################################################################
##################################################################

##TEST
label room_01_start:
    call room_events_reset
    scene temp1
    play music "mus/mus_room_01.mp3"
    show bgroom_01
    show mc backr at entrance_slot_01
    show screen stats_UI
    with fade
label room_01:
    call screen interact_button1
screen interact_button1:
    if event1 == True:
        imagebutton:
            xpos 0.2
            ypos 0.3
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("eventtest1")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event2 == True:
        imagebutton:
            xpos 0.8
            ypos 0.5
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("eventtest2")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"

label eventtest1:
    $ event1 = False
    show mc backl:
        xpos 400
        ypos 400
    with dissolve
menu:
    "OLD BOOKCASE" "The shelf  is dusty and crumbling under the weight of its contents. \n \n You count dozens of books, eaten by rats. \n \nOf the lot, only 4 seem to be in good enough condition to be read."
    "Book A  +2 {image=icon1}":
        jump room_01
    "Book B":
        jump end
    "Book C -4 {image=icon1}":
        $ stat_hlt -= 20
        call hlt_loss
        call death_check
        jump room_01
    "Book D":
        jump end

#############################################################################################
# ROOM 01
#############################################################################################
label firstroom_01:
    scene black
    with fade
    call room_events_reset
    scene bgmovie
    stop music fadeout 2
    #play music "mus/mus_room_01.mp3"
    show bgroom_01
    show mc captured:
        xpos 500
        ypos 500
    with Dissolve(2)
    pause 1
    show screen stats_UI
    with Dissolve(2)
    pause 1
label wakingup_01:
    play ambiance "sfx/amb_tension_02.mp3"
menu:
    "WAKING UP" "You wake up on the cold floor of an unfamiliar room.\n
    Your hands and feet are {b}{color=[txt_colo_01]}bound with rope{/b}{/color}.
    \n\n The last thing you remember: you were visiting the {b}{color=[txt_colo_01]}mysterious ghost town {/b}{/color} for your article,
     trying to understand its sudden abandonment by the population. \n\n
    You were close to the old school, and then... you don't remember a thing. \n\n Anyway, you'd better escape fast."
    "Break the ties.":
        call choice_selected
        call roll_str
        if success == True:
            "{color=[check_colo_01]} Strength check: Success. {/color}\n\n Focusing all your strength, you break your bonds and set yourself free."
        else:
            call hlt_loss
            $ stat_hlt -= 4
            "{color=[check_colo_01]} Strength check: Failure. {/color}\n\n You struggle for several minutes to break the rope.
            \n\n You finally free yourself, but your wrists are bloody and sore.
            {b}{color=[hlt_colo_01]}-4 {image=icon_hlt} {/b}{/color}"

        jump wakingup_02
    "Untie the knots":
        call choice_selected
        call roll_dex
        if success == True:
            "{color=[check_colo_01]} Dexterity check: Success. {/color}\n\n Using all your dexterity, you manage to undo the ropes around your wrists, then your ankles."
        else:
            call snt_loss
            $ stat_snt -= 4
            "{color=[check_colo_01]} Dexterity check: Failure. {/color}\n\n You spend long minutes wrestling with the knots, your stress mounting with the fear of never freeing yourself.\n\n Eventually, you manage to do it, but your mental state has taken a hit.
            {b}{color=[snt_colo_01]}-4 {image=icon_snt} {/b}{/color}"
        jump wakingup_02
label wakingup_02:
    stop ambiance fadeout 2
    play audio "sfx/sfx_rope_01.mp3"
    show mc frontr:
        xpos 500
        ypos 500
    with dissolve
menu:
    "TIP" "You can leave a room whenever you like. \n But staying and looking around might {b}{color=[txt_colo_01]}reveal things. {/b}{/color}
    \n\n Maybe uncover some of the {b}{color=[txt_colo_01]}secrets {/b}{/color} that led this place to become a ghost town in the first place. \n\n That was your original reason for coming, after all...
    \n\n But is it worth the risk? You can't lose all your {b}{color=[hlt_colo_01]}health{image=icon_hlt} {/b}{/color} or {b}{color=[snt_colo_01]}sanity{image=icon_snt}{/b}{/color}..."
    "Got it.":
        call choice_selected
        play music "mus/mus_exploration_02.mp3"
        jump room_01_interact
label room_01_interact:

    call screen room_01_interact
screen room_01_interact:
    if event1 == True:
        imagebutton:
            xpos 0.38
            ypos 0.2
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("first_window")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event2 == True:
        imagebutton:
            xpos 0.15
            ypos 0.6
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("bloodstain_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event3 == True:
        imagebutton:
            xpos 0.5
            ypos 0.35
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("calendar_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if eventstar == True:
        imagebutton:
            xpos 0.16
            ypos 0.39
            idle "ui/ui_interact_idle.png"
            action Jump("star_found_01")
            activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("classroom_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_ui_select_01.mp3"
label star_found_01:
    call star_found
    jump room_01_interact
############################
label first_window:
    play audio "sfx/sfx_wood_creak_01.mp3"
    $ event1 = False
    show mc backr:
        xpos 0.32
        ypos 0.26
    with dissolve
    "WINDOW" "You look outside. \n\n It looks like you've been brought into the {b}{color=[txt_colo_01]} abandoned high school{/b}{/color}. \n\n
    The window seems to be jammed, and anyway, you're too high up to jump. \n\n You'll have to find another way out."
    jump room_01_interact
###############################
label bloodstain_01:
    $ event2 = False
    show mc frontl:
        xpos 0.15
        ypos 0.4
    with dissolve
    "STAIN ON THE FLOOR" "Is that... {b}{color=[txt_colo_01]}blood{/b}{/color}? {b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color}"
    $ stat_snt -=1
    call snt_loss
    jump room_01_interact
################################
label calendar_01:
    $ event3 = False
    show mc backr:
        xpos 0.42
        ypos 0.38
    with dissolve
menu:
    "CALENDAR" "An old calendar. \n\n Like the rest of the town, this school has been abandoned for years, left to rot away from the rest of the world."
    "Ignore":
        call choice_selected
        jump room_01_interact
    "Inspect":
        play audio "sfx/sfx_paper_01.mp3"
        call choice_selected
        call roll_lck
        if success == True:
            pause 0.2
            play audio "sfx/sfx_key_01.mp3"
            $ stat_key += 1
            "{color=[check_colo_01]} Luck check: Success. {/color}\n\n
            A small key has been taped between two pages. It might come in handy… {b}{color=[key_colo_01]} +1 {image=icon_key} {/b}{/color}"
            jump room_01_interact
        else:
            "{color=[check_colo_01]} Luck check: Failure. {/color}\n\n
            Nothing to report..."
            jump room_01_interact
#############################################################################################
# ROOM 02
#############################################################################################
label classroom_01:
    scene black
    with fade
    call room_events_reset
    scene bgmovie
    #play music "mus/mus_room_01.mp3"
    show bgclassroom
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in a classroom."
    jump room_02_interact
label room_02_interact:
    call screen room_02_interact
screen room_02_interact:
    if event1 == True:
        imagebutton:
            xpos 0.44
            ypos 0.25
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("blackboard_poetry")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event2 == True:
        imagebutton:
            xpos 0.35
            ypos 0.65
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("table_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event3 == True:
        imagebutton:
            xpos 0.525
            ypos 0.33
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("plants_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("teacherlounge_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_ui_select_01.mp3"
#############################
label blackboard_poetry:
    $ event1 = False
    show mc backr:
        xpos 0.36
        ypos 0.3
    with dissolve
    "BLACK BOARD""A writing in chalk. \n\n {i}{color=[txt_colo_01]}The dogs have eaten all the flowers.
     \n If we eat the dogs, will we taste the flowers?{/i}{/color} \n\n Poetry, perhaps? In any case, it doesn't seem to make any sense."
    jump room_02_interact
#########################
label plants_01:
    play audio "sfx/sfx_pot_01.mp3"
    $ event3 = False
    show mc frontr:
        xpos 0.36
        ypos 0.3
    with dissolve
    "POTTED PLANTS""The last known inhabitants fled the town {b}{color=[txt_colo_01]} over 12 years ago{/b}{/color}. \n\n No wonder the plants are dead."
    jump room_02_interact
########################
label table_01:
    $ event2 = False
    show mc frontr at entrance_slot_01
    with dissolve
menu:
    "DESK & STOOLS""Standard furniture for a school of the {b}{color=[txt_colo_01]}Empire{/b}{/color}.
    \n\n It brings back memories of your own studies in the capital."
    "Ignore":
        call choice_selected
        jump room_02_interact
    "Search the desk.":
        call choice_selected
        play audio "sfx/sfx_cardboard_01.mp3"
        play audio "sfx/sfx_paper_01.mp3"
        call roll_mnd
        if success == True:
            $ stat_fir += 1
            "{color=[check_colo_01]} Perception check: Success. {/color}\n\n
            You find a match. {b}{color=[fir_colo_01]} +1 {image=icon_fir} {/b}{/color}"
            jump room_02_interact
        else:
            "{color=[check_colo_01]} Perception check: Failure. {/color}\n\n
            You found nothing..."
            jump room_02_interact

#############################################################################################
# ROOM 03
#############################################################################################
label teacherlounge_01:
    scene black
    with fade
    call room_events_reset
    scene bgmovie
    stop music fadeout 3
    play ambiance "sfx/amb_tension_01.mp3"
    show bgteacherlounge
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in the teachers' lounge. \n\n The moldy smell of the carpet is nauseating. {b}{color=[snt_colo_01]} -2 {image=icon_snt} {/b}{/color}"
    $ stat_snt -= 2
    call snt_loss
    jump room_03_interact
#####
label room_03_interact:
    call screen room_03_interact
screen room_03_interact:
    if event1 == True:
        imagebutton:
            xpos 0.15
            ypos 0.35
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("mirror_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event2 == True:
        imagebutton:
            xpos 0.37
            ypos 0.63
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("newspapers_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event3 == True:
        imagebutton:
            xpos 0.475
            ypos 0.55
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("lostkey_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event4 == True:
        imagebutton:
            xpos 0.38
            ypos 0.25
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("photo_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("classroom_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_ui_select_01.mp3"
#################################
label newspapers_01:
    $ event2 = False
    show mc backr:
        xpos 0.3
        ypos 0.58
    hide mcreflection
    with dissolve
menu:
    "OLD NEWSPAPER""A very old newspaper. \n\n It dates back to long {b}{color=[txt_colo_01]}before the city's desertion{/b}{/color},
    and was probably kept by a teacher as a {b}{color=[txt_colo_01]}souvenir{/b}{/color}."
    "Ignore":
        call choice_selected
        jump room_03_interact
    "Read":
        call choice_selected
        jump newspaper_comet
label newspaper_comet:
    play audio "sfx/sfx_paper_01.mp3"
    "THE SKY IS FALLING!""{i} (30 years ago.) {/i} \n\n
{i}{color=[txt_colo_01]}Last night, around 4 a.m., you were probably awakened by the sound of a loud explosion.
\n\n It wasn't an enemy air raid, but a comet that fell right here in our valley!
\n Fortunately, it landed in a field, and no human or animal lives were lost.
\n\nThe local authorities are already busy retrieving the object.
{/i}{/color}"
    jump room_03_interact
#################################
label lostkey_01:
    play audio "sfx/sfx_pot_01.mp3"
    $ event3 = False
    show mc backr:
        xpos 0.38
        ypos 0.42
    hide mcreflection
    with dissolve
menu:
    "LOST KEY""A {b}{color=[txt_colo_01]} key{/b}{/color} has fallen between the furnitures, but the gap is filled with pieces of {b}{color=[txt_colo_01]} broken glass{/b}{/color} and {b}{color=[txt_colo_01]} splinters of wood{/b}{/color}."
    "Ignore.":
        call choice_selected
        jump room_03_interact
    "Take the key. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}{b}{color=[key_colo_01]} +1 {image=icon_key} {/b}{/color}":
        call choice_selected
        $ stat_key +=1
        $ stat_hlt -=3
        call hlt_loss
        pause 0.2
        play audio "sfx/sfx_key_01.mp3"
        jump room_03_interact
#########################################################
label mirror_01:
    $ event1 = False
    show mc backl:
        xpos 0.155
        ypos 0.41
    show mcreflection behind mc :
        xpos 0.12
        ypos 0.365
    with dissolve
menu:
    "MIRROR""You look in the mirror. {i}You look terrible.{/i} \n\n But as you meet your own eyes, you promise yourself you'll get through this.
     \n\n You promise yourself..."
    "To be strong.":
        "Your strength is increased by 2."
        $ stat_str +=1
        call stat_increase
        pause 0.2
        $ stat_str +=1
        call stat_increase
        jump room_03_interact
    "To stay alert.":
        "Your perception is increased by 2."
        $ stat_mnd +=1
        call stat_increase
        pause 0.2
        $ stat_mnd +=1
        call stat_increase
        jump room_03_interact
    "To demonstrate dexterity.":
        "Your dexterity is increased by 2."
        $ stat_dex +=1
        call stat_increase
        pause 0.2
        $ stat_dex +=1
        call stat_increase
        jump room_03_interact
    "That your lucky star will watch over you.":
        "Your luck is increased by 2."
        $ stat_lck +=1
        call stat_increase
        pause 0.2
        $ stat_lck +=1
        call stat_increase
        jump room_03_interact
#########################################################
label photo_01:
    $ event4 = False
    show mc backr:
        xpos 0.27
        ypos 0.3
    hide mcreflection
    with dissolve
menu:
    "FRAMED PHOTOGRAPHS""Photos of school staff hang on the wall. \n\n One of the frames has fallen to the floor."
    "Ignore":
        call choice_selected
        jump room_03_interact
    "Inspect":
        call choice_selected
        "A CLASS PHOTO""The students pose in front of the school. \n You're struck by the appearance of many of them.
         \n\n Their eyes are {b}{color=[txt_colo_01]}bulging and piercingly blue{/b}{/color}. They look both exhausted and {b}{color=[txt_colo_01]}unnaturally agitated.{/b}{/color}
         \n\n This is very unsettling. {b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color} "
        $ stat_snt -= 1
        call snt_loss
        jump room_03_interact

# DEATH
##############################################################
label gameover:
    scene black
    with fade
    "you dead"
    jump end
    # This ends the game.
label end:
    $ renpy.full_restart()
