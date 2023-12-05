# Introduction

#### Objectives

Upon completing this technical guide, you will gain the following abilities:
· Upload a Security Copilot custom plugin of the Logic App type.
· Deploy an Azure Logic App capable of handling Security Copilot prompts.
· Create a Security Copilot session that triggers this Logic App.

#### Scenario
In this technical workshop, participants will learn how to upload a Security Copilot custom plugin of the Logic App type and deploy the corresponding Logic App. To successfully complete this task, you must meet the following prerequisites:

· You need your own tenant and Security Copilot instance.
· You should have permission to upload a custom plugin.
· You should have permission to deploy a Logic App.


####  instruction

## Deploy Logic app 

	1. Deploy the Logic App above by clicking the "Deploy to Azure" button

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FWorkshop%2FCustom_Plugin%2FTask01_Send_jokeByemail%2FWorkshop01-sendJokeByemail%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
	2. Once the Logic App is created, locate it and authenticate the "send email" action with a user who has a mailbox in O365.

### Upload the Custom Plugin 

Open the "SendJokeByEmail.yml" file in the same folder and edit it.
Add the following information:

1. The SubscriptionId where you deployed your Logic App.
2. The ResourceGroup where you deployed the Logic App.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/2100cbf8cdd70735495ad5c869746bf02be144dc/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/yaml_subid.jpg"/>

3. Upload the custom plugin.

4. Execute the following prompts:

"Tell me a security-related joke for today."
Run the logic to send the above joke to this email: youremail@email.com.

5. To monitor the process, open the Logic App you just created and check the last runs.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/86e2ba5cab9da11622dfa5966aa86c1223b615d0/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/run_history.jpg"/>

	6. Open your inbox and examine the email.


    We are hoping it was funny :-)
