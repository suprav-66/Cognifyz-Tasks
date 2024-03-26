#Building a web scraper using python libraries 
#pip install requests
#pip install BeautifulSoup 
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract information you want from the page
        # For example, let's say we want to extract all the links on the page
        links = soup.find_all('a')
        
        # Print the extracted links
        for link in links:
            print(link.get('href'))
    else:
        print("Failed to retrieve webpage. Status :", response.status_code)

# Example usage
if __name__ == "__main__":
    url = 'https://gietu.in'  # Replace with the URL of the website you want to scrape
    scrape_website(url)
