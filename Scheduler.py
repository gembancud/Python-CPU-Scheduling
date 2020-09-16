from Process import Process

class Scheduler:
    def __init__(self):
        self.processes = []
        self.totalTime = 0

    def addtoProcess(self, process):
        self.processes.append(process)
        self.totalTime += process.burst

    def clearProcesses(self):
        self.__init__()
    
    def FCFS(self):
        """Calulates the times using First Come First Serve Algorithm
        """
        print("Solving Scheduler using FCFS \n")
        activeproc=None
        print("( ")
        for i in range(self.totalTime):

            # ? VISUAL
            isNewProc= True
            if(activeproc):
                isNewProc = False 
            
            # get the next active proc
            for proc in self.processes:
                if proc.complete:
                    continue
                if not activeproc:
                    activeproc=proc
                elif activeproc.arrival > proc.arrival:
                    activeproc = proc
                activeproc.activatedOnce= True

            # ? VISUAL
            # print(f"{activeproc.name}, ",sep='')
            if(isNewProc):
                print(f"{activeproc.arrival}@{activeproc.name}",end='')
            # else:
            #     print(",",end='')

            #compute processes
            for proc in self.processes:
                if proc is activeproc:
                    proc.progress+=1
                    proc.totalTurnAround+=1
                    if proc.progress == proc.burst:
                        # ? VISUAL
                        print(f", {proc.progress}/{proc.burst} ({i+1}) / ")
                        proc.complete=True
                        activeproc = None
                    continue
                
                if (not proc.complete )and i >= proc.arrival :
                    proc.totalTurnAround+=1
                    # proc.totalWait+=1

                if (not proc.activatedOnce ) and i >= proc.arrival:
                    proc.totalResponse+=1

        # ? VISUAL
        print(")")
        self._Print()

    def RR(self,quantum = 4):
        """Calculates the scheduler using Round Robin Algorithm

        Args:
            quantum (int, optional): Time interval alloted for a single process to run. Defaults to 4.
        """
        print("Solving Scheduler using RR \n")
        print("( ")
        rrCounter = 0
        activeprocPointer= 0
        activeproc=None
        for i in range(self.totalTime):
            if rrCounter == quantum:
                rrCounter=0
                activeprocPointer+=1
                activeproc=None
            rrCounter+=1

            # # ? VISUAL
            isNewProc= True
            if(activeproc):
                isNewProc = False 

            # get the next active proc
            while not activeproc:
                tmpactiveproc = self.processes[activeprocPointer%len(self.processes)]
                if tmpactiveproc.complete:
                    activeprocPointer+=1
                    continue
                activeproc= tmpactiveproc
                activeproc.activatedOnce=True
            
            # # ? VISUAL
            if(isNewProc):
                print(f"{activeproc.arrival}@{activeproc.name}",end='')
            # print(f"{activeproc.name}")

            #compute processes
            for proc in self.processes:
                if proc is activeproc:
                    proc.progress+=1
                    proc.totalTurnAround+=1
                    if proc.progress == proc.burst:
                        # ? VISUAL
                        print(f", {proc.progress}/{proc.burst} ({i+1}) / ")
                        proc.complete=True
                        activeproc = None
                        rrCounter=quantum
                    elif rrCounter == quantum:
                        # ? VISUAL
                        print(f", {proc.progress}/{proc.burst} ({i+1}) / ")
                    continue
                
                if (not proc.complete )and i >= proc.arrival :
                    proc.totalTurnAround+=1
                    # proc.totalWait+=1

                if (not proc.activatedOnce ) and i >= proc.arrival:
                    proc.totalResponse+=1
        # ? VISUAL
        print(")")
        self._Print()

    def SJF_NP(self):
        print("Solving Scheduler using Shortest Job First Non Preemptive \n")
        activeproc=None
        print("( ")
        for i in range(self.totalTime):

            # ? VISUAL
            isNewProc= True
            if(activeproc):
                isNewProc = False 
            
            # get the next active proc
            if not activeproc:
                for proc in self.processes:
                    if proc.complete:
                        continue
                    if not activeproc:
                        activeproc=proc
                        continue
                    if activeproc.burst > proc.burst and i >= proc.arrival:
                        activeproc = proc
                activeproc.activatedOnce= True

            # ? VISUAL
            # print(f"{activeproc.name}")
            if(isNewProc):
                print(f"{activeproc.arrival}@{activeproc.name}",end='')
            # else:
            #     print(",",end='')

            #compute processes
            for proc in self.processes:
                if proc is activeproc:
                    proc.progress+=1
                    proc.totalTurnAround+=1
                    if proc.progress == proc.burst:
                        # ? VISUAL
                        print(f", {proc.progress}/{proc.burst} ({i+1}) / ")
                        proc.complete=True
                        activeproc = None
                    continue
                
                if (not proc.complete )and i >= proc.arrival :
                    proc.totalTurnAround+=1
                    # proc.totalWait+=1

                if (not proc.activatedOnce ) and i >= proc.arrival:
                    proc.totalResponse+=1

        # ? VISUAL
        print(")")
        self._Print()

    def SJF_P(self):
        print("Solving Scheduler using Shortest Job First Preemptive \n")
        activeproc=None
        prevProc= None
        justCompleted=False
        isChangedProc=False
        print("( ")
        for i in range(self.totalTime):

            # ? VISUAL
            isNewProc= True
            if(activeproc):
                isNewProc = False 
            
            # get the next active proc
            for proc in self.processes:
                if proc.complete:
                    continue
                if not activeproc:
                    activeproc=proc
                    isNewProc = True
                    continue
                if (activeproc.burst - activeproc.progress) > proc.burst and i >= proc.arrival:
                    activeproc = proc
                    isChangedProc=True
                    isNewProc = True
                
            activeproc.activatedOnce= True

            # ? VISUAL
            # print(f"{activeproc.name}")
            if isChangedProc:
                if prevProc and not justCompleted:
                    print(f", {prevProc.progress}/{prevProc.burst} ({i}) / ", )
            # elif justCompleted:
            #     print(f",dsa {activeproc.progress}/{activeproc.burst} ({i}) / ", )
            isChangedProc= False
            justCompleted =False
            if isNewProc:
                print(f"{activeproc.arrival}@{activeproc.name}",end='')

            #compute processes
            for proc in self.processes:
                if proc is activeproc:
                    proc.progress+=1
                    proc.totalTurnAround+=1
                    prevProc = proc
                    if proc.progress == proc.burst:
                        # ? VISUAL
                        print(f", {proc.progress}/{proc.burst} ({i+1}) / ")
                        proc.complete=True
                        activeproc = None
                        justCompleted=True
                    continue
                
                if (not proc.complete )and i >= proc.arrival :
                    proc.totalTurnAround+=1
                    # proc.totalWait+=1

                if (not proc.activatedOnce ) and i >= proc.arrival:
                    proc.totalResponse+=1

        # ? VISUAL
        print(")")
        self._Print()

    def Priority(self,zeroHighest=True):
        print("Solving Scheduler using Priority Scheduling \n")
        activeproc=None
        print("( ")
        for i in range(self.totalTime):

            # ? VISUAL
            isNewProc= True
            if(activeproc):
                isNewProc = False 
            
            # get the next active proc
            if not activeproc:
                for proc in self.processes:
                    if proc.complete:
                        continue
                    if not activeproc:
                        activeproc=proc
                        continue
                    if zeroHighest:
                        if activeproc.priority > proc.priority and i >= proc.arrival:
                            activeproc = proc
                    else:
                        if activeproc.priority < proc.priority and i >= proc.arrival:
                            activeproc = proc
                activeproc.activatedOnce= True

            # ? VISUAL
            # print(f"{activeproc.name}")
            if(isNewProc):
                print(f"{activeproc.arrival}@{activeproc.name}",end='')
            # else:
            #     print(",",end='')

            #compute processes
            for proc in self.processes:
                if proc is activeproc:
                    proc.progress+=1
                    proc.totalTurnAround+=1
                    if proc.progress == proc.burst:
                        # ? VISUAL
                        print(f", {proc.progress}/{proc.burst} ({i+1}) / ")
                        proc.complete=True
                        activeproc = None
                    continue
                
                if (not proc.complete )and i >= proc.arrival :
                    proc.totalTurnAround+=1
                    # proc.totalWait+=1

                if (not proc.activatedOnce ) and i >= proc.arrival:
                    proc.totalResponse+=1

        # ? VISUAL
        print(")")
        self._Print()


    def _Print(self):
        # Calculate Averages
        aveWait, aveTurnAround, aveResponse =0,0,0
        for proc in self.processes:
            aveWait += proc.getTotalWait()
            aveTurnAround += proc.totalTurnAround
            aveResponse += proc.totalResponse
            print(f"Process: {proc.name}   Wait:{proc.getTotalWait():>3}   TurnAround:{proc.totalTurnAround:>3}   Response:{proc.totalResponse:>3}")
        aveWait, aveTurnAround, aveResponse =aveWait/len(self.processes), aveTurnAround/len(self.processes), aveResponse/len(self.processes)
        print(f"Averages: \n   Wait: {aveWait}\n   TurnAround: {aveTurnAround}\n   Response: {aveResponse}\n")
