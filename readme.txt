1.Open PowerShell:
You can open PowerShell by typing "PowerShell" in the Start menu.
Once open, navigate to the directory where you have saved your script.
Set-Location "path\to\your\script\directory"

2.Enabling Script Execution: If you haven't set the script execution policy, you may need to change it.
Run PowerShell as an administrator and enter the following command:
Set-ExecutionPolicy RemoteSigned

3.Run the Script:
In PowerShell, enter the command to execute your script:
.\run_trade_mood.ps1
