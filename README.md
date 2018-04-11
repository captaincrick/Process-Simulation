# Process-Simulation

How To Use This Process Simulator

First you need to create an object of the type ServerProcess and pass in 5 variables (listed and explained below).

The variables:

Through Put (tp): The rate at which an event is processed. 
Standard Deviaton of Through Put (sd): the standard deviation of through put. 
Servers (servers): the number of servers available to process events
End time (end_time): how many time periods you want the simulation to last
eph: the number ofevents you want to occur randomly per unit of time. 

The default values for all variables is 1. 

Next, call the run_sim method on your object. 

Then call the report method on your object. 

Example:

sim = ServerProcess(tp =.2,sd=.1,servers = 1,end_time=5,eph=5)
sim.run_sim()
sim.report()

The above will generate something that looks like this:

Total Number of Events: 26
Simulation Time (With Overtime): 6.65618768977
Percentage of Time Servers Were Busy: 89.9100747156
Average Number of Events Waiting: 0.577463501347
Average Wait Times: 0.682456865228

That's all I've got so far folks. I plan to update this periodically. 
