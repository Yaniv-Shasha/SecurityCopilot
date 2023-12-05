# Introduction 

#### Objectives

Upon completing this technical guide, you will gain the following abilities:<br>

· Upload a cusotm plug from GPT type.<br>
· Learn how to use the fetchUrl skill.<br>
· Generete report that will levrage the custom plugin source.<br>



#### Scenario
In this technical workshop, participants will learn how to upload a Security Copilot custom plugin of the GPT type.<br> 
To successfully complete this task, you must meet the following prerequisites:<br>

· You need your own tenant and Security Copilot instance.<br>
· You should have permission to upload a custom plugin.<br>



####  Instruction
    

### Upload the Custom Plugin 


1. Upload the custom plugin and check if its turn on

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/cfcd1baf606277478b7512be8bf3e43c7074f870/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/upload_plugin.jpg"/>


<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/cfcd1baf606277478b7512be8bf3e43c7074f870/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/check_if_plugin_isON.jpg
"/>

4. Execute the following prompts:

"Tell me a security-related joke for today."
Run the logic to send the above joke to this email: youremail@email.com.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/5314df248009d620c560f0b4b0b8b1bb8444848b/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/prompts.jpg"/>

5. To monitor the process, open the Logic App you just created and check the last runs.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/86e2ba5cab9da11622dfa5966aa86c1223b615d0/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/run_history.jpg"/>

	6. Open your inbox and examine the email.


    We are hoping it was funny :-)
