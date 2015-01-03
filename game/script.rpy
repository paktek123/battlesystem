﻿#### RISER BATTLE SYSTEM #####


init -1:
    $ current_skill = None
    
    $ maxhp_increase = 0
    $ maxchakra_increase = 0
    $ exp_increase = 0
    $ bond_increase = 0
    $ moved = False
    $ battle_turn = 0
    
    image bg = im.Scale("bg.jpg", 800, 600)
    image black_fade = Solid((0, 0, 0, 150))
    image black_fade_small = Solid((0, 0, 0, 150), area=(0.4, 0.7, 0.6,0.4)) # im.Tile(im.Scale("black.png", 400, 300)
    image world_marker = im.Scale("marker.png", 33, 35)
    image leader_pic = im.Scale("leader_pic.png", 100, 150)
    define world_events = Character('World Events', color='#3399FF', window_left_padding=150, show_side_image=Image("leader_pic.png", xpos=0.03, yalign=0.96))
    image map = im.Scale("map.png", 800, 600)
    image stats_idle = Solid((0, 0, 0, 200), area=(0.62, 0.0, 300,150))
    
    image playerpic_r = im.Scale("player.png", 40, 50)
    image enemypic_r = im.Scale("enemy.png", 40, 50)
    image sakurapic_r = im.Scale("sakura.png", 40, 50)
    image kakashipic_r = im.Scale("kakashi.png", 40, 50)
    image oripic_r = im.Scale("ori.png", 40, 50)
    image itachipic_r = im.Scale("itachi.png", 40, 50)
    image playerpic_l = im.Flip(im.Scale("player.png", 40, 50), horizontal=True)
    image enemypic_l = im.Flip(im.Scale("enemy.png", 40, 50), horizontal=True)
    image sakurapic_l = im.Flip(im.Scale("sakura.png", 40, 50), horizontal=True)
    image kakashipic_l = im.Flip(im.Scale("kakashi.png", 40, 50), horizontal=True)
    image oripic_l = im.Flip(im.Scale("ori.png", 40, 50), horizontal=True)
    image itachipic_l = im.Flip(im.Scale("itachi.png", 40, 50), horizontal=True)
    
    $ player1currentpos = 1
    $ enemy1currentpos = 12

init python:
    
    IMAGE_EXCEPTIONS =  ('body.png', 'arm.png', 'leg.png', 'torso.png', 'head.png', 'tile.png', 'tileh.png', 'tilep.png', 'tiletrap.png')
    
    import os
    import copy
    import random
    for fname in os.listdir(config.gamedir + '/gfx'):
        if fname.endswith(('.jpg', '.png')) and fname not in IMAGE_EXCEPTIONS:
            tag = fname[:-4]
            fname =  'gfx/' + fname
            renpy.image(tag, im.Scale(fname, 800, 600))
            for t in ['morning', 'afternoon', 'evening', 'night']:
                if t == 'evening':
                    renpy.image((tag, t), im.Scale(im.Recolor(fname, 255, 178, 102, 255), 800, 600))
                elif t == 'night':
                    renpy.image((tag, t), im.Scale(im.Recolor(fname, 51, 153, 255, 255), 800, 600))
                else:
                    renpy.image((tag, t), im.Scale(fname, 800, 600))
    
    
    LEADER_POSITION = Position(xpos=0.5, ypos=0.9)
    
    ### MENU GRIDS ###
    LOCATION_XPOS_FIRST = 0.4
    LOCATION_YPOS_FIRST = 0.4
    start_x = 0.3
    start_y = 0.3
    x_delta = 0.2
    y_delta = 0.07
    grid_place = [(start_x,start_y), (start_x,start_y + y_delta), (start_x, start_y + 2*y_delta), (start_x, start_y + 3*y_delta), (start_x,start_y+4*y_delta), 
                  (start_x + x_delta,start_y), (start_x + x_delta,start_y + y_delta), (start_x+x_delta, start_y + 2*y_delta), (start_x+x_delta, start_y + 3*y_delta), (start_x+x_delta,start_y+4*y_delta),
                  (start_x + 2*x_delta,start_y), (start_x + 2*x_delta,start_y + y_delta), (start_x+2*x_delta, start_y + 2*y_delta), (start_x+2*x_delta, start_y + 3*y_delta), (start_x+2*x_delta,start_y+4*y_delta), ]
    
    ### TILES ###
    
    tile1 = Tile(tile1pos, TILEIDLEPIC, TILEHOVERPIC, 1)
    tile2 = Tile(tile2pos, TILEIDLEPIC, TILEHOVERPIC, 2)
    tile3 = Tile(tile3pos, TILEIDLEPIC, TILEHOVERPIC, 3)
    tile4 = Tile(tile4pos, TILEIDLEPIC, TILEHOVERPIC, 4)
    tile5 = Tile(tile5pos, TILEIDLEPIC, TILEHOVERPIC, 5)
    tile6 = Tile(tile6pos, TILEIDLEPIC, TILEHOVERPIC, 6)
    tile7 = Tile(tile7pos, TILEIDLEPIC, TILEHOVERPIC, 7)
    tile8 = Tile(tile8pos, TILEIDLEPIC, TILEHOVERPIC, 8)
    tile9 = Tile(tile9pos, TILEIDLEPIC, TILEHOVERPIC, 9)
    tile10 = Tile(tile10pos, TILEIDLEPIC, TILEHOVERPIC, 10)
    tile11 = Tile(tile11pos, TILEIDLEPIC, TILEHOVERPIC, 11)
    tile12 = Tile(tile12pos, TILEIDLEPIC, TILEHOVERPIC, 12)
    
    TILES = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, tile10, tile11, tile12]
    
    ### TIME, DAY AND MONTHS ###
            
    main_time = GameTime(9, 1, 1, 1354)
    
    months = [copy.deepcopy(Month(m)) for m in range(1,13)]
    
    def get_month(number):
        if number == 13:
            number = 1
        elif number == 0:
            number = 12
        
        return [m for m in months if m.number == number][0]
        
    def get_current_month():
        return [m for m in months if m.number == main_time.month][0]
        
    def get_today():
        return [d for d in ALL_DAYS if d.number == main_time.day and d.month.number == main_time.month][0]
    
    for m in months:
        m.days = [copy.deepcopy(Day(d, m)) for d in range(1,31)]
        
    ALL_DAYS = []
    
    for m in months:
        ALL_DAYS += m.days
        
    ##############################################################################
    # INITIALIZE ASSETS
    #
        
    ### EVENTS ###
                    
    e_chunin_exams = Event("Chunin Exams", "CE", start=(15, 5), finish=(14, 7), label="chunin_exam")
    e_jounin_training = Event("Jounin Training", "JT", frequency=(1, ))
    e_jinchurri_attack = Event("Jinchurri Attack", "???",chance=0.02, label="jinchurri_attack", occurrence=0)
    e_weapon_discount = Event("Weapon Discount", "WD", frequency=(random.randint(2,30),)) 
    e_hospital_discount = Event("Hospital Discount", "HD", frequency=(random.randint(2,30),)) 
    
    ALL_EVENTS = [e_chunin_exams, e_jounin_training, e_jinchurri_attack, e_weapon_discount, e_hospital_discount]
    
    def is_event_active_today(event):
        if event.name in [e.name for e in get_today().events]:
            return True
        return False
            
    ### VILLAGE AND LOCATIONS ###

    # locations that exist in each village
    l_travel = Location('Travel', 'village_travel')
    l_level_up = Location('Level Up', 'village_levelup')
    l_training_ground = Location('Training', 'village_training', 'training')
    l_arena = Location('Arena', 'village_arena')
    l_hospital = Location('Hospital', 'village_hospital', events=[e_hospital_discount])
    l_jounin_station = Location('Jounin Standby Station', 'village_jounin_station', events=[e_jounin_training])
    l_intelligence_division = Location('Intelligence Division', 'village_intelligence_division')
    l_ninja_tool_facility = Location('Ninja Tool Facility', 'village_ninja_tool_facility', events=[e_weapon_discount])
    l_villagemission = Location('Mission Assignment Desk', 'village_missions', events=[e_chunin_exams])
    l_home = Location('Home', 'village_home')
    
    BASE_LOCATIONS = [l_travel, l_level_up, l_training_ground, l_arena, l_hospital, l_jounin_station, l_intelligence_division, l_ninja_tool_facility, l_villagemission, l_home]
        
    hidden_stone = Village(1, "Hidden Stone", None, marker_xpos=0.25, marker_ypos=0.25, map="stones_map", locations=BASE_LOCATIONS, village_tag="stones", mission_locations=2)
    hidden_cloud = Village(2, "Hidden Cloud", None, marker_xpos=0.75, marker_ypos=0.20, map="clouds_map", locations=BASE_LOCATIONS, village_tag="cloud", mission_locations=2)
    hidden_mist = Village(3, "Hidden Mist", None, marker_xpos=0.85, marker_ypos=0.70, map="mist_map", locations=BASE_LOCATIONS, village_tag="mist", mission_locations=2)
    hidden_leaf = Village(4, "Hidden Leaf", None, marker_xpos=0.40, marker_ypos=0.60, map="konoha_map", locations=BASE_LOCATIONS, village_tag="leaf", mission_locations=2)
    hidden_sand = Village(5, "Hidden Sand", None, marker_xpos=0.25, marker_ypos=0.90, map="sand_map", locations=BASE_LOCATIONS, village_tag="sand", mission_locations=4)
        
    ALL_VILLAGES = [hidden_stone, hidden_cloud, hidden_mist, hidden_leaf, hidden_sand] 
    
    def other_villages(village):
        return [v for v in ALL_VILLAGES if v.id != village.id]
    
    ### CURRENT SESSION ###
        
    current_session = CurrentSession()
    
    ### SKILLS ###
    
    # tai skills
    onetwocombo = Skill('One Two Combo', 'tai', "onetwocombo", 3, 1, 3, 10)
    lioncombo = Skill('Lion Combo', 'tai', "lioncombo", 3, 2, 5, 20, unlock_exp=300)
    
    # nin skills
    rasengan = Skill('Rasengan', 'nin', "rasengan", 2, 1, 25, 30, unlock_exp=500)
    chidori = Skill('Chidori', 'nin', "chidori", 2, 1, 25, 30, unlock_exp=1000)
    raikiri = Skill('Raikiri', 'nin', "raikiri", 2, 1, 50, 50, unlock_exp=1500)
    
    # gen skills # replace with something new
    substitution = Skill('Substitution', 'gen', "substitution", 8, 20, 15, 0, stun=True)
    
    # defensive skills
    damage_reduction = Skill('Focus', 'defence', 'damagereduction', 12, 1, 10, duration=2, unlock_exp=300)
    chakra_defence = Skill('Chakra Defence', 'defence', 'chakradefence', 12, 2, 15, duration=3, unlock_exp=500)
    substitution = Skill('Substitution', 'counter', "substitution", 8, 20, 15, 0, stun=True)
    reflect = Skill('Reflect', 'defence', 'reflect', 12, 20, 20, duration=2, unlock_exp=1500)
    dampen = Skill('Dampen', 'defence', 'dampen', 6, 30, 30, duration=3, unlock_exp=2000)
    yata_mirror = Skill('Yata Mirror', 'defence', 'yatamirror', 12, 50, 50, duration=2, unlock_exp=2500)
    
    ### WEAPONS ###
    w_kunai = Weapon("Kunai", price=50, range=4, chakra_cost=4, damage=20)
    w_paper_bomb = Weapon("Paper Bomb", price=100, range=2, chakra_cost=5, damage=50)
    shiruken = Weapon('Shiruken', 'weapon', "shiruken", 12, 7, 1, 20)
    kunai = Weapon('Kunai', 'weapon', "kunai", 12, 4, 1, 20)
    trap = Weapon('Trap', 'weapon', "trap", 3, 1, 2, 30)
    
    ### PLAYERS AND TEAMS ###
    
    # d = defensive skill
    # f = range attack (weapon)
    # a = attack (use any attack)
    # t = set trap
    # c = use team combo (formation attacks)
    # tai = use taijutsu skills
    # nin = use ninjustsu skills
    # gen = use genjutsu skills
    # healing items and tagging will be in enemy_move itself
    defensive_enemy_pattern = 2*['d'] + 2*['f'] + 2*['a'] + 2*['t']
    attack_enemy_pattern = 3*['a'] + 2*['f']
    ranged_attack_pattern = 4*['f'] + 2*['d']
    tai_enemy_pattern = 3*['tai'] + 2*['d']
    nin_enemy_pattern = 3*['nin'] + ['d'] + ['a'] + ['f']
    gen_enemy_pattern = 3*['gen'] + 2*['d'] + ['f']
    
    hero_c = Character('NO NAME',color="#FFFF00")
    naruto_c = Character('Naruto',color="#FFFF00") 
    sasuke_c = Character('Sasuke', color="#3399FF")
    sakura_c = Character('Sakura', color="#FA58F4")
    kakashi_c = Character('Kakashi', color="#3399FF")
    itachi_c = Character('Itachi', color="#FFFFFF")
    ori_c = Character('Orichimaru', color="#FF0000")
    
    hero = Player(name='NO NAME', picname="playerpic_r", character=hero_c, tilepic=Image('player.png'), hudpic=None, 
                  hp=100, maxhp=100, chakra=80, maxchakra=80, 
                  strength=1, speed=1, evasion=1, defence=1, stamina=1, base_hit_rate=80, 
                  tile=tile1, facing='right', 
                  meleeskills=[onetwocombo], specialskills=[rasengan], rangedskills=[substitution], 
                  items=[], defensiveskills=[damage_reduction, chakra_defence, reflect, dampen, yata_mirror], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[shiruken, kunai], 
                  home_village=None)
    
    naruto = Player('Naruto', "playerpic_r", naruto_c, Image('player.png'), None, 100, 100, 80, 80, 10, 4, 3, 4, 5, 80, tile1, 'right', 
                    [onetwocombo], [rasengan], [substitution], [],
                    [damage_reduction, chakra_defence, reflect, dampen, yata_mirror], [], "leader_pic", 
                    weapons=[shiruken, kunai], home_village=hidden_leaf)
    sasuke = Player('Sasuke', "enemypic_r", sasuke_c, Image('enemy.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [chidori], [], [], [damage_reduction, chakra_defence], 
                    battle_ai=nin_enemy_pattern, weapons=[shiruken, kunai], home_village=hidden_leaf, interaction={'frequency': (1,)})
    
    sakura = Player('Sakura', "sakurapic_r", sakura_c, Image('sakura.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [chidori], [], [], [damage_reduction, chakra_defence], weapons=[shiruken, kunai], home_village=hidden_leaf)
    kakashi = Player('Kakashi', "kakashipic_r", kakashi_c, Image('kakashi.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [raikiri], [], [], [damage_reduction, chakra_defence], level=32,
                    battle_ai=nin_enemy_pattern, weapons=[shiruken, kunai], home_village=hidden_leaf)
    anko = Player('Anko', "kakashipic_r", kakashi_c, Image('kakashi.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [raikiri], [], [], [damage_reduction, chakra_defence], level=32,
                    battle_ai=nin_enemy_pattern, weapons=[shiruken, kunai], home_village=hidden_leaf)
    
    itachi = copy.deepcopy(sasuke)
    itachi.name, itachi.picname, itachi.character, itachi.level = "Itachi", "itachipic_r", itachi_c, 46
    ori = copy.deepcopy(naruto)
    ori.name, ori.picname, ori.character, ori.level = "Orichimaru", "oripic_r", ori_c, 45
    kyuubi = copy.deepcopy(naruto)
    kyuubi.name, kyuubi.picname, kyuubi.character, kyuubi.level = "Kyuubi", "kakashipic_r", kakashi_c, 79
    gai = copy.deepcopy(naruto)
    gai.name, gai.picname, gai.character, gai.level = "Gai", "oripic_r", ori_c, 32
    gai.add_to_village_ranks()
    
    team7 = Team("Team 7", kakashi, [sasuke, sakura, naruto]) 
    naruto.team = team7
    naruto.sensei = kakashi
    
    ALL_PLAYERS = [naruto, sasuke, sakura, kakashi, itachi, ori, gai]
    ALL_CHARACTERS = [c.character for c in ALL_PLAYERS]
        
    def get_random_jounin(player, village, exclude_sensei=False, exclude=[]):
        if exclude_sensei and player.sensei:
            sensei =  [player.sensei]
        else:
            sensei = [None] + exclude
            
        #renpy.say(player.character, "jounins: {}".format(village.jounins))
        
        remove_sensei_jounin = [j for j in village.jounins if j not in sensei]
        return random.choice(remove_sensei_jounin)
        
    ### STAGES ###
            
    clearing = Stage('Clearing', 1, 1)        
            
    ### SHOP ITEMS ###
    i_heal_paste = ShopItem("Heal Paste", 300, 30, health=30)
    i_chakra_paste = ShopItem("Chakra Paste", 300, 40, chakra=30)
    
    ### SHOPS ###
    hospital_shop = Shop("Hospital", 'leaf_hospital_1', items=[i_heal_paste, i_chakra_paste])
    weapon_shop = Shop("Weapons", 'leaf_shrine', items=[w_kunai, w_paper_bomb])
    
    ### MISSIONS ###
            
    # basic missions
    m_d1 = BasicMission('Farming', hours=12)
    m_d2 = BasicMission('Retrieve Cat', hours=8)
    m_d3 = BasicMission('Organise Festival', hours=10, days=2)
    m_d4 = BasicMission('Construction', hours=20, days=1)
    m_d5 = BasicMission('Paper Work', hours=14)
    m_d6 = BasicMission('Clean Academy', hours=5)
    m_label_test = LabelMission('Label Test', 'labelmissiontest', hours=10)
    
    m_test_fightmission = SimpleFightMission('Fight Itachi', days=10, rank='C', dialogue=[("", "I found you Itachi!")], 
                                             fights={'stage': clearing, 
                                                     'win_label': 'generic_win',
                                                     'lose_label': 'generic_lose',
                                                     'enemy': itachi,
                                                     'tag': []})
            
    m_test_multifight = MultiPartMission('Test Multi Fight', days=5, rank='B', 
                                          dialogue=[("scene", "sand_2"), 
                                                    ("naruto", "Testing dialogue"), 
                                                    ("fight", 1), 
                                                    ("naruto", "Now for Fight 2"), 
                                                    ("fight", 2)],
                                          fights=[{'stage': clearing, 
                                                   'win_label': 'generic_win',
                                                   'lose_label': 'generic_lose',
                                                   'enemy': itachi,
                                                   'tag': [],
                                                   'number': 1},
                                                  {'stage': clearing, 
                                                   'win_label': 'generic_win',
                                                   'lose_label': 'generic_lose',
                                                   'enemy': itachi,
                                                   'tag': [kakashi],
                                                   'number': 2}])
                                                   
    ALL_MISSIONS = [m_d1, m_d2, m_label_test, m_test_fightmission, m_test_multifight]
    
    ### GENERAL ###
    
    # populate events like this
    for d in ALL_DAYS:
        for e in ALL_EVENTS:
            if e.start and e.finish:
                for r in e.date_range():
                    if r.day == d.number and r.month == d.month.number:
                        d.events.append(e)
            elif e.frequency:
                for day in e.frequency:
                    if d.number == day:
                        d.events.append(e)
            elif e.chance:
                if (100*e.chance) > random.randint(1, 101):
                    d.events.append(e)
                    
    # only get unique events
    for d in ALL_DAYS:
        d.events = d.events #list(set(d.events))
    
    # screen vars
    screen_on = False
    calendar_on = False
    
    
            
##############################################################################
# STORY / GAME START
#

label start:
    
    jump character_creation
    
    # the below is obselete at the moment
    show screen player_stats
    show screen stats_screen(current_session.main_player)
    show screen time_screen
    $ show_village_map(current_session.village, naruto)
    #$ start_world_events()
    call fight(naruto, sasuke, [sakura], [kakashi], clearing)
    
label character_creation:
    scene black
    $ player_name = renpy.input("Set player name: ")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Maxwell"
        
    $ hero_c.name = player_name
    $ hero.name = player_name
    
    "Please choose stats for [hero.name]."
    
    $ current_session.main_player = hero
    $ current_session.main_player.allocation_points = 10
    
label allocate_points:
    if current_session.main_player.allocation_points > 0:
        call screen allocatepoints(current_session.main_player)
    else:
        hide screen explanation
        "Stats have been set, game is starting now."
        jump prologue
    
label prologue:
    "THE STORY NOW CONTINUES"
    current_session.main_player.character "Hello my name is [current_session.main_player.name]."
    # continue here
    return
    
            
##############################################################################
# MIDDLEWARE LABELS START
#
            
label skill_redirect:
    python:
        # deal with exceptions
        if current_session.skill.skill_type == 'counter':
            player.counter_state = True
        
        
        if current_session.skill_type == 'attack':
            current_session.skill.action(player,enemy)
        elif current_session.skill_type == 'defence':
            getattr(player, current_session.skill.label).apply()
            
    jump enemymove
    
label trap:
    jump settrap

label send_detective:
    "We need to investigate! Who should we send, and where should they go?"

    call screen send_detective_screen

    "Okay, we'll send [detective] to [city]."
    return

label world_update(village):
    scene map
    $ village.random_event()
    return
    
label village_redirect:
    $ current_session.location = None
    hide screen villagetravel
    python:
        main_time.advance_time(hours=current_session.time_to_advance.get('hours'),
                               days=current_session.time_to_advance.get('days'),
                               months=current_session.time_to_advance.get('months'),
                               years=current_session.time_to_advance.get('years'))
    $ current_session.clear_time_to_advance()
    
    python:
        if is_event_active_today(e_jinchurri_attack) and e_jinchurri_attack.occurrence < 1:
            e_jinchurri_attack.occurrence += 1
            renpy.call(e_jinchurri_attack.label, current_session.main_player, current_session.village)
        else:
            e_jinchurri_attack.occurrence = 0
    show screen player_stats
    show screen stats_screen(current_session.main_player)
    show screen time_screen
    $ show_village_map(current_session.village, current_session.main_player)
    current_session.main_player.character "I need to choose an action."
    jump village_redirect
    
label location_redirect:
    hide screen villagemap 
    python:
        main_time.advance_time(hours=current_session.time_to_advance.get('hours'),
                               days=current_session.time_to_advance.get('days'),
                               months=current_session.time_to_advance.get('months'),
                               years=current_session.time_to_advance.get('years'))
    # advance limb rest
    python:
        if current_session.rest:
            current_session.main_player.hp = current_session.main_player.maxhp
            current_session.main_player.chakra = current_session.main_player.maxchakra
            for limb in current_session.main_player.get_limbs():
                limb.rest(current_session.time_to_advance_in_days())
    
    $ current_session.clear_time_to_advance() # this clears rest too
    python:
        if current_session.location.background:
            renpy.hide(current_session.location.background)
            time_tag_show(current_session.location.background)
    $ renpy.call(current_session.location.label, current_session.main_player, current_session.village)
    
label missionselect_redirect:
    hide screen villagemissions
    show screen missionselect(current_session.village, current_session.main_player, current_session.mission_rank)
    current_session.main_player.character "I need to select a mission"
    jump missionselect_redirect
    
label mission_redirect:
    hide screen villagemap
    $ import random
    $ current_session.mission.do_mission(current_session.main_player, current_session.village, random.choice(ALL_VILLAGES))
    
label purchase_item_redirect:
    $ current_session.main_player.buy_item(current_session.item)
    jump location_redirect
    
label purchase_weapon_redirect:
    $ current_session.main_player.buy_weapon(current_session.item)
    jump location_redirect
    
label statscreen_show_redirect:
    hide screen player_stats
    show screen stats_screen(current_session.main_player)
    jump village_redirect
    
label statscreen_hide_redirect:
    hide screen stats_screen
    jump village_redirect
    
label injury_revert:
    
    if current_session.main_player.hp < current_session.main_player.maxhp:
        menu:
            "HP is not full, do you still want to continue?"
            
            "Yes":
                return
            "No":
                "HP/Chakra can be healed either at the hospital or by resting at home."
                $ current_session.clear_time_to_advance()
                jump village_redirect
    
    python:
        if current_session.main_player.get_injured_limbs():
            renpy.say(current_session.main_player.character, "I can't do this, I am injured and have to heal my injuries first by resting or from hospital.")
            current_session.clear_time_to_advance()
            renpy.jump("village_redirect")
            
label time_revert(opening_hour=6, closing_hour=18):
    python:
        if not main_time.hour in range(opening_hour, closing_hour):
            current_session.clear_time_to_advance()
            renpy.say("Guard",  "Sorry this place is only open between [opening_hour]AM and [closing_hour]PM.")
            renpy.jump("village_redirect")
            
    return
    
label village_travel(player, village):
    show screen villagetravel(village, player)
    player.character "I need to choose a destination"
    $ renpy.call('village_travel', player, village)
    
label village_levelup(player, village):
    show screen levelup(village, player)
    player.character "I need to choose level up stats"
    $ renpy.call('village_levelup', player, village)

label village_training(player, village):
    #scene training
    if player.hp < 50 or player.chakra < 50:
        player.character "I don't have enough hp or chakra to continue, I need to rest before I can train."
        jump village_redirect
    hide train_with_team
    hide train_skills
    show screen training(village, player)
    player.character "What should I do?"
    $ renpy.call('village_training', player, village)
    
label training_sensei:
    $ new_skill = get_sensei_skill(player.sensei, player)
    player.sensei.character "I am about to teach you is [new_skill.name]."
    if new_skill.unlock_exp < 300:
        player.sensei.character "It is a basic skill but fundamental to being a shinobi."
    elif new_skill.unlock_exp < 600:
        player.sensei.character "It is an intermediate skill but fundamental to being a shinobi."
    elif new_skill.unlock_exp < 900:
        player.sensei.character "It is an advanced skill and hard to master."
    # TODO: some sort of explanation
    player.character "[new_skill.name] added to skill set."
    $ renpy.call(current_session.location.label, current_session.main_player, current_session.village)
    
label train_skill_label:
    python:
        if current_session.main_player.get_injured_limbs():
            renpy.say(current_session.main_player.character, "I can't train, I am injured and have to heal my injuries first.")
            current_session.clear_time_to_advance()
        else:
            setattr(getattr(current_session.main_player, current_session.skill.label), current_session.skill.label,  current_session.skill.gain_exp(2000))
            renpy.say(current_session.main_player.character, "I have gained 200 exp for {}.".format(current_session.skill.name))
    jump location_redirect
    
label train_gain_exp:
    python:
        if current_session.main_player.get_injured_limbs():
            renpy.say(current_session.main_player.character, "I can't train, I am injured and have to heal my injuries first.")
            current_session.clear_time_to_advance()
        else:
            current_session.main_player.gain_exp(10)
    jump location_redirect
    
label training_spar:
    # heal the spar partners before the fight
    python:
        for p in current_session.spar:
            p.full_heal()
    
    if len(current_session.spar) == 1:
        current_session.main_player.character "Lets spar [current_session.spar[0].name]."
        current_session.spar[0].character "Lets go."
        call fight(current_session.main_player, current_session.spar[0], [], [], clearing)
    
    if len(current_session.spar) > 1:
        current_session.main_player.character "Lets spar [current_session.spar[0].name] and [current_session.spar[1].name]."
        current_session.spar[0].character "Lets go."
        current_session.spar[1].character "Lets do this."
        call fight(current_session.main_player, current_session.spar[0], [], [current_session.spar[1]], clearing)
    
label village_arena(player, village):
    show screen villagearena(village, player)
    player.character "I need to choose the arena fight."
    $ renpy.call('village_arena', player, village)
    
label village_hospital(player, village):
    # maybe show hospital for each village here
    show screen hospitalshop(village, player)
    player.character "I need to choose items to buy."
    $ renpy.call('village_hospital', player, village)
    
label hospital_injury:
    #call time_revert
    # TODO: special events, etc
    $ injury_bill = player.get_injury_bill()
    "Nurse" "Looks like you are injured."
    "Nurse" "Lets take a look here."
    "Nurse" "....."
    "Nurse" "That will be [injury_bill[0]] Ryo."
    if current_session.main_player.ryo >= injury_bill[0]:
        current_session.main_player.character "Here."
        $ current_session.main_player.ryo -= injury_bill[0]
        "Nurse" "You can stay here and rest up, we will discharge you once your fully healed."
        $ current_session.main_player.heal_all_injuries()
    else:
        current_session.main_player.character "Sorry, I do not have enough ryo."
        "Nurse" "I would suggest you heal your minor injuries by resting at home, then once you have enough ryo we can treat you."
        $ current_session.clear_time_to_advance()
    
    jump location_redirect
    
label village_jounin_station(player, village):
    # TODO: handle npc events
    python:
        if is_event_active_today(e_jounin_training) and main_time.hour in range(6, 18):
            renpy.jump("event_jounin_training")
            
    "Jounin" "Sorry, no training events today, please come back on the 1st of next month between 6AM and 6PM."
    jump village_redirect
    
label event_jounin_training:
    $ trainer = get_random_jounin(current_session.main_player, current_session.village, exclude_sensei=True)
    $ random_value = renpy.random.randint(1,3)
    if random_value == 1:
        $ new_skill = get_sensei_skill(trainer, current_session.main_player)
        trainer.character "I am about to teach you is [new_skill.name]."
        if new_skill.unlock_exp < 300:
            trainer.character "It is a basic skill but fundamental to being a shinobi."
        elif new_skill.unlock_exp < 600:
            trainer.character "It is an intermediate skill but fundamental to being a shinobi."
        elif new_skill.unlock_exp < 900:
            trainer.character "It is an advanced skill and hard to master."
        # TODO: some sort of explanation
        current_session.main_player.character "[new_skill.name] added to skill set."
    elif random_value == 2:
        trainer.character "This class is about improving general concentration and ninja skills."
        trainer.character "It will take a few hours but I'm sure you will benefit from this greater."
        $ maxhp_increase += renpy.random.randint(5, 10)
        $ maxchakra_increase += renpy.random.randint(5, 10)
        $ exp_increase = renpy.random.randint(10, 30)
        $ current_session.main_player.maxhp += maxhp_increase
        current_session.main_player.character "Max HP increased by [maxhp_increase]."
        $ current_session.main_player.maxchakra += maxchakra_increase
        current_session.main_player.character "Max HP increased by [maxchakra_increase]."
        $ current_session.main_player.gain_exp(exp_increase)
        current_session.main_player.character "Exp increased by [exp_increase]."
    else:
        trainer.character "We will focus on on particular skill today."
        python:
            skill_improve = random.choice(current_session.main_player.all_skills)
            setattr(getattr(current_session.main_player, skill_improve.label), skill_improve.label,  skill_improve.gain_exp(100))
            renpy.say(current_session.main_player.character,  "I have gained 100 exp for {}.".format(skill_improve.name))
        
    $ main_time.advance_time(hours=6)
    jump village_redirect
    
label village_intelligence_division(player, village):
    "SAMPLE" "TRAVEL HERE"
    jump start
    
label village_ninja_tool_facility(player, village):
    call time_revert
    # maybe show different weapon shop here
    show screen weaponshop(village, player)
    player.character "I need to choose weapons to buy."
    $ renpy.call('village_ninja_tool_facility', player, village)
    
label village_missions(player, village):
    hide screen missionselect
    show screen villagemissions(village, player)
    player.character "I need to choose mission."
    $ renpy.call('village_missions', player, village)
    
label village_home(player, village):
    hide rest_screen
    show screen villagehome(village, player)
    #show screen calendar_screen_toggle
    player.character "I need choose an action."
    $ renpy.call('village_home', player, village)
    
label jinchurri_attack(player, village):
    player.character "I feel a chill in the air..."
    player.character "There is an immense chakra in the air."
    # randomise the tailed beasts here
    kyuubi.character "ROAR!!!"
    # chance of finding team or random jounins
    $ random_choice = renpy.random.randint(1,2)
    if random_choice == 1:
        if player.team:
            player.team.members[0].character "[player.name] are you okay!?"
            player.team.members[1].character "The whole village is under attack."
            player.character "No! Lets fight him."
            # affects and stuff
            player.character "The huge beast faces us."
            call fight(player, kyuubi, player.team.members, [], clearing)
        else:
            player.character "The huge beast faces me."
            call fight(player, anko, [], [], clearing)
            
    else:
        player.character "I can't find my team mates."
        player.character "I see some jounins."
        $ jounin_1 = get_random_jounin(player, village, exclude=[])
        $ jounin_2 = get_random_jounin(player, village, exclude=[jounin_1])
        jounin_1.character "Lets go!"
        call fight(player, anko, [jounin_1, jounin_2], [], clearing)
        
label village_arena_level5:
    call time_revert
    call injury_revert
    # TODO: Add arena background
    scene dream_2
    current_session.main_player.character "Time to fight in the arena."
    itachi.character "I will be your opponent!"
    call fight(current_session.main_player, itachi, [], [], clearing)
    
label village_arena_level10:
    call time_revert
    call injury_revert
    # TODO: Add arena background
    scene dream_2
    current_session.main_player.character "Time to fight in the arena."
    ori.character "I will be your opponent!"
    call fight(current_session.main_player, ori, [], [], clearing)
            
### LABEL MISSIONS ###
            
label labelmissiontest(player, village):
    player.character "This is a test mission."
    player.character "Anything can go here."
    jump village_redirect
    
            
### NPC LABELS ###
label sasuke1:
    $ sasuke.npc_event.count += 1
    $ time_tag_show("leaf_1")
    current_session.main_player.character "Hi Sasuke, we are meeting the first time."
    # TODO: character sprites??
    sasuke.character "How is it going."
    " " "We eat ramen at the ramen shop."
    $ bond_increase = renpy.random.randint(10, 15)
    $ sasuke.bond += bond_increase
    current_session.main_player.character "My bond with Sasuke goes up by [bond_increase]."
    jump village_redirect
    
label sasuke2:
    $ sasuke.npc_event.count += 1
    $ time_tag_show("leaf_1")
    $ sasuke.npc_event.stop = True
    current_session.main_player.character "Hi Sasuke, we are meeting the second time."
    sasuke.character "How is it going."
    " " "We eat ramen at the ramen shop."
    $ bond_increase = renpy.random.randint(10, 15)
    $ sasuke.bond += bond_increase
    current_session.main_player.character "My bond with Sasuke goes up by [bond_increase]."
    jump village_redirect
    

label tag_partner:
    $ info = get_tag_info(player, tag_p)
    $ renpy.hide(player.picname)
    $ renpy.call('fight', info['main'], enemy, info['tag'], tag_e, stage, win_label, lose_label, draw_label)
    
label fight(player, enemy, tag_p, tag_e, stage=clearing, win_label='generic_win', lose_label='generic_lose', draw_label='generic_draw', fight_limit=20):
    #scene bg
    $ hide_battle_screen(all=True)
    
    # set current_session
    $ current_session.enemy_tag = tag_e
    $ current_session.player_tag = tag_p
    $ current_session.stage = stage
    $ current_session.win_label = win_label
    $ current_session.lose_label = lose_label
    $ current_session.draw_label = draw_label
    $ current_session.fight_limit = fight_limit
    
    call hidetiles
    call showtiles
    hide screen movemenu
    hide screen settrap
    # initial position
    call remove_projections
    call initial_pos(player, enemy)
        
    $ highlight_position(player, enemy, stage)
    $ end_match(player, enemy, tag_p, tag_e, win_label, lose_label, draw_label)
    $ remove_all_skill_affects(player, enemy)
    
    show screen battlebars(tag_p, tag_e)
    #show screen stats
    call screen battlemenu(player, tag_p)
    
label initial_pos(player, enemy):
    python:
        if current_session.initial_pos:
            show_player_at_pos(player, enemy, current_session.stage, tile1)
            show_player_at_pos(enemy, player, current_session.stage, tile12)
            current_session.initial_pos = False
    return
    
label remove_projections:
    python:
        for tile in TILES:
            tile.deproject()
    return
    
label generic_win(player):
    $ hide_battle_screen(all=True)
    $ battle_turn = 0
    $ exp = renpy.random.randint(100,200) + 200
    $ player.gain_exp(exp)
    if current_session.spar:
        $ chemistry = renpy.random.randint(10, 15)
        $ player.team.increase_chemistry(chemistry)
        player.character "I gained [chemistry] team chemistry."
        $ current_session.spar = []
    # maybe rotated random dialogues here? TODO
    player.character "I won the match and gained [exp] exp."
    player.character "Now to head back to the village."
    player.character "..."
    player.character "..........."
    player.character "......................."
    python:
        main_time.advance_time(hours=current_session.time_to_advance.get('hours'),
                               days=current_session.time_to_advance.get('days'),
                               months=current_session.time_to_advance.get('months'),
                               years=current_session.time_to_advance.get('years'))
    
    $ current_session.clear_time_to_advance() # this clears rest too
    call mission_report(player, current_session.mission)
    $ show_village_map(current_session.village, current_session.main_player)

label generic_lose(player):
    $ hide_battle_screen(all=True)
    $ battle_turn = 0
    $ exp = renpy.random.randint(50,100) + 50
    $ player.gain_exp(exp)
    if current_session.spar:
        $ chemistry = renpy.random.randint(10, 15)
        $ player.team.increase_chemistry(chemistry)
        player.character "I gained [chemistry] team chemistry."
        $ current_session.spar = []
    player.character "I lost the match and gained [exp] exp."
    player.character "Now to head back to the village."
    player.character "..."
    player.character "..........."
    player.character "......................."
    python:
        main_time.advance_time(hours=current_session.time_to_advance.get('hours'),
                               days=current_session.time_to_advance.get('days'),
                               months=current_session.time_to_advance.get('months'),
                               years=current_session.time_to_advance.get('years'))
    
    $ current_session.clear_time_to_advance() # this clears rest too
    call mission_report(player, current_session.mission)
    $ show_village_map(current_session.village, current_session.main_player)
    
label generic_draw(player):
    $ hide_battle_screen(all=True)
    $ battle_turn = 0
    $ exp = renpy.random.randint(100,200) + 100
    $ player.gain_exp(exp)
    if current_session.spar:
        $ chemistry = renpy.random.randint(10, 15)
        $ player.team.increase_chemistry(chemistry)
        player.character "I gained [chemistry] team chemistry."
        $ current_session.spar = []
    player.character "I draw the match and gained [exp] exp."
    player.character "Now to head back to the village."
    player.character "..."
    player.character "..........."
    player.character "......................."
    python:
        main_time.advance_time(hours=current_session.time_to_advance.get('hours'),
                               days=current_session.time_to_advance.get('days'),
                               months=current_session.time_to_advance.get('months'),
                               years=current_session.time_to_advance.get('years'))
    
    $ current_session.clear_time_to_advance() # this clears rest too
    call mission_report(player, current_session.mission)
    $ show_village_map(current_session.village, current_session.main_player)
    
label mission_report(player, mission):
    # scene mission table?? TODO 
    python:
        if mission:
            if mission.success:
                renpy.say(player.home_village.leader.character, "Good work {}.".format(player.name))
                reward = mission.reward(player)
                renpy.say(player.home_village.leader.character, "Here is your reward ryo {} and exp {}.".format(reward['ryo'], reward['exp']))
            else:
                renpy.say(player.home_village.leader.character, "It is unfortunate {} but you failed.".format(player.name))
                reward = mission.reward(player, half=True)
                renpy.say(player.home_village.leader.character, "Here is your reward ryo {} and exp {} for your trouble.".format(reward['ryo'], reward['exp']))
    $ current_session.mission = None
    return
    
label standby:
    $ player.chakra += player.stamina * 5
    jump enemymove
    
label enemymove:
    $ moved = False
    $ end_match(player, enemy, tag_p, tag_e, win_label, lose_label, draw_label)
    $ remove_all_skill_affects(player, enemy)
    
    python:
        if enemy.stunned:
            renpy.say(player.character, "The enemy is stunned and cannot move.")
            enemy.stunned = False
        else:
            if player.counter_state:
                counter_move(player, enemy)
            else:
                enemy_move(player, enemy, clearing, tag_p, tag_e)

    $ battle_turn += 1
    call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label showtiles:
    show tile1im at tile1pos
    show tile2im at tile2pos
    show tile3im at tile3pos
    show tile4im at tile4pos
    show tile5im at tile5pos
    show tile6im at tile6pos
    show tile7im at tile7pos
    show tile8im at tile8pos
    show tile9im at tile9pos
    show tile10im at tile10pos
    show tile11im at tile11pos
    show tile12im at tile12pos
    return
    
label hidetiles:
    hide tile1im
    hide tile2im
    hide tile3im
    hide tile4im
    hide tile5im
    hide tile6im
    hide tile7im
    hide tile8im
    hide tile9im
    hide tile10im
    hide tile11im
    hide tile12im
    return
