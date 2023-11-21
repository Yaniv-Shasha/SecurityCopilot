# Sec-Copilot-UserReportedPhishing
Author: Yaniv Shasha


### As of this moment, please deploy this logic app in West-US-2 region

By initiating the deployment process, you will set up an Azure Logic App integrated with Security Copilot Actions.<br>
This setup activates when a user reports a phishing attempt in Outlook.<br>
As configured by Defender for Office, these reported emails are rerouted to a designated shared mailbox.<br>
Each new email arriving in this shared mailbox triggers the Security Copilot automation, initiating an automated investigation process.<br> 
During this phase, Security Copilot examines the email to determine the likelihood of it being a phishing attempt.<br>
Depending on the assessed risk level, the system will send a notification email.<br>
Additionally, if the phishing probability exceeds 75%, a Sentinel Incident will be automatically generated.<br>

### Prerequisites

Prior to beginning the installation process, it's crucial to confirm that you have met the following prerequisites: <br>
• The user that will deploy this Logic app need to have a Contributor Role.<br>
• You enabled the Security Copilot license on your tenant <br>
• The user that authenticted in the Copilot logic app action, need to have Security Admin permission and Microsoft sentinel contributer (as its need to create incident comment).<br>
 
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSentinel%2Fmaster%2FPlaybooks%2FSec-Copilot-UserReportedPhishing%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>

<br>

<br>

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/00853308e8949cc7279640aa9743759f586bb190/Playbooks/Copilot-Sentinel_investigation-DynamicSev/images/copilot_auth.jpg"/>

<br>

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/00853308e8949cc7279640aa9743759f586bb190/Playbooks/Copilot-Sentinel_investigation-DynamicSev/images/Sentinel_auth.jpg"/>

<br>

• This logic app can be run in a manual way, or in automatic way, if you select the automated way, you will need to create a new automation rule in Sentinel and configure this logic app as an action.<br>

### Deployment 

To deploy the above logic app, you need to<br>
•   Press on the Deploy option, select your subscription and the resource group (select the same tenant that Security Copilot is enabled)<br>

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSentinel%2Fmaster%2FPlaybooks%2FSec-Copilot-UserReportedPhishing%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>