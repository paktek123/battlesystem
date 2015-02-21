##############################################################################
# BATTLE ALLOCATION DEFINITIONS
#

init -6 python:
    
    class Battle:
        def __init__(self, id, good_team=[], bad_team=[], xpos=0, ypos=0):
            self.id = id
            self.good_team = good_team
            self.bad_team = bad_team
            self.xpos = xpos
            self.ypos = ypos
            
        def add_good_member(self, player):
            self.good_team.append(player)
            
        def remove_good_member(self, player):
            self.good_team.remove(player)
            
        def cleanup(self, other_battles):
            """
            This method is required to clean up this race condition 
            where players are being added to other battles for no reason
            """
            iterbattle = [b for b in other_battles if b != self]
            for b in iterbattle:
                for p in b.good_team:
                    if p in self.good_team:
                        b.good_team.remove(p)
            
            
        def clean_dead_members(self):
            for p in self.bad_team:
                if p.hp < 1:
                    self.bad_team.remove(p)
            
            for p in self.good_team:
                if p.hp < 1:
                    self.good_team.remove(p)
                    
        def fight(self, stage, win_label='generic_win', lose_label='generic_win', draw_label='generic_win', fight_limit=20):
            if not self.good_team:
                raise Exception("No good team members")
                
            if not self.bad_team:
                raise Exception("No bad team members")
                
            if len(self.good_team) == 1:
                good_tag = []
            elif len(self.good_team) > 1:
                good_tag = self.good_team[1:]
            else:
                raise Exception("More than 3 members not supported in good team")
                
            if len(self.bad_team) == 1:
                bad_tag = []
            elif len(self.bad_team) > 1:
                bad_tag = self.bad_team[1:]
            else:
                raise Exception("More than 3 members not supported in bad team")
                
                
            renpy.call('fight', self.good_team[0], self.bad_team[0], good_tag, bad_tag, clearing, win_label, lose_label, draw_label, fight_limit)
