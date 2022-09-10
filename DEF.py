class Microbiology:
    def __init__(self, school, department, matric, mcb201, mcb301):
        self.school = school
        self.department = department
        self.matric = matric
        self.mcb201 = mcb201
        self.mcb301 = mcb301

    def output(self):
        return "my name is Olowolaju tolulope, i attended " + self.school + " and graduated from department of \n" + self.department + " with a matric number of " + self.matric + ". when i was in school then i offered courses like " + self.mcb201 + " and " +self.mcb301
class Secondary(Microbiology):
    def __init__(self, school, department, matric, mcb201, mcb301, bass, ball, fellowship, games):
        super(Secondary, self).__init__(school, department, matric, mcb201, mcb301)
        self.bass = bass
        self.ball = ball
        self.fellowship = fellowship
        self.games = games
    def tbass(self):
            return "Olowolaju Tolulope happens to be the " + self.bass + "in" + self.fellowship + "he also engage himself in some games such as, " + self.games



