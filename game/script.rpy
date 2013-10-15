# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
image bg = im.Scale("bg.jpg", 800, 600)
image tile1 = im.Scale("tile.png", 50, 30)
image tile2 = im.Scale("tile.png", 50, 30)
image tile3 = im.Scale("tile.png", 50, 30)
image tile4 = im.Scale("tile.png", 50, 30)
image tile5 = im.Scale("tile.png", 50, 30)
image tile6 = im.Scale("tile.png", 50, 30)
image tile7 = im.Scale("tile.png", 50, 30)
image tile8 = im.Scale("tile.png", 50, 30)
image tile9 = im.Scale("tile.png", 50, 30)
image tile10 = im.Scale("tile.png", 50, 30)
image tile11 = im.Scale("tile.png", 50, 30)
image tile12 = im.Scale("tile.png", 50, 30)



init:
    $ bob_points = 0 # this is a variable for bob's affection points throughout your game
    $ larry_points = 0 # this is a variable for larry's affection points throughout your game 
    $ bob_max = 10 # this variable should be set to bob's maximum affection points
    $ larry_max = 10 # this variable should be set to larry's maximum affection points
    $ variable = False # when false, the affection screen button doesn't appear on the screen
    
    $ current_skill = None
    
    image playerpic = im.Scale("player.png", 40, 50)
    image enemypic = im.Scale("enemy.png", 40, 50)
    
    $ TILE1POS = 100
    $ TILE2POS = 150
    $ TILE3POS = 200
    $ TILE4POS = 250
    $ TILE5POS = 300
    $ TILE6POS = 350
    $ TILE7POS = 400
    $ TILE8POS = 450
    $ TILE9POS = 500
    $ TILE10POS = 550
    $ TILE11POS = 600
    $ TILE12POS = 650
    
    $ TILEYPOS = 0.5
    $ PLAYERYPOS = 0.5
    
    # Positions
    $ tile1pos = Position(xpos=TILE1POS+25, ypos=TILEYPOS)
    $ tile2pos = Position(xpos=TILE2POS+25, ypos=TILEYPOS)
    $ tile3pos = Position(xpos=TILE3POS+25, ypos=TILEYPOS)
    $ tile4pos = Position(xpos=TILE4POS+25, ypos=TILEYPOS)
    $ tile5pos = Position(xpos=TILE5POS+25, ypos=TILEYPOS)
    $ tile6pos = Position(xpos=TILE6POS+25, ypos=TILEYPOS)
    $ tile7pos = Position(xpos=TILE7POS+25, ypos=TILEYPOS)
    $ tile8pos = Position(xpos=TILE8POS+25, ypos=TILEYPOS)
    $ tile9pos = Position(xpos=TILE9POS+25, ypos=TILEYPOS)
    $ tile10pos = Position(xpos=TILE10POS+25, ypos=TILEYPOS)
    $ tile11pos = Position(xpos=TILE11POS+25, ypos=TILEYPOS)
    $ tile12pos = Position(xpos=TILE12POS+25, ypos=TILEYPOS)
    
    # Player positon on tiles
    $ player1pos = Position(xpos=TILE1POS+25, ypos=PLAYERYPOS)
    $ player2pos = Position(xpos=TILE2POS+25, ypos=PLAYERYPOS)
    $ player3pos = Position(xpos=TILE3POS+25, ypos=PLAYERYPOS)
    $ player4pos = Position(xpos=TILE4POS+25, ypos=PLAYERYPOS)
    $ player5pos = Position(xpos=TILE5POS+25, ypos=PLAYERYPOS)
    $ player6pos = Position(xpos=TILE6POS+25, ypos=PLAYERYPOS)
    $ player7pos = Position(xpos=TILE7POS+25, ypos=PLAYERYPOS)
    $ player8pos = Position(xpos=TILE8POS+25, ypos=PLAYERYPOS)
    $ player9pos = Position(xpos=TILE9POS+25, ypos=PLAYERYPOS)
    $ player10pos = Position(xpos=TILE10POS+25, ypos=PLAYERYPOS)
    $ player11pos = Position(xpos=TILE11POS+25, ypos=PLAYERYPOS)
    $ player12pos = Position(xpos=TILE12POS+25, ypos=PLAYERYPOS)
    
    $ player1currentpos = 1
    $ enemy1currentpos = 12


init python:
    
    class Player:
        def __init__(self, name, picname, tilepic, hudpic, hp, maxhp, chakra, maxchakra, 
                     strength, speed, evasion, defence, stamina, position, facing,
                     taiskills=[], ninskills=[], genskills=[], items=[], teamskills=[], bloodlineskills=[]):
            self.name = name
            self.picname = picname
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
            self.position = position
            self.facing = facing
            self.taiskills = taiskills
            self.ninskills = ninskills
            self.genskills = genskills
            self.items = items
            self.teamskills = teamskills
            self.bloodlineskills = bloodlineskills
            
        def change_direction(self, direction):
            if direction == 'left':
                self.tilepic = im.Flip(self.tilepic, horizontal=True)
                
        def __repr__(self):
            return "<Player>: {}".format(self.name)
            
    class Skill:
        def __init__(self, name, skill_type, damage=0, stun=False):
            self.name = name
            self.skill_type = skill_type
            self.damage = damage 
            self.stun = stun
            
        def action(self, player, enemy):
            enemy.hp -= 20
            #renpy.say(e, "{} lost 20 hp, his hp is now {}".format(enemy.name, enemy.hp))
            #ui.close()
            
            #renpy.jump("fight")
            
    #renpy.image('playerpic', Image('player.png'))
    #renpy.image('enemypic', Image('enemy.png'))
    
    # tai skills
    onetwocombo = Skill('One Two Combo', 'tai', 10)
    lioncombo = Skill('Lion Combo', 'tai', 20)
    
    # nin skills
    rasengan = Skill('Rasengan', 'nin', 30)
    chidori = Skill('Chidori', 'nin', 30)
    raikiri = Skill('Raikiri', 'nin', 50)
    
    # gen skills
    substitution = Skill('Substitution', 'gen', 0, stun=True)
    
    # tool skills
    shiruken = Skill('Shiruken', 'tool', 20)
    kunai = Skill('Kunai', 'tool', 20)
    
    player = Player('Naruto', "playerpic", Image('player.png'), None, 100, 100, 80, 80, 10, 4, 3, 4, 5, 1, 'right', 
                    [onetwocombo, lioncombo], [rasengan], [substitution], [])
    enemy = Player('Kabuto', "enemypic", Image('enemy.png'), None, 200, 200, 150, 150, 20, 6, 3, 6, 4, 12, 'left')
    
    def show_player_at_pos(player, enemy, value):
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
        #renpy.say(e, "I say this %s" %)
        player.position = value
        
        if player.position < enemy.position:
            player.facing = 'right'
        else:
            player.facing = 'left'
            player.change_direction(player.facing)
            
        #renpy.say(e, "I am facing {}".format(player.position))
            
        renpy.show(player.picname, [ POSITIONS[value] ])
                        

screen taiactions(player):
    vbox:
        for skill in player.taiskills:
            textbutton skill.name action [skill.action(player, enemy), Jump("doskill")]  xpos 0.4

label doskill:
    e "Hey this is the skill"
    return

screen battlemenu(player):
    vbox:
        textbutton "Tai" action Jump("taiactions")
        textbutton "Nin" action Jump("ninactions")
        textbutton "Gen" action Jump("genactions")
        textbutton "Move" action Jump("movemenu")
        textbutton "Items" action Jump("itemselection")
        textbutton "Team" action Jump("teamactions")
        
screen battlebars:
    #frame:
        #has vbox 

    text "[player.name]" xpos 0.5 ypos 0.15
    text "[player.chakra]" xpos 0.49 ypos 0.45
    text "[player.hp]" xpos 0.55 ypos 0.45
    vbar value player.hp range player.maxhp xpos 0.5 ypos 0.2 ymaximum 150
    vbar value player.chakra range player.maxchakra xpos 0.55 ypos 0.2 ymaximum 150
    
    text "[enemy.name]" xpos 0.65 ypos 0.15
    text "[enemy.chakra]" xpos 0.64 ypos 0.45
    text "[enemy.hp]" xpos 0.70 ypos 0.45
    vbar value enemy.hp range enemy.maxhp xpos 0.7 ypos 0.2 ymaximum 150
    vbar value enemy.chakra range enemy.maxchakra xpos 0.66 ypos 0.2 ymaximum 150
        
        
        


label taiactions:
    hide screen battlemenu
    show screen taiactions(player)
    

label start:
    with None
    jump fight
    
label fight:
    scene bg
    
    show screen battlemenu(player)
    show screen battlebars
    
    "Tiger" "Gao gao! You're strong!"
    "Sample" "Sample...."
    
    call movemenu
    
label showplayers:
    #show playerpic at player1pos
    show enemypic at player12pos
    return
    
label showtiles:
    show tile1 at tile1pos
    show tile2 at tile2pos
    show tile3 at tile3pos
    show tile4 at tile4pos
    show tile5 at tile5pos
    show tile6 at tile6pos
    show tile7 at tile7pos
    show tile8 at tile8pos
    show tile9 at tile9pos
    show tile10 at tile10pos
    show tile11 at tile11pos
    show tile12 at tile12pos
    return
    
#label battlemenu:
#    python:
#        ui.textbutton("tile.png", "tileh.png", clicked=ui.returns(1), xpos=TILE1POS, ypos=TILEYPOS)
    
label movemenu:
    call showplayers
    # initial position
    $ show_player_at_pos(player, enemy, player.position)
    python:
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(1), xpos=TILE1POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(2), xpos=TILE2POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(3), xpos=TILE3POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(4), xpos=TILE4POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(5), xpos=TILE5POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(6), xpos=TILE6POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(7), xpos=TILE7POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(8), xpos=TILE8POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(9), xpos=TILE9POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(10), xpos=TILE10POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(11), xpos=TILE11POS, ypos=TILEYPOS)
        ui.imagebutton("tile.png", "tileh.png", clicked=ui.returns(12), xpos=TILE12POS, ypos=TILEYPOS)
        choice = ui.interact()
        
    #hide playerpic
    $ show_player_at_pos(player, enemy, choice)
    jump movemenu


