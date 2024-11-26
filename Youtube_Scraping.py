# Import necessary libraries for web scraping and data processing
from playwright.sync_api import sync_playwright  # Playwright for browser automation
import time  # Time library for delays
from bs4 import BeautifulSoup  # BeautifulSoup for parsing HTML content (not used in the current code but can be useful)
import pandas as pd  # Pandas for data manipulation and storing scraped data in a DataFrame
import os






# Save Extracted Data
def Save_Dataset(pd):

    Excutable = os.path.dirname(os.path.abspath(__file__))

    pd.to_csv(Excutable + "//Comments.csv")

    print(f"\nDataset Saved successfully in:-> {Excutable}\Comments.csv")

    print()
    #      print the dataset last 5 rows
    print("Extracted Data:-")
    print(pd.tail(5))


# Define a class for YouTube web scraping
class Youtube_Web_Scraping():

   # Initialize the class with the maximum scrolls, web link, and headless browser setting
   def __init__(self, Max_Scroll, Web_Link, Headless):
       self.link = Web_Link  # URL of the YouTube page
       self.num_scroll = Max_Scroll  # Maximum number of scrolls for loading more comments
       self.is_headless = Headless  # Whether the browser should run in headless mode

   # Function to launch and run the browser
   def Run_Browser(self):
       playwright = sync_playwright().start()  # Start the Playwright instance
       # Launch Chromium browser with headless setting
       browser = playwright.chromium.launch(headless=self.is_headless)
       print("\nBrowser is running...")
       page = browser.new_page()  # Open a new browser page
       page.goto(self.link)  # Navigate to the specified YouTube link
       page.wait_for_load_state()  # Wait until the page is fully loaded
       return page, browser  # Return the page and browser instances

   # Static method for scrolling the page
   @staticmethod
   def Scrolling(Page, Max_Scroll):

       for _ in range(Max_Scroll):  # Scroll down a specified number of times
           Page.evaluate("window.scrollBy(0, 1000)")  # Scroll down by 1000 pixels
           Page.wait_for_load_state()  # Wait for the page to load additional content
       # Locate the comment input area to verify if comments are loaded

       Page.wait_for_timeout(3000)  # Wait for 3 seconds for content to load
       return Page  # Return the page regardless

   # Static method to extract comments from the page
   @staticmethod
   def Extract_Comments(Page):


       # Get the page content
       html_content = Page.content()

       # Fetch all comments

       Content = BeautifulSoup(html_content,"html.parser")

       comments = Content.find_all("yt-attributed-string",class_="style-scope ytd-comment-view-model")


       All_comments = []
       # Extract and clean text from nested <span> tags
       for comment in comments:
           text = comment.get_text(strip=True)  # Get only the text content
           All_comments.append(text)


       # Check if Comments list not empty
       if(len(All_comments)!=0):

         return Save_Dataset(pd.DataFrame({"comments": All_comments}))  # Function To save extracted dataset

       else:

           print("\nNo data Extracted from web please re-run the script")
