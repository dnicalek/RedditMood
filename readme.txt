#TradeMood Project
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

If you prefer, you can manually execute reddit_data_downloader.py and main_processor.py
on your local device using a development environment such as PyCharm.
Follow these steps:
1) Open Your IDE: Launch your preferred Python development environment, for example, PyCharm.

2)Navigate to the Scripts: Using the IDE's file explorer,
navigate to the directory where reddit_data_downloader.py and main_processor.py are located.

3)Execute Scripts: Open each script in the IDE
and use the run or execute command to run them individually.
- for reddit_data_downloader.py, locate the script in your IDE, open it, and run or execute it.
- Similarly, do the same for main_processor.py.
This manual approach allows you to observe any console outputs
or errors directly within your development environment.
