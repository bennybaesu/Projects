class Team:
    def __init__(self):
        self.city = " "
        self.name = " "
        self.division = " "
        self.conference = " "
        self.stadium = " "
        self.stadiumLocation = " "
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.divisionWins = 0
        self.divisionLosses = 0
        self.divisionTies = 0
        self.pointsScored = 0
        self.pointsAllowed = 0

    def __init__(self, city, name, division, conference, stadium, stadiumLocation, wins, losses, ties, divisionWins,
                 divisionLosses, divisionTies, pointsScored, pointsAllowed):
        self.city = city
        self.name = name
        self.division = division
        self.conference = conference
        self.stadium = stadium
        self.stadiumLocation = stadiumLocation
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.divisionWins = divisionWins
        self.divisionLosses = divisionLosses
        self.divisionTies = divisionTies
        self.pointsScored = pointsScored
        self.pointsAllowed = pointsAllowed

    def setCity(self, city):
        self.city = city

    def setName(self, name):
        self.name = name

    def setDivision(self, division):
        self.division = division

    def setConference(self, conference):
        self.conference = conference

    def setStadium(self, stadium):
        self.stadium = stadium

    def setStadiumLocation(self, location):
        self.stadiumLocation = location

    def setWins(self, wins):
        self.wins = wins

    def setLosses(self, losses):
        self.losses = losses

    def setTies(self, ties):
        self.ties = ties

    def setDivisionWins(self, wins):
        self.divisionWins = wins

    def setDivisionLosses(self, losses):
        self.divisionLosses = losses

    def setDivisionTies(self, ties):
        self.divisionTies = ties

    def setPointsAllowed(self, pa):
        self.pointsAllowed = pa

    def setPointsScored(self, ps):
        self.pointsScored = ps

    def getCity(self):
        return self.city

    def getName(self):
        return self.name

    def getDivision(self):
        return self.division

    def getConference(self):
        return self.conference

    def getStadium(self):
        return self.stadium

    def getStadiumLocation(self):
        return self.stadiumLocation

    def getWins(self):
        return self.wins

    def getLosses(self):
        return self.losses

    def getTies(self):
        return self.ties

    def getDivisionWins(self):
        return self.divisionWins

    def getDivisionLosses(self):
        return self.divisionLosses

    def getDivisionTies(self):
        return self.divisionTies

    def getPointsScored(self):
        return self.pointsScored

    def getPointsAllowed(self):
        return self.pointsAllowed

    def appendWin(self):
        self.wins += 1

    def appendLoss(self):
        self.losses += 1

    def appendTie(self):
        self.ties += 1

    def appendDivisionWin(self):
        self.divisionWins += 1

    def appendDivisionLoss(self):
        self.divisionLosses += 1

    def appendDivisionTie(self):
        self.divisionTies += 1

    def appendPointsScored(self, points):
        self.pointsScored += points

    def appendPointsAllowed(self, points):
        self.pointsAllowed += points
