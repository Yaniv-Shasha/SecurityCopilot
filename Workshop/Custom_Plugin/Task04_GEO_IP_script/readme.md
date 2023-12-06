# Introduction 

### Objectives

Upon completing this technical guide, you will gain the following abilities:<br>

* Upload a cusotm plug from API type.<br>
* Learn how to use script analysis promptbook.<br>
* Learn how to analze and encode Script.<br>
* Generete report that will levrage the custom plugin source.<br>

### Scenario
In this technical workshop, participants will learn how to upload a Security Copilot custom plugin of the API type.<br> 
To successfully complete this task, you must meet the following prerequisites:<br>

· You need your own tenant and Security Copilot instance.<br>
· You should have permission to upload a custom plugin.<br>



###  Instruction
    

#### Upload the Custom Plugin 


1. Obtain the file named "Geo.yaml" from this directory.<br>
2. Inspect it to appreciate the simplicity of creating a API-type plugin.<br>
3. Upload the custom plugin and verify if it's activated.<br>

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/5cd2b8bb01eb8e3762371631aef03dd55697aded/Workshop/Custom_Plugin/Task03_GEO_IP_report/images/upload_plugin.jpg"/>


<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/5cd2b8bb01eb8e3762371631aef03dd55697aded/Workshop/Custom_Plugin/Task03_GEO_IP_report/images/plugin_turn_on.jpg"/>


####  Use case


You are Soc Analyst in woodgrove Domain, During an endpoint Incident investigation, you found suspicious script that run on your DMZ server, your job is to analyze this script, and share your final to your team member.<br> 



**Your task is:**<br>

1. Input this information about the script from the script_decode.txt and ask Copilot to decode it
2. Extract only the IPs from this script.
3. Employ the MDTI reputation score to assess these Ip.
4. Identify IPs with scores
5. In order to compile a report with your findings, utilize the custom plugin you recently uploaded to GeoIP the suspicious Ips.
6. Share report that include the reputation score and the Geo IP data.

**Bouns task:**<br>

1. Copy the script from script_decode.txt
2. Open the Suspicious Script analysis
3. past the Script you copief in setp one into the prompts and press run 
4. share the report and notice if this script was malicious


####   Example prompts:

1. Decode the above script "Replace this with the script you copied".<br> 

2. check reputation score for the above ip.<br> 

3. Use Geo location for the above IP.<br> 

4. create report that include the reputation score and the Geo Ip address.<br> 


#### Final results:
<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/b6515cc05c037db8e9118bcb1dcbe5c458d2fbd7/Workshop/Custom_Plugin/Task04_GEO_IP_script/images/final_free%20text.png"/>
