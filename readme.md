# TradeMood: an app for monitoring and forecasting investor sentiments

TradeMood is an  application leveraging state-of-the-art natural language processing techniques to analyze sentiment from Reddit user discussions. The project employs a fine-tuned BERT model to assess sentiment across various cryptocurrency-related discussions on Reddit. 
Through a modular architecture, it efficiently gathers, processes, and analyzes Reddit data to provide valuable insights to users.

![417310641_355446647351929_2775448231361787738_n](https://github.com/dnicalek/TradeMood/assets/85755046/544cdae0-fcc7-49f4-b648-4b75819c2a1d)
![420096186_1060556711859623_7879777516756496644_n](https://github.com/dnicalek/TradeMood/assets/85755046/1fbe73f5-deb5-43e2-ab5f-ce626bf9963d)
![420086803_300385883031258_8371382278944011289_n](https://github.com/dnicalek/TradeMood/assets/85755046/6b3bfa01-3c28-4083-bf81-4669142b3d16)
![420444720_353543184109956_413422663852504775_n](https://github.com/dnicalek/TradeMood/assets/85755046/99625d93-b8ab-4c37-8c7d-89bb1b6ae667)


## Features:

- Reddit Data Acquisition Module: This module interfaces with the Reddit API through PRAW to gather posts, comments, and replies relevant to cryptocurrency discussions. It fetches data in real-time to ensure the latest information is analyzed.

- Data Processing and Storage Module: After fetching the Reddit data, this module processes and stores it in appropriate formats. Utilizing NLTK for text data cleaning and normalization ensures high-quality input for sentiment analysis.

- Sentiment Analysis Module: The core component of the application, this module employs a trained BERT model to analyze the sentiment of Reddit discussions. It provides graphical representations of sentiment trends over time.

- Reddit User Activity Analysis Module: This module calculates the daily and weekly volatility of Reddit user activities related to various cryptocurrencies. By measuring the percentage change in the number of posts, comments, and replies, it offers insights into community engagement dynamics.

- Database Integration with Google Firestore: Results from sentiment analysis and user activity calculations are stored and transmitted to Google Firestore, ensuring secure and scalable data management.

- Mobile and Web Application Interface: Users access sentiment analysis results and user activity trends through intuitive graphical representations in both mobile and web applications. Real-time updates ensure users have access to the latest insights.

- Cryptocurrency Price Tracker: Alongside sentiment analysis and user activity trends, the application provides real-time cryptocurrency prices, enabling users to correlate market sentiment with price movements.

- Interactive Discussion Board: Registered users can engage in discussions and share insights on a dedicated discussion board within the application. This fosters a collaborative environment for cryptocurrency enthusiasts to exchange ideas and information.


## How to run a project? 
1. Open PowerShell:
You can open PowerShell by typing "PowerShell" in the Start menu.
Once open, navigate to the directory where you have saved your script.
Set-Location "path\to\your\script\directory"

2. Enabling Script Execution: If you haven't set the script execution policy, you may need to change it.
Run PowerShell as an administrator and enter the following command:
Set-ExecutionPolicy RemoteSigned

3. Run the Script:
In PowerShell, enter the command to execute your script:
.\run_trade_mood.ps1

If you prefer, you can manually execute reddit_data_downloader.py and main_processor.py
on your local device using a development environment such as PyCharm.
Follow these steps:
1) Open Your IDE: Launch your preferred Python development environment, for example, PyCharm.

2) Navigate to the Scripts: Using the IDE's file explorer,
navigate to the directory where reddit_data_downloader.py and main_processor.py are located.

3) Execute Scripts: Open each script in the IDE
and use the run or execute command to run them individually.
- for reddit_data_downloader.py, locate the script in your IDE, open it, and run or execute it.
- Similarly, do the same for main_processor.py.
This manual approach allows you to observe any console outputs
or errors directly within your development environment.
