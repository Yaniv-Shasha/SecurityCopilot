# Copilot-Sentinelinvestigation-DynamicSev
Author: Yaniv Shasha



By clicking deploy above you will deploy an Azure Logic App with Security Copilot Actions that will use Microsoft Sentinel incident trigger.<br>
This Logic app will change the status of the incident for active, will create dynamic tags (labels) and ill add them into sentinel incident tags, also this automation will calculate the incident severity based on MDTI enrichment and will modify the incident severity.
the automation will write the full investigation reports and the incident classification logic in the sentinel incident comment.<br>


### Prerequisites

Prior to beginning the installation process, it's crucial to confirm that you have met the following prerequisites: <br>
• The user that will deploy this Logic app need to have Contributor Role.<br>
• You enabled the Security Copilot license on your tenant <br>
• The user that authenticted in the Copilot logic app action, need to have Security Admin permission and Microsoft sentinel contributer (as its need to create incident comment).<br>
• This logic app can be run in a manual way, or in automatic way, if you select the automated way, you will need to create a new automation rule in Sentinel and configure this logic app as an action.<br>

### Deployment 

To deploy the above logic app, you need to<br>
•   Press on the Deploy option, select your subscription and the resource group (select the same tenant that Security Copilot is enabled)<br>

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FPlaybooks%2FCopilot-Sentinel_investigation-DynamicSev%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<br>
### Post Deployment

•   Authenticate with the users mention above (you can use different user for the Copilot actions and to the sentinel actions)<br>
•   To run the logic app in a manual way, open Microsoft Sentinel incident page, right click on specific incident and press run playbook, select logic app you just deploy and press run.<br>
•   To run the logic in automatic way, create an automation rule in sentinel and connect this playbook as the action for this rule.<br>


<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/ccbd305c539800eea2a1f7c1a0905aff954e2e25/Playbooks/Copilot-Sentinel_investigation-DynamicSev/images/full_logic_app.jpg"/>


