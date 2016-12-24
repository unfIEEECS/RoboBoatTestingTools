import string,time, re

#Definition Validation Functions
class RoboBoatValidator():
    courses = ["courseA","courseB","openTest"]
    teamCodeRegex = r'([a-zA-Z]{2,5})'
    entrances = range(1,4)
    exits = ["x","y","z"]
    shapes = ["cruciform","triangle","circle"]
    dockColors = ["black","red","green","blue"]
    imageIds = []
    buoyColors = ["yellow","black","red","green","blue"]
    frequencyRange = range(25,41)
    timeFormat = "%Y%m%d%H%M%S"
    challenges = ["gates","obstacles","docking","pinger","interop","return"]
    symbolRegex = r'([0-9a-fA-F])'
    @classmethod
    def validateCourse(cls,courseName):
        if(courseName not in cls.courses):
            return False
        return True
    @classmethod
    def validateTeamCode(cls,teamCode):
        if(re.match(cls.teamCodeRegex,teamCode) is None):
            return False
        return True
    @classmethod
    def validateEntrance(cls,entrance):
        if(int(entrance) not in cls.entrances):
            return False
        return True
    @classmethod
    def validateExit(cls,exit):
        if(exit.lower() not in cls.exits):
            return False
        return True
    @classmethod
    def validateSymbol(cls,symbol):
        if(symbol not in cls.shapes):
            return False
        return True
    @classmethod
    def validateDockColor(cls,color):
        if(color.lower() not in cls.dockColors):
            return False
        return True
    @classmethod
    def validateImageId(cls,id):
        if(type(id) != str and id not in cls.imageIds):
            return False
        return True
    @classmethod
    def validateShape(cls,shape):
        if(re.match(cls.symbolRegex,shape) is None):
            return False
        return True
    @classmethod
    def validateBuoyColor(cls,buoyColor):
        if(buoyColor.lower() not in cls.buoyColors):
            return False
        return True
    @classmethod
    def validateFrequency(cls,frequency):
        try:
            print str(cls.frequencyRange)
            if(int(frequency) in cls.frequencyRange):
                return True
        except Exception:
            return False
    @classmethod
    def validateStatus(cls,status):
        if(type(status) is not bool):
            return False
        return True
    @classmethod
    def validateTimestamp(cls,timestamp):
        try:
            time.strptime(timestamp,cls.timeFormat)
            return True
        except Exception:
            return False
    @classmethod
    def validateChallenge(cls,challenge):
        if(challenge.lower() not in cls.challenges):
            return False
        return True
    @classmethod
    def validateLatitudeOrLatitude(cls,degree):
        try:
            float(degree)
            return True
        except Exception:
            return False
    @classmethod
    def addImageId(cls,id):
        cls.imageIds.append(id)