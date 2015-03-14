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
    image black_fade = "gfx/black.png" #Solid((0, 0, 0, 150))
    image black_fade_small = Solid((0, 0, 0, 150), area=(0.4, 0.7, 0.6,0.4)) # im.Tile(im.Scale("black.png", 400, 300)
    image world_marker = im.Scale("marker.png", 33, 35)
    image leader_pic = im.Scale("leader_pic.png", 100, 150)
    define world_events = Character('World Events', color='#3399FF', window_left_padding=150, show_side_image=Image("leader_pic.png", xpos=0.03, yalign=0.96))
    image map = im.Scale("map.png", 800, 600)
    image stats_idle = Solid((0, 0, 0, 200), area=(0.62, 0.0, 300,150))
    
    $ HUD_WIDTH = 140
    $ HUD_HEIGHT = 150
    
    ### HUD PICS ###
    image hero_hud = im.Scale("hero_hud.png", HUD_WIDTH, HUD_HEIGHT)
    image thug_hud = im.Scale("thug_hud.png", HUD_WIDTH, HUD_HEIGHT)
    image bison_hud = im.Scale("bison_hud.png", HUD_WIDTH, HUD_HEIGHT)
    image ai_hud = im.Scale("ai_hud.png", HUD_WIDTH, HUD_HEIGHT)
    image monk_hud = im.Scale("monk_hud.png", HUD_WIDTH, HUD_HEIGHT)
    
    ### TILE PICS ###
    
    image hero_tile_l = im.Scale("hero_1_tile.png", 40, 50)
    image hero_tile_r = im.Flip(im.Scale("hero_1_tile.png", 40, 50), horizontal=True)
    image thug_tile_l = im.Scale("thug_1_tile.png", 40, 50)
    image thug_tile_r = im.Flip(im.Scale("thug_1_tile.png", 40, 50), horizontal=True)
    image will_tile_l = im.Scale("hero_1_tile.png", 40, 50)
    image will_tile_r = im.Flip(im.Scale("hero_1_tile.png", 40, 50), horizontal=True)
    
    # 120, 150 for large enemies
    #image dragon_tile_l = im.Scale("attack_1.png", 120, 150)
    
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
    image sam_2 = im.Scale("sam_2.png", 270, 500)
    image adam_1 = im.Scale("adam_1.png", 400, 600)
    image adam_2 = im.Scale("adam_2.png", 400, 600)
    image adam_3 = im.Scale("adam_3.png", 400, 600)
    image amy_1 = im.Scale("amy_1.png", 270, 500)
    image amy_2 = im.Scale("amy_2.png", 270, 500)
    image amy_3 = im.Scale("amy_3.png", 270, 500)
    image greyson_1 = im.Scale("greyson_1.png", 270, 500)
    image will_1 = im.Scale("will_1.png", 270, 500)
    image bison_1 = im.Scale("bison_1.png", 270, 500)
    image ai_1 = im.Scale("ai_1.png", 300, 600)
    image monk_1 = im.Scale("monk_1.png", 300, 600)
    
    ### SPECIAL EFFECTS ###
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    $ red_flash = Fade(.25, 0, .75, color="#ff0000")
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

    # Define tilepics in the teams folder
    #for fname in os.listdir(config.gamedir + '/teams'):
    #    if fname.endswith(('.jpg', '.png')) and fname not in IMAGE_EXCEPTIONS:
    #        tag = fname[:-4]
    #        fname =  'teams/' + fname
    #        renpy.image(tag + '_r', im.Scale(fname, 50, 60))
    #        renpy.image(tag + '_l', im.Flip(im.Scale(fname, 50, 60), horizontal=True))
    
    
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
    
    ### CURRENT SESSION ###
        
    current_session = CurrentSession()
    
    ### SKILLS ###
    
    # melee skills
    punching_flurry = Skill(name='Punching Flurry', skill_type='melee', label="punchingflurry", range=2, damage=20)
    onetwocombo = Skill(name='One Two Combo', skill_type='melee', label="onetwocombo", range=3, damage=30)
    jaw_breaker = Skill(name="Jaw Breaker", skill_type='melee', label='jaw_breaker', range=2, damage=40)
    thug_smash = Skill(name='Thug Smash', skill_type='melee', label="thug_smash", range=2, damage=25)
    
    
    lioncombo = Skill('Lion Combo', 'melee', "lioncombo", 3, 2, 5, 20, unlock_exp=300)
    
    # special skills
    blasting_kick = Skill(name="Blast Kick", skill_type="special", label="blast_kick", range=3, chakra_cost=30, damage=60)
    rise_punch = Skill(name="Rise Punch", skill_type="special", label="rise_punch", range=2, chakra_cost=40, damage=35)
    
    rasengan = Skill('Rasengan', 'special', "rasengan", 2, 1, 25, 30, unlock_exp=500)
    chidori = Skill('Chidori', 'special', "chidori", 2, 1, 25, 30, unlock_exp=1000)
    raikiri = Skill('Raikiri', 'special', "raikiri", 2, 1, 50, 50, unlock_exp=1500)
    
    # ranged skills
    rock_throw = Skill(name="Rock Throw", skill_type="ranged", label="rock_throw", range=7, chakra_cost=10, damage=15)
    distance_hit = Skill(name="Distance Hit", skill_type="ranged", label="distance_hit", range=8, chakra_cost=20, damage=20)
    
    substitution = Skill('Substitution', 'ranged', "substitution", 8, 20, 15, 0, stun=True)
    
    # defensive skills
    metal_jacket = Skill(name='Metal Jacket', skill_type='defence', label='metal_jacket', range=12, duration=3)
    intimidate = Skill(name='Intimidate', skill_type='defence', label='intimidate', range=6, duration=3)
    
    
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
    w_bbgun = Weapon(name='BB Gun', price=400, range=10, chakra_cost=0, damage=40)
    
    w_kunai = Weapon("Kunai", price=50, range=4, chakra_cost=4, damage=20)
    w_paper_bomb = Weapon("Paper Bomb", price=100, range=2, chakra_cost=5, damage=50)
    shiruken = Weapon('Shiruken', 'weapon', "shiruken", 12, 7, 1, 20)
    kunai = Weapon('Kunai', 'weapon', "kunai", 12, 4, 1, 20)
    trap = Weapon('Trap', 'weapon', "trap", 3, 1, 2, 30)
    
    THUG_MELEE_SKILL_SET = [onetwocombo, jaw_breaker, thug_smash, metal_jacket, intimidate, w_knife, w_bat]
    THUG_RANGED_SKILL_SET = [rock_throw, distance_hit, metal_jacket, w_bbgun]
    
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
    nar_c = Character('    ',color="#FFFF00", who_color="#FFFF00")
    hero_c = Character('NO NAME',color="#FFFF00")
    thug_c = Character('Thug',color="#FFFFFF")
    sam_c = Character('Sam', color="#FFFFFF")
    adam_c = Character('Adam',color="#FFFF00")
    amy_c = Character('Amy',color="#FFFF00")
    greyson_c = Character('Greyson',color="#FFFF00")
    will_c = Character('Will',color="#FFFF00")
    bison_c = Character('Bison',color="#FFFF00")
    ai_c = Character('Ai',color="#FFFF00")
    monk_c = Character('Monk',color="#FFFF00")
    
    naruto_c = Character('Naruto',color="#FFFF00") 
    sasuke_c = Character('Sasuke', color="#3399FF")
    sakura_c = Character('Sakura', color="#FA58F4")
    kakashi_c = Character('Kakashi', color="#3399FF")
    itachi_c = Character('Itachi', color="#FFFFFF")
    ori_c = Character('Orichimaru', color="#FF0000")
    
    lvl_1_thug_melee = LevelledEnemy(lvl=1, skill_pool=THUG_MELEE_SKILL_SET, character=thug_c, tile=tile12)
    lvl_1_thug_ranged = LevelledEnemy(lvl=1, skill_pool=THUG_RANGED_SKILL_SET, character=thug_c, tile=tile12)
    
    lvl_4_thug_melee = LevelledEnemy(lvl=4, skill_pool=THUG_MELEE_SKILL_SET, character=thug_c, tile=tile12)
    lvl_4_thug_ranged = LevelledEnemy(lvl=4, skill_pool=THUG_RANGED_SKILL_SET, character=thug_c, tile=tile12)
    
    # give him unique skill set
    lvl_8_bison_melee = LevelledEnemy(lvl=8, skill_pool=THUG_MELEE_SKILL_SET, character=bison_c, tile=tile12, hudpic="bison_hud")
    
    lvl_15_adam = LevelledEnemy(lvl=15, skill_pool=THUG_RANGED_SKILL_SET, character=adam_c, tile=tile12, picname="adam_1")
    lvl_15_ai = LevelledEnemy(lvl=15, skill_pool=THUG_RANGED_SKILL_SET, character=ai_c, tile=tile12, picname="ai_1")
    lvl_15_monk = LevelledEnemy(lvl=15, skill_pool=THUG_RANGED_SKILL_SET, character=monk_c, tile=tile12, picname="monk_1")

    # Use this for quick character creation
    #lvl_15_daniel = LevelledEnemy(lvl=15, skill_pool=THUG_MELEE_SKILL_SET, character=daniel_c, tile=tile12, tilepic="fe_1_r")
    
    hero = Player(name='NO NAME', picname="hero_tile_r", character=hero_c, tilepic="hero_tile_r", hudpic='hero_hud', 
                  hp=100, maxhp=100, chakra=80, maxchakra=80, 
                  strength=1, speed=1, evasion=1, defence=1, stamina=1, base_hit_rate=80, 
                  tile=tile1, facing='right', 
                  meleeskills=[punching_flurry], specialskills=[], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[], 
                  home_village=None)
    
    thug = Player(name='Thug', picname="thug_tile_r", character=thug_c, tilepic="thug_tile_r", hudpic='thug_hud', 
                  hp=100, maxhp=100, chakra=80, maxchakra=80, 
                  strength=5, speed=5, evasion=1, defence=1, stamina=1, base_hit_rate=80, 
                  tile=tile1, facing='left', 
                  meleeskills=[onetwocombo], specialskills=[], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_knife], 
                  home_village=None)
    
    # unique moves
    sam = Player(name='Sam', picname="thug_tile_r", character=thug_c, tilepic="thug_tile_r", hudpic='thug_1_hud', 
                  hp=150, maxhp=150, chakra=120, maxchakra=120, 
                  strength=9, speed=6, evasion=6, defence=8, stamina=6, base_hit_rate=80, 
                  tile=tile1, facing='left', 
                  meleeskills=[onetwocombo], specialskills=[blasting_kick], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_knife, w_brass_knuckles], 
                  home_village=None)
    
    will = Player(name='Will', picname="will_tile_r", character=thug_c, tilepic="will_tile_r", hudpic='will_1_hud', 
                  hp=200, maxhp=200, chakra=150, maxchakra=150, 
                  strength=10, speed=6, evasion=6, defence=10, stamina=10, base_hit_rate=90, 
                  tile=tile1, facing='left', 
                  meleeskills=[onetwocombo, jaw_breaker], specialskills=[blasting_kick], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_brass_knuckles], 
                  home_village=None)
    
    greyson = Player(name='Greyson', picname="will_tile_r", character=thug_c, tilepic="will_tile_r", hudpic='will_1_hud', 
                  hp=120, maxhp=120, chakra=60, maxchakra=60, 
                  strength=7, speed=3, evasion=3, defence=4, stamina=3, base_hit_rate=70, 
                  tile=tile1, facing='left', 
                  meleeskills=[onetwocombo, jaw_breaker], specialskills=[blasting_kick], rangedskills=[], 
                  items=[], defensiveskills=[], bloodlineskills=[], 
                  leader_pic="leader_pic", 
                  weapons=[w_brass_knuckles], 
                  home_village=None)
    
    naruto = Player('Naruto',"thug_tile_r", naruto_c, "thug_tile_r", "thug_tile_r", 100, 100, 80, 80, 10, 4, 3, 4, 5, 80, tile1, 'right', 
                    [onetwocombo], [rasengan], [substitution], [],
                    [damage_reduction, chakra_defence, reflect, dampen, yata_mirror], [], "leader_pic", 
                    weapons=[shiruken, kunai], home_village=None)
    sasuke = Player('Sasuke', "thug_tile_r", sasuke_c, "thug_tile_r", "thug_tile_r", 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [chidori], [], [], [damage_reduction, chakra_defence], 
                    battle_ai=special_enemy_pattern, weapons=[shiruken, kunai], home_village=None) #, interaction={'frequency': (1,)})
    
    sakura = Player('Sakura', "thug_tile_r", sakura_c, "thug_tile_r", "thug_tile_r", 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [chidori], [], [], [damage_reduction, chakra_defence], weapons=[shiruken, kunai])
    kakashi = Player('Kakashi', "thug_tile_r", kakashi_c, "thug_tile_r", "thug_tile_r", 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [raikiri], [], [], [damage_reduction, chakra_defence], level=32,
                    battle_ai=special_enemy_pattern, weapons=[shiruken, kunai])
    anko = Player('Anko', "thug_tile_r", kakashi_c, "thug_tile_r","thug_tile_r", 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo], [raikiri], [], [], [damage_reduction, chakra_defence], level=32,
                    battle_ai=special_enemy_pattern, weapons=[shiruken, kunai])
    
    itachi = copy.deepcopy(sasuke)
    itachi.name, itachi.picname, itachi.character, itachi.level = "Itachi", "thug_tile_r", itachi_c, 46
    ori = copy.deepcopy(naruto)
    ori.name, ori.picname, ori.character, ori.level = "Orichimaru", "thug_tile_r", ori_c, 45
    kyuubi = copy.deepcopy(naruto)
    kyuubi.name, kyuubi.picname, kyuubi.character, kyuubi.level = "Kyuubi", "thug_tile_r", kakashi_c, 79
    gai = copy.deepcopy(naruto)
    gai.name, gai.picname, gai.character, gai.level = "Gai", "thug_tile_r", ori_c, 32
    gai.add_to_village_ranks()
    
    team7 = Team("Team 7", kakashi, [sasuke, sakura, naruto]) 
    naruto.team = team7
    naruto.sensei = kakashi
    
    team_first = Team("First Team", None, [will, hero, greyson])
    
    ALL_PLAYERS = [hero, thug, will, lvl_1_thug_melee, lvl_1_thug_ranged]
    
    #ALL_PLAYERS = [naruto, sasuke, sakura, kakashi, itachi, ori, gai]
    ALL_CHARACTERS = [c.character for c in ALL_PLAYERS]
        
    def get_random_jounin(player, village, exclude_sensei=False, exclude=[]):
        if exclude_sensei and player.sensei:
            sensei =  [player.sensei]
        else:
            sensei = [None] + exclude
            
        #renpy.say(player.character, "jounins: {}".format(village.jounins))
        
        remove_sensei_jounin = [j for j in village.jounins if j not in sensei]
        return random.choice(remove_sensei_jounin)
        
    ### VILLAGE AND LOCATIONS ###

    ### Use existing already defined labels not new ones 
    
    l_hospital = Location('Hospital', 'village_hospital', 'street_4', events=[e_hospital_discount])
    l_police_station = Location('Police Station', 'village_police_station', 'building_1', events=[e_weapon_discount])
    l_level_up = Location('Level Up', 'village_levelup', 'apartment_1')
    l_training_ground = Location('Training', 'village_training', 'forest_2')
    l_town_mission = Location('Mission', 'village_missions', events=[],)
    l_apartment = Location('Apartment', 'village_home', 'apartment_1')

    # locations that exist in each village
    l_travel = Location('Travel', 'village_travel')
    #l_level_up = Location('Level Up', 'village_levelup')
    #l_training_ground = Location('Training', 'village_training', 'training')
    l_arena = Location('Arena', 'village_arena')
    l_jounin_station = Location('Jounin Standby Station', 'village_jounin_station', events=[e_jounin_training])
    l_intelligence_division = Location('Intelligence Division', 'village_intelligence_division')
    l_ninja_tool_facility = Location('Ninja Tool Facility', 'village_ninja_tool_facility', events=[e_weapon_discount])
    l_villagemission = Location('Mission Assignment Desk', 'village_missions', events=[e_chunin_exams])
    l_home = Location('Home', 'village_home')
    
    BASE_LOCATIONS = [l_level_up, l_training_ground, l_town_mission, l_apartment, l_hospital, l_police_station]
    
    #BASE_LOCATIONS = [l_travel, l_level_up, l_training_ground, l_arena, l_hospital, l_jounin_station, l_intelligence_division, l_ninja_tool_facility, l_villagemission, l_home]
    
    middle_town = Village(1, "Middle Town", lvl_15_adam, marker_xpos=0.40, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="middle_town", mission_locations=2, wealth=50)
    east_town = Village(2, "East Town", lvl_15_monk, marker_xpos=0.60, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="east_town", mission_locations=2)    
    south_town = Village(3, "South Town", lvl_15_ai, marker_xpos=0.45, marker_ypos=0.65, map="town_map_1", locations=BASE_LOCATIONS, village_tag="south_town", mission_locations=2)
    west_town = Village(4, "West Town", None, marker_xpos=0.25, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="west_town", mission_locations=2)    
    north_town = Village(5, "North Town", None, marker_xpos=0.25, marker_ypos=0.25, map="town_map_1", locations=BASE_LOCATIONS, village_tag="north_town", mission_locations=2)    
        
    hidden_stone = Village(1, "Hidden Stone", None, marker_xpos=0.25, marker_ypos=0.25, map="stones_map", locations=BASE_LOCATIONS, village_tag="stones", mission_locations=2)
    hidden_cloud = Village(2, "Hidden Cloud", None, marker_xpos=0.75, marker_ypos=0.20, map="clouds_map", locations=BASE_LOCATIONS, village_tag="cloud", mission_locations=2)
    hidden_mist = Village(3, "Hidden Mist", None, marker_xpos=0.85, marker_ypos=0.70, map="mist_map", locations=BASE_LOCATIONS, village_tag="mist", mission_locations=2)
    hidden_leaf = Village(4, "Hidden Leaf", None, marker_xpos=0.40, marker_ypos=0.60, map="konoha_map", locations=BASE_LOCATIONS, village_tag="leaf", mission_locations=2)
    hidden_sand = Village(5, "Hidden Sand", None, marker_xpos=0.25, marker_ypos=0.90, map="sand_map", locations=BASE_LOCATIONS, village_tag="sand", mission_locations=4)
        
    ALL_VILLAGES = [east_town, south_town, middle_town] # west_town, north_town] 
    
    def other_villages(village):
        return [v for v in ALL_VILLAGES if v.id != village.id]
        
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
    m_secure_hospital = LabelMission('Secure Hospital', 'prologue_hospital', hours=11, location=l_hospital)
    m_secure_police_station = LabelMission('Secure Police Station', 'prologue_police_station', hours=11, location=l_police_station)
    m_infiltrate_hold = LabelMission('Infiltrate Hold', 'mission_infiltrate_hold', hours=5, rank='D')
    m_defeat_sam = LabelMission('Defeat Sam', 'mission_defeat_sam', hours=6, rank='C')
    
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
                                                   
    ALL_MISSIONS = [m_secure_hospital, m_secure_police_station, m_infiltrate_hold, m_defeat_sam]
    
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
    
    battle1 = Battle(id="1", good_team=[], bad_team=[], xpos=100, ypos=100, battle_label="b_battle_1")
    battle2 = Battle(id="2", good_team=[], bad_team=[], xpos=300, ypos=100, battle_label="b_battle_2")
    battle_last = Battle(id="last", good_team=[], bad_team=[], xpos=500, ypos=100, battle_label="b_battle_last")
    
    ALL_BATTLES = [battle1, battle2, battle_last]

    ### BattleMission Class
    m_infiltrate_hold_battle = BattleMission(name="Infiltrate Hold", 
                                      hours=6, 
                                      good_team=team_first,
                                      battles={'1':[lvl_4_thug_ranged], '2':[lvl_4_thug_melee], 'last':[lvl_8_bison_melee]}, 
                                      follow_on='prologue_continue', 
                                      all_battles=ALL_BATTLES)
    
    #ALL_MISSIONS += m_infiltrate_hold

    # called like this
    #$ battlemission1.do_mission(hero_c)
    
            
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
    
    #jump intro_world_events
    
    $ at_map = False
        
    jump character_creation
    
    # the below is obselete at the moment
    show screen player_stats
    show screen stats_screen(current_session.main_player)
    show screen time_screen
    $ show_village_map(current_session.village, naruto)
    #$ start_world_events()
    call fight(naruto, sasuke, [sakura], [kakashi], clearing)
    
label character_creation:
    show creation_background
    
    nar_c "This is an example of a very long test that I am writing here right this instant and it will reach to the end of the this window where I cannot see anything and I dont like this very much."
    
    # Assign a default value
    $ player_name="Maxwell"
    
    $ player_name = renpy.input("Set player name: ")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Maxwell"
        
    $ hero_c.name = player_name.lower().capitalize()
    $ hero.name = player_name
    
    nar_c "Please choose stats for [hero.name]."
    
    $ current_session.main_player = hero
    $ current_session.main_player.allocation_points = 10
    
    
label allocate_points:
    
    if current_session.main_player.allocation_points > 0:
        call screen allocatepoints(current_session.main_player)
    else:
        hide screen explanation
        nar_c "Stats have been set, game is starting now."
        jump prologue1
        
label reset_allocation_points:
    python:
        stats = ['strength', 'speed', 'evasion', 'defence', 'stamina', 'melee', 'special', 'ranged']
        for stat in stats:
            setattr(current_session.main_player, stat, 1)
        current_session.main_player.allocation_points = 10
    jump allocate_points
    
label prologue1:
    #"THE STORY NOW CONTINUES"
    #hero_c "Hello my name is [current_session.main_player.name]."
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
    show thug_1 with dissolve
    "Thug 1" "You bastard! I'll make sure you never stand up again!"
    "Thug 2" "I'll.... oooff."
    hide thug_1 with dissolve
    nar_c "Both of them are throwing punches at each other and rolling on the ground."
    nar_c "Just seeing those two go at it, puts me at unease."
    nar_c "My heart starts pounding faster and body fills up with adrenaline."
    nar_c "..."
    nar_c "They are fighting in front of me, I need to somehow get round them and call the police."
    "Thug 2" "Oooooffff." with sshake
    nar_c "One of the thugs flies off to the side and bangs his head against the wall."
    nar_c "There are blood stains everywhere, he soon looses conciousness."
    show thug_1 with dissolve
    "Thug 1" "You!"
    nar_c "He looks at me, I freeze."
    nar_c "My heart is pounding, I really don't want to be involved in this..."
    nar_c "...."
    hide thug_1 with dissolve
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
    show thug_1 with dissolve
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
    hide thug_1 with dissolve
    nar_c "He turns around and starts to walk away."
    ### TODO: Add some motivation for our hero to get back on this feet and challenge Mr Thug to a fight
    ### Maybe some sort of past flashback or something
    nar_c "I fix my collar and stand up."
    hero_c "Ohey... Bastard..."
    hero_c "You think you can do whatever you want, let me kick your ass."
    nar_c "As soon as he hears this, he turns around with an angry expression."
    show thug_1 with dissolve
    "Thug" "Say that again!"
    nar_c "He throws a punch..."
    nar_c "... I grab his fist and push him away."
    "Thug" "Heh.... I'll pound you to death!"
    nar_c "I know I can't go back now but maybe that is what I want."
    hide thug_1 with dissolve
    $ renpy.call('fight', hero, thug, [], [], clearing, lose_label='prologue2', draw_label='prologue2', fight_limit=5)
    # fight redirects to prologue2 label
    return
    
label prologue2:
    scene street_2 night with dissolve
    hero_c "...." with sshake
    hero_c "Huff...."
    hero_c "Ughhh...." with red_flash
    nar_c "Blood splatters everywhere."
    nar_c "My body is covered in bruises and cuts from his knife."
    show thug_1 with dissolve
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
    hide thug_1 with dissolve
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
    #### I AM HERE #### RESIZE GREYSON
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
    "The Doctor interrupts us."
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
    nar_c "{color=#006400}Hospital Secured! New location unlocked!{/color}" 
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
    "I see a familiar face."
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
    "Will puts both of us down."
    will_c "Adam! Help!"
    show adam_1 with dissolve
    adam_c "Amy bring the equipment!"
    nar_c "......."
    nar_c "....."
    scene black_fade with black_flash
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
    "He sighs."
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
    "It is the same as we saw the other day."
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
    
    $ m_infiltrate_mission_battle.do_mission(hero_c)
    
label prologue_continue:
    call hidetiles
    # hero gains experience
    $ hide_battle_screen(all=True)
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
    if hero.lvl < 3:
        adam_c "You must be level 3 or above to do this mission, use level up to increase level."
        jump town_map
        
    
    scene apartment_1 with squares
    nar_c "............"
    show adam_1 with dissolve
    adam_c "The seurity around the school has cleared."
    adam_c "We can go in a defeat Sam, the leader of the gang here."
    adam_c "............"
    adam_c "Go."
    scene school_1 with squares
    nar_c "............"
    nar_c "........"
    nar_c "There is no security, I make my way towards the roof."
    scene rooftop with squares
    sam_c "Long time, no see."
    sam_c "Fight me 1 on 1."
    hero_c "I'll defeat you!"
    
    $ renpy.call('fight', hero, sam, [], [], clearing, win_label='prologue_end', lose_label='prologue_end', draw_label='prologue_end', fight_limit=15)
    
label prologue_end:
    
    scene rooftop_1 with squares
    
    nar_c "Sam overpowers me." with sshake
    
    show sam_1 with dissolve
    
    sam_c "You still cannot defeat me!"
    
    show sam_1 at left with dissolve
    show will_1 at right with dissolve
    
    will_c "Thats enough Sam!"
    will_c "Lets end this before we all get hurt."
    "Sam is bleeding too, he is in pain from our fight just now."
    sam_c "If I don't takeover this city, that guy will walk all over us."
    will_c "What do you mean!?"
    sam_c "You don't understand, the leader that came back was our father!"
    will_c "....."
    "Will stares at Sam in shock."
    will_c "I... had no idea...."
    sam_c "Work with me Will, we do this."
    will_c "I don't approve of your methods and I am going to take you down here."
    # will vs sam fight
    nar_c ".............."
    will_c "Blast kick!" with sshake
    nar_c "The kick connects and send Sam flying into the wall."
    sam_c "......ughhh...."
    "Sam is knocked out."
    
    hide sam_c with dissolve
    show will_1 with dissolve
    
    will_c "Its over."
    
    nar_c ".............."
    nar_c "Greyson helps me up and we head back to the apartment."
    
    scene apartment_1 with squares
    nar_c "..........."
    nar_c ".........."
    "Will brings Sam and Bison to the apartment too."
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
    scene forest_1 with squares
    show ai_1 with dissolve
    ai_c "Seems like middle town are starting gather some force."
    ai_c "We should start to prepare for his return too."
    ai_c "I won't let what happened 10 years ago repeat again."
    nar_c "..........."
    nar_c "......."
    scene home_1 with squares
    show monk_1 with dissolve
    nar_c ".............."
    monk_c "Looks like the vision were true."
    monk_c "I can't wait to spill blood again!"
    nar_c "..........."
    jump intro_world_events
    
label intro_world_events:
    
    $ start_world_events('prologue_end2')
    
label prologue_end2:
    scene apartment_1 with squares
    nar_c "............"
    nar_c "........"
    nar_c "A week has gone by since we defeated Sam."
    nar_c "He and Bison have been recovering."
    show sam_1 with dissolve
    sam_c "Ok ok... I will join to help."
    show sam_1 at left with dissolve
    show bison_1 at right with dissolve
    bison_c "If Sam joins that leaves me no choice, I will join too."
    show adam_1 with dissolve
    adam_c "That is good to know."
    adam_c "We need to stop your Father from making his comeback."
    adam_c "Sam and Bison you will join Will, Greyson and [hero.name] in their battles."
    hide sam_1 with dissolve
    hide bison_1 with dissolve
    hide adam_1 with dissolve
    nar_c ".........."
    nar_c "Bison and Sam join Party!"
    $ team_first.members += sam
    $ team_first.members += bison
    show amy_1 with dissolve
    amy_c "I want to fight too."
    "Amy joins party"
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
    show screen villagemap(middle_town, hero)
    
    $ renpy.pause(2.0, hard=True)
    
    show screen announce("GANG RISER EPISODE 1")
    
    $ renpy.pause(2.0, hard=True)
    
    # end game
    return
    
    
    
    
            
##############################################################################
# MIDDLEWARE LABELS START
#

label reset_battle:
    python:
        for b in current_session.battles:
            b.good_team = []
    # battle_follow_on is set in battle_prep_screen
    $ renpy.call('battle_choose')
    
label b_battle_2:
    $ second_battle = get_battle_from_label('b_battle_2')
    $ current_session.battle = second_battle
    $ second_battle.fight(stage=clearing, win_label=second_battle.next_battle_label, lose_label=second_battle.next_battle_label, draw_label=second_battle.next_battle_label, fight_limit=10)
    
label b_battle_last:
    $ last_battle = get_battle_from_label('b_battle_last')
    $ current_session.battle = last_battle
    $ last_battle.fight(stage=clearing, win_label='battle_choose', lose_label='battle_choose', draw_label='battle_choose', fight_limit=10)
    
label battle_start:
    
    $ first_battle = current_session.battles[0]
    $ current_session.battle = first_battle
    
    $ first_battle.fight(stage=clearing, win_label=first_battle.next_battle_label, lose_label=first_battle.next_battle_label, draw_label=first_battle.next_battle_label, fight_limit=10)
            
    
label battle_choose:
    call hidetiles
    
    hide screen battle_selection_screen
    hide screen battle_prep_screen
    
    python:
        battle_result = battle_finished(current_session.battles)
        if battle_result['is_finished']:
            if battle_result['outcome'] == 'lose':
                # TODO: jump retreat label
                pass
            else:
                renpy.jump(current_session.battle_follow_on) 
    
    $ populate_battles(current_session.battles, current_session.battle_follow_on)
    show screen battle_prep_screen
    "Choose battlefield for players."
    jump battle_choose
    
            
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
    $ hide_battle_screen(all=True)
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
    
label village_police_station(player, village):
    call time_revert
    # maybe show different weapon shop here
    show screen weaponshop(village, player)
    player.character "I need to choose weapons to buy."
    $ renpy.call('village_ninja_tool_facility', player, village)
    
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
    $ renpy.hide(player.tilepic)
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
    #show screen player_limbs(player=player)
    call screen battlemenu(player, tag_p)
    
label initial_pos(player, enemy):
    python:
        if current_session.initial_pos:
            show_player_at_pos(enemy, player, current_session.stage, tile12)
            show_player_at_pos(player, enemy, current_session.stage, tile1)
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
