##############################################################################
# VILLAGE AND LOCATION DEFINITIONS
#

init -6 python:

    NINJA_RANKS = {'genin': range(1, 21), 'chunin': range(21, 31), 'jounin': range(31, 41), 
                   'sannin': range(41, 51), 'kage': range(51, 71), 'legend': range(71, 101)}
    
    import random
    class Village:
        def __init__(self, id, name, leader, marker_xpos, marker_ypos, map, wealth=10000, army=1000, control=100, influence=100, uprising=0, 
                     locations=None, village_tag='', mission_locations=1):
            self.id = id
            self.name = name
            self.leader = leader
            self.army = army
            self.wealth = wealth
            self. wealth_original = wealth
            self.marker_xpos = marker_xpos
            self.marker_ypos = marker_ypos
            self.marker_position = Position(xpos=marker_xpos, ypos=marker_ypos)
            self.map = map
            self.control = control
            self.influence = influence
            self.uprising = uprising
            self.control_change = 0
            self.influence_change = 0
            self.wealth_change = 0
            self.locations = locations
            self.genins = []
            self.chunins = []
            self.jounins = []
            self.sannins = []
            self.mission_locations = ["{}_{}".format(village_tag, x) for x in range(1,mission_locations+1)]

        def add_to_ninja_ranks(self, player):
            for rank, level_range in NINJA_RANKS.iteritems():
                if player.level in level_range:
                    village_ranks = getattr(self, "{}s".format(rank))
                    village_ranks.append(player)
                    setattr(self, "{}s".format(rank), village_ranks)
                    
        def update_ninja_ranks(self, player):
            self.genins = [g for g in self.genins if g != player]
            self.chunins = [g for g in self.chunins if g != player]
            self.jounins = [g for g in self.jounins if g != player]
            self.sannins = [g for g in self.sannins if g != player]
            
            village_ranks = getattr(self, "{}s".format(player.ninja_rank()))
            village_ranks.append(player)
            setattr(self, "{}s".format(player.ninja_rank()), village_ranks)

        def random_mission_location(self):
            return random.choice(self.mission_locations)

        def update_wealth(self):
            self.wealth += self.wealth_change
            
        def random_wealth_event(self):
            change = renpy.random.randint(-1000, 1000)
            add_say = ["Many pull requests merged", "New functionality added", "QA are feeling generous", "Upgrade to latest software", "Not much bad code",
                       "Code health is improving", "Everybody is coding better", "Other teams are helping us better", "Faster team efforts"]
            minus_say = ["Pull requests rejected", "No functionality added", "QA are angry today", "The QA guy went to play football", 
                         "Team members are getting lazy", "Everybody was playing pool all day", "The team is slacking", "Code retreat"]
            self.wealth_original = self.wealth
            self.wealth += change
            self.wealth_change = change

            if self.wealth_change < 0:
                sign = "-"
            else:
                sign = "+"

            change_say = " {color=#000}Code Q: %s %s %s = %s{/color}" %(self.wealth_original, sign, abs(self.wealth_change), self.wealth) 
            if change < 0:
                renpy.say(self.leader, minus_say[renpy.random.randint(0, len(minus_say) - 1)] + " " + change_say)
            else:
                renpy.say(self.leader, add_say[renpy.random.randint(0, len(add_say) - 1)] + " " + change_say)
            
            
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
            #self.random_control_event()
            #self.random_influence_event()
            
        def __repr__(self):
            return "<Village>: {}".format(self.name)
            
    class Location:
        def __init__(self, name, label, background=None, events=[], map_pic_idle=None, map_pic_hover=None, npc=[], visits=0):
            self.name = name
            self.label = label
            self.background = background
            #self.village = village
            self.events = events
            self.map_pic_idle = map_pic_idle
            self.map_pic_hover = map_pic_hover
            self.npc = npc
            self.visits = visits
            self.unlocked = False
            
        def interact(self, player, village):
            renpy.call(self.label, player, village)
            
    import math
    def time_between_village(village1, village2):
        distance = math.sqrt( (village1.marker_xpos - village2.marker_xpos)**2 + (village1.marker_ypos - village2.marker_ypos)**2 )
        time_weeks = abs(distance / 0.1)
        days = time_weeks * 7
        return int(days/4)
        
    
            