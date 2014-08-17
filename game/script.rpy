# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define naruto_c = Character('Naruto',color="#FFFF00") 
define sasuke_c = Character('Sasuke', color="#3399FF")
define sakura_c = Character('Sakura', color="#FA58F4")
define kakashi_c = Character('Kakashi', color="#3399FF")
image bg = im.Scale("bg.jpg", 800, 600)
image world_marker = im.Scale("marker.png", 33, 35)
image leader_pic = im.Scale("leader_pic.png", 100, 150)
define world_events = Character('World Events', color='#3399FF', window_left_padding=150, show_side_image=Image("leader_pic.png", xpos=0.03, yalign=0.96))
image tile1im = im.Scale("tile.png", 50, 30)
image tile2im = im.Scale("tile.png", 50, 30)
image tile3im = im.Scale("tile.png", 50, 30)
image tile4im = im.Scale("tile.png", 50, 30)
image tile5im = im.Scale("tile.png", 50, 30)
image tile6im = im.Scale("tile.png", 50, 30)
image tile7im = im.Scale("tile.png", 50, 30)
image tile8im = im.Scale("tile.png", 50, 30)
image tile9im = im.Scale("tile.png", 50, 30)
image tile10im = im.Scale("tile.png", 50, 30)
image tile11im = im.Scale("tile.png", 50, 30)
image tile12im = im.Scale("tile.png", 50, 30)
image map = im.Scale("map.png", 800, 600)
image konoha_map = im.Scale("konoha.png", 800, 600)
image stones_map = im.Scale("ishigakure.png", 800, 600)
image mist_map = im.Scale("kirivillage.png", 800, 600)
image clouds_map = im.Scale("kumogakure.png", 800, 600)
image sand_map = im.Scale("sunagakure.jpg", 800, 600)
image training_ground = im.Scale("training.jpg", 800, 600)
image training_ground evening = im.Scale(im.Recolor("training.jpg", 255, 165, 0, 255), 800, 600)

python:
    import os
    for fname in os.listdir(config.gamedir + '/gfx'):
        if fname.endswith(('.jpg', '.png')):
            tag = fname[:-4]
            fname =  'gfx/' + fname
            im.Scale(renpy.image(tag, fname), 800, 600)


init:
    $ bob_points = 0 # this is a variable for bob's affection points throughout your game
    $ larry_points = 0 # this is a variable for larry's affection points throughout your game 
    $ bob_max = 10 # this variable should be set to bob's maximum affection points
    $ larry_max = 10 # this variable should be set to larry's maximum affection points
    $ variable = False # when false, the affection screen button doesn't appear on the screen
    
    $ current_skill = None
    
    image playerpic_r = im.Scale("player.png", 40, 50)
    image enemypic_r = im.Scale("enemy.png", 40, 50)
    image playerpic_l = im.Flip(im.Scale("player.png", 40, 50), horizontal=True)
    image enemypic_l = im.Flip(im.Scale("enemy.png", 40, 50), horizontal=True)
    
    $ player1currentpos = 1
    $ enemy1currentpos = 12

init python:
    
    battle_menu_dict = {"Tai": "taiactions",
                        "Nin": "ninactions",
                        "Gen": "genactions",
                        "Move": "move_player",
                        "Items": "player_items",
                        "Team": "team_moves"}
    
    TILE1POS = 100
    TILE2POS = 150
    TILE3POS = 200
    TILE4POS = 250
    TILE5POS = 300
    TILE6POS = 350
    TILE7POS = 400
    TILE8POS = 450
    TILE9POS = 500
    TILE10POS = 550
    TILE11POS = 600
    TILE12POS = 650
    
    TILEYPOS = 0.7
    PLAYERYPOS = 0.65
    
    TILEIDLEPIC = "tile.png"
    TILEHOVERPIC = "tileh.png"
    TILETRAPPIC = "tiletrap.png"
    
    # Positions
    tile1pos = Position(xpos=TILE1POS+25, ypos=TILEYPOS)
    tile2pos = Position(xpos=TILE2POS+25, ypos=TILEYPOS)
    tile3pos = Position(xpos=TILE3POS+25, ypos=TILEYPOS)
    tile4pos = Position(xpos=TILE4POS+25, ypos=TILEYPOS)
    tile5pos = Position(xpos=TILE5POS+25, ypos=TILEYPOS)
    tile6pos = Position(xpos=TILE6POS+25, ypos=TILEYPOS)
    tile7pos = Position(xpos=TILE7POS+25, ypos=TILEYPOS)
    tile8pos = Position(xpos=TILE8POS+25, ypos=TILEYPOS)
    tile9pos = Position(xpos=TILE9POS+25, ypos=TILEYPOS)
    tile10pos = Position(xpos=TILE10POS+25, ypos=TILEYPOS)
    tile11pos = Position(xpos=TILE11POS+25, ypos=TILEYPOS)
    tile12pos = Position(xpos=TILE12POS+25, ypos=TILEYPOS)
    
    tile1pos.xpos, tile1pos.ypos = TILE1POS+25, TILEYPOS
    tile2pos.xpos, tile2pos.ypos = TILE2POS+25, TILEYPOS
    tile3pos.xpos, tile3pos.ypos = TILE3POS+25, TILEYPOS
    tile4pos.xpos, tile4pos.ypos = TILE4POS+25, TILEYPOS
    tile5pos.xpos, tile5pos.ypos = TILE5POS+25, TILEYPOS
    tile6pos.xpos, tile6pos.ypos = TILE6POS+25, TILEYPOS
    tile7pos.xpos, tile7pos.ypos = TILE7POS+25, TILEYPOS
    tile8pos.xpos, tile8pos.ypos = TILE8POS+25, TILEYPOS
    tile9pos.xpos, tile9pos.ypos = TILE9POS+25, TILEYPOS
    tile10pos.xpos, tile10pos.ypos = TILE10POS+25, TILEYPOS
    tile11pos.xpos, tile11pos.ypos = TILE11POS+25, TILEYPOS
    tile12pos.xpos, tile12pos.ypos = TILE12POS+25, TILEYPOS
    
    # Player positon on tiles
    player1pos = Position(xpos=TILE1POS+25, ypos=PLAYERYPOS)
    player2pos = Position(xpos=TILE2POS+25, ypos=PLAYERYPOS)
    player3pos = Position(xpos=TILE3POS+25, ypos=PLAYERYPOS)
    player4pos = Position(xpos=TILE4POS+25, ypos=PLAYERYPOS)
    player5pos = Position(xpos=TILE5POS+25, ypos=PLAYERYPOS)
    player6pos = Position(xpos=TILE6POS+25, ypos=PLAYERYPOS)
    player7pos = Position(xpos=TILE7POS+25, ypos=PLAYERYPOS)
    player8pos = Position(xpos=TILE8POS+25, ypos=PLAYERYPOS)
    player9pos = Position(xpos=TILE9POS+25, ypos=PLAYERYPOS)
    player10pos = Position(xpos=TILE10POS+25, ypos=PLAYERYPOS)
    player11pos = Position(xpos=TILE11POS+25, ypos=PLAYERYPOS)
    player12pos = Position(xpos=TILE12POS+25, ypos=PLAYERYPOS)
    
    player1pos.xpos, player1pos.ypos = TILE1POS+25, PLAYERYPOS
    player2pos.xpos, player2pos.ypos = TILE2POS+25, PLAYERYPOS
    player3pos.xpos, player3pos.ypos = TILE3POS+25, PLAYERYPOS
    player4pos.xpos, player4pos.ypos = TILE4POS+25, PLAYERYPOS
    player5pos.xpos, player5pos.ypos = TILE5POS+25, PLAYERYPOS
    player6pos.xpos, player6pos.ypos = TILE6POS+25, PLAYERYPOS
    player7pos.xpos, player7pos.ypos = TILE7POS+25, PLAYERYPOS
    player8pos.xpos, player8pos.ypos = TILE8POS+25, PLAYERYPOS
    player9pos.xpos, player9pos.ypos = TILE9POS+25, PLAYERYPOS
    player10pos.xpos, player10pos.ypos = TILE10POS+25, PLAYERYPOS
    player11pos.xpos, player11pos.ypos = TILE11POS+25, PLAYERYPOS
    player12pos.xpos, player12pos.ypos = TILE12POS+25, PLAYERYPOS
    
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
    
    POSITIONS = {
                        1: player1pos,
                        2: player2pos,
                        3: player3pos,
                        4: player4pos,
                        5: player5pos,
                        6: player6pos,
                        7: player7pos,
                        8: player8pos,
                        9: player9pos,
                        10: player10pos,
                        11: player11pos,
                        12: player12pos
                    }
    
    class Time:
        def __init__(self, hour, day, month, year):
            self.hour = hour
            self.day = day
            self.month = month
            self.year = year
            self.months = ["Stub", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
            
        def now(self):
            minute = renpy.random.randint(0, 59)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def dawn(self);
            minute = renpy.random.randint(0, 59)
            self.hour = renpy.random.randint(1,5)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def morning(self):
            minute = renpy.random.randint(0, 59)
            self.hour = renpy.random.randint(6,11)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def afternoon(self):
            minute = renpy.random.randint(0, 59)
            self.hour = renpy.random.randint(12,17)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def evening(self):
            minute = renpy.random.randint(0, 59)
            self.hour = renpy.random.randint(18,20)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def night(self):
            minute = renpy.random.randint(0, 59)
            self.hour = renpy.random.randint(21,0)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def next_month(self):
            if self.month > 11:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
            
        def next_day():
            if self.day > 29:
                self.next_month()
                self.day = 1
            else:
                self.day += 1
                
        def next_hour():
            if self.hour > 23:
                self.next_day()
                self.hour = 1
            else:
                self.hour += 1
                
        def advance_time(hours=0, days=0, months=0, years=0):
            if hours:
                [self.next_hour() for i in [0]*hours]
            
            if days:
                [self.next_day() for i in [0]*days]
                
            if months:
                [self.next_month() for i in [0]*hours]
            
    main_time = Time(9, 1, 1, 1354)
    
    class Mission:
        def __init__(self, name, hours=0, days=0, months=0, rank="D", dialogue=[]):
           self.name = name
           self.hours = hours
           self.days = days
           self.months = months
           self.dialogue = dialogue
           self.rank = rank
           self.REWARDS = {"D": 5000,
                           "C": 30000,
                           "B": 150000,
                           "A": 450000,
                           "S": 1000000}
           
        def reward(self, player):
            player.ryo += renpy.random.randint(0, self.REWARDS[self.rank]) + self.REWARDS[self.rank]
    
    class BasicMission(Mission):
        """
        No fighting just advance time with a blank background
        One line of dialogue, Rank D
        Mission cannot fail
        Dialogue Structure = [('character', "I say this")]
        """
        def __init__(self, name, hours=0, days=0, months=0, rank="D", dialogue=[("char", " ")]):
            super(BasicMission, self).__init__(name, hours, days, months, rank, dialogue)
            
        def do_mission(player, village):
            # play clock animation here / black background?
            for p, d in self.dailogue:
                renpy.say(player.character, d)
            player.injury_chance(0.05)
            main_time.advance_time(self.hours, self.days)
            self.reward(player)
            show_village_map(village, player)
    
    class Village:
        def __init__(self, id, name, leader, marker_xpos, marker_ypos, map, wealth=10000, army=1000, control=100, influence=100, uprising=0, locations=None):
            self.id = id
            self.name = name
            self.leader = leader
            self.army = army
            self.wealth = wealth
            self.marker_xpos = marker_xpos
            self.marker_ypos = marker_ypos
            self.marker_position = Position(xpos=marker_xpos, ypos=marker_ypos)
            self.map = map
            self.control = control
            self.influence = influence
            self.uprising = uprising
            self.control_change = 0
            self.influence_change = 0
            self.waelth_change = 0
            self.locations = locations
            
        def random_wealth_event(self):
            change = renpy.random.randint(-1000, 1000)
            add_say = ["Many missions completed", "Taxes are raised", "Feudal Lord is feeling generous", "It rains money!", "Not many expenses",
                       "Economy is improving", "Wealth is compounding", "Negotiations are increasing", "Merchants are trading more"]
            minus_say = ["Economy is doing bad", "Not many missions are coming through", "Tax are decreased", "Feudal lord is unhappy", 
                         "Expenses have gone up", "Bad negotiations are failing", "Recession is underway", "Corrupt leader stole wealth and left"]
            if change < 0:
                renpy.say(world_events, minus_say[renpy.random.randint(0, len(minus_say) - 1)])
            else:
                renpy.say(world_events, add_say[renpy.random.randint(0, len(add_say) - 1)])
            self.wealth += change
            self.wealth_change = change
            
        def random_control_event(self):
            change = renpy.random.randint(-10, 10)
            add_say = ["Panel is formed", "Negotiations are doing good", "New settlements are formed", "Village expands", "Cooperation between clands increase",
                       "Economy is improving", "Leader boosts morale", "Moral is high", "Boosting economy"]
            minus_say = ["Economy is doing bad", "Not many missions are coming through", "Power is falling", "Coup attempt failed", 
                         "Other nations are increasing in power", "Clan massacarred", "People hate the leaders", "Bad management"]
            if change < 0:
                renpy.say(world_events, minus_say[renpy.random.randint(0, len(minus_say) - 1)])
            else:
                renpy.say(world_events, add_say[renpy.random.randint(0, len(add_say) - 1)])
            self.control += change
            self.control_change = change
            
        def random_influence_event(self):
            change = renpy.random.randint(-10, 10)
            add_say = ["Other nations are getting weaker", "Spies are executed", "Foriegn policy is working", "Leader has 100th child", "Feudal lords are feeling happier",
                       "Chance to take over other nation", "Leader boosts morale", "Moral is high", "Spies return successfully"]
            minus_say = ["Other nations getting stronger", "Influence increases", "Foriegn policy is not working", "Leaders leave", 
                         "Failed to takeover other nation", "Clan massacarred", "People hate the leaders", "Bad management"]
            if change < 0:
                renpy.say(world_events, minus_say[renpy.random.randint(0, len(minus_say) - 1)])
            else:
                renpy.say(world_events, add_say[renpy.random.randint(0, len(add_say) - 1)])
            self.influence += change
            self.influence_change = change
            
        def random_event(self):
            renpy.show("world_marker", [ self.marker_position ])
            #renpy.show(self.leader.leader_pic, [ LEADER_POSITION ])
            self.random_wealth_event()
            self.random_control_event()
            self.random_influence_event()
            
        def __repr__(self):
            return "<Village>: {}".format(self.name)
            
    class Location:
        def __init__(self, name, label, special_event=False, map_pic_idle=None, map_pic_hover=None, npc=[], visits=None):
            self.name = name
            self.label = label
            #self.village = village
            self.special_event = special_event
            self.map_pic_idle = map_pic_idle
            self.map_pic_hover = map_pic_hover
            self.npc = npc
            self.visits = visits
            
        def interact(self, player, village):
            renpy.call(self.label, player, village)
            
    # locations that exist in each village
    travel = Location('Travel', 'village_travel')
    level_up = Location('Level Up', 'village_levelup')
    training_ground = Location('Training', 'village_training')
    arena = Location('Arena', 'village_arena')
    hospital = Location('Hospital', 'village_hospital')
    jounin_station = Location('Jounin Standby Station', 'village_jounin_station')
    intelligence_division = Location('Intelligence Division', 'village_intelligence_division')
    ninja_tool_facility = Location('Ninja Tool Facility', 'village_ninja_tool_facility')
    mission = Location('Mission Assignment Desk', 'village_missions')
    
    BASE_LOCATIONS = [travel, level_up, training_ground, arena, hospital, jounin_station, intelligence_division, ninja_tool_facility, mission]
    
    # This used to store information about recent actions (since renpy does not have a call action for screens)
    class CurrentSession:
        def __init__(self):
            self.player = None
            self.location = None
            self.village = None
            self.limb = None
            
        def clear(self):
            self.player = None
            self.location = None
            self.village = None
            self.limb = None
        
    current_session = CurrentSession()
    
    class Limb:
        def __init__(self, name):
            self.name = name
            self.bleeding = False
            self.crippled = False
            self.cripple_count = 0
            self.injury = False
            
        def bleed(self):
            self.bleeding = True
            self.cripple_count += 1
            
        def stop_bleeding(self):
            self.bleeding = False
            
        def cripple(self):
            if self.cripple_count > 5:
                self.cripple = True
                
        def injure(self):
            self.injury = True
            
    limb_head = Limb('head')
    limb_torso = Limb('torso')
    limb_left_arm = Limb('left arm')
    limb_right_arm = Limb('right arm')
    limb_left_leg = Limb('left leg')
    limb_right_leg = Limb('right leg')
    
    LIMBS = [limb_head, limb_torso, limb_left_arm, limb_right_arm, limb_left_leg, limb_right_leg]
    
    class Team:
        def __init__(self, name, sensei=None, members=[], chemistry=0):
            self.name = name
            self.sensei = name
            self.members = members
            self.chemistry = chemistry
            
        def add_member(self, new_member):
            self.members.append(new_member)
            
        def remove_member(self, old_member):
            self.members.remove(old_member)
            
        def increase_chemistry(self, exp):
            self.chemistry += exp
            return self.chemistry
            
        def decrease_chemistry(self, exp):
            self.chemistry -= exp
    
    LEVELS = {level: level*100 for level in range(1,100)}
    MAX_BOND = 100
    
    import copy
    import random

    class Player:
        def __init__(self, name, picname, character, tilepic, hudpic, hp, maxhp, chakra, maxchakra, 
                     strength, speed, evasion, defence, stamina, base_hit_rate, tile, facing,
                     taiskills=[], ninskills=[], genskills=[], items=[], defensiveskills=[], bloodlineskills=[],
                     leader_pic=None, taijutsu=1, ninjutsu=1, genjutsu=1):
            self.name = name
            self.picname = picname
            self.character = character
            self.tilepic = tilepic
            self.hudpic = hudpic
            self.hp = hp
            self.maxhp = maxhp
            self.chakra = chakra
            self.maxchakra = maxchakra
            self.strength = strength
            self.speed = speed
            self.evasion = evasion
            self.defence = defence
            self.stamina = stamina
            self.base_hit_rate = base_hit_rate
            self.taijutsu = taijutsu
            self.ninjutsu = ninjutsu
            self.genjutsu = genjutsu
            self.tile = tile # position 
            self.facing = facing
            self.taiskills = taiskills
            self.ninskills = ninskills
            self.genskills = genskills
            self.items = items
            self.defensiveskills = defensiveskills
            self.bloodlineskills = bloodlineskills
            self.all_skills = self.taiskills + self.ninskills + self.genskills + self.items + self.defensiveskills + self.bloodlineskills
            self.action_counter = 0
            self.battlescreen = None
            self.stunned = False
            self.counter_state = False
            self.head = copy.deepcopy(limb_head)
            self.torso = copy.deepcopy(limb_torso)
            self.left_arm = copy.deepcopy(limb_left_arm)
            self.right_arm = copy.deepcopy(limb_right_arm)
            self.left_leg = copy.deepcopy(limb_left_leg)
            self.right_leg = copy.deepcopy(limb_right_leg)
            self.limbs = [self.head, self.torso, self.left_arm, self.right_arm, self.left_leg, self.right_leg]
            self.blood = 100
            self.max_blood = 100
            self.damage_dealt = 0
            self.main = False
            self.exp = 0
            self.level = 1
            self.allocation_points = 0
            self.leader_pic = leader_pic
            self.team = None
            self.sensei = self.team.sensei or None
            self.bond = 0
            self.ryo = 100
            #self.damage_reduction = False
            #self.chakra_defence = False
            #self.reflect = False
            #self.dampen = False
            #self.ignore_damage = False
            
            self.assign_all_skills()
            
        def is_injured(self):
            for limb in self.limbs:
                if limb.injury:
                    return True
            return False
            
        def injured_limbs(self):
            injured = [limb for limb in self.limbs if limb.injury]
            return injured
            
        def injury_chance(self, chance=0.00):
            percent = chance * 100
            if renpy.random.randint(1,101) > percent:
                random.choice(self.limbs).injure()
            
        def increase_bond(self, bond):
            self.bond += bond + renpy.random.randint(1,3)
            if self.bond > MAX_BOND:
                self.bond = MAX_BOND
            
        def level_up(self):
            difference = self.exp - LEVELS[self.level + 1]
            if difference < 0:
                return
            else:
                self.level +=1
                self.allocation_points += 3
                self.maxhp += renpy.random.randint(20, 30)
                self.maxchakra += renpy.random.randint(10, 20)
                self.exp = 0
                self.gain_exp(difference)
                
        def gain_exp(exp):
            exp += renpy.random.randint(1,10)
            self.exp += exp
            self.level_up()
            return self.exp
        
        def change_direction(self, direction):
            #renpy.say(self.character, "I was {} : {}".format(direction, self.picname))
            if direction == 'left':
                self.picname = self.picname.replace("_r", "_l")
            else:
                self.picname = self.picname.replace("_l", "_r")
            #renpy.say(self.character, "Now I am {} : {}".format(direction, self.picname))
            
        def is_bleeding(self):
            for limb in self.limbs:
                if limb.bleeding:
                    return True
            return False
            
        def bleeding_limbs_count(self):
            bad_limbs = [limb for limb in self.limbs if limb.bleeding]
            return len(bad_limbs)
            
        def get_skill(self, name):
            for skill in self.all_skills:
                if skill.name == name:
                    return skill
                    
        def remove_skill(self, name):
            for skill in self.all_skills:
                if skill.name == name:
                    self.all_skills.remove(skill)
                    
        def assign_all_skills(self):
            for skill in self.all_skills:
                setattr(self, skill.label, skill)
                
        def remove_skill(self, skill):
            delattr(self, skill.label)
            
        def assign_skill(self, skill):
            setattr(self, skill.label, skill)
            
        def apply_skill(self, skill):
            skill.apply()
            setattr(self, skill.label, skill)
            
        def check_active_skill(self, skill):
            s = getattr(self, skill.label, None)
            if s:
                if s.active:
                    return True
                else:
                    return False 
            else:
                return False
            
        def active_defensive_skill(self):
            defensive_skills = [self.check_active_skill(skill) for skill in self.defensiveskills]
            if True in defensive_skills:
                return True
            else:
                return False
            #for skill in self.defensiveskills:
            #    check = getattr(self, skill.label)
            #    renpy.say(self.character, "{} {}".format(check.label, check.active))
            #    if check.active:
            #        return True
            #return False
            
        def fix_stats(self):
            if self.hp < 0:
                self.hp = 0
            
            if self.chakra < 0:
                self.chakra = 0
                
        def __repr__(self):
            return "<Player>: {}".format(self.name)
            
    class Stage:
        def __init__(self, name, pull, range):
            self.name = name
            self.pull = pull
            self.range = range
            
        def remove_chakra(self):
            return self.pull + renpy.random.randint(-1, self.range)
            
    class Tile:
        def __init__(self, pos, idle, hover, position):
            self.pos = pos 
            self.idle = idle
            self.hover = hover
            self.position = position
            self.trap = False
            self.active = False
            self.trap_pic = TILETRAPPIC
            
        def activate(self):
            self.idle = self.hover
            self.active = True
            
        def deactivate(self):
            self.idle = TILEIDLEPIC
            self.active = False
            
        def activate_trap(self):
            self.trap = True
            self.idle = TILETRAPPIC
            
        def deactivate_trap(self):
            self.trap = False
            self.idle = TILEIDLEPIC
            
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
    
    def get_tile_from_position(position):
        for tile in TILES:
            if tile.position == position:
                return tile
    
    def remove_trap(trap_tile):
        for tile in TILES:
            if tile.position == trap_tile.position:
                tile.deactivate_trap()
    
    class Skill:
        def __init__(self, name, skill_type, label, range, tech=0, chakra_cost=0, damage=0, stun=False, duration=None, exp=0, unlock_exp=0):
            self.name = name
            self.skill_type = skill_type
            self.label = label
            self.range = range
            self.tech = tech
            self.exp = exp
            self.unlock_exp = unlock_exp
            self.chakra_cost = chakra_cost
            self.damage = damage 
            self.stun = stun
            self.duration = duration
            self.used = 0
            self.active = False
            
        def set_to_default(self):
            self.active = False
            self.tech = 0
            self.exp = 0
            
        def unlock(self, player):
            new_skill = self
            player.assign_skill(new_skill)
            
        def gain_exp(self, exp):
            self.exp += exp
            if self.exp > self.unlock_exp:
                self.exp = self.unlock_exp
            return self.exp
            
        def activate(self):
            self.active = True
            
        def deactivate(self):
            self.active = False
            
        def action(self, player, enemy):
            if player.chakra < self.chakra_cost:
                renpy.say(player.character, "I don't have enough chakra")
                Jump("fight")
            
            if self.hit_successful(player, enemy):
                renpy.say(player.character, "{}".format(self.name))
                self.deal_damage(player, enemy)
                enemy.fix_stats()
                player_bleed(enemy)
            else:
                renpy.say(player.character, "{} dodges my attack.".format(enemy.name))
                
            player.chakra -= self.chakra_cost
            player.fix_stats()
            self.tech += 1
            return
            
        def apply(self):
            self.activate()
            
        def remove(self):
            self.deactivate()
                
        def append_to_skill(self):
            self.used += 1
            
        def deal_damage(self, player, target):
            #renpy.say(target.character, "{}".format(self.active))
            #if not self.active:
            #    return
                
            #renpy.say(target.character, "HELLO2")
            
            self.append_to_skill()
            
            damage = (self.damage - target.defence) + self.tech
            
            if check_active_skill(target, "damagereduction"):
                damage = damage - (target.hp * 0.1)
                target.damagereduction.used += 1
                
            if check_active_skill(target, "chakradefence"):
                damage = damage - (target.chakra * 0.1)
                target.chakradefence.used += 1
                            
            if check_active_skill(target, "dampen"):
                damage = damage * 0.5
                target.dampen.used += 1
                
            if check_active_skill(target, "reflect"):
                renpy.say(target.character, "Reflect!".format(target.name))
                player.hp -= (self.damage - player.defence) 
                target.reflect.used += 1
                
            elif check_active_skill(target, "yatamirror"):
                renpy.say(target.character, "Your skills won't affect me!".format(target.name))
                damage = 0
                target.yatamirror.used += 1
            else:
                target.hp -= damage
                
            player.damage_dealt = damage + self.tech
            
           
        def hit_successful(self, player, enemy):
            hit_rate = player.base_hit_rate + self.tech - (enemy.evasion * enemy.speed)
            renpy.say(player.character, "Hit rate is {}".format(hit_rate))
            if renpy.random.randint(1, 100) <= hit_rate:
                return True
            else:
                return False
                
        def stun(self, player, enemy):
            enemy.stunned = True
            return 
            
        def saysay(self):
            renpy.say(enemy.character, "Skill: {} {}".format(self.skill_type, self.name))
            
        def __repr__(self):
            return "Skill: {} {}".format(self.skill_type, self.name)
    
    # tai skills
    onetwocombo = Skill('One Two Combo', 'tai', "onetwocombo", 3, 1, 3, 10)
    lioncombo = Skill('Lion Combo', 'tai', "lioncombo", 3, 2, 5, 20)
    
    # nin skills
    rasengan = Skill('Rasengan', 'nin', "rasengan", 2, 1, 25, 30)
    chidori = Skill('Chidori', 'nin', "chidori", 2, 1, 25, 30)
    raikiri = Skill('Raikiri', 'nin', "raikiri", 2, 1, 50, 50)
    
    # gen skills # replace with something new
    substitution = Skill('Substitution', 'gen', "substitution", 8, 20, 15, 0, stun=True)
    
    # tool skills
    shiruken = Skill('Shiruken', 'tool', "shiruken", 12, 7, 1, 20)
    kunai = Skill('Kunai', 'tool', "kunai", 12, 4, 1, 20)
    trap = Skill('Trap', 'tool', "trap", 3, 1, 2, 30)
    
    # defensive skills
    damage_reduction_p = Skill('Focus', 'defence', 'damagereduction', 12, 1, 10, duration=2)
    damage_reduction_e = Skill('Focus', 'defence', 'damagereduction', 12, 1, 10, duration=2)
    chakra_defence = Skill('Chakra Defence', 'defence', 'chakradefence', 12, 2, 15, duration=3)
    chakra_defence_e = Skill('Chakra Defence', 'defence', 'chakradefence', 12, 2, 15, duration=3)
    substitution = Skill('Substitution', 'defence', "substitution", 8, 20, 15, 0, stun=True)
    reflect = Skill('Reflect', 'defence', 'reflect', 12, 20, 20, duration=2)
    dampen = Skill('Dampen', 'defence', 'dampen', 6, 30, 30, duration=3)
    yata_mirror = Skill('Yata Mirror', 'defence', 'yatamirror', 12, 50, 50, duration=2)
    
    naruto = Player('Naruto', "playerpic_r", naruto_c, Image('player.png'), None, 100, 100, 80, 80, 10, 4, 3, 4, 5, 80, tile1, 'right', 
                    [onetwocombo, lioncombo], [rasengan], [substitution], [shiruken, kunai, trap], 
                    [damage_reduction_p, chakra_defence, reflect, dampen, yata_mirror], [], "leader_pic")
    sasuke = Player('Sasuke', "enemypic_r", sasuke_c, Image('enemy.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo, shiruken, kunai], [chidori], [], [], [damage_reduction_e, chakra_defence_e])
    
    sakura = Player('Sakura', "enemypic_r", sakura_c, Image('enemy.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo, shiruken, kunai], [chidori], [], [], [damage_reduction_e, chakra_defence_e])
    kakashi = Player('Kakashi', "enemypic_r", kakashi_c, Image('enemy.png'), None, 100, 100, 80, 80, 11, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo, shiruken, kunai], [chidori], [], [], [damage_reduction_e, chakra_defence_e])
    
    clearing = Stage('Clearing', 1, 1)
    
    # villages
    hidden_stone = Village(1, "Hidden Stone", naruto, marker_xpos=0.25, marker_ypos=0.25, map="stones_map", locations=BASE_LOCATIONS)
    hidden_cloud = Village(2, "Hidden Cloud", naruto, marker_xpos=0.75, marker_ypos=0.20, map="clouds_map", locations=BASE_LOCATIONS)
    hidden_mist = Village(3, "Hidden Mist", naruto, marker_xpos=0.85, marker_ypos=0.70, map="mist_map", locations=BASE_LOCATIONS)
    hidden_leaf = Village(4, "Hidden Leaf", naruto, marker_xpos=0.40, marker_ypos=0.60, map="konoha_map", locations=BASE_LOCATIONS)
    hidden_sand = Village(5, "Hidden Sand", naruto, marker_xpos=0.25, marker_ypos=0.90, map="sand_map", locations=BASE_LOCATIONS)
    
    ALL_VILLAGES = [hidden_stone, hidden_cloud, hidden_mist, hidden_leaf, hidden_sand]
    
    import math
    def time_between_village(village1, village2):
        distance = math.sqrt( (village1.marker_xpos - village2.marker_xpos)**2 + (village1.marker_ypos - village2.marker_ypos)**2 )
        time_weeks = abs(distance / 0.1)
        days = time_weeks * 7
        return int(days)
        
    def other_villages(village):
        return [v for v in ALL_VILLAGES if v.id != village.id]
    
    def show_village_map(village, player):
        renpy.hide(village.map) # remove it first otherwise it does not show the new image on top
        renpy.show(village.map)
        renpy.show_screen('villagemap', village, player)
        renpy.say(player.character, "I need to choose an action.")
        return show_village_map(village, player)
    
    def start_world_events():
        renpy.show("map") #, [ Position(xpos=0, ypos=0) ])
        for village in ALL_VILLAGES:
            renpy.show_screen('worldevents', village)
            village.random_event()
            renpy.hide_screen('worldevents')
            #renpy.call('world_update', village)
            
        #renpy.say(world_events, "I am here now")
        renpy.jump('start')
    
    def check_active_skill(player, skillname):
        try:
            skill = getattr(player, skillname)
            if skill.active:
                return True
            else:
                return False
        except AttributeError as e:
            return False
    
    def highlight_position(player, enemy, stage):
        for tile in TILES:
            if not tile.trap:
                tile.deactivate()
            
        #player.tile.activate()
        show_player_at_pos(player, enemy, stage, player.tile)
        #renpy.show(player.picname, [ POSITIONS[player.tile.position] ])
        #enemy.tile.activate()
        show_player_at_pos(enemy, player, stage, enemy.tile)
        #renpy.show(enemy.picname, [ POSITIONS[enemy.tile.position] ])
    
    def show_player_at_pos(player, enemy, stage, tile, initial_movement=False):
        
        difference = abs(player.tile.position - tile.position)
        player.tile.deactivate()
        player.tile = tile
        player.tile.activate()
        
        if player.tile.position < enemy.tile.position:
            player.facing = 'right'
            player.change_direction(player.facing)
        else:
            player.facing = 'left'
            player.change_direction(player.facing)
            
        #if not initial_movement:
            #player.chakra -= (stage.remove_chakra() + (difference * stage.pull))
            
        #renpy.hide(player.picname)
        renpy.show(player.picname, [ POSITIONS[tile.position] ])
        
        # Handle traps
        if tile.trap:
            renpy.say(player.character, "Oh no there is a trap here!")
            player.hp -= 30
            remove_trap(tile)
        
    def hide_battle_screen():
        renpy.hide_screen("battlemenu")
        renpy.hide_screen("taiactions")
        renpy.hide_screen("ninactions")
        renpy.hide_screen("defenceactions")
        renpy.hide_screen("itemselection")
        
    def enemy_move(player, enemy, stage):
        hide_battle_screen()
        show_player_at_pos(enemy, player, stage, enemy.tile)
        skills = enemy.all_skills 
        skill_index = 1 #renpy.random.randint(0, (len(skills) - 1))
        current_skill = skills[skill_index]
        
        if current_skill.skill_type == 'defence':
            if not enemy.active_defensive_skill():
                enemy.apply_skill(current_skill)
                Jump("fight")
            else:
                skill_index = renpy.random.randint(0, (len(enemy.taiskills) - 1))
                current_skill = enemy.taiskills[skill_index]
        
        if current_skill.range >= abs(player.tile.position - enemy.tile.position):
            current_skill.action(enemy, player)
        else:
            # move enemy to near player
            enemy_position = player.tile.position + current_skill.range
            enemy.tile = get_tile_from_position(enemy_position)
            
            # Do the attack
            current_skill.action(enemy, player)
            
            # take away movement chakra too
            enemy.chakra -= (current_skill.range * stage.pull) 
            
        renpy.show(enemy.picname, [ POSITIONS[enemy.tile.position] ])
        #renpy.show("show_damage_e", [ Position(xpos=0.45, ypos=200) ], what=show_damage_e)
        
        # bleeding
        player_bleed(player)
        
        # trap
        if enemy.tile.trap:
            renpy.say(player.character, "You got stuck in my trap!")
            renpy.say(enemy.character, "Oh no!")
            enemy.hp -= 30
            remove_trap(enemy.tile)
            
        Jump("fight")
        
    def player_bleed(target):
        if target.hp < (0.3 * target.maxhp):
            if renpy.random.randint(1,3) > 2:
                limb_index = renpy.random.randint(0, len(target.limbs) - 1)
                limb = target.limbs[limb_index]
                renpy.say(target.character, "No my {} is bleeding".format(limb.name))
                if not limb.bleeding:
                    limb.bleed()
        
    def drain_blood(target):
        if target.is_bleeding():
            target.blood -= target.bleeding_limbs_count() * (5 + renpy.random.randint(0, 2))
            renpy.say(target.character, "I need to end this soon, I am loosing too much blood.")
        
    def counter_move(player, enemy):
        renpy.say(enemy.character, "You left yourself open.")
        enemy_pos = enemy.tile.position
        if enemy_pos < 12:
            player.tile = get_tile_from_position(enemy_pos + 1)
            player.change_direction(player.facing)
        else:
            player.tile = get_tile_from_position(player.tile.position - 1)
            
        player.counter_state = False
        renpy.say(player.character, "Got you!")
        renpy.show(player.picname, [ POSITIONS[player.tile.position] ])
        Jump("fight")    
        
    def set_trap_at_pos(player, enemy, stage, tile):
        if not tile.trap:
            renpy.say(player.character, "I set a trap here.")
            tile.activate_trap()
        else:
            renpy.say(player.character, "A trap is already set there.")
            set_trap_at_pos(player, enemy, stage, tile)
            
        Jump("fight")
        
    def remove_all_skill_affects(player, enemy):
        player.fix_stats()
        enemy.fix_stats()
        
        for skill in player.all_skills:
            s = getattr(player, skill.label)
            if s.used == s.duration:
                s.used = 0
                s.remove()
                setattr(player, s.label, s)
                
        for skill in enemy.all_skills:
            s = getattr(enemy, skill.label)
            if s.used == s.duration:
                s.used = 0
                s.remove()
                setattr(enemy, s.label, s)

    def show_damage(st, at, player):
        return Text("-{}".format(player.damage_dealt), color="#fff", size=20), None
        
    def end_match(player, enemy, win_label, lose_label, draw_label):
        #renpy.say(player.character, "I AM RUNNING {} {} {} {} {}".format(player.hp, enemy.hp, win_label, lose_label, draw_label))
        if draw_label:
            renpy.jump(draw_label)
        elif player.hp == 0:
            renpy.jump(lose_label)
        elif enemy.hp == 0:
            renpy.jump(win_label)
            
    def get_tag_info(player, tag_p):
        one_list = [player] + tag_p
        info = {}
        new_tag_p = []
        
        for p in one_list:
            if not p.main:
                new_tag_p.append(p)
            
        for p in one_list:
            if p.main:
                info['main'] = p
            else:
                info['tag'] = new_tag_p
        return info
        
    import copy
    def get_sensei_skill(sensei, student):
        sensei_skills = [skill.label for skill in sensei.all_skills]
        student_skills = [skill.label for skill in student.all_skills]
        skills_to_teach = list(set(sensei_kills) - set(student_skills))
        if skills_to_teach:
            skill_index = renpy.random.randint(0, len(skills_to_teach) - 1)
            new_skill = skills_to_teach[skill_index]
            learnt_skill = copy.deepcopy(new_skill.set_to_default())
            student.assign_skill(learnt_skill)
            return learnt_skill
        else:
            return None

screen training(village, player):
    textbutton "Train skills" action [Hide("training"), Show("train_skills", village, player)] xpos grid_place[0][0] ypos grid_place[0][1]
    if player.team:
        # maybe add formation, 
        text "Team Chemistry: [player.team.chemistry]" xpos 0.1 ypos 0.1
        textbutton "Train with team" action [SetField(getattr(player, 'team'), 'chemistry', getattr(player, team).increase_chemistry(10),
                                             Hide("training"), 
                                             Show("training", village, player)] xpos grid_place[1][0] ypos grid_place[1][1]
    if player.sensei:
        textbutton "Learn skills" action [SetField(current_session, 'village', village), 
                                          SetField(current_session, 'player', player), 
                                          SetField(current_session, 'location', training_ground),
                                          Hide("training"), 
                                          Jump("training_sensei")] xpos grid_place[2][0] ypos grid_place[2][1]
                                      
    textbutton "Train (+ exp)" action [SetField(player, 'exp', player.gain_exp(10)),
                                       Hide("training"), 
                                       Show("train_skills", village, player)] xpos grid_place[3][0] ypos grid_place[3][1]
    
screen train_skills(village, player):
    $ counter = 0
    for skill in player.all_skills:
        if skill.exp < skill.unlock_exp:
            textbutton "[skill.name] [skill.exp]/[skill.unlock_exp]" action [SetField(getattr(player, skill.label), 'exp', getattr(player, skill.label).gain_exp(10), 
                                                                             Hide("train_skills"),
                                                                             Show("training", village, player)] xpos grid_place[counter][0] ypos grid_place[counter][1]
            $ counter += 1

screen levelup(village, player):
    $ STATS = ['strength', 'speed', 'evasion', 'defence', 'stamina', 'taijutsu', 'ninjutsu', 'genjutsu']
    $ counter = 0
    text "Allocation Points: [player.allocation_points]" xpos 0.1
    text "Str: [player.strength] Def: [player.defence] Eva: [player.evasion]" xpos 0.50
    text "Sta: [player.stamina] Speed: [player.speed] Hit: [player.base_hit_rate]" xpos 0.50 ypos 0.05
    text "Tai: [player.taijutsu] Nin: [player.ninjutsu] Gen: [player.genjutsu]" xpos 0.50 ypos 0.1
    
    if player.allocation_points:
        for stat in STATS:
            textbutton "[stat] +1" action [SetField(player, stat, getattr(player, stat) + 1), 
                                           SetField(player, 'allocation_points', getattr(player, 'allocation_points') - 1), 
                                           SetField(current_session, 'village', village), 
                                           SetField(current_session, 'player', player), 
                                           SetField(current_session, 'location', level_up), 
                                           Jump('location_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
            $ counter +=1 
    else:
        text "No allocation points" xpos 0.5 ypos 0.5
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'player', player), 
                                                 Hide('levelup'), 
                                                 Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]

screen villagetravel(village, player):
    $ counter = 0
    $ village_time = 0
    
    for v in other_villages(village):
        $ village_time = time_between_village(v, village)
        textbutton "[v.name] [village_time]" action [SetField(current_session, 'village', v), 
                                                     SetField(current_session, 'player', player), 
                                                     Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
        $ counter += 1
        
    textbutton "Back to Location select" action [SetField(current_session, 'village', village), 
                                                 SetField(current_session, 'player', player), 
                                                 Jump('village_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]

screen villagemap(village, player):
    # show player time details here
    $ counter = 0
    
    for location in village.locations:
        textbutton [location.name] action [SetField(current_session, 'player', player), 
                                           SetField(current_session, 'village', village), 
                                           SetField(current_session, 'location', location), 
                                           Jump('location_redirect')] xpos grid_place[counter][0] ypos grid_place[counter][1]
        $ counter += 1

screen worldevents(village):
    text "Wealth: [village.wealth]" xpos 0.3 ypos 0.03
    text "Control:" xpos 0.3 ypos 0.08
    text "Influence:" xpos 0.3 ypos 0.13
    text "Uprising:" xpos 0.3 ypos 0.18
    bar value village.control range 100 xpos 0.45 ypos 0.08 xmaximum 100 ymaximum 30
    bar value village.influence range 100 xpos 0.45 ypos 0.13 xmaximum 100 ymaximum 30
    bar value village.uprising range 100 xpos 0.45 ypos 0.18 xmaximum 100 ymaximum 30
        

screen taiactions:
    vbox:
        for skill in player.taiskills:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                if player.chakra > skill.chakra_cost:
                    textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
                else:
                    textbutton "[skill.name]" xpos 0.6
            else:
                textbutton "[skill.name]" xpos 0.6
        
screen ninactions:
    vbox:
        for skill in player.ninskills:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                if player.chakra > skill.chakra_cost:
                    textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
                else:
                    textbutton "[skill.name]" xpos 0.6
            else:
                textbutton "[skill.name]" xpos 0.6
        
screen genactions:
    vbox:
        for skill in player.genskills:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                if player.chakra > skill.chakra_cost:
                    textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
                else:
                    textbutton "[skill.name]" xpos 0.6
            else:
                textbutton "[skill.name]" xpos 0.6
                
screen defenceactions:
    vbox:
        for skill in player.defensiveskills:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                if player.chakra > skill.chakra_cost:
                    textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
                else:
                    textbutton "[skill.name]" xpos 0.6
            else:
                textbutton "[skill.name]" xpos 0.6

screen itemselection:
    vbox:
        for skill in player.items:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                if player.chakra > skill.chakra_cost:
                    textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
                else:
                    textbutton "[skill.name]" xpos 0.6
            else:
                textbutton "[skill.name]" xpos 0.6

label onetwocombo:
    $ onetwocombo.action(player, enemy)
    jump enemymove
    
label lioncombo:
    $ lioncombo.action(player, enemy)
    jump enemymove
    
label rasengan:
    $ rasengan.action(player, enemy)
    jump enemymove

label chidori:
    $ chidori.action(player, enemy)
    jump enemymove
    
label substitution:
    $ renpy.say(player.character, "{}".format(substitution.name))
    $ player.counter_state = True
    jump enemymove
    
label shiruken:
    $ shiruken.action(player, enemy)
    jump enemymove
    
label kunai:
    $ kunai.action(player, enemy)
    jump enemymove
    
label trap:
    jump settrap
    
label damagereduction:
    "S" "ENEMY BEFORE DR: [enemy.damagereduction.active]"
    $ player.damagereduction.apply()
    "S" "ENEMY AFTER DR: [enemy.damagereduction.active]"
    jump enemymove
    
label chakradefence:
    $ player.chakradefence.apply()
    jump enemymove
    
label reflect:
    $ player.reflect.apply()
    jump enemymove
    
label dampen:
    $ player.dampen.apply()
    jump enemymove
    
label yatamirror:
    $ player.yatamirror.apply()
    jump enemymove

screen battlemenu(player, tag_p):
    vbox:
        textbutton "Tai" action [Hide("ninactions"), Hide("genactions"), Hide("movemenu"), Hide("itemselection"), Hide("defenceactions"), Show("taiactions")]
        textbutton "Nin" action [Hide("taiactions"), Hide("genactions"), Hide("movemenu"), Hide("itemselection"), Hide("defenceactions"), Show("ninactions")]
        textbutton "Gen" action [Hide("ninactions"), Hide("taiactions"), Hide("movemenu"), Hide("itemselection"), Hide("defenceactions"), Show("genactions")]
        textbutton "Move" action [Hide("ninactions"), Hide("genactions"), Hide("taiactions"), Hide("itemselection"), Hide("defenceactions"), Show("movemenu")]
        textbutton "Items" action [Hide("ninactions"), Hide("genactions"), Hide("movemenu"), Show("itemselection"), Hide("defenceactions"), Hide("taiactions")]
        textbutton "Defence" action [Hide("ninactions"), Hide("genactions"), Hide("movemenu"), Hide("itemselection"), Show("defenceactions"), Hide("taiactions")]
        textbutton "Standby" action Jump("standby")
        for partner in tag_p:
            textbutton "Tag [partner.name]" action [SetField(partner, 'main', True), SetField(partner, 'tile', player.tile), SetField(player, 'main', False), Jump('tag_partner')]
        
screen stats:
    text "Str: [player.strength] Def: [player.defence] Eva: [player.evasion]" xpos 0.30
    text "Sta: [player.stamina] Hit: [player.base_hit_rate]" xpos 0.30 ypos 0.05
    text "Str: [enemy.strength] Def: [enemy.defence] Eva: [enemy.evasion]" xpos 0.65
    text "Sta: [enemy.stamina] Hit: [enemy.base_hit_rate]" xpos 0.65 ypos 0.05
        
screen battlebars:
    #frame:
        #has vbox 
    $ rel_pos = abs(player.tile.position - enemy.tile.position)

    text "[player.name]" xpos 0.5 ypos 0.15
    text "[player.chakra]" xpos 0.49 ypos 0.45
    text "[player.hp]" xpos 0.55 ypos 0.45
    vbar value player.chakra range player.maxchakra xpos 0.5 ypos 0.2 ymaximum 150
    vbar value player.hp range player.maxhp xpos 0.55 ypos 0.2 ymaximum 150
    if enemy.damage_dealt > 0:
        text "-[enemy.damage_dealt]" xpos 0.59 ypos 0.3
    
    text "[player.facing]" xpos 0.2 ypos 0.25
    if player.check_active_skill(damage_reduction_p):
        text "DR" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(chakra_defence):
        text "CD" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(reflect):
        text "Ref" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(dampen):
        text "Dam" xpos 0.3 ypos 0.15
        
    if player.check_active_skill(yata_mirror):
        text "Yata" xpos 0.3 ypos 0.15
    
    if player.is_bleeding():
        text "blood" vertical True xpos 0.40 ypos 0.2
        vbar value player.blood range player.max_blood xpos 0.45 ypos 0.2 ymaximum 150
    
    text "[enemy.name]" xpos 0.65 ypos 0.15
    text "[enemy.chakra]" xpos 0.64 ypos 0.45
    text "[enemy.hp]" xpos 0.70 ypos 0.45
    vbar value enemy.hp range enemy.maxhp xpos 0.7 ypos 0.2 ymaximum 150
    vbar value enemy.chakra range enemy.maxchakra xpos 0.66 ypos 0.2 ymaximum 150
    if player.damage_dealt > 0:
        text "-[player.damage_dealt]" xpos 0.75 ypos 0.3
    
    if enemy.is_bleeding():
        text "blood" vertical True xpos 0.78 ypos 0.2
        vbar value enemy.blood range enemy.max_blood xpos 0.74 ypos 0.2 ymaximum 150
        
    if enemy.check_active_skill(damage_reduction_e):
        text "DR" xpos 0.75 ypos 0.15
        
    if enemy.check_active_skill(chakra_defence_e):
        text "CD" xpos 0.75 ypos 0.15
        
    text "[enemy.facing] [enemy.picname]" xpos 0.75 ypos 0.15
        
    #if enemy.reflect.active:
    #    text "Ref" xpos 0.75 ypos 0.15
        
    #if enemy.dampen.active:
    #    text "Dam" xpos 0.75 ypos 0.15
        
    #if enemy.yatamirror.active:
    #    text "Yata" xpos 0.75 ypos 0.15

label world_update(village):
    scene map
    $ village.random_event()
    return
    
label village_redirect:
    hide screen villagetravel
    $ show_village_map(current_session.village, current_session.player)
    jump village_redirect
    
label location_redirect:
    hide screen villagemap 
    $ renpy.call(current_session.location.label, current_session.player, current_session.village)
    
label village_travel(player, village):
    show screen villagetravel(village, player)
    player.character "I need to choose a destination"
    $ renpy.call('village_travel', player, village)
    
label village_levelup(player, village):
    show screen levelup(village, player)
    player.character "I need to choose level up stats"
    $ renpy.call('village_levelup', player, village)

label village_training(player, village):
    scene training_ground evening
    "SAMPLE" "TRAVEL HERE"
    jump start
    
label training_sensei:
    $ new_skill = get_sensei_skill(player.sensei, player)
    player.sensei.character "I am about to teach you is [new_skill.name]."
    if new_skill.unlock_exp < 300:
        player.sensei.character "It is a basic skill but fundamental to being a shinobi."
    elif new_skill.unlock_exp < 600:
        player.sensei.character "It is an intermediate skill but fundamental to being a shinobi."
    elif new_skill.unlock_exp < 900:
        player.sensei.character "It is an advanced skill and hard to master."
    # some sort of explanation
    player.character "[new_skill.name] added to skill set."
    $ renpy.call(current_session.location.label, current_session.player, current_session.village)
    
label village_arena(player, village):
    "SAMPLE" "TRAVEL HERE"
    jump start
    
label village_hospital(player, village):
    "SAMPLE" "TRAVEL HERE"
    jump start
    
label village_jounin_station(player, village):
    "SAMPLE" "TRAVEL HERE"
    jump start
    
label village_intelligence_division(player, village):
    "SAMPLE" "TRAVEL HERE"
    jump start
    
label village_ninja_tool_facility(player, village):
    "SAMPLE" "TRAVEL HERE"
    jump start
    
label village_missions(player, village):
    "SAMPLE" "TRAVEL HERE"
    jump start

label tag_partner:
    $ info = get_tag_info(player, tag_p)
    $ renpy.call('fight', info['main'], enemy, info['tag'], tag_e, stage, win_label, lose_label, draw_label)
    
label start:
    $ show_village_map(hidden_mist, naruto)
    #$ start_world_events()
    call fight(naruto, sasuke, [sakura, kakashi], [], clearing, 'fight1_w', 'fight1_l', None)
    
label fight(player, enemy, tag_p, tag_e, stage=clearing, win_label, lose_label, draw_label=None):
    scene bg
    
    call showtiles
    hide screen movemenu
    hide screen settrap
    # initial position
    $ highlight_position(player, enemy, stage)
    $ end_match(player, enemy, win_label, lose_label, draw_label)
    $ remove_all_skill_affects(player, enemy)
    #$ show_player_at_pos(player, enemy, clearing, player.tile, initial_movement=True)
    
    #$ drain_blood(player)
    #$ drain_blood(enemy)
    show screen battlemenu(player, tag_p)
    show screen battlebars
    show screen stats
    
    python:
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(1), xpos=1000, ypos=1000)
        choice = ui.interact()
    
    "Tiger" "Gao gao! You're strong!"
    "Sample" "Sample...."
    
    call movemenu
    
label fight1_w:
    "Sample" "I WON EVERYTHING"
    #return

label fight1_l:
    "Sample" "I LOST EVERYTHING"
    #return
    
label fight1_d:
    "Sample" "I DRAW EVERYTHING"
    #return
    
label standby:
    $ player.chakra += player.stamina * 5
    jump enemymove
    
label enemymove:
    #hide show_damage_p
    #show show_damage_p at Position(xpos=0.75, ypos=200)
    #xpos 0.75
    #ypos 120
    #linear 1.0 ypos 200
    #linear 1.0 alpha 0
    #pause 1.0
    #show show_damage_e at Position(xpos=0.45, ypos=200)
    #xpos 0.45
    #ypos 120
    #linear 1.0 ypos 200
    #linear 1.0 alpha 0
    #pause 1.0
    python:
        if enemy.stunned:
            renpy.say(player.character, "The enemy is stunned and cannot move.")
            enemy.stunned = False
        else:
            if player.counter_state:
                counter_move(player, enemy)
            else:
                enemy_move(player, enemy, clearing)
                #renpy.hide(show_damage_e)
                #renpy.show("show_damage_e", [ Position(xpos=0.45, ypos=200) ], what=show_damage_e)
    #hide show_damage_e
    #show show_damage_e at Position(xpos=0.45, ypos=200)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
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
    
label movemenu:
    call hidetiles
    show screen movemenu
    
screen movemenu:
    
    $ highlight_position(player, enemy, clearing)
    
    for tile in TILES:
        imagebutton idle tile.idle hover tile.hover xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05) action Jump("move{}".format(tile.position))
        text "{}".format(tile.idle.split('.')[0]) xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos + 0.15)
    
label settrap:
    call hidetiles
    hide screen movemenu
    show screen settrap
    player.character "Where should I place the trap?"
    
screen settrap:
    $ highlight_position(player, enemy, clearing)
    
    for tile in TILES:
        imagebutton idle tile.idle hover TILETRAPPIC xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05) action Jump("trap{}".format(tile.position))
    
label move1:
    $ show_player_at_pos(player, enemy, clearing, tile1)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move2:
    $ show_player_at_pos(player, enemy, clearing, tile2)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move3:
    $ show_player_at_pos(player, enemy, clearing, tile3)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move4:
    $ show_player_at_pos(player, enemy, clearing, tile4)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)

label move5:
    $ show_player_at_pos(player, enemy, clearing, tile5)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)

label move6:
    $ show_player_at_pos(player, enemy, clearing, tile6)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move7:
    $ show_player_at_pos(player, enemy, clearing, tile7)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move8:
    $ show_player_at_pos(player, enemy, clearing, tile8)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move9:
    $ show_player_at_pos(player, enemy, clearing, tile9)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move10:
    $ show_player_at_pos(player, enemy, clearing, tile10)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move11:
    $ show_player_at_pos(player, enemy, clearing, tile11)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label move12:
    $ show_player_at_pos(player, enemy, clearing, tile12)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap1:
    $ set_trap_at_pos(player, enemy, clearing, tile1)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap2:
    $ set_trap_at_pos(player, enemy, clearing, tile2)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap3:
    $ set_trap_at_pos(player, enemy, clearing, tile3)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap4:
    $ set_trap_at_pos(player, enemy, clearing, tile4)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap5:
    $ set_trap_at_pos(player, enemy, clearing, tile5)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap6:
    $ set_trap_at_pos(player, enemy, clearing, tile6)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap7:
    $ set_trap_at_pos(player, enemy, clearing, tile7)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap8:
    $ set_trap_at_pos(player, enemy, clearing, tile8)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap9:
    $ set_trap_at_pos(player, enemy, clearing, tile9)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap10:
    $ set_trap_at_pos(player, enemy, clearing, tile10)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap11:
    $ set_trap_at_pos(player, enemy, clearing, tile11)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
label trap12:
    $ set_trap_at_pos(player, enemy, clearing, tile12)
    call fight(player, enemy, tag_p, tag_p, clearing, win_label, lose_label, draw_label)
    
#label movemenu:
    
#    python:
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(1), xpos=TILE1POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(2), xpos=TILE2POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(3), xpos=TILE3POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(4), xpos=TILE4POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(5), xpos=TILE5POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(6), xpos=TILE6POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(7), xpos=TILE7POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(8), xpos=TILE8POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(9), xpos=TILE9POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(10), xpos=TILE10POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(11), xpos=TILE11POS, ypos=TILEYPOS)
#        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(12), xpos=TILE12POS, ypos=TILEYPOS)
#        choice = ui.interact()
        
    #hide playerpic
#    $ show_player_at_pos(player, enemy, clearing, choice)
#    jump fight


