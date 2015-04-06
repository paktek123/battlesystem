##############################################################################
# FUNCTIONAL TESTS
#

# All the test objects can go in the init block because we don't care about saving in the tests

init python:
    
    import copy
    
    ### TEST DATA ###
    
    test_player_character = Character('Test Player',color="#FFFFFF")
    test_enemy_character = Character('Test Enemy',color="#FFFFFF")
    test_stage = Stage('Test Stage', 1, 1)
    test_heal_paste = ShopItem("Test Heal Paste", 300, 30, health=30)
    test_chakra_paste = ShopItem("Test Chakra Paste", 300, 40, chakra=30)
    test_potion_shop = Shop("Hospital", 'test_1', items=[test_heal_paste, test_chakra_paste])
    test_battle1 = Battle(id="1", good_team=[], bad_team=[], xpos=100, ypos=100, battle_label="b_battle_1")
    test_main_time = GameTime(9, 1, 1, 2015)
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
                      test_damage_reduction, test_chakra_defence, test_reflect, test_dampen, test_yata_mirror,
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
    test_location = None #Location('Test', 'test_label', 'test_background', events=[test_frequency_event])
    
    BASE_LOCATIONS = [test_location]
    
    test_village_1 = Village(1, "Test Village 1", test_player_sensei, marker_xpos=0.40, marker_ypos=0.25, map="test_map", 
                             locations=BASE_LOCATIONS, village_tag="middle_town", mission_locations=2, wealth=50)
    
    test_village_2 = Village(1, "Test Village 2", test_player_sensei, marker_xpos=0.40, marker_ypos=0.25, map="test_map", 
                             locations=BASE_LOCATIONS, village_tag="middle_town", mission_locations=2, wealth=50)
    
    ALL_VILLAGES = [test_village_1, test_village_2]
        
    # Test helpers
    def record_test(description, result, expected_result, accumulated_results):
        test_entry = {description: ( result == expected_result) }
        accumulated_results.append(test_entry)
    
    battle_tests_results = []
    event_tests_results = []
        
label run_tests:
    call battle_tests
    call event_tests
    #call gametime_tests
    #call helper_tests
    #call mission_tests
    #call player_tests
    #call shop_tests
    #call skill_tests
    #call stage_tests
    #call tile_tests
    #call village_tests
    
    show screen test_results("Event", event_tests_results)
    nar_c "Click for next set of tests..."
    
    hide screen test_results
    show screen test_results("Battle", battle_tests_results)
    nar_c "Click for next set of tests..."
    
    
label battle_tests:
    
    # functional testing
    python:
        test_battle1 = Battle(id="1", good_team=[test_player_2], bad_team=[test_enemy_1, test_enemy_2], xpos=100, ypos=100, battle_label="b_battle_1")
        test_battle2 = Battle(id="2", good_team=[test_player_2], bad_team=[], xpos=300, ypos=100, battle_label="b_battle_2")
        
        test_battle1.add_good_member(test_player_1)
        record_test('Add Good Member', test_battle1.good_team, [test_player_2, test_player_1], battle_tests_results)
        
        test_battle1.add_good_member(test_player_1)
        record_test('Add Duplicate Member', test_battle1.good_team, [test_player_2, test_player_1], battle_tests_results)
        
        test_battle1.remove_good_member(test_player_1)
        record_test('Remove Good Member', test_battle1.good_team, [test_player_2], battle_tests_results)
        
        test_battle1.remove_good_member(test_player_1)
        record_test('Cannot remove non-existant member', test_battle1.good_team, [test_player_2], battle_tests_results)
        
        false_result = test_battle1.finished()
        record_test('Battle Not finished', false_result, False, battle_tests_results)
        
        # set hp to zero for bad team
        zero_hp_enemy_1 = copy.deepcopy(test_enemy_1)
        zero_hp_enemy_1.hp = 0
        zero_hp_enemy_2 = copy.deepcopy(test_enemy_1)
        zero_hp_enemy_2.hp = 0
        test_battle1.bad_team = [zero_hp_enemy_1, zero_hp_enemy_2]
        
        true_result = test_battle1.finished()
        record_test('Battle finished', true_result, True, battle_tests_results)
        
        other_battles = [test_battle1, test_battle2]
        
        test_battle1.cleanup(other_battles)
        record_test('Cleanup duplicate good team members', test_battle2.good_team, [], battle_tests_results)
        
        test_battle1.clean_dead_members()
        record_test('Cleanup dead good members', test_battle1.good_team, [test_player_2], battle_tests_results)
        record_test('Cleanup dead bad members', test_battle1.bad_team, [], battle_tests_results)
        
    return
    
label event_tests:
    
    # functional testing
    python:
        test_ranged_event = Event("Ranged Event", "CE", start=(15, 5), finish=(14, 7), label="ranged_event")
        test_frequency_event = Event("Frequency Event", "JT", frequency=(1, ))
        test_probability_event = Event("Probability Event", "???", chance=0.02, label="probability_event", occurrence=0)
        
        ALL_EVENTS += [test_ranged_event, test_frequency_event, test_probability_event]
        
        # populate events
        for d in ALL_DAYS:
            for e in ALL_EVENTS:
                if e.start and e.finish:
                    for r in e.date_range(test_main_time):
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
        
        test_date_range = test_ranged_event.date_range(test_main_time)
        # should generate 61 days (2 months)
        record_test('Check correct number of date range', len(test_date_range), 61, event_tests_results)
        
        # fast forward to ranged event month and day
        test_main_time.month, test_main_time.day = 6, 15
        result = is_event_active_today(test_ranged_event, test_main_time)
        record_test('Check if ranged event active on date', result, True, event_tests_results)
        
        # fast forward to ranged event month and day
        test_main_time.month, test_main_time.day = 8, 16
        result = is_event_active_today(test_ranged_event, test_main_time)
        record_test('Check if ranged event is inactive out of range', result, False, event_tests_results)
        
        # check freqency event should happen every 1st
        test_main_time.month, test_main_time.day = 8, 1
        result = is_event_active_today(test_frequency_event, test_main_time)
        record_test('Check if frequency event happens every first of month', result, True, event_tests_results)
        
        # check freqency event should happen every 1st
        test_main_time.month, test_main_time.day = 9, 1
        result = is_event_active_today(test_frequency_event, test_main_time)
        record_test('Check if frequency event happens every first of month', result, True, event_tests_results)
        
        # check freqency event should happen every 2nd
        test_main_time.month, test_main_time.day = 8, 2
        result = is_event_active_today(test_frequency_event, test_main_time)
        record_test('Check if frequency event does not happen every second of month', result, False, event_tests_results)
        
        # how do I test probablity events?
        
    return
        
        