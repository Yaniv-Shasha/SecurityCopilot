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

<br>




<br>

### Deployment 

To deploy the above logic app, you need to<br>
•   Press on the Deploy option, select your subscription and the resource group (select the same tenant that Security Copilot is enabled)<br>

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FYaniv-Shasha%2FSecurityCopilot%2Fmain%2FSolutions%2FUserreportedphishing%2Fazuredeploy.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<br>

### Post Deployment

•   Authenticate with the users mention above (you can use different user for the Copilot actions and to the sentinel actions)<br>
•   To run the logic app in a manual way, open Microsoft Sentinel incident page, right click on specific incident and press run playbook, select logic app you just deploy and press run.<br>
•   To run the logic in automatic way, create an automation rule in sentinel and connect this playbook as the action for this rule.<br>


<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/ccbd305c539800eea2a1f7c1a0905aff954e2e25/Playbooks/Copilot-Sentinel_investigation-DynamicSev/images/full_logic_app.jpg"/>


