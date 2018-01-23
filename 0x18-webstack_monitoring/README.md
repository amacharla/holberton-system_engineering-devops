<h1 class="gap">0x18. Webstack monitoring</h1>


<h4 class="task">
    0. Monitor your Nginx traffic
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Let’s monitor our Nginx server traffic (access log and error log), by installing <a href="/rltoken/iZXLFtq7EfU2-iObKg2xEg" target="_blank" title="Sumlogic">Sumlogic</a> on <code>web-01</code> (feel free to do it on other servers a well). Create an account and follow the setup wizard flow.</p><p>Requirements:</p><ul>

<h4 class="task">
    1. Monitor your server
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Your Nginx is running on a server and its health will impact how well Nginx and other server running on it perform. A server that is overloaded with tasks that are too CPU, memory, disk or network intensive will end up not performing as expected, might just freeze and crash.</p><p>Configure Sumo Logic to monitor your servers memory, CPU, network and disk. Once you are done you should be able to explore your machine performances in the metric tab:</p><p><img alt="Sumo Logic metric tab" src="https://i.imgur.com/OKYDhCv.png"/></p>

