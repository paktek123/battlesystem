##############################################################################
# FUNCTIONAL TESTS
#

# All the test objects can go in the init block because we don't care about saving in the tests

init 2 python:
    
    ### TEST DATA ###
    
    test_player_character = Character('Test Player',color="#FFFFFF")
    test_enemy_character = Character('Test Enemy',color="#FFFFFF")
    test_stage = Stage('Test Stage', 1, 1)
    test_heal_paste = ShopItem("Test Heal Paste", 300, 30, health=30)
    test_chakra_paste = ShopItem("Test Chakra Paste", 300, 40, chakra=30)
    test_potion_shop = Shop("Hospital", 'test_1', items=[test_heal_paste, test_chakra_paste])
    test_battle1 = Battle(id="1", good_team=[], bad_team=[], xpos=100, ypos=100, battle_label="b_battle_1")
    test_main_time = GameTime(9, 1, 1, 2015)
    test_ranged_event = Event("Ranged Event", "CE", start=(15, 5), finish=(14, 7), label="chunin_exam")
    test_frequency_event = Event("Frequency Event", "JT", frequency=(1, ))
    test_probability_event = Event("Probability Event", "???",chance=0.02, label="jinchurri_attack", occurrence=0)
    #e_weapon_discount = Event("Weapon Discount", "WD", frequency=(random.randint(2,30),)) 
    #e_hospital_discount = Event("Hospital Discount", "HD", frequency=(random.randint(2,30),)) 
    
    # Skills
    test_melee_skill = Skill(name='Punching Flurry', skill_type='melee', label="punchingflurry", range=2, damage=20)
    test_special_skill = Skill(name="Blast Kick", skill_type="special", label="blast_kick", range=3, chakra_cost=30, damage=60, unlock_exp=300)
    test_sensei_skill = Skill(name="Rise Punch", skill_type="special", label="rise_punch", range=2, chakra_cost=40, damage=35)
    test_stun_skill = Skill('Substitution', 'ranged', "substitution", 8, 20, 15, 0, stun=True)
    test_damage_reduction = Skill('Focus', 'defence', 'damagereduction', 12, 1, 10, duration=2, unlock_exp=300)
    test_chakra_defence = Skill('Chakra Defence', 'defence', 'chakradefence', 12, 2, 15, duration=3, unlock_exp=500)
    test_reflect = Skill('Reflect', 'defence', 'reflect', 12, 20, 20, duration=2, unlock_exp=1500)
    test_dampen = Skill('Dampen', 'defence', 'dampen', 6, 30, 30, duration=3, unlock_exp=2000)
    test_yata_mirror = Skill('Yata Mirror', 'defence', 'ignore', 12, 50, 50, duration=2, unlock_exp=2500)
    test_knife = Weapon(name='Knife', price=30, range=2, chakra_cost=5, damage=25)
    test_bat = Weapon(name='Bat', price=50, range=3, chakra_cost=10, damage=30)
    
    # AI Skill pool
    TEST_SKILL_SET = [test_melee_skill, test_special_skill, test_stun_skill, 
                      test_damage_reduction, test_chakra_defence, test_reflect, test_dampen, test_yata_mirror
                      test_knife, test_bat]
    
    # Players
    test_player_1 = LevelledPlayer(lvl=8, name="Test Player", skill_pool=TEST_SKILL_SET, character=test_player_character, 
                                   hudpic="test_player_hud", tilepic="hero_1_tile_r")
    test_player_2 = LevelledPlayer(lvl=8, name="Test Player", skill_pool=TEST_SKILL_SET, character=test_player_character, 
                                   hudpic="test_player_hud", tilepic="hero_1_tile_r")
    test_player_3 = LevelledPlayer(lvl=8, name="Test Player", skill_pool=TEST_SKILL_SET, character=test_player_character, 
                                   hudpic="test_player_hud", tilepic="hero_1_tile_r")
    test_player_sensei = LevelledPlayer(lvl=8, name="Test Sensei", skill_pool=TEST_SKILL_SET + [test_sensei_skill], character=test_player_character, 
                                   hudpic="test_player_hud", tilepic="hero_1_tile_r")
    test_enemy_1 = LevelledPlayer(lvl=8, name="Test Enemy", skill_pool=TEST_SKILL_SET, character=test_enemy_character, 
                                  hudpic="test_enemy_hud", tilepic="thug_1_tile_l")
    test_enemy_2 = LevelledPlayer(lvl=8, name="Test Enemy", skill_pool=TEST_SKILL_SET, character=test_enemy_character, 
                                  hudpic="test_enemy_hud", tilepic="thug_1_tile_l")
    test_enemy_3 = LevelledPlayer(lvl=8, name="Test Enemy", skill_pool=TEST_SKILL_SET, character=test_enemy_character, 
                                  hudpic="test_enemy_hud", tilepic="thug_1_tile_l")
    
    test_team_first = Team("Test Team", test_player_sensei, [test_player_1, test_player_2, test_player_3])
    test_player_1.sensei = test_player_sensei
    
    # locations
    test_location = Location('Test', 'test_label', 'test_background', events=[test_frequency_event])
    
    BASE_LOCATIONS = [test_location]
    
    test_village_1 = Village(1, "Test Village 1", test_player_sensei, marker_xpos=0.40, marker_ypos=0.25, map="test_map", 
                             locations=BASE_LOCATIONS, village_tag="middle_town", mission_locations=2, wealth=50)
    
    test_village_2 = Village(1, "Test Village 2", test_player_sensei, marker_xpos=0.40, marker_ypos=0.25, map="test_map", 
                             locations=BASE_LOCATIONS, village_tag="middle_town", mission_locations=2, wealth=50)
    
    ALL_VILLAGES = [test_village_1, test_village_2]
    
    ALL_EVENTS = [test_ranged_event, test_frequency_event, test_probability_event] #, e_weapon_discount, e_hospital_discount]
    
    # populate events
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
        d.events = d.events