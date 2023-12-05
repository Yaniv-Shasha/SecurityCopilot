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


1. Obtain the file named "DefangsURLs.yaml" from this directory.<br>
2. Inspect it to appreciate the simplicity of creating a GPT-type plugin.<br>
3. Upload the custom plugin and verify if it's activated.<br>

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/cfcd1baf606277478b7512be8bf3e43c7074f870/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/upload_plugin.jpg"/>


<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/f15ba2df94fbba97cb9adf70426cdf4d471b28fb/Workshop/Custom_Plugin/Task02_Defang_URL/images/plugin-turnON.jpg"/>


####  Use case

4. Execute the following prompts:

"Tell me a security-related joke for today."
Run the logic to send the above joke to this email: youremail@email.com.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/5314df248009d620c560f0b4b0b8b1bb8444848b/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/prompts.jpg"/>

5. To monitor the process, open the Logic App you just created and check the last runs.

<img src="https://github.com/Yaniv-Shasha/SecurityCopilot/blob/86e2ba5cab9da11622dfa5966aa86c1223b615d0/Workshop/Custom_Plugin/Task01_Send_jokeByemail/Images/run_history.jpg"/>

	6. Open your inbox and examine the email.


    We are hoping it was funny :-)
