# WebScraping
Web Scraping Tool – SQLite Database Overview This Python script scrapes paragraph text (

) from a target website and stores it in an SQLite database (scraped_data.db). It includes error handling, data validation, and retrieval functions to ensure smooth execution.

Features ✅ Scrapes text content from a website.

✅ Stores extracted data in an SQLite database.

✅ Implements error handling for connection failures.

✅ Retrieves and displays saved data from the database.

✅ Tracks execution time for efficiency.

✅ View the database directly in VS Code.

Prerequisites Before running the script, install the required dependencies:

pip install requests beautifulsoup4

Ensure Python 3.x is installed on your system.

How to Run the Script

Open VS Code & Navigate to Your Project
Open VS Code (or any terminal).

Use the terminal to navigate to the directory where your script is saved:

cd path/to/your/script

Run the Script Execute the script using:
python scraper.py

Expected Output Once the script runs successfully, you should see:

A message indicating successful data extraction.

The number of extracted paragraphs.

A new database file, scraped_data.db, created in the project folder.

Sample extracted data displayed in the terminal.

The execution time printed at the end.

How to View the Database Method 1: Using SQLite Viewer in VS Code

Install SQLite Viewer Extension

Open VS Code.

Go to Extensions (Ctrl+Shift+X).

Search for "SQLite Viewer".

Install the extension by Alex Covizzi.

Open the Database in VS Code

Go to the Explorer panel.

Right-click on scraped_data.db.

Select "Open Database" from the context menu.

Click on the "Browse" tab to view stored data.

Method 2: Using SQLite Command Line

Open your terminal and navigate to the project directory: cd path/to/your/script

Open the SQLite database: sqlite3 scraped_data.db

View stored data with: SELECT * FROM scraped_content LIMIT 10;

Method 3: Using DB Browser for SQLite

Download and install DB Browser for SQLite.

Open scraped_data.db in the browser.

Navigate to the "Browse Data" tab to see stored content.

Troubleshooting 🔹 Issue: "Database file not created."

Solution: Ensure you have write permissions in the project folder.

🔹 Issue: "No data found in the database."

Solution: The website might not contain

tags, or it may require JavaScript to load content. Try scraping another website.

🔹 Issue: "Failed to connect to the database."

Solution: Ensure that scraped_data.db exists in the directory and is not locked by another process.

Project Structure /WebScraper │── scraper.py # Main Python script │── scraped_data.db # SQLite database (created after running the script) │── README.md # Documentation

Contributors 👤 S Shreeshta Reddy
