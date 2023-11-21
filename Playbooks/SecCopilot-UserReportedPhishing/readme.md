# Sec-Copilot-UserReportedPhishing
Author: Yaniv Shasha


By initiating the deployment process, you will set up an Azure Logic App integrated with Security Copilot Actions.<br>
This setup activates when a user reports a phishing attempt in Outlook.<br>
As configured by Defender for Office, these reported emails are rerouted to a designated shared mailbox.<br>
Each new email arriving in this shared mailbox triggers the Security Copilot automation, initiating an automated investigation process.<br> 
During this phase, Security Copilot examines the email to determine the likelihood of it being a phishing attempt.<br>
Depending on the assessed risk level, the system will send a notification email.<br>
Additionally, if the phishing probability exceeds 75%, a Sentinel Incident will be automatically generated.<br>

 
 
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSentinel%2Fmaster%2FPlaybooks%2FSec-Copilot-UserReportedPhishing%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
