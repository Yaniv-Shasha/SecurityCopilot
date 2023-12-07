# Introduction 

### Objectives

Upon completing this technical guide, you will gain the following abilities:<br>

* Upload a cusotm plug from KQL type.<br>
* Learn how to enrich user information form external user list <br>
* Generete report that will levrage the custom plugin source.<br>

### Scenario
In this technical workshop, participants will learn how to upload a Security Copilot custom plugin of the API type.<br> 
To successfully complete this task, you must meet the following prerequisites:<br>

· You need your own tenant and Security Copilot instance.<br>
· You should have permission to upload a custom plugin.<br>



###  Instruction
    

#### Upload the Custom Plugin 


1. Obtain the file named "UsersHR.yml" from this directory.<br>
2. Inspect a KQL-type plugin.<br>
3. Modify the YAML file config to incluse your subscription, resource group and log analytics workspace.<br>
4. Upload the custom plugin and verify if it's activated.<br>

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/5cd2b8bb01eb8e3762371631aef03dd55697aded/Workshop/Custom_Plugin/Task03_GEO_IP_report/images/upload_plugin.jpg"/>


<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/8f8d876b47d68b620e7815ab584bdf382457073d/Workshop/Custom_Plugin/Task05_KQL/images/upload_plugin_wood.jpg"/>


####  Use case

You are Soc Analyst in Woodgrove Domain, During an a SAP Incident investigation, you found a suspicious user that download file from SAP system, to act fast, you need to enrich the user quickly with information that located in your HR system name **WoodgroveHR**.<br> 
As this incident created in an air-gap environment, the analyst from Woodgrove-airgap shared the incident in a Json format that you need to retrieve..<br> 



**Your task is:**<br>

1. Fetch air-gapped sentinel incident into Copilot Session memory. 
2. Use  **WoodgroveHR User Directory** custom plugin you just uploaded and call it explicitly. 
  hint: YOU CAN DO IT BY TYPE */wood* <br> 

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/5d4c5f29d1b3cca6239fb227690ab9dce3272cc7/Workshop/Custom_Plugin/Task05_KQL/images/call_plugin.jpg"/>

3. search the victim user from the incident <br> 

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/1a379fee910284aa03dfb5a3f21a17f0bbd97094/Workshop/Custom_Plugin/Task05_KQL/images/add_paramter.jpg"/>

4. Generate report that includes the incident summary and the user enriched data from the WoodgroveHR.


####   Example prompts:

1. Fetch url https://raw.githubusercontent.com/Yaniv-Shasha/SecurityCopilot/main/Workshop/Custom_Plugin/Task05_KQL/Sentinel_Incident.json.<br> 

2. Call the explictly the cusotm skill you update by by typing **/woodgroveHD**.<br> 

3. Ddd the user name as input paramter for the **/woodgroveHD** plugin.<br> 

4. Generate report that summarize the incident and include the user information.

.<br> 


#### Final results:
<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/624416689c40b5d2bcc357bc4e40af7f612cadd0/Workshop/Custom_Plugin/Task05_KQL/images/final_results.jpg"/>

