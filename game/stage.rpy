##############################################################################
# STAGE DEFINITIONS
#

init -3 python:
    class Stage:
        def __init__(self, name, pull, range):
            self.name = name
            self.pull = pull
            self.range = range
            
        def remove_chakra(self):
            return self.pull + renpy.random.randint(-1, self.range)