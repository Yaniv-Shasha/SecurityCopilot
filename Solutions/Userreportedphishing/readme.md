# User reported phishing Copilot for Security automatic investigation
Author: **Craig Freyman & Yaniv Shasha**<br>


The given automation activates when an email arrives in a shared mailbox. Our approach to handling incoming emails includes:<br>

1.	Forwarding the email to the mailbox – here, we lose the original email and cannot perform analysis on its headers.<br>
2.	Receiving the email as an attachment – this allows us to retain the original email and conduct a thorough analysis of all email components.<br>




### How to deploy this solution

The solution consists of two primary components: <br>

• An **Azure Logic App** that triggers in response to every new email received in the shared mailbox, also handling the execution of prompts and integrating with Copilot for security.<br>
• An **Azure Function** that takes the email as blob text, extracts key entities for use in subsequent analysis. <br>


## Deployment of the Azure Function:

The initial step to deploy the solution is setting up the Azure function.<br>
Click the provided link to initiate the deployment, ensuring you alter only the target resource group parameter<br>

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FSolutions%2FUserreportedphishing%2Fazuredeploy.json" target="_blank">
<img src="https://aka.ms/deploytoazurebutton"/>
</a>

<br>

<p align="center">
<img src="./images/deploy_func.jpg?raw=true"/>
</p>
<br>

• Once the deployment is complete, proceed to the resource group to retrieve and copy both the function name and the resource group details:<br>

<p align="center">
<img src="./images/azure_func_resource_selection.jpg?raw=true"/>
</p>
<br>

## Deploying the Azure Logic app:

• To deploy the Azure logic app, click on the link provided above.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FSolutions%2FUserreportedphishing%2Flogic_app%2Fazuredeploy.json" target="_blank">
<img src="https://aka.ms/deploytoazurebutton"/>
</a>
<br>

## Enter the following details:
1.	The resource group for the Azure function we set up earlier.<br>
2.	The name given to the Azure function app from the prior step.<br>

*** keep the function names 01/02 as they are.

<p align="center">
<img src="./images/deploy_LAPP.jpg?raw=true"/>
</p>
<br>


## Post Deploying steps:

Once the installation is finished, go to the resource group and access the logic app that we have recently deployed. 
<br>

<p align="center">
<img src="./images/logapp-postdeploying.jpg?raw=true"/>
</p>
<br>

•	To set up authentication, go to the menu on the left and click on API connection. 

<p align="center">
<img src="./images/api_connection.jpg?raw=true"/>
</p>
<br>

•	Click on **Office365-1-PhishingAnalysis**, then in the left menu, open General and click Edit Api connection. <br>

<p align="center">
<img src="./images/api_connection-edit.jpg?raw=true"/>
</p>
<br>

•	Click on authorize, authenticate using the users from the shared mailbox, and then click save.
•	Repeat the process for the Security copilot API connection, except authenticate with users who have the Copilot for security contributor permission.
Your automation is ready for action! 
