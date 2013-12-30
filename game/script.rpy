# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define naruto_c = Character('Naruto',color="#FFFF00") 
define sasuke_c = Character('Sasuke', color="#3399FF")
image bg = im.Scale("bg.jpg", 800, 600)
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



init:
    $ bob_points = 0 # this is a variable for bob's affection points throughout your game
    $ larry_points = 0 # this is a variable for larry's affection points throughout your game 
    $ bob_max = 10 # this variable should be set to bob's maximum affection points
    $ larry_max = 10 # this variable should be set to larry's maximum affection points
    $ variable = False # when false, the affection screen button doesn't appear on the screen
    
    $ current_skill = None
    
    image playerpic = im.Scale("player.png", 40, 50)
    image enemypic = im.Scale("enemy.png", 40, 50)
    
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
    
    
    class Limb:
        def __init__(self, name):
            self.name = name
            self.bleeding = False
            self.crippled = False
            self.cripple_count = 0
            
        def bleed(self):
            self.bleeding = True
            self.cripple_count += 1
            
        def stop_bleeding(self):
            self.bleeding = False
            
        def cripple(self):
            if self.cripple_count > 5:
                self.cripple = True
            
    limb_head = Limb('head')
    limb_torso = Limb('torso')
    limb_left_arm = Limb('left arm')
    limb_right_arm = Limb('right arm')
    limb_left_leg = Limb('left leg')
    limb_right_leg = Limb('right leg')
    
    LIMBS = [limb_head, limb_torso, limb_left_arm, limb_right_arm, limb_left_leg, limb_right_leg]
    
    class Player:
        def __init__(self, name, picname, character, tilepic, hudpic, hp, maxhp, chakra, maxchakra, 
                     strength, speed, evasion, defence, stamina, base_hit_rate, tile, facing,
                     taiskills=[], ninskills=[], genskills=[], items=[], defensiveskills=[], bloodlineskills=[]):
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
            self.tile = tile # position 
            self.facing = facing
            self.taiskills = taiskills
            self.ninskills = ninskills
            self.genskills = genskills
            self.items = items
            self.defensiveskills = defensiveskills
            self.bloodlineskills = bloodlineskills
            self.action_counter = 0
            self.battlescreen = None
            self.stunned = False
            self.counter_state = False
            self.head = limb_head
            self.torso = limb_torso
            self.left_arm = limb_left_arm
            self.right_arm = limb_right_arm
            self.left_leg = limb_left_leg
            self.right_leg = limb_right_leg
            self.limbs = [self.head, self.torso, self.left_arm, self.right_arm, self.left_leg, self.right_leg]
            self.blood = 100
            self.max_blood = 100
            self.damage_reduction = False
            self.chakra_defence = False
            self.reflect = False
            self.dampen = False
            self.ignore_damage = False
            
        def change_direction(self, direction):
            if direction == 'left':
                self.tilepic = im.Flip(self.tilepic, horizontal=True)
            
        def is_bleeding(self):
            for limb in self.limbs:
                if limb.bleeding:
                    return True
            return False
            
        def bleeding_limbs_count(self):
            bad_limbs = [limb for limb in self.limbs if limb.bleeding]
            return len(bad_limbs)
                
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
        def __init__(self, name, skill_type, label, range, tech, chakra_cost=0, damage=0, stun=False, duration=None):
            self.name = name
            self.skill_type = skill_type
            self.label = label
            self.range = range
            self.tech = tech
            self.chakra_cost = chakra_cost
            self.damage = damage 
            self.stun = stun
            self.duration = duration
            
        def action(self, player, enemy):
            if self.hit_successful(player, enemy):
                renpy.say(player.character, "{}".format(self.name))
                enemy.hp -= (self.damage - enemy.defence)
                player_bleed(enemy)
            else:
                renpy.say(player.character, "{} dodges my attack.".format(enemy.name))
                
            player.chakra -= self.chakra_cost
            self.tech += 1
            return
           
        def hit_successful(self, player, enemy):
            hit_rate = player.base_hit_rate + self.tech - (enemy.evasion * enemy.speed)
            #renpy.say(player.character, "Hit rate is {}".format(hit_rate))
            if renpy.random.randint(1, 100) <= hit_rate:
                return True
            else:
                return False
                
        def stun(self, player, enemy):
            enemy.stunned = True
            return 
    
    # tai skills
    onetwocombo = Skill('One Two Combo', 'tai', "onetwocombo", 5, 1, 5, 10)
    lioncombo = Skill('Lion Combo', 'tai', "lioncombo", 5, 2, 10, 20)
    
    # nin skills
    rasengan = Skill('Rasengan', 'nin', "rasengan", 10, 1, 35, 30)
    chidori = Skill('Chidori', 'nin', "chidori", 10, 1, 35, 30)
    raikiri = Skill('Raikiri', 'nin', "raikiri", 10, 1, 50, 50)
    
    # gen skills # replace with something new
    substitution = Skill('Substitution', 'gen', "substitution", 8, 20, 15, 0, stun=True)
    
    # tool skills
    shiruken = Skill('Shiruken', 'tool', "shiruken", 12, 7, 2, 20)
    kunai = Skill('Kunai', 'tool', "kunai", 12, 4, 3, 20)
    trap = Skill('Trap', 'tool', "trap", 3, 1, 2, 30)
    
    # defensive skills
    damage_reduction = Skill('Focus', 'defence', 'damagereduction', 12, 1, 10, duration=2)
    chakra_defence = Skill('Chakra Defence', 'defence', 'chakradefence', 12, 2, 15, duration=3)
    substitution = Skill('Substitution', 'defence', "substitution", 8, 20, 15, 0, stun=True)
    reflect = Skill('Reflect', 'defence', 'reflect', 12, 20, 20, duration=2)
    dampen = Skill('Dampen', 'defence', 'dampen', 6, 30, 30, duration=3)
    yata_mirror = Skill('Yata Mirror', 'defence', 'yatamirror', 12, 50, 50, duration=2)
    
    player = Player('Naruto', "playerpic", naruto_c, Image('player.png'), None, 100, 100, 80, 80, 10, 4, 3, 4, 5, 80, tile1, 'right', 
                    [onetwocombo, lioncombo], [rasengan, chidori], [substitution], [shiruken, kunai, trap], 
                    [damage_reduction, chakra_defence, reflect, dampen, yata_mirror])
    enemy = Player('Sasuke', "enemypic", sasuke_c, Image('enemy.png'), None, 200, 200, 150, 150, 20, 6, 3, 6, 4, 80, tile12, 'left',
                    [onetwocombo, lioncombo, shiruken, kunai], [chidori], [], [damage_reduction, chakra_defence, reflect, dampen, yata_mirror])
    
    clearing = Stage('Clearing', 1, 1)
    
    def highlight_position(player, enemy):
        for tile in TILES:
            if not tile.trap:
                tile.deactivate()
            
        player.tile.activate()
        renpy.show(player.picname, [ POSITIONS[player.tile.position] ])
        enemy.tile.activate()
        renpy.show(enemy.picname, [ POSITIONS[enemy.tile.position] ])
    
    def show_player_at_pos(player, enemy, stage, tile, initial_movement=False):
        
        difference = abs(player.tile.position - tile.position)
        player.tile.deactivate()
        player.tile = tile
        player.tile.activate()
        
        if player.tile.position < enemy.tile.position:
            player.facing = 'right'
        else:
            player.facing = 'left'
            player.change_direction(player.facing)
            
        if not initial_movement:
            player.chakra -= (stage.remove_chakra() + (difference * stage.pull))
            
        renpy.show(player.picname, [ POSITIONS[tile.position] ])
        
        # Handle traps
        if tile.trap:
            renpy.say(player.character, "Oh no there is a trap here!")
            player.hp -= 30
            remove_trap(tile)
        
    def enemy_move(player, enemy, stage):
        skills = enemy.ninskills + enemy.taiskills # add more here
        skill_index = renpy.random.randint(0, (len(skills) - 1))
        current_skill = skills[skill_index]
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
        
        # bleeding
        player_bleed(player)
        
        # trap
        if enemy.tile.trap:
            renpy.say(player.character, "You got stuck in my trap!")
            renpy.say(enemy.character, "Oh no!")
            enemy.hp -= 30
            remove_trap(enemy.tile)
            
        Jump("fight")
        
    def player_bleed(player):
        if player.hp < (0.5 * player.maxhp):
            if renpy.random.randint(1,2) > 1:
                limb_index = renpy.random.randint(0, len(player.limbs) - 1)
                limb = player.limbs[limb_index]
                renpy.say(player.character, "No my {} is bleeding".format(limb.name))
                if not limb.bleeding:
                    limb.bleed()
        
    def drain_blood(player):
        if player.is_bleeding():
            player.blood -= player.bleeding_limbs_count() * (5 + renpy.random.randint(0, 2))
            renpy.say(player.character, "I need to end this soon, I am loosing too much blood.")
        
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
                        
screen taiactions:
    vbox:
        for skill in player.taiskills:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
            else:
                textbutton "[skill.name]" xpos 0.6
        
screen ninactions:
    vbox:
        for skill in player.ninskills:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
            else:
                textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
        
screen genactions:
    vbox:
        for skill in player.genskills:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
            else:
                textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
                
screen itemselection:
    vbox:
        for skill in player.items:
            if skill.range >= abs(player.tile.position - enemy.tile.position):
                textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6
            else:
                textbutton "[skill.name]" action Jump(skill.label)  xpos 0.6

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
    
label damage_reduction:
    $ player.damage_reduction = True
    jump enemymove
    
label chakra_defence:
    $ player.chakra_defence = True
    jump enemymove
    
label reflect:
    $ player.reflect = True
    jump enemymove
    
label dampen:
    $ enemy.dampen = True
    jump enemymove
    
label yatamirror:
    $ player.ignore_damage = True
    jump enemymove

screen battlemenu(player):
    vbox:
        textbutton "Tai" action [Hide("ninactions"), Hide("genactions"), Hide("movemenu"), Hide("itemselection"), Hide("teamactions"), Show("taiactions")]
        textbutton "Nin" action [Hide("taiactions"), Hide("genactions"), Hide("movemenu"), Hide("itemselection"), Hide("teamactions"), Show("ninactions")]
        textbutton "Gen" action [Hide("ninactions"), Hide("taiactions"), Hide("movemenu"), Hide("itemselection"), Hide("teamactions"), Show("genactions")]
        textbutton "Move" action [Hide("ninactions"), Hide("genactions"), Hide("taiactions"), Hide("itemselection"), Hide("teamactions"), Show("movemenu")]
        textbutton "Items" action [Hide("ninactions"), Hide("genactions"), Hide("movemenu"), Show("itemselection"), Hide("teamactions"), Hide("taiactions")]
        textbutton "Defence" action [Hide("ninactions"), Hide("genactions"), Hide("movemenu"), Hide("itemselection"), Show("teamactions"), Hide("taiactions")]
        textbutton "Standby" action Jump("standby")
        
screen battlebars:
    #frame:
        #has vbox 

    text "[player.name]" xpos 0.5 ypos 0.15
    text "[player.chakra]" xpos 0.49 ypos 0.45
    text "[player.hp]" xpos 0.55 ypos 0.45
    vbar value player.chakra range player.maxchakra xpos 0.5 ypos 0.2 ymaximum 150
    vbar value player.hp range player.maxhp xpos 0.55 ypos 0.2 ymaximum 150
    
    if player.is_bleeding():
        text "blood" vertical True xpos 0.40 ypos 0.2
        vbar value player.blood range player.max_blood xpos 0.45 ypos 0.2 ymaximum 150
    
    text "[enemy.name]" xpos 0.65 ypos 0.15
    text "[enemy.chakra]" xpos 0.64 ypos 0.45
    text "[enemy.hp]" xpos 0.70 ypos 0.45
    vbar value enemy.hp range enemy.maxhp xpos 0.7 ypos 0.2 ymaximum 150
    vbar value enemy.chakra range enemy.maxchakra xpos 0.66 ypos 0.2 ymaximum 150
    
    if enemy.is_bleeding():
        text "blood" vertical True xpos 0.78 ypos 0.2
        vbar value enemy.blood range enemy.max_blood xpos 0.74 ypos 0.2 ymaximum 150

    
label start:
    with None
    jump fight
    
label fight:
    scene bg
    
    call showtiles
    hide screen movemenu
    hide screen settrap
    # initial position
    $ highlight_position(player, enemy)
    #$ show_player_at_pos(player, enemy, clearing, player.tile, initial_movement=True)
    
    $ drain_blood(player)
    $ drain_blood(enemy)
    show screen battlemenu(player)
    show screen battlebars
    
    python:
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(1), xpos=1000, ypos=1000)
        choice = ui.interact()
    
    "Tiger" "Gao gao! You're strong!"
    "Sample" "Sample...."
    
    call movemenu
    
label standby:
    $ player.chakra += player.stamina * 5
    jump enemymove
    
label enemymove:
    python:
        if enemy.stunned:
            renpy.say(player.character, "The enemy is stunned and cannot move.")
            enemy.stunned = False
        else:
            if player.counter_state:
                counter_move(player, enemy)
            else:
                enemy_move(player, enemy, clearing)
    jump fight
    
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
    
    $ highlight_position(player, enemy)
    
    for tile in TILES:
        imagebutton idle tile.idle hover tile.hover xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05) action Jump("move{}".format(tile.position))
        text "{}".format(tile.idle.split('.')[0]) xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos + 0.15)
    
label settrap:
    call hidetiles
    hide screen movemenu
    show screen settrap
    player.character "Where should I place the trap?"
    
screen settrap:
    $ highlight_position(player, enemy)
    
    for tile in TILES:
        imagebutton idle tile.idle hover TILETRAPPIC xpos (tile.pos.xpos - 25) ypos (tile.pos.ypos - 0.05) action Jump("trap{}".format(tile.position))
    
label move1:
    $ show_player_at_pos(player, enemy, clearing, tile1)
    jump fight
    
label move2:
    $ show_player_at_pos(player, enemy, clearing, tile2)
    jump fight
    
label move3:
    $ show_player_at_pos(player, enemy, clearing, tile3)
    jump fight
    
label move4:
    $ show_player_at_pos(player, enemy, clearing, tile4)
    jump fight

label move5:
    $ show_player_at_pos(player, enemy, clearing, tile5)
    jump fight

label move6:
    $ show_player_at_pos(player, enemy, clearing, tile6)
    jump fight
    
label move7:
    $ show_player_at_pos(player, enemy, clearing, tile7)
    jump fight
    
label move8:
    $ show_player_at_pos(player, enemy, clearing, tile8)
    jump fight
    
label move9:
    $ show_player_at_pos(player, enemy, clearing, tile9)
    jump fight
    
label move10:
    $ show_player_at_pos(player, enemy, clearing, tile10)
    jump fight
    
label move11:
    $ show_player_at_pos(player, enemy, clearing, tile11)
    jump fight
    
label move12:
    $ show_player_at_pos(player, enemy, clearing, tile12)
    jump fight
    
label trap1:
    $ set_trap_at_pos(player, enemy, clearing, tile1)
    jump fight
    
label trap2:
    $ set_trap_at_pos(player, enemy, clearing, tile2)
    jump fight
    
label trap3:
    $ set_trap_at_pos(player, enemy, clearing, tile3)
    jump fight
    
label trap4:
    $ set_trap_at_pos(player, enemy, clearing, tile4)
    jump fight
    
label trap5:
    $ set_trap_at_pos(player, enemy, clearing, tile5)
    jump fight
    
label trap6:
    $ set_trap_at_pos(player, enemy, clearing, tile6)
    jump fight
    
label trap7:
    $ set_trap_at_pos(player, enemy, clearing, tile7)
    jump fight
    
label trap8:
    $ set_trap_at_pos(player, enemy, clearing, tile8)
    jump fight
    
label trap9:
    $ set_trap_at_pos(player, enemy, clearing, tile9)
    jump fight
    
label trap10:
    $ set_trap_at_pos(player, enemy, clearing, tile10)
    jump fight
    
label trap11:
    $ set_trap_at_pos(player, enemy, clearing, tile11)
    jump fight
    
label trap12:
    $ set_trap_at_pos(player, enemy, clearing, tile12)
    jump fight
    
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


