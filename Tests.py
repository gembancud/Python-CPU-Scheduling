from Process import Process
from Scheduler import Scheduler

if __name__ == "__main__":
    scheduler = Scheduler()

    # 1
    print("\nOUTPUT FOR #1:")
    scheduler.addtoProcess(Process("p0",13))
    scheduler.addtoProcess(Process("p1",3))
    scheduler.addtoProcess(Process("p2",6))
    scheduler.FCFS()
    scheduler.clearProcesses()

    # 2
    print("\nOUTPUT FOR #2:")
    scheduler.addtoProcess(Process("p0",13))
    scheduler.addtoProcess(Process("p1",3))
    scheduler.addtoProcess(Process("p2",6))
    scheduler.RR(quantum=4)
    scheduler.clearProcesses()

    # 3a
    print("\nOUTPUT FOR #3a:")
    scheduler.addtoProcess(Process("p1",7, arrival=0))
    scheduler.addtoProcess(Process("p2",4, arrival=2))
    scheduler.addtoProcess(Process("p3",1, arrival=4))
    scheduler.addtoProcess(Process("p4",2, arrival=5))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    # 3b
    print("\nOUTPUT FOR #3b:")
    scheduler.addtoProcess(Process("p1",7, arrival=0))
    scheduler.addtoProcess(Process("p2",4, arrival=2))
    scheduler.addtoProcess(Process("p3",1, arrival=4))
    scheduler.addtoProcess(Process("p4",2, arrival=5))
    scheduler.SJF_P()
    scheduler.clearProcesses()

    #4
    print("\nOUTPUT FOR #4:")
    scheduler.addtoProcess(Process("p1",30))
    scheduler.addtoProcess(Process("p2",6))
    scheduler.addtoProcess(Process("p3",8))
    scheduler.RR(quantum=5)
    scheduler.clearProcesses()

    #5
    print("\nOUTPUT FOR #5:")
    scheduler.addtoProcess(Process("p1",53))
    scheduler.addtoProcess(Process("p2",17))
    scheduler.addtoProcess(Process("p3",68))
    scheduler.addtoProcess(Process("p4",24))
    scheduler.RR(quantum=20)
    scheduler.clearProcesses()

    #6
    print("\nOUTPUT FOR #6:")
    scheduler.addtoProcess(Process("p1",6, priority=2))
    scheduler.addtoProcess(Process("p2",12, priority=4))
    scheduler.addtoProcess(Process("p3",1, priority=5))
    scheduler.addtoProcess(Process("p4",3, priority=1))
    scheduler.addtoProcess(Process("p5",5, priority=3))
    scheduler.Priority()
    scheduler.clearProcesses()

    #7a
    print("\nOUTPUT FOR #7A:")
    scheduler.addtoProcess(Process("p1",6 ))
    scheduler.addtoProcess(Process("p2",8 ))
    scheduler.addtoProcess(Process("p3",7 ))
    scheduler.addtoProcess(Process("p4",3 ))
    scheduler.FCFS()
    scheduler.clearProcesses()

    #7b
    print("\nOUTPUT FOR #7b:")
    scheduler.addtoProcess(Process("p1",6 ))
    scheduler.addtoProcess(Process("p2",8 ))
    scheduler.addtoProcess(Process("p3",7 ))
    scheduler.addtoProcess(Process("p4",3 ))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    #7c
    print("\nOUTPUT FOR #7c:")
    scheduler.addtoProcess(Process("p1",6 ))
    scheduler.addtoProcess(Process("p2",8 ))
    scheduler.addtoProcess(Process("p3",7 ))
    scheduler.addtoProcess(Process("p4",3 ))
    scheduler.SJF_P()
    scheduler.clearProcesses()

    #8a
    print("\nOUTPUT FOR #8a:")
    scheduler.addtoProcess(Process("p1",8 ))
    scheduler.addtoProcess(Process("p2",4 ))
    scheduler.addtoProcess(Process("p3",9 ))
    scheduler.addtoProcess(Process("p4",5 ))
    scheduler.FCFS()
    scheduler.clearProcesses()

    #8b
    print("\nOUTPUT FOR #8b:")
    scheduler.addtoProcess(Process("p1",8 ))
    scheduler.addtoProcess(Process("p2",4 ))
    scheduler.addtoProcess(Process("p3",9 ))
    scheduler.addtoProcess(Process("p4",5 ))
    scheduler.SJF_P()
    scheduler.clearProcesses()

    #8c
    print("\nOUTPUT FOR #8c:")
    scheduler.addtoProcess(Process("p1",8 ))
    scheduler.addtoProcess(Process("p2",4 ))
    scheduler.addtoProcess(Process("p3",9 ))
    scheduler.addtoProcess(Process("p4",5 ))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    #8d
    print("\nOUTPUT FOR #8d:")
    scheduler.addtoProcess(Process("p1",8 ))
    scheduler.addtoProcess(Process("p2",4 ))
    scheduler.addtoProcess(Process("p3",9 ))
    scheduler.addtoProcess(Process("p4",5 ))
    scheduler.RR(quantum=4)
    scheduler.clearProcesses()

    #9a
    print("\nOUTPUT FOR #9a: FCFS")
    scheduler.addtoProcess(Process("p1",10, priority=3 ))
    scheduler.addtoProcess(Process("p2",1, priority=1  ))
    scheduler.addtoProcess(Process("p3",2, priority=3  ))
    scheduler.addtoProcess(Process("p4",1, priority=4 ))
    scheduler.addtoProcess(Process("p5",5, priority=2  ))
    scheduler.FCFS()
    scheduler.clearProcesses()

    #9b
    print("\nOUTPUT FOR #9a: SJFP")
    scheduler.addtoProcess(Process("p1",10, priority=3 ))
    scheduler.addtoProcess(Process("p2",1, priority=1  ))
    scheduler.addtoProcess(Process("p3",2, priority=3  ))
    scheduler.addtoProcess(Process("p4",1, priority=4 ))
    scheduler.addtoProcess(Process("p5",5, priority=2  ))
    scheduler.SJF_P()
    scheduler.clearProcesses()

    #9c
    print("\nOUTPUT FOR #9a: SJFNP")
    scheduler.addtoProcess(Process("p1",10, priority=3 ))
    scheduler.addtoProcess(Process("p2",1, priority=1  ))
    scheduler.addtoProcess(Process("p3",2, priority=3  ))
    scheduler.addtoProcess(Process("p4",1, priority=4 ))
    scheduler.addtoProcess(Process("p5",5, priority=2  ))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    #9d
    print("\nOUTPUT FOR #9a: PRIORITY")
    scheduler.addtoProcess(Process("p1",10, priority=3 ))
    scheduler.addtoProcess(Process("p2",1, priority=1  ))
    scheduler.addtoProcess(Process("p3",2, priority=3  ))
    scheduler.addtoProcess(Process("p4",1, priority=4 ))
    scheduler.addtoProcess(Process("p5",5, priority=2  ))
    scheduler.Priority(zeroHighest=True)
    scheduler.clearProcesses()

    #9e
    print("\nOUTPUT FOR #9a: RR")
    scheduler.addtoProcess(Process("p1",10, priority=3 ))
    scheduler.addtoProcess(Process("p2",1, priority=1  ))
    scheduler.addtoProcess(Process("p3",2, priority=3  ))
    scheduler.addtoProcess(Process("p4",1, priority=4 ))
    scheduler.addtoProcess(Process("p5",5, priority=2  ))
    scheduler.RR(quantum=1)
    scheduler.clearProcesses()

    #10a
    print("\nOUTPUT FOR #10: RR")
    scheduler.addtoProcess(Process("A",10, priority=3 ))
    scheduler.addtoProcess(Process("B",6, priority=5  ))
    scheduler.addtoProcess(Process("C",2, priority=2  ))
    scheduler.addtoProcess(Process("D",4, priority=1 ))
    scheduler.addtoProcess(Process("E",8, priority=4  ))
    scheduler.RR(quantum=2)
    scheduler.clearProcesses()

    #10b
    print("\nOUTPUT FOR #10: PRIORITY")
    scheduler.addtoProcess(Process("A",10, priority=3 ))
    scheduler.addtoProcess(Process("B",6, priority=5  ))
    scheduler.addtoProcess(Process("C",2, priority=2  ))
    scheduler.addtoProcess(Process("D",4, priority=1 ))
    scheduler.addtoProcess(Process("E",8, priority=4  ))
    scheduler.Priority(zeroHighest=False)
    scheduler.clearProcesses()

    #10c
    print("\nOUTPUT FOR #10: FCFS")
    scheduler.addtoProcess(Process("A",10, priority=3 ))
    scheduler.addtoProcess(Process("B",6, priority=5  ))
    scheduler.addtoProcess(Process("C",2, priority=2  ))
    scheduler.addtoProcess(Process("D",4, priority=1 ))
    scheduler.addtoProcess(Process("E",8, priority=4  ))
    scheduler.FCFS()
    scheduler.clearProcesses()

    #10d
    print("\nOUTPUT FOR #10: SJF")
    scheduler.addtoProcess(Process("A",10, priority=3 ))
    scheduler.addtoProcess(Process("B",6, priority=5  ))
    scheduler.addtoProcess(Process("C",2, priority=2  ))
    scheduler.addtoProcess(Process("D",4, priority=1 ))
    scheduler.addtoProcess(Process("E",8, priority=4  ))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    #11a
    print("\nOUTPUT FOR #11: FCFS")
    scheduler.addtoProcess(Process("1",80, priority=3 ))
    scheduler.addtoProcess(Process("2",20, priority=1  ))
    scheduler.addtoProcess(Process("3",5, priority= 4 ))
    scheduler.addtoProcess(Process("4",20, priority=1 ))
    scheduler.addtoProcess(Process("5",50, priority=2  ))
    scheduler.FCFS()
    scheduler.clearProcesses()
    
    #11b
    print("\nOUTPUT FOR #11: PRIORITY")
    scheduler.addtoProcess(Process("1",80, priority=3 ))
    scheduler.addtoProcess(Process("2",20, priority=1  ))
    scheduler.addtoProcess(Process("3",5, priority= 4 ))
    scheduler.addtoProcess(Process("4",20, priority=1 ))
    scheduler.addtoProcess(Process("5",50, priority=2  ))
    scheduler.Priority(zeroHighest=True)
    scheduler.clearProcesses()

    #12
    print("\nOUTPUT FOR #12: SJF")
    scheduler.addtoProcess(Process("1",75, arrival=0 ))
    scheduler.addtoProcess(Process("2",40, arrival=10  ))
    scheduler.addtoProcess(Process("3",25, arrival=10 ))
    scheduler.addtoProcess(Process("4",20, arrival=80 ))
    scheduler.addtoProcess(Process("5",45, arrival=85  ))
    scheduler.Priority(zeroHighest=True)
    scheduler.clearProcesses()
    
    #13
    print("\nOUTPUT FOR #13: SJFP")
    scheduler.addtoProcess(Process("p1",2, arrival=0 ))
    scheduler.addtoProcess(Process("p2",1, arrival=1  ))
    scheduler.addtoProcess(Process("p3",2, arrival=3 ))
    scheduler.addtoProcess(Process("p4",3, arrival=4 ))
    scheduler.addtoProcess(Process("p5",5, arrival=6  ))
    scheduler.SJF_P()
    scheduler.clearProcesses()

    #14
    print("\nOUTPUT FOR #14: RR")
    scheduler.addtoProcess(Process("p1",3, arrival=0 ))
    scheduler.addtoProcess(Process("p2",6, arrival=1.001  ))
    scheduler.addtoProcess(Process("p3",4, arrival=4.001 ))
    scheduler.addtoProcess(Process("p4",2, arrival=6.001 ))
    scheduler.RR(quantum=2)
    scheduler.clearProcesses()

    #15a
    print("\nOUTPUT FOR #15: FCFS")
    scheduler.addtoProcess(Process("p1",10))
    scheduler.addtoProcess(Process("p2",50))
    scheduler.addtoProcess(Process("p3",4))
    scheduler.addtoProcess(Process("p4",100))
    scheduler.addtoProcess(Process("p5",5))
    scheduler.FCFS()
    scheduler.clearProcesses()

    #15b
    print("\nOUTPUT FOR #15: SJFNP")
    scheduler.addtoProcess(Process("p1",10))
    scheduler.addtoProcess(Process("p2",50))
    scheduler.addtoProcess(Process("p3",4))
    scheduler.addtoProcess(Process("p4",100))
    scheduler.addtoProcess(Process("p5",5))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    #16
    print("\nOUTPUT FOR #16: FCFS")
    scheduler.addtoProcess(Process("p1",5))
    scheduler.addtoProcess(Process("p2",24))
    scheduler.addtoProcess(Process("p3",16))
    scheduler.addtoProcess(Process("p4",10))
    scheduler.addtoProcess(Process("p5",3))
    scheduler.FCFS()
    scheduler.clearProcesses()

    #17
    print("\nOUTPUT FOR #17: FCFS")
    scheduler.addtoProcess(Process("p1",3,arrival=0))
    scheduler.addtoProcess(Process("p2",6,arrival=2))
    scheduler.addtoProcess(Process("p3",4,arrival=4))
    scheduler.addtoProcess(Process("p4",5,arrival=6))
    scheduler.addtoProcess(Process("p5",2,arrival=8))
    scheduler.FCFS()
    scheduler.clearProcesses()
    
    #18
    print("\nOUTPUT FOR #18: SJFNP")
    scheduler.addtoProcess(Process("p1",5))
    scheduler.addtoProcess(Process("p2",24))
    scheduler.addtoProcess(Process("p3",16))
    scheduler.addtoProcess(Process("p4",10))
    scheduler.addtoProcess(Process("p5",3))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    #19
    print("\nOUTPUT FOR #19: RR")
    scheduler.addtoProcess(Process("p1",3))
    scheduler.addtoProcess(Process("p2",6))
    scheduler.addtoProcess(Process("p3",8))
    scheduler.RR(quantum=5)
    scheduler.clearProcesses()

    #20a
    print("\nOUTPUT FOR #20: FCFS")
    scheduler.addtoProcess(Process("p1",5,priority=4))
    scheduler.addtoProcess(Process("p2",12,priority=1))
    scheduler.addtoProcess(Process("p3",16,priority=3))
    scheduler.addtoProcess(Process("p4",18,priority=5))
    scheduler.addtoProcess(Process("p5",2,priority=2))
    scheduler.FCFS()
    scheduler.clearProcesses()

    #20b
    print("\nOUTPUT FOR #20: SJFNP")
    scheduler.addtoProcess(Process("p1",5,priority=4))
    scheduler.addtoProcess(Process("p2",12,priority=1))
    scheduler.addtoProcess(Process("p3",16,priority=3))
    scheduler.addtoProcess(Process("p4",18,priority=5))
    scheduler.addtoProcess(Process("p5",2,priority=2))
    scheduler.SJF_NP()
    scheduler.clearProcesses()

    #20c
    print("\nOUTPUT FOR #20: SJFP")
    scheduler.addtoProcess(Process("p1",5,priority=4))
    scheduler.addtoProcess(Process("p2",12,priority=1))
    scheduler.addtoProcess(Process("p3",16,priority=3))
    scheduler.addtoProcess(Process("p4",18,priority=5))
    scheduler.addtoProcess(Process("p5",2,priority=2))
    scheduler.SJF_P()
    scheduler.clearProcesses()

    #20d
    print("\nOUTPUT FOR #20: RR")
    scheduler.addtoProcess(Process("p1",5,priority=4))
    scheduler.addtoProcess(Process("p2",12,priority=1))
    scheduler.addtoProcess(Process("p3",16,priority=3))
    scheduler.addtoProcess(Process("p4",18,priority=5))
    scheduler.addtoProcess(Process("p5",2,priority=2))
    scheduler.RR(quantum=3)
    scheduler.clearProcesses()

    #20e
    print("\nOUTPUT FOR #20: PRIORITY")
    scheduler.addtoProcess(Process("p1",5,priority=4))
    scheduler.addtoProcess(Process("p2",12,priority=1))
    scheduler.addtoProcess(Process("p3",16,priority=3))
    scheduler.addtoProcess(Process("p4",18,priority=5))
    scheduler.addtoProcess(Process("p5",2,priority=2))
    scheduler.Priority(zeroHighest=True)
    scheduler.clearProcesses()


