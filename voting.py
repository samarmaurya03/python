from datetime import datetime

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = datetime.strptime(dob, '%Y-%m-%d')
    
    def is_eligible_to_vote(self):
        today = datetime.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age >= 18
        