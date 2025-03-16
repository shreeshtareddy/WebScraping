import requests
import sqlite3
import time
from bs4 import BeautifulSoup


start_time = time.time()


DB_NAME = "scraped_data.db"

# Function to connect to the database
def connect_db():
    return sqlite3.connect(DB_NAME)

# Function to create a table
def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS scraped_content") 
    cursor.execute("""
        CREATE TABLE scraped_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paragraph TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Database setup complete.")

# Function to fetch and parse webpage
def scrape_website(url):
    print(f"Fetching data from: {url} ...")
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            print("Page successfully loaded.")
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(f"Failed to load page. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

# Function to extract and save data
def extract_and_store(soup):
    if not soup:
        print("No content to extract.")
        return
    
    paragraphs = soup.find_all("p")
    print(f"Found {len(paragraphs)} paragraphs.")

    conn = connect_db()
    cursor = conn.cursor()
    
    saved_count = 0
    for para in paragraphs:
        text = para.get_text(strip=True)
        if text:
            cursor.execute("INSERT INTO scraped_content (paragraph) VALUES (?)", (text,))
            saved_count += 1

    conn.commit()
    conn.close()
    print(f"Stored {saved_count} paragraphs in the database.")

# Function to display stored data
def display_data(limit=10):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT paragraph FROM scraped_content LIMIT {limit}")
    rows = cursor.fetchall()
    
    print("\n--- Previewing Stored Data ---")
    for row in rows:
        print(row[0])

    conn.close()

# Main execution
if __name__ == "__main__":
    setup_database()  # Prepare database
    URL = "https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/"  # Change this to your target URL
    soup = scrape_website(URL)
    extract_and_store(soup)
    display_data()

    # Execution time
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.2f} seconds")
