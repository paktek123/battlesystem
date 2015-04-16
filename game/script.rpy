#### RISER BATTLE SYSTEM #####


init -1:
    
    # 120, 150 for large enemies
    #image dragon_tile_l = im.Scale("attack_1.png", 120, 150)
    
    ### SPRITES ###
    image sam_1 = im.Scale("sprites/sam_1.png", 270, 500)
    image sam_2 = im.Scale("sprites/sam_2.png", 270, 500)
    image adam_1 = im.Scale("sprites/adam_1.png", 450, 600)
    image adam_2 = im.Scale("sprites/adam_2.png", 450, 600)
    image adam_3 = im.Scale("sprites/adam_3.png", 450, 600)
    image amy_1 = im.Scale("sprites/amy_1.png", 270, 500)
    image amy_2 = im.Scale("sprites/amy_2.png", 270, 500)
    image amy_3 = im.Scale("sprites/amy_3.png", 270, 500)
    image greyson_1 = im.Scale("sprites/greyson_1.png", 330, 500)
    image will_1 = im.Scale("sprites/will_1.png", 270, 500)
    image bison_1 = im.Scale("sprites/bison_1.png", 320, 600)
    image ai_1 = im.Scale("sprites/ai_1.png", 350, 550)
    image monk_1 = im.Scale("sprites/monk_1.png", 350, 550)
    
    ### SPECIAL EFFECTS ###
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    $ red_flash = Fade(.25, 0, .75, color="#ff0000")
    $ black_flash = Fade(.5, 0, .5, color="#000")
    

init python:

    import os
    import copy
    import random
    
        
    ##############################################################################
    # INITIALIZE ASSETS
    #
    
    ### CHARACTERS ###
    
    nar_c = Character('    ',color="#FFFF00", who_color="#FFFF00")
    thug_c = Character('Thug',color="#FFFFFF")
    sam_c = Character('Sam', color="#FFFFFF")
    adam_c = Character('Adam',color="#FFFF00")
    amy_c = Character('Amy',color="#FFFF00")
    greyson_c = Character('Greyson',color="#FFFF00")
    will_c = Character('Will',color="#FFFF00")
    bison_c = Character('Bison',color="#FFFF00")
    ai_c = Character('Ai',color="#FFFF00")
    monk_c = Character('Monk',color="#FFFF00")
        
    ### STAGES (TODO: different tiles) ###
    clearing = Stage('Clearing', 1, 1)        
    forest = Stage('Forest', 1, 1, base_texture="forest_base_texture")
            
    ### SHOP ITEMS ###
    i_heal_paste = ShopItem("Heal Paste", 300, 30, health=30)
    i_chakra_paste = ShopItem("Chakra Paste", 300, 40, chakra=30)
    
    # screen vars
    screen_on = False
    calendar_on = False
    
    battle1 = Battle(id="1", good_team=[], bad_team=[], xpos=100, ypos=100, battle_label="b_battle_1")
    battle2 = Battle(id="2", good_team=[], bad_team=[], xpos=300, ypos=100, battle_label="b_battle_2")
    battle_last = Battle(id="last", good_team=[], bad_team=[], xpos=500, ypos=100, battle_label="b_battle_last")
    
    ALL_BATTLES = [battle1, battle2, battle_last]
    

### DYNAMIC RESOURCES WITHIN THE GAME ###
### THESE NEED TO BE HERE IN ORDER TO PERSIST ON A SAVE ###

label declare_resources:
    
    ### TIME ###
    $ main_time = GameTime(9, 1, 1, 2015)
    
    ### CURRENT SESSION ###
    $ current_session = CurrentSession()
    
    ### EVENTS ###
                    
    $ e_chunin_exams = Event("Chunin Exams", "CE", start=(15, 5), finish=(14, 7), label="chunin_exam")
    $ e_jounin_training = Event("Jounin Training", "JT", frequency=(1, ))
    $ e_jinchurri_attack = Event("Jinchurri Attack", "???",chance=0.02, label="jinchurri_attack", occurrence=0)
    $ e_weapon_discount = Event("Weapon Discount", "WD", frequency=(random.randint(2,30),)) 
    $ e_hospital_discount = Event("Hospital Discount", "HD", frequency=(random.randint(2,30),)) 
    
    $ ALL_EVENTS += [e_chunin_exams, e_jounin_training, e_jinchurri_attack, e_weapon_discount, e_hospital_discount]
    
    # populate events
    $ populate_events()
    
    ### SKILLS AND AI ###
    
    # melee skills
    $ punching_flurry = Skill(name='Punching Flurry', skill_type='melee', label="punchingflurry", range=2, damage=20)
    $ onetwocombo = Skill(name='One Two Combo', skill_type='melee', label="onetwocombo", range=3, damage=30)
    $ jaw_breaker = Skill(name="Jaw Breaker", skill_type='melee', label='jaw_breaker', range=2, damage=40)
    $ thug_smash = Skill(name='Thug Smash', skill_type='melee', label="thug_smash", range=2, damage=25)
    $ lioncombo = Skill('Lion Combo', 'melee', "lioncombo", 3, 2, 5, 20, unlock_exp=300)
    
    # special skills
    $ blasting_kick = Skill(name="Blast Kick", skill_type="special", label="blast_kick", range=3, chakra_cost=30, damage=60)
    $ rise_punch = Skill(name="Rise Punch", skill_type="special", label="rise_punch", range=2, chakra_cost=40, damage=35)
    
    # ranged skills
    $ rock_throw = Skill(name="Rock Throw", skill_type="ranged", label="rock_throw", range=7, chakra_cost=10, damage=15)
    $ distance_hit = Skill(name="Distance Hit", skill_type="ranged", label="distance_hit", range=8, chakra_cost=20, damage=20)
    
    $ substitution = Skill('Substitution', 'ranged', "substitution", 8, 20, 15, 0, stun=True)
    
    # defensive skills
    $ metal_jacket = Skill(name='Metal Jacket', skill_type='defence', label='damagereduction', range=12, duration=3)
    $ intimidate = Skill(name='Intimidate', skill_type='defence', label='dampen', range=6, duration=3)
    
    $ damage_reduction = Skill('Focus', 'defence', 'damagereduction', 12, 1, 10, duration=2, unlock_exp=300)
    $ chakra_defence = Skill('Chakra Defence', 'defence', 'chakradefence', 12, 2, 15, duration=3, unlock_exp=500)
    $ substitution = Skill('Substitution', 'counter', "substitution", 8, 20, 15, 0, stun=True)
    $ reflect = Skill('Reflect', 'defence', 'reflect', 12, 20, 20, duration=2, unlock_exp=1500)
    $ dampen = Skill('Dampen', 'defence', 'dampen', 6, 30, 30, duration=3, unlock_exp=2000)
    $ yata_mirror = Skill('Yata Mirror', 'defence', 'ignore', 12, 50, 50, duration=2, unlock_exp=2500)
    
    ### WEAPONS ###
    $ w_knife = Weapon(name='Knife', price=30, range=2, chakra_cost=5, damage=25)
    $ w_bat = Weapon(name='Bat', price=50, range=3, chakra_cost=10, damage=30)
    $ w_brass_knuckles = Weapon(name='Brass Knuckles', price=100, range=1, chakra_cost=5, damage=50)
    $ w_bbgun = Weapon(name='BB Gun', price=400, range=10, chakra_cost=0, damage=40)

    ### AI ###
    
    $ THUG_MELEE_SKILL_SET = [onetwocombo, jaw_breaker, thug_smash, metal_jacket, intimidate, w_knife, w_bat]
    $ THUG_RANGED_SKILL_SET = [rock_throw, distance_hit, metal_jacket, w_bbgun]
    
    ### PLAYERS AND TEAMS ###
    
    $ lvl_1_thug_melee = LevelledPlayer(lvl=1, skill_pool=THUG_MELEE_SKILL_SET, character=thug_c)
    $ lvl_1_thug_ranged = LevelledPlayer(lvl=1, skill_pool=THUG_RANGED_SKILL_SET, character=thug_c)
    $ lvl_4_thug_melee = LevelledPlayer(lvl=4, skill_pool=THUG_MELEE_SKILL_SET, character=thug_c)
    $ lvl_4_thug_ranged = LevelledPlayer(lvl=4, skill_pool=THUG_RANGED_SKILL_SET, character=thug_c)
    
    # give him unique skill set
    $ lvl_8_bison_melee = LevelledPlayer(lvl=8, name="Bison", skill_pool=THUG_MELEE_SKILL_SET, character=bison_c, hudpic="bison_hud")
    $ lvl_15_adam = LevelledPlayer(lvl=15, skill_pool=THUG_RANGED_SKILL_SET, character=adam_c, picname="adam_1")
    $ lvl_15_ai = LevelledPlayer(lvl=15, skill_pool=THUG_RANGED_SKILL_SET, character=ai_c, picname="ai_1")
    $ lvl_15_monk = LevelledPlayer(lvl=15, skill_pool=THUG_RANGED_SKILL_SET, character=monk_c, picname="monk_1")
    
    # This has to be here because its dynamic
    $ hero_c = Character('NO NAME',color="#FFFF00")
    
    $ hero = Player(name='NO NAME', picname="hero_tile_r", character=hero_c, tilepic="hero_tile_r", hudpic='hero_hud', 
                  hp=100, maxhp=100, chakra=80, maxchakra=80, 
                  strength=1, speed=1, evasion=1, defence=1, stamina=1, base_hit_rate=80, 
                  facing='right', 
                  meleeskills=[punching_flurry], specialskills=[], rangedskills=[], 
                  items=[], defensiveskills=[damage_reduction], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[], 
                  home_village=None)
    
    $ thug = Player(name='Thug', picname="thug_tile_r", character=thug_c, tilepic="thug_tile_r", hudpic='thug_hud', 
                  hp=100, maxhp=100, chakra=80, maxchakra=80, 
                  strength=5, speed=5, evasion=1, defence=1, stamina=1, base_hit_rate=80, 
                  facing='left', 
                  meleeskills=[onetwocombo], specialskills=[], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_knife], 
                  home_village=None)
    
    # unique moves
    $ sam = Player(name='Sam', picname="thug_tile_r", character=thug_c, tilepic="thug_tile_r", hudpic='thug_hud', 
                  hp=150, maxhp=150, chakra=120, maxchakra=120, 
                  strength=9, speed=6, evasion=6, defence=8, stamina=6, base_hit_rate=80, 
                  facing='left', 
                  meleeskills=[onetwocombo], specialskills=[blasting_kick], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_knife, w_brass_knuckles], 
                  home_village=None)
    
    $ will = Player(name='Will', picname="will_tile_r", character=thug_c, tilepic="will_tile_r", hudpic='will_hud', 
                  hp=200, maxhp=200, chakra=150, maxchakra=150, 
                  strength=10, speed=6, evasion=6, defence=10, stamina=10, base_hit_rate=90, 
                  facing='left', 
                  meleeskills=[onetwocombo, jaw_breaker], specialskills=[blasting_kick], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_brass_knuckles], 
                  home_village=None)
    
    $ greyson = Player(name='Greyson', picname="will_tile_r", character=thug_c, tilepic="will_tile_r", hudpic='greyson_hud', 
                  hp=120, maxhp=120, chakra=60, maxchakra=60, 
                  strength=7, speed=3, evasion=3, defence=4, stamina=3, base_hit_rate=70, 
                  facing='left', 
                  meleeskills=[onetwocombo, jaw_breaker], specialskills=[], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_brass_knuckles], 
                  home_village=None)
    
    $ team_first = Team("First Team", lvl_15_adam, [will, hero, greyson])
    $ hero.sensei = lvl_15_adam
    
    $ ALL_PLAYERS = [hero, thug, will, lvl_1_thug_melee, lvl_1_thug_ranged]
    $ ALL_CHARACTERS = [c.character for c in ALL_PLAYERS]
    
    ### VILLAGE AND LOCATIONS ###

    ### Use existing already defined labels not new ones 
    
    $ l_hospital = Location('Hospital', 'village_hospital', 'street_4', events=[e_hospital_discount])
    $ l_police_station = Location('Police Station', 'village_police_station', 'building_1', events=[e_weapon_discount]) # weapon shop
    $ l_level_up = Location('Level Up', 'village_levelup', 'apartment_1')
    $ l_training_ground = Location('Training', 'village_training', 'forest_2')
    $ l_town_mission = Location('Mission', 'village_missions', events=[],)
    $ l_apartment = Location('Apartment', 'village_home', 'apartment_1')

    # locations that exist in each village
    $ l_travel = Location('Travel', 'village_travel')
    $ l_arena = Location('Arena', 'village_arena')
    $ l_jounin_station = Location('Jounin Standby Station', 'village_jounin_station', events=[e_jounin_training])
    $ l_intelligence_division = Location('Intelligence Division', 'village_intelligence_division')
    $ l_home = Location('Home', 'village_home')
    
    $ BASE_LOCATIONS = [l_level_up, l_training_ground, l_town_mission, l_apartment, l_hospital, l_police_station]
    
    $ middle_town = Village(1, "Middle Town", lvl_15_adam, marker_xpos=0.40, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="middle_town", mission_locations=2, wealth=50)
    $ east_town = Village(2, "East Town", lvl_15_monk, marker_xpos=0.60, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="east_town", mission_locations=2)    
    $ south_town = Village(3, "South Town", lvl_15_ai, marker_xpos=0.45, marker_ypos=0.65, map="town_map_1", locations=BASE_LOCATIONS, village_tag="south_town", mission_locations=2)
    $ west_town = Village(4, "West Town", None, marker_xpos=0.25, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="west_town", mission_locations=2)    
    $ north_town = Village(5, "North Town", None, marker_xpos=0.25, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="north_town", mission_locations=2)    
        
    $ ALL_VILLAGES = [east_town, south_town, middle_town]
    
    ### SHOPS ###
    $ hospital_shop = Shop("Hospital", 'apartment_1', items=[i_heal_paste, i_chakra_paste])
    $ weapon_shop = Shop("Weapons", 'building_1', items=[w_knife, w_bbgun, w_brass_knuckles, w_bat])
    
    ### MISSIONS (BATTLES) ###
            
    # basic missions
    $ m_secure_hospital = LabelMission('Secure Hospital', 'prologue_hospital', hours=11, location=l_hospital)
    $ m_secure_police_station = LabelMission('Secure Police Station', 'prologue_police_station', hours=11, location=l_police_station)
    $ m_infiltrate_hold = LabelMission('Infiltrate Hold', 'mission_infiltrate_hold', hours=5, rank='D')
    $ m_defeat_sam = LabelMission('Defeat Sam', 'mission_defeat_sam', hours=6, rank='C')
    
    $ m_d1 = BasicMission('Farming', hours=12)
                                                   
    $ ALL_MISSIONS = [m_secure_hospital, m_secure_police_station, m_infiltrate_hold, m_defeat_sam]
    
    return
    
            
##############################################################################
# STORY / GAME START
#
image creation_background:
    "street_1 night" with irisin
    pause 10.0
    "street_2 night" with irisin
    pause 10.0
    "street_3 night" with irisin
    pause 10.0
    "street_4 night" with irisin
    pause 10.0
    repeat
    
label start:
    
    call declare_resources
    
    $ at_map = False
        
    jump character_creation
    
label character_creation:
    show creation_background
    
    # Assign a default value
    $ player_name="Maxwell"
    
    $ player_name = renpy.input("Set player name: ")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Maxwell"
        
    $ hero_c.name = player_name.lower().capitalize()
    $ hero.name = player_name.lower().capitalize()
    
    nar_c "Please choose stats for [hero.name]."
    
    $ current_session.main_player = hero
    $ current_session.main_player.allocation_points = 10
    
label prologue1:
    
    scene street_3 night with dissolve
    nar_c "The sunsets and I finally end my shift."
    nar_c "It is a little late, I usually leave before its dark."
    nar_c "...."
    nar_c "I make my way towards the underpass."
    scene underpass_1 night with dissolve
    nar_c "My house is about a fifteen minute walk from my work place."
    nar_c "..."
    nar_c "In the distance I see two people wrestling on the road in front of me."
    nar_c "They clearly don't care about getting run over by cars."
    show sam_1 with dissolve
    "Thug 1" "You bastard! I'll make sure you never stand up again!"
    "Thug 2" "I'll.... oooff."
    hide sam_1 with dissolve
    nar_c "Both of them are throwing punches at each other and rolling on the ground."
    nar_c "Just seeing those two go at it, puts me at unease."
    nar_c "My heart starts pounding faster and body fills up with adrenaline."
    nar_c "..."
    nar_c "They are fighting in front of me, I need to somehow get round them and call the police."
    "Thug 2" "Oooooffff." with sshake
    nar_c "One of the thugs flies off to the side and bangs his head against the wall."
    nar_c "There are blood stains everywhere, he soon looses conciousness."
    show sam_1 with dissolve
    "Thug 1" "You!"
    nar_c "He looks at me, I freeze."
    nar_c "My heart is pounding, I really don't want to be involved in this..."
    nar_c "...."
    hide sam_1 with dissolve
    nar_c "I turn around and make a run for it."
    scene street_2 night with dissolve 
    nar_c "I quickly take a turn into a side street." with sshake
    hero_c "Hufff.... hufff...."
    nar_c "I hear police sirens in the background... what is going on!?"
    hero_c "My head is going crazy with random thoughts, I need to get it together."
    hero_c "Hufff...  hufff...."
    nar_c ".... I get pushed to the ground." with sshake
    hero_c "Owww...."
    nar_c "There is a sharp pain in my upper arm."
    nar_c "I look around to try to work out what just happenned."
    show sam_1 with dissolve
    "Thug" "You thought you could get away from me!?"
    hero_c "How... did..."
    nar_c "I am lost for words, how did he get behind me?"
    nar_c "He must have pushed me to the ground from behind."
    "Thug" "You saw me do that, I can't let you just leave without making sure you don't squeak."
    nar_c "He grabs me by the collar of my shirt."
    hero_c "Ughhh...."
    nar_c "My heart is pounding very hard... I don't want to get hurt..."
    hero_c "Why are you doing this? I won't tell the cops, please let me go."
    "Thug" "Here is a present." with sshake
    hero_c "Ooooffff...." 
    nar_c "He punches me in my stomach and throws me to the ground."
    nar_c "A sharp pain starts building up around my abdomen."
    "Thug" "If I ever see your face again, I will pound your face in."
    "Thug" "Don't even think of talking to the police."
    hide sam_1 with dissolve
    nar_c "He turns around and starts to walk away."
    ### TODO: Add some motivation for our hero to get back on this feet and challenge Mr Thug to a fight
    ### Maybe some sort of past flashback or something
    nar_c "I fix my collar and stand up."
    hero_c "Ohey... Bastard..."
    hero_c "You think you can do whatever you want, let me kick your ass."
    nar_c "As soon as he hears this, he turns around with an angry expression."
    show sam_1 with dissolve
    "Thug" "Say that again!"
    nar_c "He throws a punch..."
    nar_c "... I grab his fist and push him away."
    "Thug" "Heh.... I'll pound you to death!"
    nar_c "I know I can't go back now but maybe that is what I want."
    hide sam_1 with dissolve
    $ renpy.call('fight', hero, thug, [], [], forest, lose_label='prologue2', draw_label='prologue2', fight_limit=5)
    # fight redirects to prologue2 label
    return
    
label prologue2:
    scene street_2 night with dissolve
    hero_c "...." with sshake
    hero_c "Huff...."
    hero_c "Ughhh...." with red_flash
    nar_c "Blood splatters everywhere."
    nar_c "My body is covered in bruises and cuts from his knife."
    show sam_1 with dissolve
    nar_c "He is also in a similar condition, I am surprised he is standing."
    "Thug" "Hehh.... hehhh.... "
    nar_c "He gives off a strange laugh."
    "Thug" "You haven't seen anything yet!"
    nar_c "He tries to attack me..."
    "Thug" "Gahhh... cough..." with red_flash
    nar_c "He coughs blood, the damage must have gotten to him."
    nar_c ".... there is a sudden pause, both of us know if we continue this won't end well for us."
    "Thug" "You are lucky this time, I will find you and finish you off."
    hero_c "Just try it."
    nar_c "My whole body is in pain, his reply helps me to relax."
    "Thug" "Let me leave you with a present... heh..." with red_flash
    nar_c "He slashes my body with his knife and throws me to the ground." with sshake
    hero_c "Gahhh..."
    "Thug" "Next time I will kill you."
    hide sam_1 with dissolve
    nar_c "He runs away limping."
    nar_c "...."
    nar_c "My shirt has become red with my blood."
    nar_c "I don't have the strength to get up... as I lay on the ground."
    nar_c "My eyes are closing by themselves."
    nar_c "..."
    nar_c "......"
    scene black with fade
    "Voice" "Hey! Hey! Stay with me here!"
    "Voice" "Don't die please!"
    nar_c "...."
    nar_c "........."
    nar_c "..............."
    scene apartment_1 afternoon with dissolve
    nar_c "......"
    nar_c "The sun shines onto my eyes."
    nar_c "I can hear birds chirping in the background."
    nar_c "I lay on the ground... my body has been bandaged up."
    nar_c"...."
    nar_c "I hear a voice from my right."
    show amy_2 with dissolve
    "???" "Adam, he is awake!"
    nar_c "...."
    nar_c "The girl runs away."
    hide amy_2 with dissolve
    nar_c "......"
    show adam_1 with dissolve
    adam_c "Morning, how are you doing?"
    hero_c "..."
    adam_c "Sorry... I haven't introduced myself."
    adam_c "I am Adam and I carried you here after I found you on the street."
    hero_c "I am [hero_c.name], thanks for helping me out there."
    adam_c "No problem...."
    "???" "This one is awake too, Adam!"
    adam_c "Sorry I have to tend to other people, please try to rest up."
    hide adam_1 with dissolve
    nar_c "He heads inside the house."
    nar_c "I notice my surroundings..."
    nar_c "There is blood on the ground near me... bandages and surgical tools lying around everywhere."
    nar_c "The whole place is filled with many other people covered in bandages."
    nar_c "It looks like a war zone."
    nar_c "What the heck happened last night!?"
    nar_c "......"
    nar_c "I lay on my bed... hopefully this is a bad dream...."
    nar_c "...."
    scene black with fade
    # heal everything
    $ hero.full_heal()
    nar_c "......."
    nar_c "....."
    nar_c"..."
    scene apartment_1 evening with dissolve
    nar_c "..."
    nar_c "I open my eyes and sit up."
    nar_c "I feel no pain from my wounds."
    nar_c "....."
    nar_c "In the distance I see a gathering of the wounded."
    nar_c "I force myself up and head towards the gathering."
    show adam_1 with dissolve
    adam_c "We don't know the situation as of now."
    adam_c "Hey, please join us."
    nar_c "I take a seat, many others are wrapped up in bandages like me."
    ### TODO: more descriptions of the wounded and confusion, people speaking
    adam_c "I found all of you last night either wounded or near death."
    adam_c "I know that many of you have many questions, I will try my best to explain what happened."
    nar_c "....."
    nar_c "The crowd listens carefully, they are as confused as I am."
    adam_c "Last night there were many attacks carried out by various gangs... another words..."
    adam_c "There was a gang war in this town where four or five gangs all decided to go at each other at once."
    "Person 1" "Are you telling me that some stupid kids just went crazy!?"
    nar_c "The whole crowd starts to talk."
    "Person 2" "Where is the police!?"
    adam_c "Everyone please listen."
    nar_c "Everybody lowers their voices."
    adam_c "I do not know where the police is, I have called them many times but no one picks up the phone!"
    "Person 1" "What is that is crazy! Does anyone have a phone here, let me try!"
    nar_c "....."
    "Person 2" "Here, my phone still has some battery."
    "Person 1" "Give me please."
    nar_c "He dials the three digit number."
    nar_c "...."
    "Person 1" "He is right... no one is picking up!"
    "Person 1" "This is crazy, there won't be any law or order."
    adam_c "Please stay calm."
    adam_c "We can assume that the gangs have possibly taken over the local police station, preventing the staff from picking up."
    adam_c "I have fixed many of you up with little medical training I recieved from my time in military service but I have no more supplies."
    adam_c "We still have many more people that need medical assistance, the lot of you should consider yourself lucky."
    "Person 1" "We should take them to the hospital."
    adam_c "There are gang members walking around or riding around on bikes."
    adam_c "If they spot us they will discover us and the worst can happen."
    "Person 2" "But why are these people killing other people, have these teenagers gone insane!?"
    adam_c "I don't know why such violence has taken place, all I know is that many people are injured and we are taking refuge here."
    adam_c "We need to somehow escape this place, there are limited food supplies here and we cannot stay here forever."
    nar_c "There injured discuss between themselves."
    # TODO: panic?
    hero_c "What are our options?"
    adam_c "We need to organise a party amongst us to venture outside and find out more information."
    adam_c "We need to move when it is dark to avoid detection."
    adam_c "Which one of you want to volunteer?"
    nar_c "We cannot stay like this, there are roughly 5 of us here and some wounded inside."
    hide adam_1 with dissolve
    show greyson_1 with dissolve
    "???" "I will go."
    "???" "My name is Greyson."
    greyson_c "I do not want to stay here like this."
    greyson_c "I am worried about my Mom and Sister, who knows what these gangbangers have done to them?"
    hide greyson_1 with dissolve
    "???" "I will go too."
    show will_1 with dissolve
    will_c "I want to help out too."
    nar_c "That guy looks familiar, like I have seen him before..."
    nar_c "He has a resemblence to that thug I fought last night."
    nar_c "I need to help out too."
    hero_c "I will help too."
    hide will_1 with dissolve
    show adam_1 with dissolve
    adam_c "I will go too."
    will_c "No you can't you must stay here and help the wounded."
    greyson_c "Yes we will go."
    adam_c "How do you expect to survive out there!?"
    will_c "We will."
    hide adam_1 with dissolve
    nar_c "..........."
    nar_c "........"
    scene apartment_1 night with squares
    nar_c "We finally decide that only 3 of us will go without Adam."
    nar_c "......"
    show will_1 with dissolve 
    will_c "Lets move."
    greyson_c "Yes."
    scene street_1 night with squares
    nar_c "We climb over the walls and the streets seem to be clear."
    show will_1 at left with dissolve
    show greyson_1 at right with dissolve
    will_c "We have 3 locations we can possibly take and secure."
    will_c "There is a hospital to the East of here, a Police Station to the North and a School to the West."
    greyson_c "The Police station is where we should head first right!?"
    will_c ".... I would rather try the hospital first, we need to get medical supplies..."
    greyson_c "What do you think [hero_c.name]?"
    will_c "Where do you think we should go?"
    menu:
        "Hospital":
            jump prologue_hospital
        "Police Station":
            jump prologue_police_station
        "School":
            jump prologue_school
    
    return
    
label prologue_hospital:
    if not at_map:
        hero_c "We should go to the hospital to retrieve medical supplies and heal the wounded."
        hero_c "Someone there must also know what is going on here."
        greyson_c "But my family... I want make sure they are safe..."
        will_c "I think [hero_c.name] is right here, we can split up."
        # TODO: Some friction between team mates
        greyson_c "I am going to go to the Police Station myself, I don't care care!"
        hide greyson_1 with dissolve
        nar_c "We are powerless to stop him as he heads North towards the police station."
        show will_1 with dissolve
        will_c "Leave him, we must get medical supplies."
        nar_c "I reluctantly decide to move on."
        nar_c "If we quickly confirm the Hospital is safe we can come to help Greyson."
        nar_c "...."
        nar_c "..."
        
    scene street_4 night with squares
    nar_c "There are a few gang members driving around but we manage to avoid most of them."
    nar_c "Survellence is certainly low near the hospital."
    nar_c "....."
    nar_c "We see the hospital nearby, its lights are on."
    nar_c "Looks like it is under lockdown by the gang members."
    nar_c "We hear some voices near the entrance."
    "Doctor" "Stop this at once!"
    "Thug" "Shut it Doc, your staying here for now."
    nar_c "He punches the Doctor, which causes him to fall down."
    "Doctor" "Arghhh...."
    nar_c "....."
    nar_c "A nurse comes out and helps the Doctor up to his feet."
    nar_c "She takes him inside."
    "Thug" "Hehh... stupid..."
    nar_c "...."
    show will_1 with dissolve
    will_c "Looks like they are just guarding the entrance, we should be able to get inside."
    hero_c "You mean we take out that thug?"
    nar_c "...."
    nar_c "Two other thugs walk out with baseball bats."
    nar_c "We are tucked away behind a wall so they cannot see us."
    hero_c "These guys are very close, we will have to take them head on."
    will_c "Heh... we think a like..."
    nar_c "Will rolls up his sleeve and walks out unarmed."
    hide will_1 with dissolve
    hero_c "Hey... I didn't mean you walk out like that!?"
    nar_c "I follow him."
    "Thugs" "Hey! You come here."
    nar_c "The mob rushes at us.... we have no choice but to fight..."
    $ will.buy_weapon(w_brass_knuckles)
    $ will.buy_weapon(w_brass_knuckles)
    $ will.buy_item(i_heal_paste)
    $ will.buy_item(i_chakra_paste)
    $ will.hp -= 50
    $ will.chakra -= 50
    $ current_session.stage = clearing
    #$ info = str(current_session.stage.tile11.BASE_TEXTURE)
    #nar_c "[info]"
    $ renpy.call('fight', hero, copy.deepcopy(lvl_1_thug_melee), [will], [copy.deepcopy(lvl_1_thug_ranged)], clearing, win_label='prologue_hospital2', lose_label='prologue_hospital2', draw_label='prologue_hospital2', fight_limit=15)

    
label prologue_hospital2:
    # hero gains experience or level up then hospital is conquered
    $ hide_battle_screen(all=True)
    $ battle_turn = 0
    $ exp = renpy.random.randint(100,200) + 200
    $ hero.gain_exp(exp)
    hero_c "I gain [exp] exp."
    nar_c "The battle ends..."
    nar_c "Will completely dominates the fight, his fighting style is very similar..."
    scene street_4 night with dissolve
    show will_1 with dissolve
    nar_c "Will holds the thug by his collar."
    will_c "Who sent you here!?"
    thug_c "It.. it was... Sam..."
    nar_c "....."
    nar_c "The thug faints."
    hero_c "Who is Sam?"
    will_c "I knew it, just had to be him."
    hero_c "You know him?"
    "Doctor" "Are you two okay!?"
    nar_c "The Doctor interrupts us."
    hero_c "Yes we are fine, are there anymore inside?"
    "Doctor" "No it was just the ones here."
    "Doctor" "They locked us inside since yesterday, we couldn't escape."
    "Doctor" "We tried to call the police but no one answered."
    "Doctor" "Just what is going on in this town?"
    hero_c "We are heading towards the police station now."
    "Doctor" "Let me patch you guys up before you go."
    nar_c "He notices the cuts and bruises we got in the fight."
    will_c "Thanks, Doc."
    $ l_hospital.unlocked = True
    $ m_secure_hospital.success = True
    nar_c "{color=#66CD00}Hospital Secured! New location unlocked!{/color}" 
    nar_c "....................."
    if at_map:
        jump town_map
        
    nar_c "..........."
    nar_c "I have minor injuries I decided to leave early."
    hero_c "I'll go on ahead, make sure to catch up."
    will_c "On my way."
    scene street_1 night with squares
    nar_c "As soon as I am patched up, I head straight for the police station."
    nar_c "...."
    nar_c "I hope Greyson is doing okay but I can't help but worry."
    jump prologue_school
    
label prologue_police_station:
    if not at_map:
        hero_c "Lets go to the police station, we need to make sure we have some enforcement otherwise we can't survive."
        greyson_c "I knew I could count on you."
        greyson_c "Lets go!"
        will_c "I'll head to the hospital by myself then."
        hide will_1 with dissolve
        nar_c "Will walks away."
        greyson_c "Please stick with me, we have to secure the station."
        hero_c "Lets go."
        
        
    scene building_1 night with squares
    nar_c ".........."
    nar_c "........"
    nar_c "....."
    nar_c "We arrive at the Police station."
    nar_c "The whole area is trashed with windows smashed and junk everywhere."
    nar_c "We hide behind the corner."
    nar_c "The place looks deserted, this place is usually very busy with all the shopping centres."
    show greyson_1 with dissolve
    greyson_c "The police station is intact, maybe we can enter it?"
    hero_c "Something looks funny, the lights are off and no police are nearby."
    hide greyson_c with dissolve
    hero_c "Lets wait a bit."
    nar_c "........."
    nar_c "......."
    nar_c "....."
    nar_c "We hear voices coming from the building."
    nar_c "Two thugs emerge holding baseball bats."
    show greyson_1 with dissolve
    nar_c "Greyson erraticly stands up."
    greyson_c "I... can't take this anymore!"
    greyson_c "I'm going to rush in!"
    hero_c "Wait Greyson, we don't know how many are inside!"
    hide greyson_1 with dissolve
    nar_c "He rushes at them."
    "Thug" "Wow.... watch out..."
    nar_c "Greyson rugby tackles one on them to the ground and smashes him into the curb."
    nar_c "I stand up and rush at the other one."
    hero_c "Look here." with sshake
    nar_c "I punch the other thug in the back."
    "Thug" "You're going to regret that!"
    nar_c "I steady my stance bracing for the fight."
    $ renpy.call('fight', hero, copy.deepcopy(lvl_1_thug_melee), [], [], clearing, win_label='prologue_police_station2', lose_label='prologue_police_station2', draw_label='prologue_police_station2', fight_limit=15)
    
label prologue_police_station2:
    call hidetiles
    # hero gains experience or level up then hospital is conquered
    $ hide_battle_screen(all=True)
    $ battle_turn = 0
    $ exp = renpy.random.randint(100,200) + 200
    $ hero.gain_exp(exp)
    hero_c "I gain [exp] exp."
    nar_c "The battle ends..."
    show greyson_1 with dissolve 
    greyson_c "Take this!"
    nar_c "He smashes the Thug with a baseball bat."
    nar_c "........."
    nar_c "The thug is knocked out on the floor but he did deal me some damage too."
    greyson_c "I got stabbed on my side."
    nar_c "He is holding his left abdomen and its covered in blood."
    greyson_c "Please go and check out the station, I'll follow you."
    hero_c "Just wait here, I'm sure they have a medical kit inside."
    hide greyson_1 with dissolve
    nar_c "....."
    nar_c "I rush inside."
    scene night_sky with squares
    nar_c "The officers were locked up in the cells below the station."
    nar_c "I manage to free them and get Greyson and myself treated."
    "Police Officer" "Thank you for your brave work, we will try to contact neighboring towns to call for backup."
    $ l_police_station.unlocked = True
    $ m_secure_hospital.success = True
    nar_c "{color=#006400}Police Station Secured! New location unlocked!{/color}"
    nar_c "..........."
    if at_map:
        jump town_map
        
    nar_c "........"
    scene street_1 night with squares
    nar_c "I need to head for the hospital."
    nar_c "......"
    jump prologue_school

label prologue_school:
    scene street_1 night with sshake
    nar_c "There is a large explosion in the distance."
    nar_c "........."
    hero_c "What was that!?"
    nar_c "It is coming from the direction of the school."
    hero_c "Lets check it out."
    nar_c "........."
    nar_c "......"
    scene school_1 night with squares
    nar_c "......."
    nar_c "I arrive at the scene first."
    show will_1 at left with dissolve
    show greyson_1 at right with dissolve
    will_c "Hey, you heard the explosion right?"
    greyson_c "Me too, I headed over here, this is my sister's school!"
    nar_c "The windows are smashed and there is fire and smoke coming from all over the building."
    "Voice" "Ahhhh...."
    nar_c "......"
    nar_c "A body falls from one of the top floors and lands in the distance."
    will_c "Looks like this place is more dangerous than the rest."
    will_c "There is something going on."
    hide will_1 with dissolve
    nar_c "Will rushes inside."
    greyson_c "Guess he didn't leave us with much choice."
    greyson_c "Lets head inside."
    scene night_sky with squares
    nar_c "......"
    nar_c "We head inside following Will, who is knows exactly where he is going."
    nar_c ".........."
    nar_c "......."
    nar_c "Will leaves us behind and Me and Greyson follow."
    nar_c "We seem to be heading towards the rooftop."
    scene rooftop_1 night with squares
    nar_c "........"
    nar_c "The place is littered with bodies of gang members knocked out."
    nar_c "There is blood everywhere."
    nar_c "From a distance I see a familiar face."
    show will_1 with sshake
    will_c "Ahhh"
    hide will_1 with dissolve
    nar_c "Will goes flying in the distance and crashes into a wall."
    nar_c "........"
    nar_c "I see a familiar face."
    show sam_2 with dissolve
    "???" "Hey who do we have here."
    "???" "I might as well introduce myself."
    sam_c "I am Sam, the leader of this town."
    hero_c "What are you..."
    sam_c "You could say that I started all of this."
    hero_c "Do you know how many lives you have taken for this senseless voilence!?"
    sam_c "Senseless Violence!?"
    sam_c "I am protecting this place from the worst."
    hero_c "I am not going to hear your reasons, I just want to kick your ass."
    hero_c "Why don't we finish what we started that day?"
    will_c "No.... you can't stand up to him, he is too strong."
    sam_c "Lets finish it."
    hide sam_1 with dissolve
    nar_c "......" with red_flash
    nar_c "......" with sshake
    nar_c "I ... somehow end up on the ground."
    nar_c "There is a sharp pain in my nose and jaw area."
    nar_c "I can't move my body...."
    nar_c "......."
    nar_c "He takes out Greyson with ease."
    show sam_2 with dissolve
    sam_c "Is this the best you guys could do?"
    nar_c "What is this guy? Was he holding back, back then?"
    sam_c "Hahhaaha...."
    sam_c "Now this town belongs to me."
    will_c "I won't let that happen!"
    hide sam_2 with sshake
    show will_1 with dissolve
    will_c "Lets retreat for now."
    scene night_sky with dissolve
    nar_c "Will picks both me and Greyson up and runs downstairs."
    nar_c "I am amazed at his strength."
    nar_c "..............."
    nar_c "I fade in and out of conciousness, my nose is bleeding heavily."
    nar_c "......"
    nar_c "Greyson is totally out cold."
    will_c "Hufff.... huff....."
    nar_c ".........."
    scene apartment_1 night with squares
    nar_c "............"
    nar_c "Will puts both of us down."
    will_c "Adam! Help!"
    show adam_1 with dissolve
    adam_c "Amy bring the equipment!"
    nar_c "......."
    nar_c "....."
    scene black_fade with black_flash
    $ hero.full_heal()
    $ greyson.full_heal()
    $ will_full_heal()
    nar_c ".............."
    nar_c ".........."
    nar_c "........."
    scene apartment_1 afternoon with squares
    nar_c "......"
    nar_c "Sunlight hits my eyes..."
    nar_c "I wake up to find a familiar site."
    # TODO: review of what happened yesterday
    nar_c "I wake up and head towards the group of people seated."
    show adam_1 at left with dissolve
    show will_1 at right with dissolve
    adam_c "Will can you please explain to all of us, what is going on?"
    will_c "Okay, there is no point staying quiet now."
    hide adam_1 with dissolve
    show will_1 with dissolve
    will_c "This all started 10 years ago...."
    will_c "If many of you remember, this town was the center of many gang wars 10 years ago."
    will_c "These came to an end when both senior leaders of both of the local gangs were killed."
    will_c "Many gangs drifted or simply broke apart afer that event."
    will_c "Now there have been rumours that one of the senior leaders is alive."
    nar_c "I interrupt him."
    hero_c "But who is Sam?"
    will_c "He... is the leader of the current gang who are trying to claim this town as theirs and my brother..."
    nar_c "......."
    nar_c "The whole crowd are in shock."
    will_c "One of the leaders that died 10 years ago was my father and now my brother is trying to revive the gang."
    nar_c "The crowd starts to talk amongst themselves."
    will_c "His actions I think are misleading..."
    hero_c "What do you mean?"
    will_c "When the news came that one of the old leaders came back, there was a reaction from the other towns gangs."
    will_c "Due to the presence of my fathers gang in the past they felt a threatening presence and this town was surrounded from all sides by the nieghboring gangs."
    will_c "My brother had to organise a force to stop them attacking the town."
    will_c "I do not agree with his rash methods but he is trying to protect us."
    hero_c "But why did he attack us when we met him!?"
    will_c "He is an arrogant fool and won't listen to me ever."
    will_c "He prides himself in violence and wants to mirror the heartless gang my Father formed all those years ago."
    will_c "Even if that means he kill his Brother, so be it."
    will_c "unforetunely we will have to topple him from here in order to move forward."
    show will_1 at right with dissolve
    show adam_2 at left with dissolve
    adam_c "This reminds me of my days in service."
    nar_c "He sighs."
    adam_c "This violence cannot go on any longer."
    adam_c "Lets formulate a plan and quickly topple Sam."
    adam_c "I bought this map with me, when I first moved here."
    scene town_map_1 with dissolve
    
    show screen villagemap(middle_town, hero)
    adam_c "Here is the map."
    adam_c "We have some locations we have already secured."
    
    if l_hospital.unlocked:
        adam_c "We managed to secure the hospital earlier."
        adam_c "The hospital can be used to heal wounds and buy supplies for healing."
    elif l_police_station.unlocked:
        adam_c "We managed to secure the police station earlier."
        adam_c "The Police Station can be used to buy weapons."
    
    $ l_apartment.unlocked = True
    adam_c "Here is the apartment we are currently in."
    $ l_training_ground.unlocked = True
    adam_c "We have the training ground near by where we can train our skills in the mean time and unlock new skills."
    $ l_level_up.unlocked = True
    adam_c "Level up location can be used to level up and distribute skill points, make sure to spend these regularly to improve your fighting skills."
    $ l_town_mission.unlocked = True
    adam_c "Town missions are missions we must undertake to advance the story."
    adam_c "I will leave you to decide what needs to be done."
    
    $ at_map = True
    
    jump town_map
    
label town_map:
    scene town_map_1 with dissolve
    # Set the current village
    $ current_session.village = middle_town
    show screen villagemap(middle_town, hero)
    $ show_village_map(middle_town, hero)
    
label mission_infiltrate_hold:
    scene apartment_1 with squares
    show adam_1 with dissolve
    adam_c "The enemy stronghold is in the school."
    adam_c "We need to do a full assault there."
    adam_c "Since you three seem to make a good team, lets move out and take over this part of town."
    adam_c "Go Greyson, Will and [hero.name]!"
    nar_c "............"
    nar_c "The three of us make our way towards the school."
    nar_c "........."
    scene school_1 night with squares
    nar_c ".............."
    nar_c "It is the same as we saw the other day."
    show bison_1 with dissolve
    bison_c "Heh... heh... heh....."
    bison_c "So guys have arrived."
    hero_c "Bison!?"
    bison_c "[hero.name] what are you doing here?"
    hero_c "Are you with Sam?"
    bison_c "So what if I am!?"
    will_c "You guys clearly know each other."
    bison_c "There is larger wave coming soon, I don't have time ot waste here."
    nar_c "Behind Bison, many other thugs with bats show up."
    bison_c "Fight me!"
    hide bison_1 with dissolve
    
    ### BattleMission Class
    $ m_infiltrate_hold_battle = BattleMission(name="Infiltrate Hold", 
                                      hours=6, 
                                      good_team=team_first,
                                      battles={'1':[lvl_4_thug_ranged], '2':[lvl_4_thug_melee], 'last':[lvl_8_bison_melee]}, 
                                      follow_on='prologue_continue', 
                                      all_battles=ALL_BATTLES)
    
    $ m_infiltrate_hold_battle.do_mission(hero_c)
    
label prologue_continue:
    call hidetiles
    # hero gains experience
    $ hide_battle_screen(all=True)
    # mission is complete
    $ m_infiltrate_hold.success = True
    $ battle_turn = 0
    $ exp = renpy.random.randint(100,200) + 200
    $ hero.gain_exp(exp)
    hero_c "I gain [exp] exp."
    
    scene school_1 night with dissolve
    nar_c "Bison and his gang are all knocked out."
    nar_c ".... ring... ring...."
    nar_c "My phone rings, I pick it up."
    adam_c "Please return to the base, we will do a final attack later."
    hero_c "Ok, heading back."
    jump town_map
    
label mission_defeat_sam:
    if hero.level < 3:
        adam_c "You must be level 3 or above to do this mission, use level up to increase level."
        jump town_map
        
    
    scene apartment_1 evening with squares
    nar_c "............"
    show adam_1 with dissolve
    adam_c "The seurity around the school has cleared."
    adam_c "We can go in a defeat Sam, the leader of the gang here."
    adam_c "............"
    adam_c "Go."
    scene school_1 evening with squares
    nar_c "............"
    nar_c "........"
    nar_c "There is no security, I make my way towards the roof."
    scene rooftop_1 evening with squares
    show sam_1 with dissolve
    sam_c "Long time, no see."
    sam_c "Fight me 1 on 1."
    hero_c "I'll defeat you!"
    hide sam_1 with dissolve
    
    $ renpy.call('fight', hero, sam, [], [], clearing, win_label='prologue_end', lose_label='prologue_end', draw_label='prologue_end', fight_limit=15)
    
label prologue_end:
    
    scene rooftop_1 evening with squares
    nar_c "Sam overpowers me." with sshake
    show sam_2 with dissolve
    sam_c "You still cannot defeat me!"
    show sam_2 at left with dissolve
    show will_1 at right with dissolve
    will_c "Thats enough Sam!"
    will_c "Lets end this before we all get hurt."
    nar_c "Sam is bleeding too, he is in pain from our fight just now."
    sam_c "If I don't takeover this city, that guy will walk all over us."
    will_c "What do you mean!?"
    sam_c "You don't understand, the leader that came back was our father!"
    will_c "....."
    nar_c "Will stares at Sam in shock."
    will_c "I... had no idea...."
    sam_c "Work with me Will, we do this."
    will_c "I don't approve of your methods and I am going to take you down here."
    # will vs sam fight
    nar_c ".............."
    will_c "Blast kick!" with sshake
    nar_c "The kick connects and send Sam flying into the wall."
    sam_c "......ughhh...."
    nar_c "Sam is knocked out."
    hide sam_c with dissolve
    show will_1 with dissolve
    will_c "Its over."
    nar_c ".............."
    nar_c "Greyson helps me up and we head back to the apartment."
    scene apartment_1 night with squares
    nar_c "..........."
    nar_c ".........."
    nar_c "Will brings Sam and Bison to the apartment too."
    show adam_1 with dissolve
    adam_c "We have secured Middle Town."
    adam_c "The leader was Sam, who is currently receieving treatment."
    adam_c "We will watch over him, as he may have intel on who is causing all this fuss in the city."
    nar_c "..........."
    nar_c "........"
    nar_c "....."
    nar_c "I wonder what the other parts of town are doing...."
    nar_c "............"
    nar_c ".........."
    scene forest_1 night with squares
    show ai_1 with dissolve
    ai_c "Seems like middle town are starting gather some force."
    ai_c "We should start to prepare for his return too."
    ai_c "I won't let what happened 10 years ago repeat again."
    nar_c "..........."
    nar_c "......."
    scene home_1 night with squares
    show monk_1 with dissolve
    nar_c ".............."
    monk_c "Looks like the visions were true."
    monk_c "I can't wait to spill blood again!"
    nar_c "..........."
    jump intro_world_events
    
label intro_world_events:
    
    $ start_world_events(background="town_map_1", follow_on_label='prologue_end2')
    
label prologue_end2:
    scene apartment_1 with squares
    nar_c "............"
    nar_c "........"
    nar_c "A week has gone by since we defeated Sam."
    nar_c "He and Bison have been recovering."
    show sam_2 with dissolve
    sam_c "Ok ok... I will join to help."
    show sam_2 at left with dissolve
    show bison_1 at right with dissolve
    bison_c "If Sam joins that leaves me no choice, I will join too."
    show adam_1 with dissolve
    adam_c "That is good to know."
    adam_c "We need to stop your Father from making his comeback."
    adam_c "Sam and Bison you will join Will, Greyson and [hero.name] in their battles."
    hide sam_2 with dissolve
    hide bison_1 with dissolve
    hide adam_1 with dissolve
    nar_c ".........."
    nar_c "{color=#66CD00}Bison and Sam join Party!{/color}"
    $ team_first.add_member(sam)
    $ team_first.add_member(lvl_8_bison_melee)
    show amy_1 with dissolve
    amy_c "I want to fight too."
    nar_c "{color=#66CD00}Amy joins party{/color}"
    # Add Amy to the team
    hide amy_1 with dissolve
    show adam_1 with dissolve
    adam_c "To the east is East Town, their current leader is known as Monk."
    adam_c "To our south is South Town, their leader is known as Ai, the Flash."
    adam_c "As Sam and Will informed us, these two were part of this gang 10 years ago."
    adam_c "We have missions for both of these parties, our aim is to find Will and Sam's Father."
    nar_c "............"
    nar_c ".........."
    
    scene town_map_1 with dissolve
    #show screen villagemap(middle_town, hero)
    
    $ renpy.pause(5.0, hard=True)
    
    show screen announce("GANG RISER EPISODE 1")
    
    $ renpy.pause(5.0, hard=True)
    
    show screen announce("GAME OVER")
    
    # show credits
    
    # end game
    $ renpy.full_restart()
