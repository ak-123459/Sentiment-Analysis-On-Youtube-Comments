# Import necessary libraries and modules
import os  # For operating system interactions (not used directly in this script but included)
import Youtube_Scraping  # Import the custom `Youtube_Scraping` module containing the class definition

# Define a function to handle the entire scraping process
def run_all():
    # Prompt the user to enter a YouTube video link
    Weblink = input("Enter video link: ").strip()  # Use `strip()` to remove any surrounding whitespace
    # Prompt the user to enter the maximum number of scrolls
    Max_Scrolling = input("Max Scrolling(eg. 100): ")  # Input is taken as a string and converted to an integer later

    # Instantiate the `Youtube_Web_Scraping` class with user inputs
    # Parameters: max scrolls (converted to int), video link, headless=False (browser is visible)
    obj = Youtube_Scraping.Youtube_Web_Scraping(int(Max_Scrolling), Weblink, True)

    # Run the browser and open the specified YouTube video link
    # Returns a page object and browser instance
    page, browser = obj.Run_Browser()

    # Perform scrolling on the YouTube page to load more comments
    # Scrolls down the specified number of times
    page = obj.Scrolling(page, int(Max_Scrolling))

    # Extract comments from the loaded page and print them
    comments_df = obj.Extract_Comments(page)  # Extract comments into a Pandas DataFrame

    # Close the browser after extracting comments
    browser.close()

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    run_all()  # Call the `run_all` function to start the process
