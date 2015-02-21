﻿# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# CHARACTER CREATION
#

screen allocatepoints(player):
    $ STATS = ['strength', 'speed', 'evasion', 'defence', 'stamina', 'melee', 'special', 'ranged']
    $ counter = 0
    text "Allocation Points: [player.allocation_points]" xpos 0.1
    text "Str: [player.strength] Def: [player.defence] Eva: [player.evasion]" xpos 0.50
    text "Sta: [player.stamina] Speed: [player.speed] Hit: [player.base_hit_rate]" xpos 0.50 ypos 0.05
    text "Melee: [player.melee] Special: [player.special] Ranged: [player.ranged]" xpos 0.50 ypos 0.1
    
    if player.allocation_points:
        for stat in STATS:
            textbutton "[stat] +1" hovered Show('explanation', stat=stat) unhovered Hide('explanation') action [SetField(player, stat, getattr(player, stat) + 1), 
                                                                                                                SetField(player, 'allocation_points', getattr(player, 'allocation_points') - 1), 
                                                                                                                SetField(current_session, 'main_player', player), 
                                                                                                                Jump('allocate_points')] xpos grid_place[counter][0] ypos grid_place[counter][1]
            $ counter +=1 
            
screen explanation(stat):
    if stat == 'strength':
        text "This is how much damage melee attacks do." ypos 0.25
    elif stat == 'speed':
        text "This is how much distance the player can cover per move." ypos 0.25
    elif stat == 'evasion':
        text "Chance of dodging the opponents attack." ypos 0.25
    elif stat == 'defence':
        text "Resistance against all types of attacks." ypos 0.25
    elif stat == 'stamina':
        text "Rate of recovering and endurance." ypos 0.25
    elif stat == 'melee':
        text "Proficiency in close combat." ypos 0.25
    elif stat == 'special':
        text "Proficiency in mana skills." ypos 0.25
    elif stat == 'ranged':
        text "Proficiency in ranged combat." ypos 0.25

##############################################################################
# VILLAGE SCREENS
#
screen villagearena(village, player):
    $ counter = 0
    textbutton "Level 5" action [SetField(current_session, 'village', village), 
                                 SetField(current_session, 'main_player', player),
                                 SetField(current_session, 'time_to_advance', {'hours': 8}),
                                 Hide("villagearena"),
                                 SetField(current_session, 'location', l_arena), 
                                 Jump('village_arena_level5')] xpos grid_place[0][0] ypos grid_place[0][1]
    
    textbutton "Level 10" action [SetField(current_session, 'village', village), 
                                  SetField(current_session, 'main_player', player),
                                  SetField(current_session, 'time_to_advance', {'hours': 8}),
                                  Hide("villagearena"),
                                  SetField(current_session, 'location', l_arena), 
                                  Jump('village_arena_level10')] xpos grid_place[1][0] ypos grid_place[1][1]
    
    textbutton "Back" action [SetField(current_session, 'village', village), 
                              SetField(current_session, 'main_player', player),
                              Hide("villagearena"),
                              Jump('village_redirect')] xpos grid_place[2][0] ypos grid_place[2][1]
            
screen hospitalshop(village, player):
    $ counter = 1
    #$ player.left_leg.injure()
    $ injury_bill = player.get_injury_bill()
    text "Ryo: [player.ryo]" xpos 0.1
    text "Items: [player.items]" xpos 0.1 ypos 0.2
    text "[player.head.injury_severity] [player.torso.injury_severity] [player.left_arm.injury_severity] [player.right_arm.injury_severity] [player.left_leg.injury_severity] [player.right_leg.injury_severity]"
    
    python:
        if is_event_active_today(e_hospital_discount) and not hospital_shop.price_halved:
            hospital_shop.half_prices()
        elif not is_event_active_today(e_hospital_discount) and hospital_shop.price_halved:
            hospital_shop.double_prices()
    
    if injury_bill[0]:
        textbutton "Heal all injuries [injury_bill[0]] [injury_bill[1]]" action [SetField(current_session, 'village', village), 
                                                                                 SetField(current_session, 'main_player', player),
                                                                                 SetField(current_session, 'time_to_advance', {'days': injury_bill[1]}),
                                                                                 SetField(current_session, 'rest', True),
                                                                                 Hide("hospitalshop"),
                                                                                 SetField(current_session, 'location', l_hospital), 
                                                                                 Jump('hospital_injury')] xpos grid_place[0][0] ypos grid_place[0][1]
    else:
        $ counter = 0
    
    for item in hospital_shop.items:
        textbutton "[item.name] ([item.price])" action [SetField(current_session, 'village', village), 
                                                        SetField(current_session, 'main_player', player),
                                                        SetField(current_session, 'location', l_hospital),
                                                        SetField(current_session, 'item', item),
                                                        SetField(current_session, 'time_to_advance', {'hours': 2}),
                                                        Jump("purchase_item_redirect")] xpos grid_place[counter][0] ypos grid_place[counter][1]
        $ counter += 1
                                         
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'main_player', player), 
                                                 Hide("hospitalshop"),
                                                 Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
    
screen weaponshop(village, player):
    $ counter = 0
    text "Ryo: [player.ryo]" xpos 0.1
    text "Weapons: [player.weapons]" xpos 0.1 ypos 0.2
    
    python:
        if is_event_active_today(e_weapon_discount) and not weapon_shop.price_halved:
            weapon_shop.half_prices()
        elif not is_event_active_today(e_weapon_discount) and weapon_shop.price_halved:
            weapon_shop.double_prices()
    
    for weapon in weapon_shop.items:
        textbutton "[weapon.name] ([weapon.price])" action [SetField(current_session, 'village', village), 
                                                            SetField(current_session, 'main_player', player),
                                                            SetField(current_session, 'location', l_ninja_tool_facility),
                                                            SetField(current_session, 'item', weapon),
                                                            SetField(current_session, 'time_to_advance', {'hours': 2}),
                                                            Jump("purchase_weapon_redirect")] xpos grid_place[counter][0] ypos grid_place[counter][1]
        $ counter += 1
                                         
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'main_player', player), 
                                                 Hide("weaponshop"),
                                                 Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
            
screen villagemissions(village, player):
    $ counter = 0
    $ village_time = 0
    $ mission_levels = [('D', 1), ('C', 20), ('B', 30), ('A', 40), ('S', 50)]
    #$ player.level = 40
    $ avaliable_missions = [mission[0] for mission in mission_levels if player.level >= mission[1]]
    
    for rank in avaliable_missions:
        textbutton "[rank]" action [SetField(current_session, 'village', village), 
                                    SetField(current_session, 'main_player', player), 
                                    SetField(current_session, 'mission_rank', rank),
                                    Hide("villagemissions"),
                                    Jump("missionselect_redirect")] xpos grid_place[counter][0] ypos grid_place[counter][1]
        $ counter += 1
        
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'main_player', player), 
                                                 Hide("villagemissions"),
                                                 Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
    
screen missionselect(village, player, rank):
    $ counter = 0
    $ missions = [mission for mission in ALL_MISSIONS if mission.rank == rank]
    
    for mission in missions:
        textbutton "[mission.name]" action [SetField(current_session, 'village', village), 
                                            SetField(current_session, 'main_player', player), 
                                            SetField(current_session, 'mission', mission),
                                            Hide("missionselect"),
                                            Jump("mission_redirect")] xpos grid_place[counter][0] ypos grid_place[counter][1]
        $ counter += 1
    
    textbutton "Back" action [SetField(current_session, 'village', village), 
                              SetField(current_session, 'main_player', player),
                              Hide("missionselect"),
                              SetField(current_session, 'location', l_villagemission), 
                              Jump('location_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
    

screen training(village, player):
    textbutton "Train skills" action [Hide("training"), Show("train_skills", village=village, player=player)] xpos grid_place[0][0] ypos grid_place[0][1]
    if player.team:
        # maybe add formation, TODO
        text "Team Chemistry: [player.team.chemistry]" xpos 0.4 ypos 0.1
        textbutton "Train with team" action [SetField(current_session, 'village', village), 
                                             SetField(current_session, 'main_player', player), 
                                             Hide("training"), 
                                             Show("train_with_team", village=village, player=player)] xpos grid_place[2][0] ypos grid_place[2][1]
    if player.sensei:
        textbutton "Learn skills" action [SetField(current_session, 'village', village), 
                                          SetField(current_session, 'main_player', player), 
                                          SetField(current_session, 'location', l_training_ground),
                                          Hide("training"), 
                                          Jump("training_sensei")] xpos grid_place[3][0] ypos grid_place[3][1]
                                      
    textbutton "Train (+ exp)" action [SetField(current_session, 'time_to_advance', {'hours': 4}),
                                       SetField(current_session, 'village', village), 
                                       SetField(current_session, 'main_player', player), 
                                       SetField(current_session, 'location', l_training_ground),
                                       Hide("training"), 
                                       Jump('train_gain_exp')] xpos grid_place[1][0] ypos grid_place[1][1]
    
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'main_player', player), 
                                                 Hide('training'), 
                                                 Jump('village_redirect')] xpos grid_place[4][0] ypos grid_place[4][1]
    
screen train_with_team(village, player):
    $ team_length = len(player.team.members)
    # TODO: maybe add player + team member vs others (drag and drop?)
    if team_length > 0:
        textbutton "Spar with [player.team.members[0].name]" action [SetField(current_session, 'time_to_advance', {'hours': 4}),
                                                                     SetField(current_session, 'village', village), 
                                                                     SetField(current_session, 'main_player', player), 
                                                                     SetField(current_session, 'spar', [player.team.members[0]]),
                                                                     Hide("train_with_team"), 
                                                                     Jump("training_spar")] xpos grid_place[0][0] ypos grid_place[0][1]
    if team_length > 1:
        textbutton "Spar with [player.team.members[0].name] and [player.team.members[1].name] (1 on 2)" action [SetField(current_session, 'time_to_advance', {'hours': 4}),
                                                                     SetField(current_session, 'village', village), 
                                                                     SetField(current_session, 'main_player', player), 
                                                                     SetField(current_session, 'spar', player.team.members),
                                                                     Hide("train_with_team"), 
                                                                     Jump("training_spar")] xpos grid_place[1][0] ypos grid_place[1][1]  
    if player.sensei:
        textbutton "Spar with [player.sensei.name]" action [SetField(current_session, 'time_to_advance', {'hours': 4}),
                                                                     SetField(current_session, 'village', village), 
                                                                     SetField(current_session, 'main_player', player), 
                                                                     SetField(current_session, 'spar', [player.sensei]),
                                                                     Hide("train_with_team"), 
                                                                     Jump("training_spar")] xpos grid_place[2][0] ypos grid_place[2][1]
        
    textbutton "Back" action [SetField(current_session, 'village', village), 
                              SetField(current_session, 'main_player', player),
                              Hide("train_with_team"),
                              SetField(current_session, 'location', l_training_ground), 
                              Jump('location_redirect')] xpos grid_place[3][0] ypos grid_place[3][1]
    
    
screen train_skills(village, player):
    $ counter = 0
    #text "[player.all_skills[0]]" xpos 0.5 ypos 0.5
    for skill in player.all_skills:
        if skill.exp < skill.unlock_exp:
            textbutton "[skill.name] [skill.exp]/[skill.unlock_exp]" action [SetField(current_session, 'village', village), 
                                                                             SetField(current_session, 'main_player', player), 
                                                                             SetField(current_session, 'skill', skill),
                                                                             SetField(current_session, 'time_to_advance', {'hours': 4}),
                                                                             Hide("train_skills"),
                                                                             Jump("train_skill_label")] xpos grid_place[counter][0] ypos grid_place[counter][1]
            $ counter += 1
            
    textbutton "Back" action [SetField(current_session, 'village', village), 
                              SetField(current_session, 'main_player', player),
                              Hide("train_skills"),
                              SetField(current_session, 'location', l_training_ground), 
                              Jump('location_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]

screen levelup(village, player):
    $ STATS = ['strength', 'speed', 'evasion', 'defence', 'stamina', 'taijutsu', 'ninjutsu', 'genjutsu']
    $ counter = 0
    #text "Allocation Points: [player.allocation_points]" xpos 0.1
    #text "Str: [player.strength] Def: [player.defence] Eva: [player.evasion]" xpos 0.50
    #text "Sta: [player.stamina] Speed: [player.speed] Hit: [player.base_hit_rate]" xpos 0.50 ypos 0.05
    #text "Tai: [player.taijutsu] Nin: [player.ninjutsu] Gen: [player.genjutsu]" xpos 0.50 ypos 0.1
    
    if player.allocation_points:
        for stat in STATS:
            textbutton "[stat] +1" action [SetField(player, stat, getattr(player, stat) + 1), 
                                           SetField(player, 'allocation_points', getattr(player, 'allocation_points') - 1), 
                                           SetField(current_session, 'village', village), 
                                           SetField(current_session, 'main_player', player), 
                                           SetField(current_session, 'location', l_level_up), 
                                           Jump('location_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
            $ counter +=1 
    else:
        text "No allocation points" xpos 0.5 ypos 0.5
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'main_player', player), 
                                                 Hide('levelup'), 
                                                 Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]

screen villagetravel(village, player):
    $ counter = 0
    $ village_time = 0
    
    for v in other_villages(village):
        $ village_time = time_between_village(v, village)
        textbutton "[v.name] [village_time]" action [SetField(current_session, 'village', v), 
                                                     SetField(current_session, 'main_player', player), 
                                                     SetField(current_session, 'time_to_advance', {'days': village_time}),
                                                     Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
        $ counter += 1
        
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'main_player', player), 
                                                 Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]

screen villagehome(village, player):
    $ counter = 0
    
    textbutton "Show Calendar" action [SetField(current_session, 'village', village), 
                                       SetField(current_session, 'main_player', player), 
                                       Hide('villagehome'),
                                       Show('calendar_screen', player=player, village=village, current_month=get_current_month())] xpos grid_place[0][0] ypos grid_place[0][1]
    
    textbutton "Rest" action [SetField(current_session, 'village', village), 
                              SetField(current_session, 'main_player', player), 
                              Hide('villagehome'),
                              Show('rest_screen', player=player, village=village)] xpos grid_place[1][0] ypos grid_place[1][1]
        
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'main_player', player), 
                                                 Hide('villagehome'),
                                                 Jump('village_redirect')] xpos grid_place[2][0] ypos grid_place[2][1]
    
screen rest_screen(village, player):
    
    textbutton "1 Hour" action [SetField(current_session, 'village', village), 
                                SetField(current_session, 'main_player', player),
                                SetField(current_session, 'time_to_advance', {'hours': 1}),
                                SetField(current_session, 'rest', True),
                                Hide("rest_screen"),
                                SetField(current_session, 'location', l_home), 
                                Jump('location_redirect')] xpos grid_place[0][0] ypos grid_place[0][1]
    
    textbutton "2 Hours" action [SetField(current_session, 'village', village), 
                                 SetField(current_session, 'main_player', player),
                                 SetField(current_session, 'time_to_advance', {'hours': 2}),
                                 SetField(current_session, 'rest', True),
                                 Hide("rest_screen"),
                                 SetField(current_session, 'location', l_home), 
                                 Jump('location_redirect')] xpos grid_place[1][0] ypos grid_place[1][1]
    
    textbutton "12 Hours" action [SetField(current_session, 'village', village), 
                                  SetField(current_session, 'main_player', player),
                                  SetField(current_session, 'time_to_advance', {'hours': 12}),
                                  SetField(current_session, 'rest', True),
                                  Hide("rest_screen"),
                                  SetField(current_session, 'location', l_home), 
                                  Jump('location_redirect')] xpos grid_place[2][0] ypos grid_place[2][1]
    
    textbutton "1 Day" action [SetField(current_session, 'village', village), 
                               SetField(current_session, 'main_player', player),
                               SetField(current_session, 'time_to_advance', {'days': 1}),
                               SetField(current_session, 'rest', True),
                               Hide("rest_screen"),
                               SetField(current_session, 'location', l_home), 
                               Jump('location_redirect')] xpos grid_place[3][0] ypos grid_place[3][1]
    
    textbutton "1 Week" action [SetField(current_session, 'village', village), 
                                SetField(current_session, 'main_player', player),
                                SetField(current_session, 'time_to_advance', {'days': 7}),
                                SetField(current_session, 'rest', True),
                                Hide("rest_screen"),
                                SetField(current_session, 'location', l_home), 
                                Jump('location_redirect')] xpos grid_place[4][0] ypos grid_place[4][1]
    
    textbutton "1 Month" action [SetField(current_session, 'village', village), 
                                 SetField(current_session, 'main_player', player),
                                 SetField(current_session, 'time_to_advance', {'months': 1}),
                                 SetField(current_session, 'rest', True),
                                 Hide("rest_screen"),
                                 SetField(current_session, 'location', l_home), 
                                 Jump('location_redirect')] xpos grid_place[5][0] ypos grid_place[5][1]
    
    textbutton "Back" action [SetField(current_session, 'village', village), 
                              SetField(current_session, 'main_player', player),
                              Hide("rest_screen"),
                              SetField(current_session, 'location', l_home), 
                              Jump('location_redirect')] xpos grid_place[6][0] ypos grid_place[6][1]

screen villagemap(village, player):
    # show player time details here
    $ counter = 0
    $ npc_counter = 0
    $ x_adj = 0.05
    $ npc_x_adj = 0.2
    
    #text "[village.locations[0].unlocked]" xpos 0.1
    
    #imagebutton idle "black_fade_small" hover "black_fade_small"
    
    for today_e in get_today().events:
        if today_e.npc and not today_e.stop:
            textbutton today_e.npc.name action [SetField(current_session, 'main_player', player), 
                                                SetField(current_session, 'village', village), 
                                                SetField(current_session, 'time_to_advance', {'hours': 4}),
                                                Hide("villagemap"), 
                                                Jump(today_e.label.format(today_e.count))] xpos (grid_place[npc_counter][0]-npc_x_adj) ypos grid_place[npc_counter][1]
            $ npc_counter += 1
    
    for location in village.locations:
        if player.home_village:
            if not player.home_village == village:
                if location.name == 'Home':
                    $ location.name = 'Hotel'
        else:
            if location.name == 'Home':
                $ location.name = 'Hotel'
                
        if location.unlocked:
            textbutton [location.name] hovered Show('location_explanation', stat=location.label) unhovered Hide('location_explanation') action [SetField(current_session, 'main_player', player), 
                                                                                                                                    SetField(current_session, 'village', village), 
                                                                                                                                    SetField(current_session, 'location', location), 
                                                                                                                                    Hide("villagemap"), 
                                                                                                                                    Jump('location_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
        
        
        if location.events:
            for e in location.events:
                for today_e in get_today().events:
                    if e.small_name == today_e.small_name and counter < 5:
                        text "[e.small_name]" xpos (grid_place[counter][0]-x_adj) ypos grid_place[counter][1]
                    elif e.small_name == today_e.small_name and counter >= 5:
                        text "[e.small_name]" xpos (grid_place[counter][0]-x_adj) ypos grid_place[counter][1]
            
        $ counter += 1 
                
screen location_explanation(stat):
    $ expl_dict = {'location_hospital': 'Heal injuries and buy healing items.', 
                   'location_police_station': 'Buy weapons for combat.', 
                   'location_levelup': 'Spend points to increase stats like strength, speed, evasion etc.',
                   'location_training': 'Train with team members, learn new skills, unlock new skills.', 
                   'location_missions': 'Perform missions.', 
                   'location_apartment': 'Rest to heal injuries, skip time or view calendar for upcoming events.'}
    $ expl = expl_dict[stat]
    
    text "[expl]" ypos 0.8 xpos 0.2
        
screen time_screen:
    #text "[current_session.initial_pos]" xpos 0.1
    text "{color=#000}[main_time.current_time]{/color}" xpos 0.1 ypos 0.1
        
screen stats_screen(player):
    
    #python:
     #   screen_on = screen_on
    
    if screen_on:
        imagebutton idle "stats_idle" hover "stats_idle" xpos 0.38 ypos 0.0
        imagebutton idle "body" hover "body" xpos 0.62 ypos 0.00
    
        if player.head.injury:
            imagebutton idle "head_injured" hover "head_injured" xpos 0.655 ypos 0.01
        
        if player.torso.injury:
            imagebutton idle "torso_injured" hover "torso_injured" xpos 0.662 ypos 0.055
        
        if player.left_arm.injury:
            imagebutton idle "left_arm_injured" hover "left_arm_injured" xpos 0.634 ypos 0.05
        
        if player.right_arm.injury:
            imagebutton idle "right_arm_injured" hover "right_arm_injured" xpos 0.701 ypos 0.05
        
        if player.left_leg.injury:
            imagebutton idle "left_leg_injured" hover "left_leg_injured" xpos 0.645 ypos 0.145
        
        if player.right_leg.injury:
            imagebutton idle "right_leg_injured" hover "right_leg_injured" xpos 0.685 ypos 0.145
    
        text "{size=-5}Ryo: [player.ryo]{/size}" xpos 0.73 ypos 0.023
        text "{size=-5}HP: [player.hp]/[player.maxhp]{/size}" xpos 0.85 ypos 0.024
        text "{size=-5}[player.name]{/size}" xpos 0.73 ypos 0.05
        text "{size=-5}Lv.[player.level]{/size}" xpos 0.83 ypos 0.05
        # TODO: this needs to be bar
        $ next_level_exp = LEVELS[player.level + 1]
        text "{size=-5}Exp [player.exp]/[next_level_exp]{/size}" xpos 0.73 ypos 0.08
        text "{size=-5}CP: [player.chakra]/[player.maxchakra]{/size}" xpos 0.85 ypos 0.08
        text "{size=-5}Str: [player.strength]{/size}" xpos 0.735 ypos 0.12
        text "{size=-5}Def: [player.defence]{/size}" xpos 0.735 ypos 0.16
        text "{size=-5}Eva: [player.evasion]{/size}" xpos 0.735 ypos 0.20
        text "{size=-5}Sta: [player.stamina]{/size}" xpos 0.83 ypos 0.12
        text "{size=-5}Spd: [player.speed]{/size}" xpos 0.83 ypos 0.16
        text "{size=-5}Hit: [player.base_hit_rate]{size=-5}" xpos 0.83 ypos 0.20
        text "{size=-5}Tai: [player.taijutsu]{/size}" xpos 0.915 ypos 0.12
        text "{size=-5}Nin: [player.ninjutsu]{/size}" xpos 0.915 ypos 0.16
        text "{size=-5}Gen: [player.genjutsu]{/size}" xpos 0.915 ypos 0.20
    
        textbutton "Hide Stats" action [Hide("stats_screen"), Jump("toggle_screen_off")] xpos 0.4 ypos 0.0
    
screen player_stats:
    if not screen_on:
        textbutton "Show Stats" action [Show("stats_screen", player=current_session.main_player), Jump("toggle_screen_on")] xpos 0.4 ypos 0.0
        
screen calendar_screen_toggle:
    if not calendar_on:
        textbutton "Show Calendar" action Jump("toggle_calendar_on") xpos 0.2 ypos 0.0
        
screen calendar_screen(village, player, current_month):
    #$ current_month.days = [current_month.days[0]]
    $ stuff = [(d.day, d.month) for d in e_chunin_exams.date_range()]
    #$ stuff = DAY_RANGES
    
    #text "[stuff]" ypos 0.4
    #if calendar_on:
    imagebutton idle "black_fade" hover "black_fade" # "gfx/black.png" hover "gfx/black.png"
    
    textbutton "Last month" action [Hide('calendar_screen'), 
                                    Show('calendar_screen', village=village, player=player, current_month=get_month(current_month.number - 1))] xpos 0.15 ypos 0.1
    text "[current_month]" xpos 0.43 ypos 0.11
    textbutton "Next month" action [Hide('calendar_screen'), 
                                    Show('calendar_screen', village=village, player=player, current_month=get_month(current_month.number + 1))] xpos 0.65 ypos 0.1
    
    grid 6 5 spacing -200 ypos 0.2 xpos 0.15 xfill True yfill True: #6, 5 # area (0.1, 0.1, 240, 200):
        for day in current_month.days:
            $ how_many = day.parse_events()
            #if day.events:
            if main_time.day == day.number and current_month.number == main_time.month:
                text "[day.number]\n([how_many])" color "#F00"
            else:
                text "[day.number]\n([how_many])" 
            #else:
            #    text "[day.number]"
                    
    textbutton "Hide Calendar" action [Hide('calendar_screen'), Show("villagehome", player=player, village=village)] xpos 0.2 ypos 0.0

label toggle_screen_on:
    $ screen_on = True
    python:
        if current_session.location:
            renpy.jump("location_redirect")
        #elif current_session.location
        else:
            renpy.jump("village_redirect")
    
label toggle_screen_off:
    $ screen_on = False
    python:
        if current_session.location:
            renpy.jump("location_redirect")
        else:
            renpy.jump("village_redirect")
            
label toggle_calendar_on:
    $ calendar_on = True
    hide screen villagemap
    python:
        renpy.jump("village_redirect")
    
label toggle_calendar_off:
    $ calendar_on = False
    python:
        renpy.jump("village_redirect")


##############################################################################
# WORLD EVENTS
#
screen worldevents(village):
    text "Wealth: [village.wealth]" xpos 0.3 ypos 0.03
    text "Control:" xpos 0.3 ypos 0.08
    text "Influence:" xpos 0.3 ypos 0.13
    text "Uprising:" xpos 0.3 ypos 0.18
    bar value village.control range 100 xpos 0.45 ypos 0.08 xmaximum 100 ymaximum 30
    bar value village.influence range 100 xpos 0.45 ypos 0.13 xmaximum 100 ymaximum 30
    bar value village.uprising range 100 xpos 0.45 ypos 0.18 xmaximum 100 ymaximum 30
        

##############################################################################
# BATTLE SCREENS
#
screen battle_selection_screen(battles):
    #text "[battle1.good_team]" xpos battle1.xpos ypos battle1.ypos
    #text "[battle2.good_team]" xpos battle2.xpos ypos battle2.ypos
    for battle in battles:
        text "[battle.good_team]" xpos battle.xpos ypos battle.ypos
    

screen battle_prep_screen(follow_on):

    # A map as background.
    #add "europe.jpg"
    $ start = 50
    $ counter = 1
    $ battle_c = 1
    $ team = current_session.team.members
    $ battles = current_session.battles
    
    for battle in battles:
        text "[battle.good_team]" xpos battle.xpos ypos battle.ypos
    
    textbutton "Reset" action [Hide('battle_prep_screen'), 
                               Jump('reset_battle', follow_on=follow_on)] xpos 0.8
    textbutton "Done" action [Hide('battle_prep_screen'), Jump(follow_on)] xpos 0.7

    draggroup:
        #if len(team) > 0:
        #    drag:
        #        drag_name team[0].name
        #        child team[0].tilepic
        #        droppable False
        #        #dropped player_dragged
        #        dragged player_dragged
        #        xpos 50 ypos 300
                
        #if len(team) > 1:
        #    drag:
        #        drag_name team[1].name
        #        child team[1].tilepic
        #        droppable False
        #        #dropped player_dragged
        #        dragged player_dragged
        #        xpos 100 ypos 300
                
        #if len(team) > 2:
        #    drag:
        #        drag_name team[2].name
        #        child team[2].tilepic
        #        droppable False
        #        #dropped player_dragged
        #        dragged player_dragged
        #        xpos 150 ypos 300

        for p in current_session.team.members:
            drag:
                drag_name p.name
                child p.tilepic
                droppable False
                dragged player_dragged
                xpos (50*counter) ypos 300
                
            $ counter += 1
        
        #if len(battles) > 0:
             
        #drag:
        #    drag_name battle.id
        #    child "marker.png"
        #    draggable False
        #    xpos battle.xpos ypos battle.ypos
            
            
        #if len(battles) > 1:
            #text "[battles[1].id]" xpos 0.8
        #    drag:
        #        drag_name battles[1].id
        #        child "marker.png"
        #        draggable False
        #        xpos 200 ypos 200
                
        for battle in current_session.battles:
            drag:
                drag_name battle.id
                child "marker.png"
                draggable False
                xpos (100*battle_c) ypos 200
                
            $ battle_c += 1



screen skill_actions(action_type):
    $ initial_pos = 0.8
    $ interval = 0.1
    $ counter = 0
    
    vbox:
        for skill in getattr(player, action_type):
            
            if skill.is_usable(player, enemy):
                textbutton "[skill.name]" action [SetField(current_session, 'skill', skill), 
                                                  SetField(current_session, 'skill_type', 'attack'),
                                                  Jump('skill_redirect')]  xpos 0.6
            else:
                $ reason = skill.unusable_reason(player, enemy)
                # show another type of imagebutton here
                textbutton "[skill.name]" hovered Show('move_explanation', reason=reason) unhovered Hide('move_explanation') xpos 0.6 action [[]]

screen battlemenu(player, tag_p):
    $ move_types = ["melee", "special", "ranged", "weapons", "defensive"]
    vbox:
        # TODO: Add items menu
        for move_type in move_types:
            $ capital = move_type.capitalize()
            if move_type == "weapons":
                $ player_atr = "weapons"
            else:
                $ player_atr = move_type + "skills"
                
            #text "[player_atr]" xpos 0.5
                
            if getattr(player, player_atr):
                textbutton "[capital]" hovered Show('battle_explanation', stat=move_type) unhovered Hide('battle_explanation') action [Hide("skill_actions"), Show("skill_actions", action_type=player_atr)]
            else:
                textbutton "[capital]"
       
        if not moved:
            textbutton "Move" hovered Show('battle_explanation', stat='move') unhovered Hide('battle_explanation') action [Hide("skill_actions"), Show("movemenu")]
        textbutton "Standby" hovered Show('battle_explanation', stat='standby') unhovered Hide('battle_explanation') action Jump("standby")
        
        # TODO: move trap to weapons
        #textbutton "Trap" action [Hide("specialactions"), Hide("rangedactions"), Hide("meleeactions"), Hide("weaponselection"), Hide("defenceactions"), Show("settrap")]
        for partner in tag_p:
            textbutton "Tag [partner.name]" action [SetField(partner, 'main', True), SetField(partner, 'tile', player.tile), SetField(player, 'main', False), Jump('tag_partner')] ypos 3.5
        
screen move_explanation(reason):
    text "[reason]" ypos 0.8 xpos 0.2
        
screen battle_explanation(stat):
    $ expl_dict = {'melee': 'Close ranged attacks.', 
                   'special': 'Attacks that use magic.', 
                   'ranged': 'Attacks from distance.',
                   'move': 'Move across the battle area.', 
                   'weapons': 'Fixed damage attacks limited by quantity.', 
                   'defence': 'Reduce enemy damage for a limited amount of time.',
                   'standby': 'Regain magic, slightly heal health.'}
    $ expl = expl_dict[stat]
    
    text "[expl]" ypos 0.8 xpos 0.2
        
screen stats:
    text "Str: [player.strength] Def: [player.defence] Eva: [player.evasion]" xpos 0.30
    text "Sta: [player.stamina] Hit: [player.base_hit_rate]" xpos 0.30 ypos 0.05
    text "Str: [enemy.strength] Def: [enemy.defence] Eva: [enemy.evasion]" xpos 0.65
    text "Sta: [enemy.stamina] Hit: [enemy.base_hit_rate]" xpos 0.65 ypos 0.05
        
screen battlebars(tag_p, tag_e):
    #frame:
        #has vbox 
    $ rel_pos = abs(player.tile.position - enemy.tile.position)
    
    text "[battle_turn] [current_session.fight_limit]" xpos 0.7 ypos 0.05
    text "[player.facing]" xpos 0.7 ypos 0.1

    text "[player.name]" xpos 0.5 ypos 0.15
    text "[player.chakra]" xpos 0.49 ypos 0.45
    text "[player.hp]" xpos 0.55 ypos 0.45
    vbar value player.chakra range player.maxchakra xpos 0.5 ypos 0.2 ymaximum 150 #ymaximum 30 left_bar "blue_bar"
    vbar value player.hp range player.maxhp xpos 0.55 ypos 0.2 ymaximum 150
    if enemy.damage_dealt > 0:
        text "-[enemy.damage_dealt]" xpos 0.59 ypos 0.3
    
    #text "[player.facing]" xpos 0.2 ypos 0.25
    if player.check_active_skill(damage_reduction):
        text "DR" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(chakra_defence):
        text "CD" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(reflect):
        text "Ref" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(dampen):
        text "Dam" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(yata_mirror):
        text "Yata" xpos 0.3 ypos 0.15
    
    text "[enemy.name]" xpos 0.65 ypos 0.15
    text "[enemy.chakra]" xpos 0.64 ypos 0.45
    text "[enemy.hp]" xpos 0.70 ypos 0.45
    vbar value enemy.hp range enemy.maxhp xpos 0.7 ypos 0.2 ymaximum 150
    vbar value enemy.chakra range enemy.maxchakra xpos 0.66 ypos 0.2 ymaximum 150
    if player.damage_dealt > 0:
        text "-[player.damage_dealt]" xpos 0.75 ypos 0.3
        
    if enemy.check_active_skill(damage_reduction):
        text "DR" xpos 0.75 ypos 0.15
        
    if enemy.check_active_skill(chakra_defence):
        text "CD" xpos 0.75 ypos 0.15
        
    #text "[tag_e]" xpos 0.45 ypos 0.10
        
    # show tag partners health here
    for position, partner in enumerate(tag_p):
        if position == 0:
            text "[partner.name]" xpos 0.25 ypos 0.75
            vbar value partner.hp range partner.maxhp xpos 0.28 ypos 0.8 ymaximum 100 xmaximum 20
            vbar value partner.chakra range partner.maxchakra xpos 0.25 ypos 0.8 ymaximum 100 xmaximum 20
        else:
            text "[partner.name]" xpos 0.35 ypos 0.75
            vbar value partner.hp range partner.maxhp xpos 0.38 ypos 0.8 ymaximum 100 xmaximum 20
            vbar value partner.chakra range partner.maxchakra xpos 0.35 ypos 0.8 ymaximum 100 xmaximum 20
        
    # show tag partners health here
    for position, partner in enumerate(tag_e):
        if position == 0:
            text "[partner.name]" xpos 0.65 ypos 0.75
            vbar value partner.hp range partner.maxhp xpos 0.68 ypos 0.8 ymaximum 100 xmaximum 20
            vbar value partner.chakra range partner.maxchakra xpos 0.65 ypos 0.8 ymaximum 100 xmaximum 20
        else:
            text "[partner.name]" xpos 0.75 ypos 0.75
            vbar value partner.hp range partner.maxhp xpos 0.78 ypos 0.8 ymaximum 100 xmaximum 20
            vbar value partner.chakra range partner.maxchakra xpos 0.75 ypos 0.8 ymaximum 100 xmaximum 20

label movemenu:
    call hidetiles
    show screen movemenu
    
screen movemenu:
    
    $ highlight_position(player, enemy, clearing)
    
    for tile in TILES:
        if tile.potential:
            imagebutton idle tile.idle hover tile.hover xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05) action Jump("move{}".format(tile.position))
        elif tile.trap:
            imagebutton idle TILETRAPPIC hover TILETRAPPIC xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05)
        else:
            imagebutton idle tile.idle hover tile.idle xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05)
        #text "{}".format(tile.idle.split('.')[0]) xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos + 0.15)
        if player.tile == tile:
            text "P" xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos + 0.25)
            
        if enemy.tile == tile:
            text "E" xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos + 0.25)
    
label settrap:
    call hidetiles
    hide screen movemenu
    show screen settrap
    player.character "Where should I place the trap?"
    
screen settrap:
    $ highlight_position(player, enemy, clearing)
    
    for tile in TILES:
        if tile.potential:
            imagebutton idle tile.idle hover TILETRAPPIC xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05) action Jump("trap{}".format(tile.position))
        else:
            imagebutton idle tile.idle hover tile.idle xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05)
        #imagebutton idle tile.idle hover TILETRAPPIC xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05) action Jump("trap{}".format(tile.position))

label move_continue:
    $ moved = True
    call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label, fight_limit)
    
label move1:
    $ show_player_at_pos(player, enemy, clearing, tile1)
    jump move_continue
    
label move2:
    $ show_player_at_pos(player, enemy, clearing, tile2)
    jump move_continue
    
label move3:
    $ show_player_at_pos(player, enemy, clearing, tile3)
    jump move_continue
    
label move4:
    $ show_player_at_pos(player, enemy, clearing, tile4)
    jump move_continue

label move5:
    $ show_player_at_pos(player, enemy, clearing, tile5)
    jump move_continue

label move6:
    $ show_player_at_pos(player, enemy, clearing, tile6)
    jump move_continue
    
label move7:
    $ show_player_at_pos(player, enemy, clearing, tile7)
    jump move_continue
    
label move8:
    $ show_player_at_pos(player, enemy, clearing, tile8)
    jump move_continue
    
label move9:
    $ show_player_at_pos(player, enemy, clearing, tile9)
    jump move_continue
    
label move10:
    $ show_player_at_pos(player, enemy, clearing, tile10)
    jump move_continue
    
label move11:
    $ show_player_at_pos(player, enemy, clearing, tile11)
    jump move_continue
    
label move12:
    $ show_player_at_pos(player, enemy, clearing, tile12)
    jump move_continue
    
label trap1:
    $ set_trap_at_pos(player, enemy, clearing, tile1)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap2:
    $ set_trap_at_pos(player, enemy, clearing, tile2)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap3:
    $ set_trap_at_pos(player, enemy, clearing, tile3)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap4:
    $ set_trap_at_pos(player, enemy, clearing, tile4)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap5:
    $ set_trap_at_pos(player, enemy, clearing, tile5)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap6:
    $ set_trap_at_pos(player, enemy, clearing, tile6)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap7:
    $ set_trap_at_pos(player, enemy, clearing, tile7)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap8:
    $ set_trap_at_pos(player, enemy, clearing, tile8)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap9:
    $ set_trap_at_pos(player, enemy, clearing, tile9)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap10:
    $ set_trap_at_pos(player, enemy, clearing, tile10)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap11:
    $ set_trap_at_pos(player, enemy, clearing, tile11)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)
    
label trap12:
    $ set_trap_at_pos(player, enemy, clearing, tile12)
    jump enemymove
    #call fight(player, enemy, tag_p, tag_e, clearing, win_label, lose_label, draw_label)

screen send_detective_screen:

    # A map as background.
    add "bg.jpg"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "Ivy"
            child "enemy.png"
            droppable False
            dragged detective_dragged
            xpos 100 ypos 100
        drag:
            drag_name "Zack"
            child "itachi.png"
            droppable False
            dragged detective_dragged
            xpos 150 ypos 100

        # The cities they can go to.
        drag:
            drag_name "London"
            child "button_hover.png"
            draggable False
            xpos 450 ypos 140
        drag:
            drag_name "Paris"
            draggable False
            child "button_idle.png"
            xpos 500 ypos 280



##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 3
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign 1.0

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
screen button: 
    if variable:    
        vbox xalign 0.1 yalign 0.1:
            textbutton "Show affection points" action ui.callsinnewcontext("aff_screen_label")
            # you can also use an image button:
            #imagebutton:
            #    idle "button_idle.png"
            #    hover "button_hover.png"
            #    action ui.callsinnewcontext("aff_screen_label")
                
screen aff_screen:
    frame:
        has vbox
        text "Bob: [bob_points] points"
        text "Larry: [larry_points] points"
        textbutton "Return" action Return()

label aff_screen_label:
    call screen aff_screen
    return
    
screen hello_world:
     tag example
     zorder 1
     modal False

     text "Hello, World."



    
    
