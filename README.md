# Process-Simulation 

<h1>Discrete Event Simulation</h1>

<h2>How To Use This Process Simulator</h2>

<p>First you need to create an object of the type ServerProcess and pass in 5 variables (listed and explained below).</p>

<h4>The variables:</h4>

<ol>
  <li>Through Put (tp): The rate at which an event is processed. </li>
  <li>Standard Deviaton of Through Put (sd): the standard deviation of through put. </li>
  <li>Servers (servers): the number of servers available to process events</li>
  <li>End time (end_time): how many time periods you want the simulation to last</li>
  <li>Inter-arrival (eph): the number of events you want to occur randomly per unit of time. </li>
 </ol>

<p>The default values for all variables is 1. </p>

<h4>Next, call the run_sim method on your object. </h4>

<h4>Then call the report method on your object. </h4>

<p><strong>Example:</strong></p>

<p>sim = ServerProcess(tp =.2,sd=.1,servers = 1,end_time=5,eph=5)</p>
<p>sim.run_sim()</p>
<p>sim.report()</p>

<p><strong>The above will generate something that looks like this:</strong></p>

<p>Total Number of Events: 26</p>
<p>Simulation Time (With Overtime): 6.65618768977</p>
<p>Percentage of Time Servers Were Busy: 89.9100747156</p>
<p>Average Number of Events Waiting: 0.577463501347</p>
<p>Average Wait Times: 0.682456865228</p>

<p>That's all I've got so far folks. I plan to update this periodically. </p>
