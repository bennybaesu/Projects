from Team import *


class Game:
    def __init__(self):
        self.homeTeam = Team()  # TODO - Set to a certain team
        self.awayTeam = Team()  # TODO - Set to a certain team
        self.homeTeamScore = 0
        self.awayTeamScore = 0

    def setHomeTeam(self, team):
        self.homeTeam = team

    def setAwayTeam(self, team):
        self.awayTeam = team

    def setHomeTeamScore(self, score):
        self.homeTeamScore = score

    def setAwayTeamScore(self, score):
        self.awayTeamScore = score

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getHomeTeamScore(self):
        return self.homeTeamScore

    def getAwayTeamScore(self):
        return self.awayTeamScore
