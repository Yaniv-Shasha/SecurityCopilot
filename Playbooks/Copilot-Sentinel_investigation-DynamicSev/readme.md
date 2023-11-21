# Copilot-Sentinelinvestigation-DynamicSev
author: Yaniv Shasha


By clicking deploy above you will deploy an Azure Logic App with Security Copilot Actions that will use Microsoft Sentinel incident trigger, this logic app will change the status of the incident for active, will create dynamic tags (labels) and ill add them into sentinel incident tags, also this automation will calculate the incident severity based on MDTI enrichment and will modify the incident severity.
the automation will write the full investigation reports and the incident classification logic in the sentinel incident comment.<br>


### Prerequisites

Prior to beginning the installation process, it's crucial to confirm that you have met the following prerequisites: <br>
• The user that will deploy this Logic app need to have Contributor Role.<br>
• You enabled the Security Copilot license on your tenant <br>
• The user that authenticted in the Copilot logic app action, need to have Security Admin permission and Microsoft sentinel contributer (as its need to create incident comment).<br>
• This logic app can be run in a manual way, or in automatic way, if you select the automated way, you will need to create a new automation rule in Sentinel and configure this logic app as an action.<br>

### Deployment 

To deploy the above logic app, you need to<br>
•	Press on the Deplot opetion, select your subscription and the respource group (this need to be resource under the same tenant that Security Copilot is enabled<br>
•	select .<br>
•	Workbook – act as the presentation layer.<br>
