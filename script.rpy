
define a = Character("STRANGE MAN")
define z = Character("???")
define b = Character("FIGURE")

###AUDIO  ##########################################
init python:
    renpy.music.register_channel('ambiance', "music")
define config.default_music_volume = 0.8
define config.default_sfx_volume = 0.8
define config.default_voice_volume = 0.8

###IMAGE DEFINE ##########################################
#backgrounds
image bgroom_01 = "bg/bg_room_01.png"
image bgclassroom = "bg/bg_classroom_01.png"
image bgteacherlounge = "bg/bg_teacherlounge_01.png"
image bgcouselor_A = "bg/bg_counselor_A_01.png"
image bgcouselor_B = "bg/bg_counselor_B_01.png"
image bgbotanic_A = "bg/bg_botanic_A_01.png"
image bgbotanic_B = "bg/bg_botanic_B_01.png"
image bgbotanic_C = "bg/bg_botanic_C_01.png"
image bgritual_01 = "bg/bg_ritual_01.png"
image bgoutdoor_01 = "bg/bg_outdoor_01.png"
image bgstaircase_01 = "bg/bg_staircase_01.png"
image bginfirmary_01 = "bg/bg_infirmary_01.png"
image bgexit_01 = "bg/bg_exit_01.png"
image bgcloset_01 = "bg/bg_closet_01.png"
image bgcloset_01a = "bg/bg_closet_01_a.png"
image bghole_A = "bg/bg_hole_A_01.png"
image bghole_B = "bg/bg_hole_B_01.png"
image bgstardoor_01 = "bg/bg_stardoor_01.png"
image bgstardoor_02 = "bg/bg_stardoor_02.png"

image bgflower_01 = "bg/bg_flowerfield_A_01.png"
image bgflower_02 = "bg/bg_flowerfield_B_01.png"
image bgwhite = "bg/bg_white_01.png"


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

image starqueen = "chr/chr_npc2_01.png"

image flies:
    "chr/chr_fly_01.png"
    pause 0.1
    "chr/chr_fly_02.png"
    pause 0.1
    "chr/chr_fly_03.png"
    pause 0.1
    repeat

image npc1 frontl:
    pause 0.2
    "chr/chr_npc1_A_01.png"
    pause 0.75
    "chr/chr_npc1_A_02.png"
    pause 0.73
    repeat
image npc1 dead = "chr/chr_npc1_dead_01.png"
image npc1 hurt = "chr/chr_npc1_hurt_01.png"
#ui
image icon_hlt = "ui/icon_01.png"
image icon_snt = "ui/icon_02.png"
image icon_key = "ui/icon_03.png"
image icon_fir = "ui/icon_04.png"

#
default txt_colo_01 = "#ffad5a"
default check_colo_01 = "#a99e94"
default check_colo_02 = "#726c67"
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
default  stat_mnd = 8
default  stat_dex = 6
default  stat_lck = 5
default  stat_hlt = 10
default  stat_snt = 10
default  stat_key = 0
default  stat_fir = 0
default stat_knw = 0
default have_shovel = False
default have_screwdriver = False
#####################
default event1 = True
default event2 = True
default event3 = True
default event4 = True
default eventstar = True
default  stat_star = 0

default ending = 0
default ending_locked = False
########################################################
############### GAME START #############################
########################################################
label start:
    $ config.rollback_enabled = False
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
    return
label snt_loss:
    play audio "sfx/sfx_sanity_01.mp3"
    show screen stat_overlay_snt
    pause 0.01
    hide screen stat_overlay_snt
    with Dissolve(0.5)
    return
label hlt_gain:
    if stat_hlt > 10:
            $stat_hlt = 10
    play audio "sfx/sfx_health_01.mp3"
    pause 0.1
    play audio "sfx/sfx_stat_increase_01.mp3"
    show screen stat_overlay_hlt
    pause 0.01
    hide screen stat_overlay_hlt
    with Dissolve(0.5)
    return
label snt_gain:
    if stat_snt > 10:
            $stat_snt = 10
    play audio "sfx/sfx_stat_increase_01.mp3"
    show screen stat_overlay_snt
    pause 0.01
    hide screen stat_overlay_snt
    with Dissolve(0.5)
    return
label death_check:
    if stat_snt < 0:
            $stat_snt = 0
    if stat_snt <= 0:
        jump gameover
    if stat_hlt < 0:
            $stat_hlt = 0
    if stat_hlt <= 0:
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
label key_gain:
    play audio "sfx/sfx_key_01.mp3"
    show screen stat_overlay_01
    pause 0.01
    hide screen stat_overlay_01
    with Dissolve(0.5)
    return
label fir_gain:
    play audio "sfx/sfx_match_pick_01.mp3"
    show screen stat_overlay_01
    pause 0.01
    hide screen stat_overlay_01
    with Dissolve(0.5)
    return

label star_found:
    play audio "sfx/sfx_ui_star_01.mp3"
    $ eventstar = False
    $ stat_star += 1
    "You found an hidden star..."
    return
label walk_01:
    play audio "sfx/sfx_steps_01.mp3"
    return

#############################################################################################
# ROOM 01
#############################################################################################
label firstroom_01:
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_1
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
    "Break the ties. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
        call choice_selected from _call_choice_selected
        call roll_str from _call_roll_str
        if success == True:
            "{color=[check_colo_01]} Strength check: Success. {/color}\n\n Focusing all your strength, you break your bonds and set yourself free."
        else:
            "{color=[check_colo_01]} Strength check: Failure. {/color}\n\n You struggle for several minutes to break the rope.
            \n\n You finally free yourself, but your wrists are bloody and sore.
            {b}{color=[hlt_colo_01]}-4 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_1
            $ stat_hlt -= 4
            call death_check from _call_death_check_1
        jump wakingup_02
    "Untie the knots.{i}{color=[check_colo_02]}  (Dexterity){/i}{/color}":
        call choice_selected from _call_choice_selected_1
        call roll_dex from _call_roll_dex
        if success == True:
            "{color=[check_colo_01]} Dexterity check: Success. {/color}\n\n Using all your dexterity, you manage to undo the ropes around your wrists, then your ankles."
        else:
            "{color=[check_colo_01]} Dexterity check: Failure. {/color}\n\n You spend long minutes wrestling with the knots, your stress mounting with the fear of never freeing yourself.\n\n Eventually, you manage to do it, but your mental state has taken a hit.
            {b}{color=[snt_colo_01]}-4 {image=icon_snt} {/b}{/color}"
            call snt_loss from _call_snt_loss
            $ stat_snt -= 4
            call death_check from _call_death_check_2
        jump wakingup_02
label wakingup_02:
    stop ambiance fadeout 2
    play audio "sfx/sfx_rope_01.mp3"
    show mc frontr:
        xpos 500
        ypos 500
    with dissolve
    "TIP" "You can leave a room whenever you like. \n But staying and looking around might {b}{color=[txt_colo_01]}reveal things. {/b}{/color}
    \n\n Maybe uncover some of the {b}{color=[txt_colo_01]}secrets {/b}{/color} that led this place to become a ghost town in the first place.
    \n\n But is it worth the risk? You can't lose all your {b}{color=[hlt_colo_01]}health{image=icon_hlt} {/b}{/color} or {b}{color=[snt_colo_01]}sanity{image=icon_snt}{/b}{/color}...
    \n\n {color=[check_colo_01]}Click anywhere to continue.{/color}"
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
            idle "ui/ui_interact_invisible.png"
            action Jump("star_found_01")
            activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("classroom_01")
        # action Jump("counselor_office_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        # activate_sound "sfx/sfx_ui_select_01.mp3"
        activate_sound "sfx/sfx_steps_02.mp3"
label star_found_01:
    call star_found from _call_star_found
    jump room_01_interact
############################
label first_window:
    call walk_01 from _call_walk_01
    pause 0.2
    play audio "sfx/sfx_wood_creak_01.mp3"
    $ event1 = False
    show mc backr:
        xpos 0.32
        ypos 0.26
    with dissolve
    "WINDOW" "You look outside. \n\n It looks like you've been brought into the {b}{color=[txt_colo_01]} abandoned high school{/b}{/color}. \n\n
    The window seems to be jammed, and anyway, you're too high up to jump. \n\n You'll have to find {b}{color=[txt_colo_01]}another way out{/b}{/color}."
    jump room_01_interact
###############################
label bloodstain_01:
    call walk_01 from _call_walk_01_1
    $ event2 = False
    show mc frontl:
        xpos 0.15
        ypos 0.4
    with dissolve
    "STAIN ON THE FLOOR" "Is that... {b}{color=[txt_colo_01]}blood{/b}{/color}? {b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color}"
    $ stat_snt -=1
    call snt_loss from _call_snt_loss_1
    call death_check from _call_death_check_3
    jump room_01_interact
################################
label calendar_01:
    call walk_01 from _call_walk_01_2
    $ event3 = False
    show mc backr:
        xpos 0.42
        ypos 0.38
    with dissolve
menu:
    "CALENDAR" "An old calendar. \n\n Like the rest of the town, this school has been abandoned for years, left to rot away from the rest of the world."
    "Ignore":
        call choice_selected from _call_choice_selected_3
        jump room_01_interact
    "Inspect{i}{color=[check_colo_02]}  (Perception){/i}{/color}":
        play audio "sfx/sfx_paper_01.mp3"
        call choice_selected from _call_choice_selected_4
        call roll_mnd from _call_roll_lck
        if success == True:
            "{color=[check_colo_01]} Perception check: Success. {/color}\n\n
            A small key has been taped between two pages. It might come in handy… {b}{color=[key_colo_01]} +1 {image=icon_key} {/b}{/color}"
            $ stat_key += 1
            call key_gain from _call_key_gain
            jump room_01_interact
        else:
            "{color=[check_colo_01]} Perception check: Failure. {/color}\n\n
            Nothing to report..."
            jump room_01_interact
#############################################################################################
# ROOM 02
#############################################################################################
label classroom_01:
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_2
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
        action Jump("counselor_office_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_steps_02.mp3"
#############################
label blackboard_poetry:
    $ event1 = False
    $ stat_knw +=1
    call walk_01 from _call_walk_01_3
    show mc backr:
        xpos 0.36
        ypos 0.3
    with dissolve
    "BLACK BOARD""A writing in chalk. \n\n {i}{color=[txt_colo_01]}The dogs have eaten all the flowers.
     \n If we eat the dogs, will we taste the flowers?{/i}{/color} \n\n Poetry, perhaps? In any case, it doesn't seem to make any sense."
    jump room_02_interact
#########################
label plants_01:
    call walk_01 from _call_walk_01_4
    pause 0.1
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
    call walk_01 from _call_walk_01_5
    show mc frontr at entrance_slot_01
    with dissolve
menu:
    "DESK & STOOLS""Standard furniture for a school.
    \n\n It brings back memories of your own studies in the capital."
    "Ignore":
        call choice_selected from _call_choice_selected_5
        jump room_02_interact
    "Search the desk.{i}{color=[check_colo_02]}  (Luck){/i}{/color}":
        call choice_selected from _call_choice_selected_6
        play audio "sfx/sfx_cardboard_01.mp3"
        play audio "sfx/sfx_paper_01.mp3"
        call roll_lck from _call_roll_lck_4
        if success == True:
            "{color=[check_colo_01]} Luck check: Success. {/color}\n\n
            You find a match. {b}{color=[fir_colo_01]} +1 {image=icon_fir} {/b}{/color}"
            $ stat_fir += 1
            call fir_gain from _call_fir_gain
            jump room_02_interact
        else:
            "{color=[check_colo_01]} Luck check: Failure. {/color}\n\n
            You found nothing..."
            jump room_02_interact

#############################################################################################
# ROOM 03
#############################################################################################
label teacherlounge_01:
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_3
    play audio "sfx/amb_steps_01.mp3"
    scene bgmovie
    stop music fadeout 3
    play ambiance "sfx/amb_tension_01.mp3"
    show bgteacherlounge
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in the teachers' lounge. \n\n The moldy smell of the carpet is nauseating. {b}{color=[snt_colo_01]} -2 {image=icon_snt} {/b}{/color}"
    $ stat_snt -= 2
    call snt_loss from _call_snt_loss_2
    call death_check from _call_death_check_4
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
    if eventstar == True:
        imagebutton:
            xpos 0.325
            ypos 0.8
            idle "ui/ui_interact_invisible.png"
            action Jump("star_found_03")
            activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("botanic_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_steps_02.mp3"
#################################
label star_found_03:
    call star_found from _call_star_found_1
    jump room_03_interact

label newspapers_01:
    call walk_01 from _call_walk_01_6
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
        call choice_selected from _call_choice_selected_7
        jump room_03_interact
    "Read":
        call choice_selected from _call_choice_selected_8
        $ stat_knw +=1
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
    call walk_01 from _call_walk_01_7
    pause 0.1
    play audio "sfx/sfx_wood_creak_01.mp3"
    $ event3 = False
    show mc backr:
        xpos 0.38
        ypos 0.42
    hide mcreflection
    with dissolve
menu:
    "LOST KEY""A {b}{color=[txt_colo_01]} key{/b}{/color} has fallen between the furnitures, but the gap is filled with pieces of {b}{color=[txt_colo_01]} broken glass{/b}{/color} and {b}{color=[txt_colo_01]} splinters of wood{/b}{/color}."
    "Ignore.":
        call choice_selected from _call_choice_selected_9
        jump room_03_interact
    "Take the key. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}{b}{color=[key_colo_01]} +1 {image=icon_key} {/b}{/color}":
        call choice_selected from _call_choice_selected_10
        $ stat_key +=1
        $ stat_hlt -=3
        call hlt_loss from _call_hlt_loss_2
        call death_check from _call_death_check_5
        pause 0.2
        play audio "sfx/sfx_key_01.mp3"
        jump room_03_interact
#########################################################
label mirror_01:
    call walk_01 from _call_walk_01_8
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
        call stat_increase from _call_stat_increase
        pause 0.2
        $ stat_str +=1
        call stat_increase from _call_stat_increase_1
        jump room_03_interact
    "To stay alert.":
        "Your perception is increased by 2."
        $ stat_mnd +=1
        call stat_increase from _call_stat_increase_2
        pause 0.2
        $ stat_mnd +=1
        call stat_increase from _call_stat_increase_3
        jump room_03_interact
    "To demonstrate dexterity.":
        "Your dexterity is increased by 2."
        $ stat_dex +=1
        call stat_increase from _call_stat_increase_4
        pause 0.2
        $ stat_dex +=1
        call stat_increase from _call_stat_increase_5
        jump room_03_interact
    "That your lucky star will watch over you.":
        "Your luck is increased by 2."
        $ stat_lck +=1
        call stat_increase from _call_stat_increase_6
        pause 0.2
        $ stat_lck +=1
        call stat_increase from _call_stat_increase_7
        jump room_03_interact
#########################################################
label photo_01:
    call walk_01 from _call_walk_01_9
    $ event4 = False
    show mc backr:
        xpos 0.27
        ypos 0.3
    hide mcreflection
    with dissolve
menu:
    "FRAMED PHOTOGRAPHS""Photos of school staff hang on the wall. \n\n One of the frames has fallen to the floor, {b}{color=[txt_colo_01]}showing something disturbing{/b}{/color}."
    "Ignore":
        call choice_selected from _call_choice_selected_11
        jump room_03_interact
    "Inspect {b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color}":
        $ stat_knw +=1
        call choice_selected from _call_choice_selected_12
        "A CLASS PHOTO""The students pose in front of the school. \n You're struck by the appearance of many of them.
         \n\n Their eyes are {b}{color=[txt_colo_01]}bulging and piercingly blue{/b}{/color}. They look both exhausted and {b}{color=[txt_colo_01]}unnaturally agitated.{/b}{/color}
         \n\n This is very unsettling. {b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color} "
        $ stat_snt -= 1
        call snt_loss from _call_snt_loss_3
        call death_check from _call_death_check_6
        jump room_03_interact

#############################################################################################
# ROOM 04
#############################################################################################
label counselor_office_01:
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_4
    scene bgmovie
    stop ambiance fadeout 2
    play music "mus/mus_npc_01.mp3"
    show bgcouselor_A zorder 0
    show npc1 frontl zorder 5:
        xpos 0.377
        ypos 0.39
    show bgcouselor_B zorder 10
    show mc backr zorder 15:
        xpos 0.242
        ypos 0.6
    with Dissolve(2)
    "You arrive in a counselor's office... \n\n But there is {b}{color=[txt_colo_01]}someone here.{/b}{/color} \n\nA stranger, wearing a dress decorated with fabric flowers, and a dog mask"
    jump npc1_01
label npc1_01:
menu:
    a"Oh. Hello. \n\n
    I wasn't expecting to run into anyone here.\n\n It's not exactly a tourist destination...
    \n\n {b}{color=[txt_colo_01]}What are you doing here?{/b}{/color}"
    "{i}\"You're the one who kidnapped me, right?\"{/i}":
            a"I don't know what you're talking about.
            \n\n I'm just a {b}{color=[txt_colo_01]}peaceful hermit{/b}{/color} on a pilgrimage through the city."
            jump npc1_02
    "{i}\"Who are you?\"{/i}":
            a"I'm just a {b}{color=[txt_colo_01]}peaceful hermit{/b}{/color} on a pilgrimage through the city."
            jump npc1_02
    "{i}\"I'm investigating what happened to the town.\"{/i}":
            a"\"What happened?\" \n\n Oh, you're probably wondering why the residents left.
            \n\nThe answer is simple: sometimes, {b}{color=[txt_colo_01]}people move{/b}{/color}. And sometimes, they all move at the same time...
            \n\n {b}{color=[txt_colo_01]}Mistery solved!{/b}{/color}"
            jump npc1_02
    # "Attack him with your fists. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
    #     jump npc1_04
label npc1_02:
menu:
    a"You should leave quickly. The building is old and can be dangerous.
    \n\n Keep moving, you're only {b}{color=[txt_colo_01]}5 rooms from the exit{/b}{/color}.
    \n\n Keep going, {b}{color=[txt_colo_01]}don't waste time looking around{/b}{/color}, and you'll be out in no time!
    \n\nAs for me, I have to leave too. \n \nGoodbye!"
    "{i}\"Ok, thanks...\"{/i}":
        jump npc1_03
    "{i}\"Why the dog mask?\"{/i}":
        a"...There used to be lots of dogs here. Flowers too.
        \n\n Now there are neither.
        \n\nThis is my way of {b}{color=[txt_colo_01]}paying tribute{/b}{/color} to them. "
        jump npc1_03
    "{i}\"Were you a student here?\"{/i}":
        a"...A long time ago."
        jump npc1_03
    # "Attack him with your fists. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
    #     jump npc1_04
label npc1_03:
    a"Have a nice day."
    stop music fadeout 3
    call walk_01 from _call_walk_01_10
    hide npc1
    with dissolve
    pause 0.5
    play music "mus/mus_exploration_02.mp3"
    jump room_04_interact
label npc1_04:
    stop music fadeout 2
    call choice_selected from _call_choice_selected_2
    call roll_str from _call_roll_str_1
    if success == True:
        "{color=[check_colo_01]} Strength check: Success. {/color}
        \n\n You leap on him, throwing a big punch.
        \n\n {b}{color=[txt_colo_01]}Blood spurts{/b}{/color} from behind his mask as he {b}{color=[txt_colo_01]}screams in pain{/b}{/color}."
        a"AAARG."
        jump npc1_05
    else:
        "{color=[check_colo_01]} Strength check: Failure. {/color}
        \n\n You jump at him, but the {b}{color=[txt_colo_01]}weakness{/b}{/color} of your blow has {b}{color=[txt_colo_01]}little effect{/b}{/color}.
        \n\nThe stranger isn't hurt, but you can feel his anger behind his mask."
        jump npc1_05
label npc1_05:
    play music "mus/mus_npc_tension_01.mp3" fadein 1
    a"You little brat... \n\n I should have {b}{color=[txt_colo_01]}finished the job{/b}{/color} when I had the chance.
    \n\n No more mister nice guy.
    \n\nSee you soon, {b}{color=[txt_colo_01]}dead meat{/b}{/color}."
    "The stranger runs out of the room."
label npc1_end1:
    stop music fadeout 3
    play audio "sfx/sfx_steps_03.mp3"
    hide npc1
    with dissolve
    pause 0.5
    play music "mus/mus_exploration_02.mp3"
    jump room_04_interact
jump room_04_interact
#####
label room_04_interact:
    call screen room_04_interact
screen room_04_interact:
    if event1 == True:
        imagebutton:
            xpos 0.4
            ypos 0.55
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("cigarette_case_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event2 == True:
        imagebutton:
            xpos 0.48
            ypos 0.4
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("note_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event3 == True:
        imagebutton:
            xpos 0.335
            ypos 0.4
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("bloodstain_02")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if eventstar == True:
        imagebutton:
            xpos 0.2
            ypos 0.47
            idle "ui/ui_interact_invisible.png"
            action Jump("star_found_02")
            activate_sound "sfx/sfx_ui_select_01.mp3"
    # if event4 == True:
    #     imagebutton:
    #         xpos 0.225
    #         ypos 0.67
    #         idle "ui/ui_interact_idle.png"
    #         hover "ui/ui_interact_hover.png"
    #         action Jump("locked_01")
    #         hover_sound "sfx/sfx_ui_hover_01.mp3"
    #         activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("teacherlounge_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_steps_02.mp3"
#################################
label star_found_02:
    call star_found from _call_star_found_2
    jump room_04_interact

label cigarette_case_01:
    call walk_01 from _call_walk_01_11
    $ event1 = False
    show mc frontl zorder 5:
        xpos 0.377
        ypos 0.39
    with dissolve
    play audio "sfx/sfx_wood_open_01.mp3"
menu:
    "CIGARETTE CASE""In the desk drawer, you find a small, finely decorated metal box containing a few cigarettes and a match."
    "Smoke a cigarette.{i}{color=[check_colo_02]}  (Luck){/i}{/color}":
        play audio "sfx/sfx_match_use_01.mp3"
        call roll_lck from _call_roll_lck_1
        if success == True:
            "{color=[check_colo_01]} Luck check: Success. {/color}\n\n
            It relaxes you… {b}{color=[snt_colo_01]} +3 {image=icon_snt} {/b}{/color}"
            $ stat_snt +=3
            call snt_gain from _call_snt_gain_2
            jump room_04_interact
        else:
            "{color=[check_colo_01]} Luck check: Failure.{/color}\n\n
            How disgusting! \n\n The tobacco must have molded, and made you nauseous.
            {b}{color=[hlt_colo_01]} -2 {image=icon_hlt} {/b}{/color}"
            $ stat_hlt -= 4
            call hlt_loss from _call_hlt_loss_3
            call death_check from _call_death_check_7
            jump room_04_interact

    "Take the match.":
        play audio "sfx/sfx_match_pick_01.mp3"
        $ stat_fir += 1
        call fir_gain from _call_fir_gain_1
        jump room_04_interact

#################################
label note_01:
    call walk_01 from _call_walk_01_12
    pause 0.1
    play audio "sfx/sfx_metal_01.mp3"
    $ event2 = False
    show mc backr zorder 5:
        xpos 0.4
        ypos 0.41
    with dissolve
menu:
    "A NOTE""A note, adressed to the school's principal."
    "Ignore":
        call choice_selected from _call_choice_selected_13
        jump room_04_interact
    "Read":
        $ stat_knw +=1
        call choice_selected from _call_choice_selected_14
        jump note_read_01
label note_read_01:
    play audio "sfx/sfx_paper_01.mp3"
    "NOTE TO THE PRINCIPAL""{i}{color=[txt_colo_01]} Mr Leclaire \n\n The problem of the blue flowers is getting worse. More and more students are using them. \n\n
    They drink them as infusions, or chew the petals like gum. Some have started selling them, for absurd sums of money.
    \n\n I don't care if grades are up, I'm afraid you're underestimating the side effects.
{/i}{/color}"
    jump room_04_interact
#########################################################
label bloodstain_02:
    call walk_01 from _call_walk_01_13
    $ event3 = False
    show mc backr zorder 5:
        xpos 0.25
        ypos 0.3
    with dissolve
    "STAIN ON THE FLOOR" "Is that... {b}{color=[txt_colo_01]}blood{/b}{/color}? {b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color}"
    $ stat_snt -=1
    call snt_loss from _call_snt_loss_4
    call death_check from _call_death_check_8
    jump room_04_interact
#########################################################
# label locked_01:
#     call walk_01
#     $ event4 = False
#     show mc backl zorder 15:
#         xpos 0.2
#         ypos 0.55
#     with dissolve
# menu:
#     "LOCKED""It's locked."
#     "Ignore":
#         call choice_selected from _call_choice_selected_15
#         jump room_04_interact
#     "Use a key" if stat_key >0:
#         play audio "sfx/sfx_unlock.mp3"
#         $ stat_key -= 1
#         "**To be implemented.**"
#         jump room_04_interact




 #############################################################################################
 # BOTANIC ROOM 1
 #############################################################################################
label botanic_01:
     scene black
     with fade
     call room_events_reset from _call_room_events_reset_6
     scene bgmovie
     play music "mus/mus_exploration_02.mp3"
     show bgbotanic_A
     show bgbotanic_B
     play ambiance "sfx/sfx_buzzing_01.mp3" volume 0.15
     show flies:
        xpos 0.32
        ypos 0.2
     show mc backr at entrance_slot_01
     with Dissolve(2)
     "An old botany room. \n\n All the plants are dead..."
     jump room_botanic_interact
label room_botanic_interact:
     call screen room_botanic_interact
screen room_botanic_interact:
     if event1 == True:
         imagebutton:
             xpos 0.15
             ypos 0.35
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("notice_board_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if event2 == True:
         imagebutton:
             xpos 0.5
             ypos 0.45
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("botanic_pots_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if event3 == True:
         imagebutton:
             xpos 0.3
             ypos 0.593
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("hidden_trapdoor_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     imagebutton:
         xpos 0.47
         ypos 0.74
         idle "ui/ui_exit_idle.png"
         hover "ui/ui_exit_hover.png"
         action Jump("infirmary_01")
         hover_sound "sfx/sfx_ui_hover_01.mp3"
         activate_sound "sfx/sfx_steps_02.mp3"
 #############################
label notice_board_01:
     call walk_01 from _call_walk_01_14
     $ stat_knw +=1
     $ event1 = False
     show mc backl:
         xpos 0.13
         ypos 0.4
     with dissolve
     "NOTICE BOARD""Old announcements. \n\n Among the oldest ones, there are many posters of {b}{color=[txt_colo_01]}lost dogs{/b}{/color}.
      \n\n The most recent flyers, covering the old ones, are posters of {b}{color=[txt_colo_01]}missing students{/b}{/color}...
      \n\n First the dogs disappeared, then the townspeople? What happened?"
     jump room_botanic_interact
label botanic_pots_01:
     call walk_01 from _call_walk_01_15
     $ event2 = False
     show mc backr:
         xpos 0.4
         ypos 0.45
     with dissolve
menu:
    "POT""You see a {b}{color=[txt_colo_01]}key{/b}{/color} at the bottom of the jar.
    \n\nBut the pot is full of dry, {b}{color=[txt_colo_01]}thorn-covered brambles{/b}{/color} and {b}{color=[txt_colo_01]}wriggling maggots{/b}{/color}."
    "Take the key. {b}{color=[hlt_colo_01]}-2 {image=icon_hlt}{/b}{/color}{b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color}{b}{color=[key_colo_01]} +1 {image=icon_key} {/b}{/color}":
        call choice_selected from _call_choice_selected_15
        $ stat_hlt -=2
        call hlt_loss from _call_hlt_loss
        $ stat_snt -=1
        call snt_loss from _call_snt_loss_5
        call death_check from _call_death_check
        pause 0.2
        $ stat_key +=1
        call key_gain from _call_key_gain_2
        play audio "sfx/sfx_key_01.mp3"
        jump room_botanic_interact
    "Ignore.":
        call choice_selected from _call_choice_selected_18
        jump room_botanic_interact
label hidden_trapdoor_01:
     $ event3 = False
     show mc frontl:
         xpos 0.3
         ypos 0.37
     with dissolve
     "RED TILES.""Strange...\n\n But there's nothing to do for now."
     jump room_botanic_interact

#############################################################################################
# BOTANIC ROOM 2
#############################################################################################
label botanic_02:
    scene black
    with fade
    call walk_01 from _call_walk_01_16
    call room_events_reset from _call_room_events_reset_7
    $ event4 = False
    scene bgmovie
    #play music "mus/mus_room_01.mp3"
    show bgbotanic_A
    play ambiance "sfx/sfx_buzzing_01.mp3" volume 0.15
    show flies:
       xpos 0.32
       ypos 0.2
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "An old botany room. \n\n But... Haven't you been here before? \n\n This piece looks identical. Or maybe not."
    jump room_botanic_interact2
label room_botanic_interact2:
    call screen room_botanic_interact2
screen room_botanic_interact2:
    # if event1 == True:
    #     imagebutton:
    #         xpos 0.15
    #         ypos 0.35
    #         idle "ui/ui_interact_idle.png"
    #         hover "ui/ui_interact_hover.png"
    #         action Jump("notice_board_01")
    #         hover_sound "sfx/sfx_ui_hover_01.mp3"
    #         activate_sound "sfx/sfx_ui_select_01.mp3"
    # if event2 == True:
    #     imagebutton:
    #         xpos 0.5
    #         ypos 0.45
    #         idle "ui/ui_interact_idle.png"
    #         hover "ui/ui_interact_hover.png"
    #         action Jump("table_01")
    #         hover_sound "sfx/sfx_ui_hover_01.mp3"
    #         activate_sound "sfx/sfx_ui_select_01.mp3"
    if event3 == True:
        imagebutton:
            xpos 0.3
            ypos 0.593
            idle "ui/ui_interact_invisible.png"
            hover "ui/ui_interact_invisible.png"
            action Jump("hidden_trapdoor_02")
            # hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event4 == True:
        imagebutton:
            xpos 0.3
            ypos 0.593
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("hidden_trapdoor_03")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("staircaise_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_ui_select_01.mp3"
#############################
label notice_board_02:
    $ event1 = False
    show mc backl:
        xpos 0.13
        ypos 0.4
    with dissolve
    "NOTICE BOARD""Old announcements. \n\n Among the oldest ones, there are many posters of {b}{color=[txt_colo_01]}lost dogs{/b}{/color}.
     \n\n The most recent flyers, covering the old ones, are posters of {b}{color=[txt_colo_01]}missing students{/b}{/color}...
     \n\n First the dogs disappeared, then the townspeople? What happened?"
    jump room_botanic_interact2

label hidden_trapdoor_02:
    $ event3 = False
    $ event4 = True
    show mc frontl:
        xpos 0.3
        ypos 0.37
    with dissolve
    "HIDDEN PASSAGE""The slab seems to move.
    \n\n Lifting it reveals a {b}{color=[txt_colo_01]}narrow passage{/b}{/color} to a room beneath your feet."
    play audio "sfx/sfx_wood_creak_01.mp3" volume 0.2
    play audio "sfx/sfx_pot_01.mp3"
    show bgbotanic_C
    jump room_botanic_interact2
label hidden_trapdoor_03:
    show mc frontl:
        xpos 0.3
        ypos 0.37
    with dissolve
menu:
    "HIDDEN PASSAGE""A narrow passage to a room beneath your feet.\n\n It's too dark to see what's awaiting you."
    "Go down":
        call choice_selected from _call_choice_selected_48
        play audio "sfx/sfx_wood_creak_01.mp3"
        show bgbotanic_C
        jump stardoor_01
    "Ignore":
        call choice_selected from _call_choice_selected_49
        jump room_botanic_interact3

#############################################################################################
# RITUAL ROOM
#############################################################################################
label ritual_01:
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_8
    scene bgmovie
    play audio "sfx/amb_steps_01.mp3"
    #play music "mus/mus_room_01.mp3"
    show bgritual_01
    stop music fadeout 3
    play ambiance "sfx/amb_tension_02.mp3"
    show mc backr at entrance_slot_01
    with Dissolve(2)
    # "An old botany room. \n\n But... Haven't you been here before?"
    jump room_ritual_interact
label room_ritual_interact:
    call screen room_ritual_interact
screen room_ritual_interact:
    if event1 == True:
        imagebutton:
            xpos 0.395
            ypos 0.35
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("altar_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event2 == True:
        imagebutton:
            xpos 0.5
            ypos 0.45
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("table_01")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event3 == True:
        imagebutton:
            xpos 0.3
            ypos 0.593
            idle "ui/ui_interact_invisible.png"
            hover "ui/ui_interact_invisible.png"
            action Jump("hidden_trapdoor_02")
            # hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event4 == True:
        imagebutton:
            xpos 0.3
            ypos 0.593
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("hidden_trapdoor_03")
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
label altar_01:
    $ event1 = False
    show mc backr:
        xpos 0.29
        ypos 0.38
    with dissolve
    if  stat_snt > 2:
        jump altar_01_sane
    else:
        jump altar_01_insane

label altar_01_sane:
menu:
    "ALTAR""A grotesque sculpture, made of wood, paper and glue, and painted red. A foul smell emanates from it, but you also feel a powerful, inexplicable energy."
    "You're too sane to interact with the altar." :
        jump room_ritual_interact
label altar_01_insane:
menu:
    "ALTAR""A grotesque sculpture, made of wood, paper and glue, and painted red. A foul smell emanates from it, but you also feel a powerful, inexplicable energy."
    "Interact with the altar.":
        "boo"
        jump room_ritual_interact
    "Ignore":
        jump room_ritual_interact

#############################################################################################
# INFIRMARY
#############################################################################################
label infirmary_01:
    stop ambiance fadeout 1
    scene black
    with fade
    call room_events_reset from _call_room_events_reset
    scene bgmovie
    show bginfirmary_01
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in the infirmary."
    jump room_infirmary_interact
label room_infirmary_interact:
     call screen room_infirmary_interact
screen room_infirmary_interact:
     if event1 == True:
         imagebutton:
             xpos 0.21
             ypos 0.38
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("medical_closet_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if event2 == True:
         imagebutton:
             xpos 0.27
             ypos 0.3
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("medical_note_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if event3 == True:
         imagebutton:
             xpos 0.33
             ypos 0.755
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("bloodstain_03")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if event4 == True:
         imagebutton:
             xpos 0.5
             ypos 0.35
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("dark_corner_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if eventstar == True:
         imagebutton:
             xpos 0.335
             ypos 0.163
             idle "ui/ui_interact_invisible.png"
             action Jump("star_found_04")
             activate_sound "sfx/sfx_ui_select_01.mp3"
     imagebutton:
         xpos 0.47
         ypos 0.74
         idle "ui/ui_exit_idle.png"
         hover "ui/ui_exit_hover.png"
         action Jump("botanic_02")
         hover_sound "sfx/sfx_ui_hover_01.mp3"
         activate_sound "sfx/sfx_steps_02.mp3"

label star_found_04:
    call star_found from _call_star_found_3
    jump room_infirmary_interact
#############################################################################################
# DARK CORNER
#############################################################################################
label dark_corner_01:
    $ event4 = False
    call walk_01 from _call_walk_01_17
    pause 0.2
    # play audio "sfx/sfx_wood_creak_01.mp3"
    show mc backr:
        xpos 0.37
        ypos 0.5
    with dissolve
menu:
    "DARKNESS""This corner of the room is plunged into {b}{color=[txt_colo_01]}darkness{/b}{/color}.\n\n
    You can make out some cupboards.\n\n {b}{color=[txt_colo_01]}A source of light{/b}{/color}, even a dim one,
    would enable you to rummage through them."
    "Search the cupboards. {b}{color=[fir_colo_01]} -1 {image=icon_fir} {/b}{/color} {i}{color=[check_colo_02]}(Luck){/i}{/color}":
        call choice_selected from _call_choice_selected_19
        play audio "sfx/sfx_wood_open_01.mp3"
        call roll_lck from _call_roll_lck_3
        if success == True:
            "{color=[check_colo_01]} Luck check: Success. {/color}\n\nThe cupboards contain maintenance equipment that nobody has touched in years.
            \n\nYou find an intact bandage  {b}{color=[hlt_colo_01]}+1{image=icon_hlt} {/b}{/color}
            two small keys {b}{color=[key_colo_01]} +2 {image=icon_key} {/b}{/color}
            and a match{b}{color=[fir_colo_01]} +1 {image=icon_fir} {/b}{/color}."
            $ stat_hlt += 1
            call hlt_gain from _call_hlt_gain
            pause 0.1
            $ stat_key += 2
            call key_gain from _call_key_gain_1
            pause 0.1
            $ stat_fir += 1
            call fir_gain from _call_fir_gain_2
            jump room_infirmary_interact
        else:
            "{color=[check_colo_01]} Luck check: Failure. {/color}\n\nThe cupboards are practically empty, containing nothing but a small key
            {b}{color=[key_colo_01]} +1 {image=icon_key} {/b}{/color}."
            $ stat_key += 1
            jump room_infirmary_interact
    "Ignore":
        call choice_selected from _call_choice_selected_50
        jump room_infirmary_interact

#############################################################################################
# MEDICAL CLOSET
#############################################################################################
label medical_closet_01:
    $ event1 = False
    call walk_01 from _call_walk_01_18
    pause 0.2
    play audio "sfx/sfx_wood_creak_01.mp3"
    show mc backl:
        xpos 0.18
        ypos 0.42
    with dissolve
menu:
    "MEDICAL CLOSET""An old medical closet.\n\n The bandages have gone moldy, and the medicine jars are almost empty,
     each containing only a few pills.\n\n The instructions seem to be very strict, advising you to take only one pill at a
      time.\n\n What do you want to take?"
    "Coagulant. {b}{color=[hlt_colo_01]}+2 {image=icon_hlt} {/b}{/color}":
        call choice_selected from _call_choice_selected_20
        $ stat_hlt +=2
        call hlt_gain from _call_hlt_gain_1
        jump room_infirmary_interact
    "Anxiolytic. {b}{color=[snt_colo_01]} +2 {image=icon_snt} {/b}{/color}":
        call choice_selected from _call_choice_selected_21
        $ stat_snt +=2
        call snt_gain from _call_snt_gain
        jump room_infirmary_interact
    "Performance enhancer. {color=[check_colo_01]} Strength +3 {/color}":
        call choice_selected from _call_choice_selected_22
        "Your strength is increased by 3."
        $ stat_str +=1
        call stat_increase from _call_stat_increase_8
        pause 0.1
        $ stat_str +=1
        call stat_increase from _call_stat_increase_9
        pause 0.1
        $ stat_str +=1
        call stat_increase from _call_stat_increase_10
        jump room_infirmary_interact
    "Unidentified pill. {i}{color=[check_colo_02]}  (Luck){/i}{/color}":
        call choice_selected from _call_choice_selected_23
        call roll_lck from _call_roll_lck_2
        if success == True:
            "{color=[check_colo_01]} Luck check: Success. {/color}\n\n All your stats are increased by 1."
            $ stat_str +=1
            call stat_increase from _call_stat_increase_11
            pause 0.1
            $ stat_mnd +=1
            call stat_increase from _call_stat_increase_12
            pause 0.1
            $ stat_dex +=1
            call stat_increase from _call_stat_increase_13
            pause 0.1
            $ stat_lck +=1
            call stat_increase from _call_stat_increase_14
            pause 0.1
            jump room_infirmary_interact
        else:
            "{color=[check_colo_01]} Luck check: Failure. {/color}\n\n
            You feel really sick!
            {b}{color=[hlt_colo_01]} -3 {image=icon_hlt} {/b}{/color}"
            $ stat_hlt -= 3
            call hlt_loss from _call_hlt_loss_4
            call death_check from _call_death_check_9
            jump room_infirmary_interact
    "Nothing.":
        call choice_selected from _call_choice_selected_24
        jump room_infirmary_interact
label bloodstain_03:
    call walk_01 from _call_walk_01_19
    $ event3 = False
    show mc frontr:
        xpos 0.22
        ypos 0.53
    with dissolve
    "STAIN ON THE FLOOR" "Is that... {b}{color=[txt_colo_01]}blood{/b}{/color}? {b}{color=[snt_colo_01]} -1 {image=icon_snt} {/b}{/color}"
    $ stat_snt -=1
    call snt_loss from _call_snt_loss_6
    call death_check from _call_death_check_10
    jump room_infirmary_interact

# MEDICAL NOTE
############################
label medical_note_01:
    $ event2 = False
    call walk_01 from _call_walk_01_20
    pause 0.2
    play audio "sfx/sfx_metal_01.mp3"
    show mc backl:
        xpos 0.24
        ypos 0.32
    with dissolve
menu:
    "NOTE""A note, written by a nurse."
    "Ignore":
        call choice_selected from _call_choice_selected_16
        jump room_infirmary_interact
    "Read":
        $ stat_knw +=1
        call choice_selected from _call_choice_selected_17
        jump medical_note_01_read
label medical_note_01_read:
    play audio "sfx/sfx_paper_01.mp3"
    "MEDICAL NOTE""{i}{color=[txt_colo_01]} Symptoms:\n\n
    - Hallucinations\n
    - Trembling\n
    - Loss of sleep\n
    - God complex (?)\n
    - Iris coloration\n\n
    These symptoms are no longer confined to students, but can be seen throughout the city.
 {/i}{/color}"
    jump room_infirmary_interact

#############################################################################################
# CLOSET
#############################################################################################
label closet_01:
    # stop music fadeout 2
    play audio "sfx/amb_steps_01.mp3"
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_9
    scene bgmovie
    show bgcloset_01
    show bgcloset_01a
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in a maintenance closet."
    jump room_closet_interact
label room_closet_interact:
     call screen room_closet_interact
screen room_closet_interact:
     if event1 == True:
         imagebutton:
             xpos 0.18
             ypos 0.37
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("firstaid_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if event2 == True:
         imagebutton:
             xpos 0.5
             ypos 0.32
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("wall_writing_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     if event3 == True:
         imagebutton:
             xpos 0.35
             ypos 0.45
             idle "ui/ui_interact_idle.png"
             hover "ui/ui_interact_hover.png"
             action Jump("toolbox_01")
             hover_sound "sfx/sfx_ui_hover_01.mp3"
             activate_sound "sfx/sfx_ui_select_01.mp3"
     imagebutton:
         xpos 0.47
         ypos 0.74
         idle "ui/ui_exit_idle.png"
         hover "ui/ui_exit_hover.png"
         action Jump("exit_01")
         hover_sound "sfx/sfx_ui_hover_01.mp3"
         activate_sound "sfx/sfx_steps_02.mp3"
label firstaid_01:
    $ event1 = False
    call walk_01 from _call_walk_01_21
    show mc backl:
        xpos 0.2
        ypos 0.46
    with dissolve
menu:
    "FIRST-AID KIT""An old first aid kit, almost empty. What do you want to take?"
    "Coagulant. {b}{color=[hlt_colo_01]}+2 {image=icon_hlt} {/b}{/color}":
        $ stat_hlt +=2
        call hlt_gain from _call_hlt_gain_2
        jump room_closet_interact
    "Anxiolytic. {b}{color=[snt_colo_01]} +2 {image=icon_snt} {/b}{/color}":
        $ stat_snt +=2
        call snt_gain from _call_snt_gain_1
        jump room_closet_interact
    "Nothing.":
        jump room_closet_interact
label wall_writing_01:
    $ event2 = False
    $ stat_knw +=1
    call walk_01 from _call_walk_01_22
    show mc backr:
        xpos 0.36
        ypos 0.5
    with dissolve
    "WRITING ON A WALL""A writing in a red substance. \n\n {i}{color=[txt_colo_01]}I'll find you all. \n\nI'll be the Great Glutton, no one else. {/i}{/color}
    \n\n The message seems ancient. You don't think it's addressed to you."
    jump room_closet_interact
label toolbox_01:
    $ event3 = False
    call walk_01 from _call_walk_01_23
    show mc backr:
        xpos 0.27
        ypos 0.39
    with dissolve
menu:
    "LOCKED CHEST""A large wooden chest, locked with chains and two padlocks."
    "Ignore":
        call choice_selected from _call_choice_selected_25
        jump room_closet_interact
    "Open the chest {b}{color=[key_colo_01]} -2 {image=icon_key} {/b}{/color}" if stat_key >=2:
        call choice_selected from _call_choice_selected_26
        play audio "sfx/sfx_unlock.mp3"
        pause 0.2
        play audio "sfx/sfx_wood_open_01.mp3"
        hide bgcloset_01a
        with dissolve
        $ stat_key -= 2
        jump toolbox_02
label toolbox_02:
menu:
    "TOOLBOX""A large crate full of tools. Some of them would make a good improvised weapon."
    "Search for a light, short weapon (Uses Dexterity).":
        call choice_selected from _call_choice_selected_27
        play audio "sfx/sfx_metal_02.mp3"
        $ have_screwdriver = True
        "You find a screwdriver. Long and pointy, it could be used as a weapon."
        jump room_closet_interact
    "Search for a long, thin weapon (Uses Perception).":
        call choice_selected from _call_choice_selected_28
        play audio "sfx/sfx_metal_02.mp3"
        $ have_shovel = True
        "You find a pitchfork, for gardening. It might come in handy..."
        jump room_closet_interact
    "Ignore":
        call choice_selected from _call_choice_selected_29
        jump room_closet_interact
#############################################################################################
# STAIRCASE
#############################################################################################
label staircaise_01:
    stop ambiance fadeout 1
    play audio "sfx/amb_steps_01.mp3"
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_10
    scene bgmovie
    show bgstaircase_01
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in a staircase."
jump room_staircase_interact
label room_staircase_interact:
 call screen room_staircase_interact
screen room_staircase_interact:
 if event1 == True:
     imagebutton:
         xpos 0.48
         ypos 0.57
         idle "ui/ui_interact_idle.png"
         hover "ui/ui_interact_hover.png"
         action Jump("stairs_01")
         hover_sound "sfx/sfx_ui_hover_01.mp3"
         activate_sound "sfx/sfx_ui_select_01.mp3"
 if event2 == True:
     imagebutton:
         xpos 0.22
         ypos 0.22
         idle "ui/ui_interact_idle.png"
         hover "ui/ui_interact_hover.png"
         action Jump("window_03")
         hover_sound "sfx/sfx_ui_hover_01.mp3"
         activate_sound "sfx/sfx_ui_select_01.mp3"
label stairs_01:
    call walk_01 from _call_walk_01_24
    pause 0.2
    play audio "sfx/sfx_wood_creak_01.mp3"
    $ event1 = False
    show mc backr:
        xpos 0.32
        ypos 0.52
    with dissolve
menu:

    "STAIRS" "The staircase to the first floor. It's pitch-dark, and the steps look uneven and dangerously dilapidated."
    "Go down into the darkness.{i}{color=[check_colo_02]}  (Perception){/i}{/color}":
        call choice_selected from _call_choice_selected_30
        hide mc
        with dissolve
        call roll_mnd from _call_roll_mnd
        if success == True:
            play audio "sfx/sfx_wood_creak_01.mp3" volume 0.4
            play audio "sfx/sfx_steps_02.mp3"
            "{color=[check_colo_01]} Perception check: Success. {/color}\n\n You descend with precaution, and arrive on the lower floor."
            jump exit_01
        else:
            play audio "sfx/sfx_falling_stairs_01.mp3"
            "{color=[check_colo_01]} Perception check: Failure. {/color} \n\n You stumble and fall down the stairs.{b}{color=[hlt_colo_01]}-2 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_5
            $ stat_hlt -= 2
            call death_check from _call_death_check_11
            pause 1
            jump exit_01
    "Light your way down. {b}{color=[fir_colo_01]} -1 {image=icon_fir} {/b}{/color}" if stat_fir>0:
        call choice_selected from _call_choice_selected_31
        pause 0.2
        play audio "sfx/sfx_match_use_01.mp3"
        $stat_fir -=1
        hide mc
        with dissolve
        pause 0.1
        play audio "sfx/sfx_wood_creak_01.mp3" volume 0.4
        play audio "sfx/sfx_steps_02.mp3"
        "With the light of a match, you descend the stairs to the lower floor. "
        jump exit_01
label window_03:
    call walk_01 from _call_walk_01_25
    pause 0.2
    play audio "sfx/sfx_wood_creak_01.mp3"
    $ event2 = False
    show mc backl:
        xpos 0.2
        ypos 0.32
    with dissolve
    "WINDOW" "The boards barricading the window {b}{color=[txt_colo_01]}won't budge{/b}{/color}."
    jump room_staircase_interact
#############################################################################################
# STAR ROOM
#############################################################################################
label stardoor_01:
    stop ambiance fadeout 1
    # play ambiance "sfx/amb_steps_01.mp3"
    scene black
    with fade
    call room_events_reset from _call_room_events_reset_11
    scene bgmovie
    show bg_stardoor_01
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in a strange empty room."
    jump room_stardoor_interact
label room_stardoor_interact:
    call screen room_stardoor_interact
screen room_stardoor_interact:
    if event1 == True:
        imagebutton:
            xpos 0.437
            ypos 0.27
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("stardoor_use")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    if event2 == True:
        imagebutton:
            xpos 0.21
            ypos 0.22
            idle "ui/ui_interact_idle.png"
            hover "ui/ui_interact_hover.png"
            action Jump("window_02")
            hover_sound "sfx/sfx_ui_hover_01.mp3"
            activate_sound "sfx/sfx_ui_select_01.mp3"
    imagebutton:
        xpos 0.47
        ypos 0.74
        idle "ui/ui_exit_idle.png"
        hover "ui/ui_exit_hover.png"
        action Jump("closet_01")
        hover_sound "sfx/sfx_ui_hover_01.mp3"
        activate_sound "sfx/sfx_ui_select_01.mp3"
label stardoor_use:
    $ event1 = False
    call walk_01 from _call_walk_01_26
    pause 0.2
    # play audio "sfx/sfx_metal_01.mp3"
    show mc backr:
        xpos 0.35
        ypos 0.32
    with dissolve
    if stat_star == 4:
        jump stardoor_use_yes
    else:
        jump stardoor_use_no
label stardoor_use_yes:
menu:
    "STRANGE PAINTED DOOR""You feel a powerful energy, as you recall the 4 star symbols you observed earlier."
    "Interact with the door":
        jump stardoor_open
    "Ignore":
        call choice_selected from _call_choice_selected_32
        jump room_stardoor_interact
label stardoor_use_no:
menu:
    "STRANGE PAINTED DOOR""You didn't find enough {b}{color=[txt_colo_01]}stars{/b}{/color} to enter."
    "Ignore":
        call choice_selected from _call_choice_selected_33
        jump room_stardoor_interact
label stardoor_open:
    stop music fadeout 1
    play audio "sfx/sfx_impact_01.mp3"
    play audio "sfx/sfx_stardoor_01.mp3"
    show bg_stardoor_02
    show mc backr at entrance_slot_01
    with Dissolve(4)
    "You are swallowed up by the shining door."
#############################################################################################
# FLOWER FIELD
#############################################################################################
label flower_field_01:
    scene bgflower_01
    show mc backr at entrance_slot_01
    show bgflower_02
    show bgwhite
    with Dissolve(2)
    # call room_events_reset from _call_room_events_reset_5
    "You remain blind for a long time, blinded by the surrounding light. \n\n
    But eventually, your sight returns, and you discover a {b}{color=[txt_colo_01]}landscape that makes no sense{/b}{/color}."
    #play music "mus/mus_room_01.mp3"
    play music "mus/mus_flowerfield_01.mp3" fadein 0.5
    hide bgwhite
    with Dissolve(2)
    "You've arrived in a vast {b}{color=[txt_colo_01]}field of flowers{/b}{/color}, stretching as far as the eye can see.\n\nThe flowers, caressed by a gentle breeze, spread their sweet fragrance.\n\n
     The petals are {b}{color=[txt_colo_01]}luminescent{/b}{/color}, and {b}{color=[txt_colo_01]}hypnotic{/b}{/color}."
    "When you look up, you see a constellation of stars in a {b}{color=[txt_colo_01]}deep, black sky{/b}{/color}. \n\n
    But it doesn't really look like a night sky. \n\n It's more like you're lost in {b}{color=[txt_colo_01]}deep space{/b}{/color}."
    pause 0.5
    play audio "sfx/sfx_impact_01.mp3"
    show starqueen
    with Dissolve(2)
    b"Congratulations. \n\nYou've found the {b}{color=[txt_colo_01]}hidden stars {/b}{/color} I left behind.\n\nWe never wanted to land in your world.\n And now we're trapped in a perverse cycle."
    b"I can give you a {b}{color=[txt_colo_01]}gift{/b}{/color}.\n\n Or give you a {b}{color=[txt_colo_01]}duty{/b}{/color}."
menu:
    b"You can {b}{color=[txt_colo_01]}stay here{/b}{/color}. \nSmell the flowers for eternity, and open your mind to {b}{color=[txt_colo_01]}all the secrets of the universe{/b}{/color}.
    \n\nOr you can return to your world as {b}{color=[txt_colo_01]}a Herald {/b}{/color}, and {b}{color=[txt_colo_01]}punish {/b}{/color} those who have perverted the very essence of flowers, rectifying the balance of the universe."
    "{i}\"I want to stay here.\"{/i}":
        call choice_selected from _call_choice_selected_46
        "So be it. \n\nWelcome home."
        show black
        hide screen stats_UI
        with Dissolve(2)
        "You came to find secrets, but now all the secrets of the universe will be revealed to you. \n\nForever under the starry sky, you'll see the whole universe, and beyond."
        play audio "sfx/sfx_impact_01.mp3"
        "YOU GOT ENDING 3/4
        \n\n \"One with the flowers\""
        jump credits_01
    "{i}\"I will be your Herald.\"{/i}":
        call choice_selected from _call_choice_selected_47
        b"Thank you. \n\nMay your blade guide you, Herald."
        $ ending = 3
        $ ending_locked = True
        play audio "sfx/sfx_stardoor_01.mp3"
        stop music fadeout 2
        show bgwhite
        with Dissolve(2)
        scene bgmovie behind bgwhite
        show bg_stardoor_01 behind bgwhite
        show mc frontl behind bgwhite:
            xpos 0.35
            ypos 0.32
        hide bgwhite
        with Dissolve(2)
        play music "mus/mus_exploration_02.mp3"
        play audio "sfx/sfx_metal_02.mp3"
        "You've received the {b}{color=[txt_colo_01]}Herald's sword{/b}{/color}, a strange ebony blade with plant-like shapes."
        jump room_stardoor_interact


label window_02:
    call walk_01 from _call_walk_01_27
    pause 0.2
    play audio "sfx/sfx_wood_creak_01.mp3"
    $ event2 = False
    show mc backl:
        xpos 0.18
        ypos 0.32
    with dissolve
    "WINDOW" "You look outside. You're now on the {b}{color=[txt_colo_01]}ground floor{/b}{/color}.  \n\n Alas, the boards barricading the window {b}{color=[txt_colo_01]}won't budge{/b}{/color}."
    jump room_stardoor_interact
#############################################################################################
# EXIT
#############################################################################################
label exit_01:
    stop ambiance fadeout 0.5
    scene black
    with fade
    play music "mus/mus_mainmenu_01.mp3" fadein 0.5
    call room_events_reset from _call_room_events_reset_12
    scene bgmovie
    show bgexit_01
    show mc backr at entrance_slot_01
    with Dissolve(2)
    "You arrive in the entrance hall.\n\n You see the large doors leading to the {b}{color=[txt_colo_01]}outside{/b}{/color}, and through the filthy glass, the sun's rays.\n\n  Freedom.\n\n {b}{color=[txt_colo_01]}The exit{/b}{/color}."
label room_exit_interact1:
 call screen room_exit_interact1
screen room_exit_interact1:
  imagebutton:
     xpos 0.55
     ypos 0.82
     idle "ui/ui_exit_idle.png"
     hover "ui/ui_exit_hover.png"
     action Jump("confrontation_01")
     hover_sound "sfx/sfx_ui_hover_01.mp3"
     activate_sound "sfx/sfx_steps_02.mp3"
label confrontation_01:
    stop music fadeout 2
    show mc backr:
        xpos 0.32
        ypos 0.51
    with Dissolve(2)
    play audio "sfx/sfx_steps_03.mp3"
    pause 0.2
    play music "mus/mus_npc_01.mp3"
    show npc1 frontl:
        xpos 0.4
        ypos 0.43
    with Dissolve(2)
menu:
    a"Hello friend.\n\n I see you found your way out. \n\n Good. I was very worried."
    "{i}\"Stop. I know it was you who brought me here.\"{/i}"if ending != 3:
        a"That's true.\n\n But it was a {b}{color=[txt_colo_01]}misunderstanding{/b}{/color} on my part."
        jump confrontation_02
    "{i}\"Let me pass, I'm leaving now.\"{/i}"if ending != 3:
        a"Let me first explain myself, please."
        jump confrontation_02
    "{i}\"I saw the flowers. I am the Herald.\"{/i}" if ending == 3:
        stop music fadeout 1
        jump herald_fight_01
label herald_fight_01:
    play music "mus/mus_flowerfield_01.mp3"
menu:
    a"...What? No, it can't be. \n\nAfter everything I've done, everything I've eaten, {b}{color=[txt_colo_01]}I should have been chosen{/b}{/color}! \n\nIT'S NOT FAIR, IT'S NOT FAIR!!!"
    "Attack him with the Herald's sword.":
            # play audio "sfx/sfx_ui_star_01.mp3"
            jump npc1_fight_05
label confrontation_02:
    a"I mistook you for a {b}{color=[txt_colo_01]}resident{/b}{/color} of this town.\n\nI didn't realize my mistake until it was too late.\n\nI tied you up in the abandonned school, then you freed yourself, and here I was with a {b}{color=[txt_colo_01]}wandering problem... You."
    stop music fadeout 2
    play ambiance "sfx/amb_tension_02.mp3" fadein 0.5
    a"So I had to improvise.
    \n\nI {b}{color=[txt_colo_01]}spied on you{/b}{/color} through the holes in the walls.
    \n\nI had to make sure you {b}{color=[txt_colo_01]}didn't find out too much{/b}{/color} about the town's dirty little secrets.
    \n\nAnd the answer is..."
    if stat_knw <4:
        a"{color=[check_colo_01]}(Your secret knowledge score is [stat_knw]/7){/color}
        \n\nThat {b}{color=[txt_colo_01]}you know nothing{/b}{/color}. Which is very smart of you.
        \n\n{b}{color=[txt_colo_01]}Curiosity killed the cat{/b}{/color}, as they say."
        jump confrontation_02a
    else:
        a"{color=[check_colo_01]}(Your secret knowledge score is [stat_knw]/7){/color}
        \n\n{b}{color=[txt_colo_01]}You know too much{/b}{/color}.
        \n\nWhy dig up the town's {b}{color=[txt_colo_01]}old secrets{/b}{/color}? \n\n You should have left us alone. I can't let you go.  "
        jump confrontation_02b
label confrontation_02a:
    $ event1 = False
    if ending_locked == False:
        $ ending = 1
    a"You're no danger to us. And I have no reason to be a danger to you.\n\n So, let's put the past behind us, and {b}{color=[txt_colo_01]}part ways here{/b}{/color}."
    a"{b}{color=[txt_colo_01]}You're free to go{/b}{/color}. Goodbye.\n\n Oh and of course..."
    a"{b}{color=[txt_colo_01]}NEVER COME BACK!{/b}{/color}"
    stop ambiance fadeout 3
    play audio "sfx/sfx_steps_03.mp3"
    hide npc1
    with dissolve
    "Before you can do anything, the strange man flees, disappearing forever into the school corridors."
    play music "mus/mus_mainmenu_01.mp3" fadeout 0.5
    jump room_exit_interact2
label confrontation_02b:
menu:
    a"You should have known that {b}{color=[txt_colo_01]}curiosity killed the cat{/b}{/color}.
    \n\n You've nearly {b}{color=[hlt_colo_01]}died{/b}{/color} or {b}{color=[snt_colo_01]}gone mad{/b}{/color} with every secret you've discovered, and I'm here to {b}{color=[txt_colo_01]}finish the job{/b}{/color}!"
    "Who are you really?":
        a"I'm a resident of this town. \n\nA former student of this school. \n\nAnd I was there when it all began. When the blue flowers appeared in the nearby fields."
        jump confrontation_03
    "What have you done to the residents?":
        a"I'm not the only one responsible. There were a lot of us. \n\nWhen the blue flowers appeared in the nearby fields. "
        jump confrontation_03
    #"Attack him with your fists. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
    #     jump confrontation_03
label confrontation_03:
    a"At first, we {b}{color=[txt_colo_01]}ate the flowers{/b}{/color}, and we became intoxicated by its glorious {b}{color=[txt_colo_01]}power{/b}{/color}.\n\n When the wild dogs came and ate all the flowers, we {b}{color=[txt_colo_01]}ate the dogs{/b}{/color}, just so we could taste the flower within them. \n\nAnd when there were {b}{color=[txt_colo_01]}no more dogs left{/b}{/color}..."
    play audio "sfx/sfx_impact_01.mp3"
menu:
    a"{b}{color=[txt_colo_01]}We ate the ones \n\nwho had eaten the dogs{/b}{/color}."
    "The residents ate each other?":
        a"Many have just fled the town. But we who stayed {b}{color=[txt_colo_01]}hunted each other down{/b}{/color}."
        jump confrontation_04
    "You're crazy.":
        jump confrontation_04
label confrontation_04:
    a"The taste of the sweet petals lingers, and matures through each ingestion.\n\n
    One day, only one of us will remain.
    \n\n{b}{color=[txt_colo_01]}The Great Glutton{/b}{/color}.
    \n\nThe last inhabitant of the town. Who will have the flower all within him hehehe.\n\n
    ALL ITS POWER!"
    stop ambiance fadeout 1
    play music "mus/mus_npc_tension_01.mp3"
    jump npc1_fight_01
label npc1_fight_01:
    a"AND I WON'T LET ANYONE RUIN THIS VIRTUOUS CIRCLE BY STICKING THEIR NOSE IN OUR BUSINESS!!!"
menu:
    "He's getting ready to leap out at you."
    "Evade the attack. {i}{color=[check_colo_02]}  (Perception){/i}{/color}":
        call choice_selected from _call_choice_selected_34
        call roll_mnd from _call_roll_mnd_1
        play audio "sfx/sfx_woosh_01.mp3"
        if success == True:
            "{color=[check_colo_01]} Perception check: Success. {/color}\n\n You evade the attack."
            jump npc1_fight_02
        else:
            "{color=[check_colo_01]} Perception check: Failure. {/color} \n\n His attack hits you with full force. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_6
            $ stat_hlt -= 3
            call death_check from _call_death_check_12
            jump npc1_fight_02
    "Block the attack. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
        call choice_selected from _call_choice_selected_35
        call roll_str from _call_roll_str_2
        play audio "sfx/sfx_woosh_01.mp3"
        if success == True:
            "{color=[check_colo_01]} Strength check: Success. {/color}\n\n You evade the attack.  "
            jump npc1_fight_02
        else:
            "{color=[check_colo_01]} Strength check: Failure. {/color} \n\n His attack hits you with full force. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_7
            $ stat_hlt -= 3
            call death_check from _call_death_check_13
            jump npc1_fight_02
    "Hope he misses. {i}{color=[check_colo_02]}  (Luck){/i}{/color}":
        call choice_selected from _call_choice_selected_36
        call roll_lck from _call_roll_lck_5
        play audio "sfx/sfx_woosh_01.mp3"
        if success == True:
            "{color=[check_colo_01]} Luck check: Success. {/color}\n\n He stumbles and his attack narrowly misses you.  "
            jump npc1_fight_02
        else:
            "{color=[check_colo_01]} Luck check: Failure. {/color} \n\n His attack hits you with full force. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_8
            $ stat_hlt -= 3
            call death_check from _call_death_check_14
            jump npc1_fight_02

label npc1_fight_02:
menu:
    a"You little brat... \n\n I should have {b}{color=[txt_colo_01]}finished the job{/b}{/color} when I had the chance."
    "Attack him with your fists. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
        call choice_selected from _call_choice_selected_37
        call roll_str from _call_roll_str_3
        if success == True:
            "{color=[check_colo_01]} Strength check: Success. {/color}
            \n\n You jump on him and begin to pummel him furiously, until he collapses to the ground."
            jump npc1_fight_05
        else:
            "{color=[check_colo_01]} Strength check: Failure. {/color}
            \n\n You jump at him, but the {b}{color=[txt_colo_01]}weakness{/b}{/color} of your blow has {b}{color=[txt_colo_01]}little effect{/b}{/color}.
            \n\nThe stranger isn't hurt, but you can feel his anger behind his mask."
            jump npc1_fight_03

    "Attack him with your pitchfork. {i}{color=[check_colo_02]}  (Perception){/i}{/color}" if have_shovel == True:
        call choice_selected from _call_choice_selected_38
        call roll_mnd from _call_roll_mnd_2
        if success == True:
            "{color=[check_colo_01]} Perception check: Success. {/color}\n\n You use the length of the pitchfork to attack him, keeping your distance, and with one great thrust, drive the spikes of your weapon into his stomach."
            jump npc1_fight_05
        else:
            "{color=[check_colo_01]} Perception check: Failure. {/color}\n\n You use the length of the fork to attack him, keeping your distance, but don't find the opportunity to attack."
            jump npc1_fight_03
    "Attack him with your screwdriver. {i}{color=[check_colo_02]}  (Dexterity){/i}{/color}" if have_screwdriver == True:
        call choice_selected from _call_choice_selected_39
        call roll_dex from _call_roll_dex_1
        if success == True:
            "{color=[check_colo_01]} Strength check: Success. {/color}
            \n\nWith the energy of desperation, you leap at him, screaming, and drive your screwdriver through his neck."
            jump npc1_fight_05
        else:
            "{color=[check_colo_01]} Strength check: Failure. {/color}
            \n\n You miss your attack.
            \n\nThe stranger isn't hurt, but you can feel his anger behind his mask."
            jump npc1_fight_03

label npc1_fight_03:
menu:
    a"TAKE THAT!!!"
    "Evade the attack. {i}{color=[check_colo_02]}  (Perception){/i}{/color}":
        call choice_selected from _call_choice_selected_40
        call roll_mnd from _call_roll_mnd_3
        play audio "sfx/sfx_woosh_01.mp3"
        if success == True:
            "{color=[check_colo_01]} Perception check: Success. {/color}\n\n You evade the attack.  "
            jump npc1_fight_04
        else:
            "{color=[check_colo_01]} Perception check: Failure. {/color} \n\n His attack hits you with full force. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_9
            $ stat_hlt -= 3
            call death_check from _call_death_check_15
            jump npc1_fight_04
    "Block the attack. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
        call choice_selected from _call_choice_selected_41
        call roll_str from _call_roll_str_4
        if success == True:
            play audio "sfx/sfx_woosh_01.mp3"
            "{color=[check_colo_01]} Strength check: Success. {/color}\n\n You evade the attack.  "
            jump npc1_fight_04
        else:
            "{color=[check_colo_01]} Strength check: Failure. {/color} \n\n His attack hits you with full force. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_10
            $ stat_hlt -= 3
            call death_check from _call_death_check_16
            jump npc1_fight_04
    "Hope he misses. {i}{color=[check_colo_02]}  (Luck){/i}{/color}":
        call choice_selected from _call_choice_selected_42
        call roll_lck from _call_roll_lck_6
        play audio "sfx/sfx_woosh_01.mp3"
        if success == True:
            "{color=[check_colo_01]} Luck check: Success. {/color}\n\n He stumbles and his attack narrowly misses you.  "
            jump npc1_fight_04
        else:
            "{color=[check_colo_01]} Luck check: Failure. {/color} \n\n His attack hits you with full force. {b}{color=[hlt_colo_01]}-3 {image=icon_hlt} {/b}{/color}"
            call hlt_loss from _call_hlt_loss_11
            $ stat_hlt -= 3
            call death_check from _call_death_check_17
            jump npc1_fight_04
label npc1_fight_04:
menu:
    a"The power of flowers flows through me, you don't stand a chance!"
    "Attack him with your fists. {i}{color=[check_colo_02]}  (Strength){/i}{/color}":
        call choice_selected from _call_choice_selected_43
        "{color=[check_colo_01]} Strength check: Success. {/color}
        \n\nYou jump on him and begin to pummel him furiously, until he collapses to the ground."
        jump npc1_fight_05
    "Attack him with your pitchfork. {i}{color=[check_colo_02]}  (Perception){/i}{/color}" if have_shovel == True:
        call choice_selected from _call_choice_selected_44
        "{color=[check_colo_01]} Perception check: Success. {/color}\n\n You use the length of the pitchfork to attack him, keeping your distance, and with one great thrust, drive the spikes of your weapon into his stomach."
        jump npc1_fight_05
    "Attack him with your screwdriver. {i}{color=[check_colo_02]}  (Dexterity){/i}{/color}" if have_screwdriver == True:
        call choice_selected from _call_choice_selected_45
        "{color=[check_colo_01]} Strength check: Success. {/color}
        \n\nWith the energy of desperation, you leap at him, screaming, and drive your screwdriver through his neck."
        jump npc1_fight_05
label npc1_fight_05:
    play audio "sfx/sfx_attack_01.mp3"
    play audio "sfx/sfx_hurt_02.mp3"
    play audio "sfx/sfx_impact_01.mp3"
    show npc1 hurt
    with dissolve
    a"AAAAARG."
    if ending != 3:
        stop music fadeout 2
    show npc1 dead behind mc:
        xpos 0.38
        ypos 0.5
    with dissolve
    a"My precious petals... \nHow can this be?\n\n I've eaten so much... \n\nEaten so much..."
    if ending_locked == False:
        $ ending = 2
    if ending != 3:
        play music "mus/mus_mainmenu_01.mp3" fadeout 1
    # a"Please, the power must be preserved... Devour my flesh... \n\n So that the magic may continue through you..."
label room_exit_interact2:

    call screen room_exit_interact2
screen room_exit_interact2:
 if event1 == True:
     imagebutton:
         xpos 0.43
         ypos 0.6
         idle "ui/ui_interact_idle.png"
         hover "ui/ui_interact_hover.png"
         action Jump("npc1_corpse_01")
         hover_sound "sfx/sfx_ui_hover_01.mp3"
         activate_sound "sfx/sfx_ui_select_01.mp3"
 imagebutton:
     xpos 0.55
     ypos 0.82
     idle "ui/ui_exit_idle.png"
     hover "ui/ui_exit_hover.png"
     action Jump("outdoor_01")
     hover_sound "sfx/sfx_ui_hover_01.mp3"
     activate_sound "sfx/sfx_steps_02.mp3"

label npc1_corpse_01:
    $ event1 = False
    a"He's dead."
    jump room_exit_interact2
#############################################################################################
# OUTDOOR
#############################################################################################
label outdoor_01:
    scene black
    with fade
    play audio "sfx/sfx_steps_01.mp3"
    pause 0.1
    # play music "mus/mus_mainmenu_01.mp3" fadeout 0.5
    call room_events_reset from _call_room_events_reset_13
    scene bgoutdoor_01
    show mc frontr:
        xpos 0.37
        ypos 0.5
    with Dissolve(2)
    pause 1
    "You feel the air on your face as you gaze out over the schoolyard. \n\n Congratulations, you've survived this terrible journey."
    if ending == 1:
        play audio "sfx/sfx_impact_01.mp3"
        "YOU GOT ENDING 1/4
        \n\n \"Blessed is the ignorant\""
    if ending == 2:
        play audio "sfx/sfx_impact_01.mp3"
        "YOU GOT ENDING 2/4
        \n\n \"Fighting your way out\""
    if ending == 3:
        "As Herald of the Stars, you've righted the wrongs of one sinner. \n\nBut you sense there are others still hidden in the town. \n\nAnd flowers and stars will guide your blade towards them. "
        play audio "sfx/sfx_impact_01.mp3"
        "YOU GOT ENDING 4/4
        \n\n \"Herald of the Stars\""
    jump credits_01
label credits_01:
        "CREDITS""Thank you so much for playing!
        \n\n All art, writing, music, and dev by {b}{color=[txt_colo_01]}Delphin Casado.{/b}{/color}
        \n\n Made for the Game Off game jam 2024.
        \n\n{color=[check_colo_01]}Click to go back to main menu.{/color}"
        jump end

# DEATH
##############################################################
label gameover:
    play audio "sfx/sfx_impact_01.mp3"
    if stat_snt <=0:
        jump gameover_snt
    else:
        jump gameover_hlt
label gameover_snt:
    stop music fadeout 1
    stop ambiance fadeout 1
    scene black
    with fade
    "Your mind is {b}{color=[snt_colo_01]}too tired and disturbed{/b}{/color} to go on, and you collapse to the groun.
    \n\nYou haven't managed to escape from the school, and perhaps haven't discovered all its {b}{color=[txt_colo_01]}secrets {/b}{/color}...
    \n\n{color=[check_colo_01]}Click to go back to main menu.{/color}"
    jump end
    # This ends the game.
label gameover_hlt:
    stop music fadeout 1
    stop ambiance fadeout 1
    scene black
    with fade
    "Your body is {b}{color=[hlt_colo_01]}too bruised and tired{/b}{/color} to go on, and you collapse to the ground.
    \n\nYou haven't managed to escape from the school, and perhaps haven't discovered all its {b}{color=[txt_colo_01]}secrets {/b}{/color}...
    \n\n{color=[check_colo_01]}Click to go back to main menu.{/color}"
    jump end
    # This ends the game.
label end:
    hide screen stats_UI
    with dissolve
    scene black
    with fade
    pause 1
    $ renpy.full_restart()
