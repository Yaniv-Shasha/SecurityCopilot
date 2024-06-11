# Sec-Copilot-UserReportedPhishing
Author: Yaniv Shasha




By initiating the deployment process, you will set up an Azure Logic App integrated with Security Copilot Actions.<br>
This setup activates when a user reports a phishing attempt in Outlook.<br>
As configured by Defender for Office, these reported emails are rerouted to a designated shared mailbox.<br>

<img src="./images/config_mailbox.jpg"/>

Each new email arriving in this shared mailbox triggers the Security Copilot automation, initiating an automated investigation process.<br> 
During this phase, Security Copilot examines the email to determine the likelihood of it being a phishing attempt.<br>






### Before starting the installation, ensure you have fulfilled these prerequisites:

• The user deploying this Logic app must possess a Contributor Role.<br>
• Activation of the Security Copilot license on your tenant is required.<br>
• The user authenticated in the Copilot logic app action should have Security Reader permissions and read access to the shared mailbox and send email permission

<br>

<br>







### Deployment 

To deploy the above logic app, you need to<br>
•   Press on the Deploy option, select your subscription and the resource group (select the same tenant that Security Copilot is enabled)<br>

## Required Paramaters

- Playbook Name<br />
- An Azure AD App registration with required API permissions and secret will needed to provide the following parameters<br />
https://docs.microsoft.com/microsoft-365/security/mtp/api-advanced-hunting?view=o365-worldwide<br />

    - Tenant ID<br />
    - Client ID<br />
    - Secret<br />
    - Shared mail address (this is where the email trigger will connected)<br />

<br>


<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FPlaybooks%2FSec-Copilot-UserReportedPhishing-ShardMB%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>


<img src="./images/deploy.png"/>


###  Full Logic App view

<img src="./images/full_view.png"/>
<img src="./images/full_view2.png"/>