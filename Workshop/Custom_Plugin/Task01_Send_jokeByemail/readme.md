# Introduction

#### Objectives

Upon completing this technical guide, you will gain the following abilities:<br>

* Upload a Security Copilot custom plugin of the Logic App type.<br>
* Deploy an Azure Logic App capable of handling Security Copilot prompts.<br>
* Create a Security Copilot session that triggers this Logic App.<br>

#### Scenario
In this technical workshop, participants will learn how to upload a Security Copilot custom plugin of the Logic App type and deploy the corresponding Logic App. To successfully complete this task, you must meet the following prerequisites:<br>

* You need your own tenant and Security Copilot instance.<br>
* You should have permission to upload a custom plugin.<br>
* You should have permission to deploy a Logic App.<br>


####  Instruction

## Deploy Logic app 

	1. Deploy the Logic App above by clicking the "Deploy to Azure" button

Select the subscription, resource group and logicapp name.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FWorkshop%2FCustom_Plugin%2FTask01_Send_jokeByemail%2FWorkshop01-sendJokeByemail%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<br>

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/9859a2c50eec7150aec74fee8ab85c91611d099c/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/deploy_logic_app.jpg"/>

<br>
	2. Once the Logic App is created, locate it and authenticate the "send email" action with a user who has a mailbox in O365.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/32db9c9a0a69d4bafeefb0e92aea4b540572adaa/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/auth_logicapp.jpg"/>

    

### Upload the Custom Plugin 

Downalod a local copy of "SendJokeByEmail.yml" file located in the same folder and edit it.<br>
Add the following information:

1. The SubscriptionId where you deployed your Logic App.
2. The ResourceGroup where you deployed the Logic App.
2. If you changed the default logic app name adapt the logic app name.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/2100cbf8cdd70735495ad5c869746bf02be144dc/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/yaml_subid.jpg"/>

3. Upload the custom plugin and check if its turn on

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/cfcd1baf606277478b7512be8bf3e43c7074f870/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/upload_plugin.jpg"/>


<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/cfcd1baf606277478b7512be8bf3e43c7074f870/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/check_if_plugin_isON.jpg"/>

4. **Execute the following prompts:**

* Tell me a security-related joke for today.<br>
* Run the logic to send the above joke to this email: <youremailaddress@email.com>..<br>

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/5314df248009d620c560f0b4b0b8b1bb8444848b/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/prompts.jpg"/>

5. To monitor the process, open the Logic App you just created and check the last runs.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/86e2ba5cab9da11622dfa5966aa86c1223b615d0/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/run_history.jpg"/>

	6. Open your inbox and examine the email.<br>

###  See you in the Next Task!
