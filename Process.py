class Process:
    def __init__(self, name, burst, arrival = 0, priority = 0 ):
        self.name = name
        self.burst = burst
        self.progress = 0
        self.arrival = arrival
        self.priority = priority
        self.totalTurnAround = 0
        self.totalResponse = 0
        self.complete = False
        self.activatedOnce = False
        # self.totalWait=0
    
    def getTotalWait(self):
        return self.totalTurnAround-self.burst
