#### RISER BATTLE SYSTEM #####


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
    
    ### HUD PICS ###
    image hero_1_hud = im.Scale("hero_1_hud.png", 150, 200)
    image thug_1_hud = im.Scale("thug_1_hud.png", 150, 200)
    
    ### TILE PICS ###
    
    image hero_tile_l = im.Scale("hero_1_tile.png", 40, 50)
    image hero_tile_r = im.Flip(im.Scale("hero_1_tile.png", 40, 50), horizontal=True)
    image thug_tile_l = im.Scale("thug_1_tile.png", 40, 50)
    image thug_tile_r = im.Flip(im.Scale("thug_1_tile.png", 40, 50), horizontal=True)
    
    
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
    
    ### BARS ###
    image blue_bar = im.Scale("bar_blue.png", 130, 20) 
    
    ### SPRITES ###
    image thug_1 = im.Scale("thug_1.png", 270, 500)
    image adam_1 = im.Scale("adam_1.png", 270, 500)
    image adam_2 = im.Scale("adam_2.png", 270, 500)
    image adam_3 = im.Scale("adam_3.png", 270, 500)
    image amy_1 = im.Scale("amy_1.png", 270, 400)
    image amy_2 = im.Scale("amy_2.png", 270, 400)
    image amy_3 = im.Scale("amy_3.png", 270, 400)
    image greyson_1 = im.Scale("greyson_1.png", 270, 500)
    
    ### SPECIAL EFFECTS ###
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    $ red_flash = Fade(.25, 0, .75, color="#ff0")
    $ black_flash = Fade(.5, 0, .5, color="#000")

    
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
    
    # melee skills
    punching_flurry = Skill(name='Punching Flurry', skill_type='melee', label="punchingflurry", range=2, damage=20)
    onetwocombo = Skill(name='One Two Combo', skill_type='melee', label="onetwocombo", range=3, damage=30)
    jaw_breaker = Skill(name="Jaw Breaker", skill_type='melee', label='jaw_breaker', range=2, damage=40)
    
    
    lioncombo = Skill('Lion Combo', 'melee', "lioncombo", 3, 2, 5, 20, unlock_exp=300)
    
    # special skills
    blasting_kick = Skill(name="Blast Kick", skill_type="special", "blast_kick", range=3, chakra_cost=30, damage=60)
    
    rasengan = Skill('Rasengan', 'special', "rasengan", 2, 1, 25, 30, unlock_exp=500)
    chidori = Skill('Chidori', 'special', "chidori", 2, 1, 25, 30, unlock_exp=1000)
    raikiri = Skill('Raikiri', 'special', "raikiri", 2, 1, 50, 50, unlock_exp=1500)
    
    # ranged skills # replace with something new
    substitution = Skill('Substitution', 'ranged', "substitution", 8, 20, 15, 0, stun=True)
    
    # defensive skills
    damage_reduction = Skill('Focus', 'defence', 'damagereduction', 12, 1, 10, duration=2, unlock_exp=300)
    chakra_defence = Skill('Chakra Defence', 'defence', 'chakradefence', 12, 2, 15, duration=3, unlock_exp=500)
    substitution = Skill('Substitution', 'counter', "substitution", 8, 20, 15, 0, stun=True)
    reflect = Skill('Reflect', 'defence', 'reflect', 12, 20, 20, duration=2, unlock_exp=1500)
    dampen = Skill('Dampen', 'defence', 'dampen', 6, 30, 30, duration=3, unlock_exp=2000)
    yata_mirror = Skill('Yata Mirror', 'defence', 'yatamirror', 12, 50, 50, duration=2, unlock_exp=2500)
    
    ### WEAPONS ###
    w_knife = Weapon(name='Knife', price=30, range=2, chakra_cost=5, damage=25)
    w_bat = Weapon(name='Bat', price=50, range=3, chakra_cost=10, damage=30)
    w_brass_knuckles = Weapon(name='Brass Knuckles', price=100, range=1, chakra_cost=5, damage=50)
    
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
    # melee = use taijutsu skills
    # special = use ninjustsu skills
    # ranged = use genjutsu skills
    # healing items and tagging will be in enemy_move itself
    defensive_enemy_pattern = 2*['d'] + 2*['f'] + 2*['a'] + 2*['t']
    attack_enemy_pattern = 3*['a'] + 2*['f']
    ranged_attack_pattern = 4*['f'] + 2*['d']
    melee_enemy_pattern = 3*['melee'] + 2*['d']
    special_enemy_pattern = 3*['special'] + ['d'] + ['a'] + ['f']
    ranged_enemy_pattern = 3*['ranged'] + 2*['d'] + ['f']
    
    ### CHARACTERS ###
    hero_c = Character('NO NAME',color="#FFFF00")
    thug_c = Character('Thug',color="#FFFFFF")
    adam_c = Character('Adam',color="#FFFF00")
    amy_c = Character('Amy',color="#FFFF00")
    greyson_c = Character('Greyson',color="#FFFF00")
    will_c = Character('Will',color="#FFFF00")
    
    
    naruto_c = Character('Naruto',color="#FFFF00") 
    sasuke_c = Character('Sasuke', color="#3399FF")
    sakura_c = Character('Sakura', color="#FA58F4")
    kakashi_c = Character('Kakashi', color="#3399FF")
    itachi_c = Character('Itachi', color="#FFFFFF")
    ori_c = Character('Orichimaru', color="#FF0000")
    
    hero = Player(name='NO NAME', picname="hero_tile_r", character=hero_c, tilepic="hero_tile_r", hudpic='hero_1_hud', 
                  hp=100, maxhp=100, chakra=80, maxchakra=80, 
                  strength=5, speed=5, evasion=1, defence=1, stamina=1, base_hit_rate=80, 
                  tile=tile1, facing='right', 
                  meleeskills=[punching_flurry], specialskills=[], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[], 
                  home_village=None)
    
    thug = Player(name='Thug', picname="thug_tile_r", character=thug_c, tilepic="thug_tile_r", hudpic='thug_1_hud', 
                  hp=100, maxhp=100, chakra=80, maxchakra=80, 
                  strength=5, speed=5, evasion=1, defence=1, stamina=1, base_hit_rate=80, 
                  tile=tile1, facing='left', 
                  meleeskills=[onetwocombo], specialskills=[], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_knife], 
                  home_village=None)
    
    will = Player(name='Will', picname="will_tile_r", character=thug_c, tilepic="will_tile_r", hudpic='will_1_hud', 
                  hp=200, maxhp=200, chakra=150, maxchakra=150, 
                  strength=10, speed=6, evasion=6, defence=10, stamina=10, base_hit_rate=90, 
                  tile=tile1, facing='left', 
                  meleeskills=[onetwocombo, jaw_breaker], specialskills=[blast_kick], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_brass_knuckles], 
                  home_village=None)
    
    naruto = Player('Naruto', "playerpic_r", naruto_c, Image('player.png'), None, 100, 100, 80, 80, 10, 4, 3, 4, 5, 80, tile1, 'right', 
                    [onetwocombo], [rasengan], [substitution], [],
                    [damage_reduction, chakra_defence, reflect, dampen, yata_mirror], [], "leader_pic", 
                    weapons=[shiruken, kunai], home_village=hidden_leaf)
    sasuke = Player('Sasuke', "enemypic_r", sasuke_c, Image('enemy.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [chidori], [], [], [damage_reduction, chakra_defence], 
                    battle_ai=special_enemy_pattern, weapons=[shiruken, kunai], home_village=hidden_leaf, interaction={'frequency': (1,)})
    
    sakura = Player('Sakura', "sakurapic_r", sakura_c, Image('sakura.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [chidori], [], [], [damage_reduction, chakra_defence], weapons=[shiruken, kunai], home_village=hidden_leaf)
    kakashi = Player('Kakashi', "kakashipic_r", kakashi_c, Image('kakashi.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [raikiri], [], [], [damage_reduction, chakra_defence], level=32,
                    battle_ai=special_enemy_pattern, weapons=[shiruken, kunai], home_village=hidden_leaf)
    anko = Player('Anko', "kakashipic_r", kakashi_c, Image('kakashi.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [raikiri], [], [], [damage_reduction, chakra_defence], level=32,
                    battle_ai=special_enemy_pattern, weapons=[shiruken, kunai], home_village=hidden_leaf)
    
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
    
    
    $ player_name="Maxwell"
    $ hero_c.name = player_name
    $ hero.name = player_name
    $ current_session.main_player = hero
    
    jump prologue1 # remove the above
    
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
        jump prologue1
    
label prologue1:
    #"THE STORY NOW CONTINUES"
    #hero_c "Hello my name is [current_session.main_player.name]."
    scene street_3 night with dissolve
    
    "The sunsets and I finally end my shift."
    "It is a little late, I usually leave before its dark."
    "...."
    "I make my way towards the underpass."
    scene underpass_1 night with dissolve
    "My house is about a fifteen minute walk from my work place."
    "..."
    "In the distance I see two people wrestling on the road in front of me."
    "They clearly don't care about getting run over by cars."
    show thug_1 with dissolve
    "Thug 1" "You bastard! I'll make sure you never stand up again!"
    "Thug 2" "I'll.... oooff."
    hide thug_1 with dissolve
    "Both of them are throwing punches at each other and rolling on the ground."
    "Just seeing those two go at it, puts me at unease."
    "My heart starts pounding faster and body fills up with adrenaline."
    "..."
    "They are fighting in front of me, I need to somehow get round them and call the police."
    "Thug 2" "Oooooffff." with sshake
    "One of the thugs flies off to the side and bangs his head against the wall."
    "There are blood stains everywhere, he soon looses conciousness."
    show thug_1 with dissolve
    "Thug 1" "You!"
    "He looks at me, I freeze."
    "My heart is pounding, I really don't want to be involved in this..."
    "...."
    hide thug_1 with dissolve
    "I turn around and make a run for it."
    scene street_2 night with dissolve 
    "I quickly take a turn into a side street." with sshake
    "Hufff.... hufff...."
    "I hear police sirens in the background... what is going on!?"
    "My head is going crazy with random thoughts, I need to get it together."
    "Hufff...  hufff...."
    ".... I get pushed to the ground." with sshake
    hero_c "Owww...."
    "There is a sharp pain in my upper arm."
    "I look around to try to work out what just happenned."
    show thug_1 with dissolve
    "Thug" "You thought you could get away from me!?"
    hero_c "How... did..."
    "I am lost for words, how did he get behind me?"
    "He must have pushed me to the ground from behind."
    "Thug" "You saw me do that, I can't let you just leave without making sure you don't squeak."
    "He grabs me by the collar of my shirt."
    hero_c "Ughhh...."
    "My heart is pounding very hard... I don't want to get hurt..."
    hero_c "Why are you doing this? I won't tell the cops, please let me go."
    "Thug" "Here is a present." with sshake
    hero_c "Ooooffff...." 
    "He punches me in my stomach and throws me to the ground."
    "A sharp pain starts building up around my abdomen."
    "Thug" "If I ever see your face again, I will pound your face in."
    "Thug" "Don't even think of talking to the police."
    hide thug_1 with dissolve
    "He turns around and starts to walk away."
    ### TODO: Add some motivation for our hero to get back on this feet and challenge Mr Thug to a fight
    ### Maybe some sort of past flashback or something
    "I fix my collar and stand up."
    hero_c "Ohey... Bastard..."
    hero_c "You think you can do whatever you want, let me kick your ass."
    "As soon as he hears this, he turns around with an angry expression."
    show thug_1 with dissolve
    "Thug" "Say that again!"
    "He throws a punch..."
    "... I grab his fist and push him away."
    "Thug" "Heh.... I'll pound you to death!"
    "I know I can't go back now but maybe that is what I want."
    hide thug_1 with dissolve
    $ renpy.call('fight', hero, thug, [], [], clearing, lose_label='prologue2', draw_label='prologue2', fight_limit=5)
    # fight redirects to prologue2 label
    return
    
label prologue2:
    scene street_2 night with dissolve
    hero_c "...." with sshake
    hero_c "Huff...."
    hero_c "Ughhh...." with red_flash
    "Blood splatters everywhere."
    "My body is covered in bruises and cuts from his knife."
    show thug_1 with dissolve
    "He is also in a similar condition, I am surprised he is standing."
    "Thug" "Hehh.... hehhh.... "
    "He gives off a strange laugh."
    "Thug" "You haven't seen anything yet!"
    "He tries to attack me..."
    "Thug" "Gahhh... cough..." with red_flash
    "He coughs blood, the damage must have gotten to him."
    ".... there is a sudden pause, both of us know if we continue this won't end well for us."
    "Thug" "You are lucky this time, I will find you and finish you off."
    hero_c "Just try it."
    "My whole body is in pain, his reply helps me to relax."
    "Thug" "Let me leave you with a present... heh..." with red_flash
    "He slashes my body with his knife and throws me to the ground." with sshake
    hero_c "Gahhh..."
    "Thug" "Next time I will kill you."
    hide thug_1 with dissolve
    "He runs away limping."
    "...."
    "My shirt has become red with my blood."
    "I don't have the strength to get up... as I lay on the ground."
    "My eyes are closing by themselves."
    "..."
    "......"
    scene black_fade with black_flash
    "Voice" "Hey! Hey! Stay with me here!"
    "Voice" "Don't die please!"
    "...."
    "........."
    "..............."
    scene apartment_1 afternoon with dissolve
    "......"
    "The sun shines onto my eyes."
    "I can hear birds chirping in the background."
    "I lay on the ground... my body has been bandaged up."
    "...."
    "I hear a voice from my right."
    show amy_2 with dissolve
    "???" "Adam, he is awake!"
    "...."
    "The girl runs away."
    hide amy_2 with dissolve
    "......"
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
    "He heads inside the house."
    "I notice my surroundings..."
    "There is blood on the ground near me... bandages and surgical tools lying around everywhere."
    "The whole place is filled with many other people covered in bandages."
    "It looks like a war zone."
    "What the heck happened last night!?"
    "......"
    "I lay on my bed... hopefully this is a bad dream...."
    "...."
    scene black_fade with dissolve
    "......."
    "....."
    "..."
    scene apartment_1 evening with dissolve
    "..."
    "I open my eyes and sit up."
    "I feel no pain from my wounds."
    "....."
    "In the distance I see a gathering of the wounded."
    "I force myself up and head towards the gathering."
    show adam_1 with dissolve
    adam_c "We don't know the situation as of now."
    adam_c "Hey, please join us."
    "I take a seat, many others are wrapped up in bandages like me."
    ### TODO: more descriptions of the wounded and confusion, people speaking
    adam_c "I found all of you last night either wounded or near death."
    adam_c "I know that many of you have many questions, I will try my best to explain what happened."
    "....."
    "The crowd listens carefully, they are as confused as I am."
    adam_c "Last night there were many attacks carried out by various gangs... another words..."
    adam_c "There was a gang war in this town where four or five gangs all decided to go at each other at once."
    "Person 1" "Are you telling me that some stupid kids just went crazy!?"
    "The whole crowd starts to talk."
    "Person 2" "Where is the police!?"
    adam_c "Everyone please listen."
    "Everybody lowers their voices."
    adam_c "I do not know where the police is, I have called them many times but no one picks up the phone!"
    "Person 1" "What is that is crazy! Does anyone have a phone here, let me try!"
    "....."
    "Person 2" "Here, my phone still has some battery."
    "Person 1" "Give me please."
    "He dials the three digit number."
    "...."
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
    "There injured discuss between themselves."
    # TODO: panic?
    hero_c "What are our options?"
    adam_c "We need to organise a party amongst us to venture outside and find out more information."
    adam_c "We need to move when it is dark to avoid detection."
    adam_c "Which one of you want to volunteer?"
    "We cannot stay like this, there are roughly 5 of us here and some wounded inside."
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
    "That guy looks familiar, like I have seen him before..."
    "He has a resemblence to that thug I fought last night."
    "I need to help out too."
    hero_c "I will help too."
    hide will_1 with dissolve
    show adam_1 with dissolve
    adam_c "I will go too."
    will_c "No you can't you must stay here and help the wounded."
    greyson_c "Yes we will go."
    adam_c "How do you expect to survive out there!?"
    will_c "We will."
    hide adam_1 with dissolve
    "..........."
    "........"
    scene apartment_1 night with squares
    "We finally decide that only 3 of us will go without Adam."
    "......"
    show will_1 with dissolve 
    will_c "Lets move."
    greyson_c "Yes."
    scene street_1 night with squares
    "We climb over the walls and the streets seem to be clear."
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
    hero_c "We should go to the hospital to retrieve medical supplies and heal the wounded."
    hero_c "Someone there must also know what is going on here."
    greyson_c "But my family... I want make sure they are safe..."
    will_c "I think [hero_c.name] is right here, we can split up."
    # TODO: Some friction between team mates
    greyson_c "I am going to go to the Police Station myself, I don't care care!"
    hide greyson_1 with dissolve
    "We are powerless to stop him as he heads North towards the police station."
    show will_1 with dissolve
    will_c "Leave him, we must get medical supplies."
    "I reluctantly decide to move on."
    "If we quickly confirm the Hospital is safe we can come to help Greyson."
    "...."
    "..."
    scene street_4 night with squares
    "There are a few gang members driving around but we manage to avoid most of them."
    "Survellence is certainly low near the hospital."
    "....."
    "We see the hospital nearby, its lights are on."
    "Looks like it is under lockdown by the gang members."
    "We hear some voices near the entrance."
    "Doctor" "Stop this at once!"
    "Thug" "Shut it Doc, your staying here for now."
    "He punches the Doctor, which causes him to fall down."
    "Doctor" "Arghhh...."
    "....."
    "A nurse comes out and helps the Doctor up to his feet."
    "She takes him inside."
    "Thug" "Hehh... stupid..."
    "...."
    show will_1 with dissolve
    will_c "Looks like they are just guarding the entrance, we should be able to get inside."
    hero_c "You mean we take out that thug?"
    "...."
    "Two other thugs walk out with baseball bats."
    "We are tucked away behind a wall so they cannot see us."
    hero_c "These guys are very close, we will have to take them head on."
    will_c "Heh... we think a like..."
    "Will rolls up his sleeve and walks out unarmed."
    hide will_1 with dissolve
    hero_c "Hey... I didn't mean you walk out like that!?"
    "I follow him."
    "Thugs" "Hey! You come here."
    "The mob rushes at us.... we have no choice but to fight..."
    # create a weaker thug, a thug generator depending on level
    $ renpy.call('fight', hero, thug, [will], [copy.deepcopy(thug)], clearing, lose_label='prologue2', draw_label='prologue2', fight_limit=5)
    
    
    
            
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
    call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label, fight_limit)
    
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
