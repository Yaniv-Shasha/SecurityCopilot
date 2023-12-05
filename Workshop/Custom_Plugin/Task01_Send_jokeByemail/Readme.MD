# Introduction
#### Objectives
After completing this lab, you will be able to:
· Upload Security Copilot custom plugin of Logic app type
· Deploy Azure Logic App that will except Security Copilot Prompts 
· Create Security Copilot session that will trigger this logic app 

#### Scenario
In this technical workshop, attendees will upload Security Copilot custom plugin from LogicApp type and deploy the corresponding logic app. 
To be able to complete this task:
You will need your own tenant and Security Copilot instance. 
Have permission to upload custom plugin
Have Permission to deploy logic app 


####  instruction

## Deploy Logic app 

	1. Deploy the above logic app, by pressing on the deploy button
	2. Located the newly created logic app and authenticate the send email action with user that has mailbox in O365

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FWorkshop%2FCustom_Plugin%2FTask01_Send_jokeByemail%2FWorkshop01-sendJokeByemail%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>

### upload the custom plugin 

	1. Open the SendJokeByEmail.yml in the same folder and edit it 
	2. Add the above information: 

The SubscriptionId where you deployed your logic app 
The ResourceGroup where you deployed the logicapp 

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/2100cbf8cdd70735495ad5c869746bf02be144dc/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/yaml_subid.jpg"/>





	3. Upload the custom plugin 
	4. Run the above prompts:

Tell me a security related joke for today

Run logic and send the above joke to this email youremail@email.com

	5. To check the process, open the logic app you just created and check the last runs 
	6. Open your inbox and examine the email
