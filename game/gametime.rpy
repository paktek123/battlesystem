##############################################################################
# GAMETIME DEFINITIONS
#

init -9 python:
    import random
    import copy
    class GameTime:
        def __init__(self, hour, day, month, year):
            self.minute = 5
            self.hour = hour
            self.day = day
            self.month = month
            self.year = year
            self.months = ["Stub", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
            self.counter = 0
            self.current_time = self.now()
            
        def now(self):
            if self.counter == 2:
                self.counter = 0
                self.advance_time(minutes=1)
            else:
                self.counter += 1
            return "{}:{} {} {} {}".format(str(self.hour).zfill(2), str(self.minute).zfill(2), self.day, self.months[self.month], self.year)
            
        def dawn(self):
            minute = random.randint(0, 59)
            self.hour = random.randint(1,5)
            return "{0}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def morning(self):
            minute = random.randint(0, 59)
            self.hour = random.randint(6,11)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def afternoon(self):
            minute = random.randint(0, 59)
            self.hour = random.randint(12,17)
            return "{}:} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def evening(self):
            minute = random.randint(0, 59)
            self.hour = random.randint(18,20)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def night(self):
            minute = random.randint(0, 59)
            self.hour = random.randint(21,0)
            return "{}:{} {} {} {}".format(self.hour, minute, self.day, self.months[self.month], self.year)
            
        def next_month(self):
            if self.month > 11:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
            
        def next_day(self):
            if self.day > 29:
                self.next_month()
                self.day = 1
            else:
                self.day += 1
                
        def next_hour(self):
            if self.hour > 23:
                self.next_day()
                self.hour = 1
            else:
                self.hour += 1
                
        def next_minute(self):
            if self.minute > 59:
                self.next_hour()
                self.minute = 1
            else:
                self.minute += 1
                
        def advance_time(self, minutes=0, hours=0, days=0, months=0, years=0):
            
            #renpy.say(current_session.player.character, "{} {} {}".format(hours, days, months))
            
            if minutes:
                while minutes > 0:
                    minutes -= 1
                    self.next_minute()
            
            if hours:
                while hours > 0:
                    hours -= 1
                    self.next_hour()
            
            if days:
                while days > 0:
                    days -= 1
                    self.next_day()
                
            if months:
                while months > 0:
                    months -= 1
                    self.next_month()
                    
            self.current_time = self.now()
            
    class Month:
        def __init__(self, number, days=[]):
            self.number = number 
            self.days = []
            
        def __repr__(self):
            return "Month: {}".format(self.number)
            
    class Day:
        def __init__(self, number, month, events=[]):
            self.number = number
            self.events = events
            self.month = month
            
        def parse_events(self):
            if self.events:
                names = [e.small_name for e in self.events]
                return ', '.join(names)
            else:
                return ' '
            
        def __repr__(self):
            return "Day: {}".format(self.number)