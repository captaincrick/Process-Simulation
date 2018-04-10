import random

#This simulation models the processing of random events as they enter a process.
#It could be used to simulate an emergency room or customers entering a bank.


class ServerProcess:
    #These are the default variable values. Your process will need different values.
    #Read below to see what each of these are:
    def __init__(self,tp = 1,sd = 1,servers = 1,end_time = 1,eph = 1):

        #when do you want your simulation to end? end_time equals units of time.
        self.end_time = end_time
        #tp = through put, the average rate you process events
        self.tp = tp
        #sd = standard deviation of throughput.
        self.sd = sd
        #How many events occur, on average, per unit of time? EPH uses Exponential Distribution
        self.eph = eph

        #How many servers do you have in your process? Minimum is 1.
        self.servers = [[0,i] for i in range(servers)]

        #These variables are used to track statistics or are integral to the smooth running of this program.
        self.sim_time = 0
        self.events = []
        self.total_events = 0
        self.total_time = 0
        self.total_processing_time = 0
        self.total_waiting_time = 0
        self.over_time = 0
        self.event_waited = 0

    def create_event(self):

        self.update_sim_time()
        if self.sim_time <= self.end_time:
            self.events.append([self.sim_time,None,None,None])

    def update_sim_time(self):

        self.sim_time += random.expovariate(self.eph)

    def process_event(self):
            #first check if a server is available from n server
        for server in self.servers:
                    #checks if a server is available
            if server[0] <= self.events[0][0]:
                        #if server is available, make it busy until the process is finished.
                server[0] = self.events[0][0] + random.gauss(self.tp,self.sd)
                        #next you want to process the event
                        #When did the processing end?
                self.events[0][1] = server[0]
                        #total time spent waiting plus being processed
                self.events[0][2] = server[0] - self.events[0][0]
                        #total time spent waiting (should be zero)
                self.events[0][3] = 0
                self.total_events += 1
                        #now store the statistics and destroy the event from memory
                self.total_time += self.events[0][2]
                self.total_processing_time += self.events[0][2]
                self.over_time = self.events[0][1]
                self.events.pop(0)
                break

        next_available_server_num = self.servers[0]
        #If the above part of process does not eliminate the event, that means no server was immediately available.
        #So the logic changes a bit.
        while len(self.events) > 0:
            server_id = None
            for server in self.servers:
                if server[0] <= next_available_server_num[0]:
                    next_available_server_num = server
                    server_id = next_available_server_num[1]
            processing_time = random.gauss(self.tp,self.sd)
            process_start_time = next_available_server_num[0]
            next_available_server_num[0] += processing_time

            #When did processing end?
            self.events[0][1] = next_available_server_num[0]
            #How long did it spend processing?
            self.events[0][2] = processing_time
            #How long did just waiting take?
            self.events[0][3] = process_start_time - self.events[0][0]
            self.total_events += 1
            self.event_waited += 1
            self.total_time += self.events[0][2]
            self.total_processing_time += self.events[0][2]
            self.total_waiting_time += self.events[0][3]
            self.servers[server_id] = next_available_server_num
            self.over_time = self.events[0][1]
            self.events.pop(0)
            #you also need to set the server to next available server at the end.

    def run_sim(self):
        if self.servers < 1:
            self.servers = 1
           #we start by creating our first event
        self.create_event()
            #run the program until we run out of events
        while len(self.events) > 0:

            self.process_event()
            #start by checking if you can process an event, and processing it.
            self.create_event()

    def report(self):

        average_events_waiting = self.total_waiting_time / self.total_events
        percentage_busy = ((self.total_processing_time / len(self.servers)) / self.over_time) * 100
        extra_time = self.over_time - self.end_time #This can only be max 1
        if self.event_waited > 0:
            avg_wait_time = self.total_waiting_time / self.event_waited
        else:
            avg_wait_time = 0.0
        print("Total Number of Events: " + str(self.total_events))
        print("Simulation Time (With Overtime): " + str(self.over_time))
        print("Percentage of Time Servers Were Busy: " + str(percentage_busy))
        print("Average Number of Events Waiting: " + str(average_events_waiting))
        print("Average Wait Times: " + str(avg_wait_time))
        print("Overtime: " + str(extra_time))
