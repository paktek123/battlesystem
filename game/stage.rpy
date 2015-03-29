##############################################################################
# STAGE DEFINITIONS
#

init -3 python:
    class Stage:
        def __init__(self, name, pull, range, 
                     base_texture="tile.png", active_texture="tileh.png", project_texture="tilep.png", trap_texture="tiletrap.png"):
            self.name = name
            self.pull = pull
            self.range = range
            self.base_texture = base_texture
            self.active_texture = active_texture
            self.project_texture = project_texture
            self.trap_texture = trap_texture
            self.tiles = []
            self.tile1 = Tile(1, tile1pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile2 = Tile(2, tile2pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile3 = Tile(3, tile3pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile4 = Tile(4, tile4pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile5 = Tile(5, tile5pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile6 = Tile(6, tile6pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile7 = Tile(7, tile7pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile8 = Tile(8, tile8pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile9 = Tile(9, tile9pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile10 = Tile(10, tile10pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile11 = Tile(11, tile11pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile12 = Tile(12, tile12pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, 
                          self.tile7, self.tile8, self.tile9, self.tile10, self.tile11, self.tile12]
            
            #self.populate_tiles()
            
        def populate_tiles(self):
            self.tile1 = Tile(1, tile1pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile2 = Tile(2, tile2pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile3 = Tile(3, tile3pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile4 = Tile(4, tile4pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile5 = Tile(5, tile5pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile6 = Tile(6, tile6pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile7 = Tile(7, tile7pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile8 = Tile(8, tile8pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile9 = Tile(9, tile9pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile10 = Tile(10, tile10pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile11 = Tile(11, tile11pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
            self.tile12 = Tile(12, tile12pos, self.base_texture, self.active_texture, self.trap_texture, self.project_texture)
    
            self.tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, 
                          self.tile7, self.tile8, self.tile9, self.tile10, self.tile11, self.tile12]
        
            
        def remove_chakra(self):
            return self.pull + renpy.random.randint(-1, self.range)