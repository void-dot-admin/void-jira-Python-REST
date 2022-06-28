# void-jira-Python-REST
A repo with Python REST API scripts for Jira Server & Data Center  

These scripts could not be created without the ```atlassian-python-api``` package  
created by the awesome people from: https://github.com/atlassian-api  
please give them a follow and you could find more information  
on how you can create your own scripts using their documentation below:  
https://atlassian-python-api.readthedocs.io/ 

# Usage Guide
In order to be able to use these Python scripts there are some steps needed as pre-condition:  
1. First make sure that you have Python v.3+ installed on your computer  
   you can check via CMD (command prompt) with ```py -V```  
   if you cannot find any version of Python on your pc, make sure you install it  
   if you install it and still cannot find the version via cmd  
   make sure you are in the right path, for me it worked with ```cd C:\Users\MyUsername\```  
   the above line in CMD should provide you the correct path to check with ```py -V```  
2. Make sure that you have "pip" installed & upgraded  
   you can directly write via CMD ```py -m pip install --upgrade pip```  
   you can also check the version of pip with ```py -m pip --version```  
3. Ensure that you have setuptools and wheel up to date  
   run via CMD ```py -m pip install --upgrade pip setuptools wheel```  
   you should see a confirmation that tools & wheel have been installed/upgraded  
4. The last step is to install atlassian-python-api  
   run via CMD ```py -m pip install atlassian-python-api```  
   you should see a lot of download & successful installation messages  

:exclamation: Make sure that you add the "atlassian-python-api" package to your IDE in order to run the scripts   
I personally use PyCharm, adding the package you installed at step 4 is eazy:  
  * Go to File -> Settings -> find "Project: pythonProject"  
    -> select Python Interpreter  -> on the right side window pree the plus icon ":heavy_plus_sign:"  
    -> search for ```atlassian-python-api``` -> click on it and press "Install Package" :white_check_mark:

# Find me on:
Youtube: https://www.youtube.com/channel/UCOv7EWVV4seJgHVB1AjJtUw  
Discord: https://discord.com/invite/KmhjNmZxhS
