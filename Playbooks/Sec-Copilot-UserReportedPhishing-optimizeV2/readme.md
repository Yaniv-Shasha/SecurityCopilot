# Sec-Copilot-UserReportedPhishing
Author: Yaniv Shasha




By initiating the deployment process, you will set up an Azure Logic App integrated with Security Copilot Actions.<br>
This setup activates when a user reports a phishing attempt in Outlook.<br>
As configured by Defender for Office, these reported emails are rerouted to a designated shared mailbox.<br>
Each new email arriving in this shared mailbox triggers the Security Copilot automation, initiating an automated investigation process.<br> 
During this phase, Security Copilot examines the email to determine the likelihood of it being a phishing attempt.<br>
Depending on the assessed risk level, the system will send a notification email.<br>
Additionally, if the phishing probability exceeds 75%, a Sentinel Incident will be automatically generated.<br>


### Before starting the installation, ensure you have fulfilled these prerequisites:

• The user deploying this Logic app must possess a Contributor Role.<br>
• Activation of the Security Copilot license on your tenant is required.<br>
• The user authenticated in the Copilot logic app action should have Security Admin permissions and the role of a Microsoft Sentinel contributor, as this is necessary for creating incident comments.<br>
• Upload and enable custom KQL plugin, this need to be on the same user profile that running automation. <br>

## Required Paramaters

- Playbook Name<br />
- An Azure AD App registration with required API permissions and secret will needed to provide the following parameters<br />
https://docs.microsoft.com/microsoft-365/security/mtp/api-advanced-hunting?view=o365-worldwide<br />

    - Tenant ID<br />
    - Client ID<br />
    - Secret<br />


<br>

### Necessary configuration steps

Once this Playbooks template is deployed, you will need to go into the Logic App, edit it and click on each of the steps that require an authenticated connection to your tenant and complete the connection process.  These steps will have and exclamation point showing that the connection needs to be completed.  





### Deployment 

To deploy the above logic app, you need to<br>
•   Press on the Deploy option, select your subscription and the resource group (select the same tenant that Security Copilot is enabled)<br>

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FPlaybooks%2FSec-Copilot-UserReportedPhishing-optimizeV2%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>


    




###  Full Logic App view

<img src="./images/full_view.png"/>