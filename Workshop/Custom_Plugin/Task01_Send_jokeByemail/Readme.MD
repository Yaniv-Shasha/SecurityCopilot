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


### upload the custom plugin 

	1. Open the SendJokeByEmail.yml in the same folder and edit it 
	2. Add the above information: 

The SubscriptionId where you deployed your logic app 
The ResourceGroup where you deployed the logicapp 


	3. Upload the custom plugin 
	4. Run the above prompts:

Tell me a security related joke for today

Run logic and send the above joke to this email youremail@email.com

	5. To check the process, open the logic app you just created and check the last runs 
	6. Open your inbox and examine the email
