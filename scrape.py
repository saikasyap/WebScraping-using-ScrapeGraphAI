import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = 'https://www.wisdomlib.org/glossary'

print("hello")
# Send an HTTP GET request to the website
response = requests.get(url)
print(response)
# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the request using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all glossary items (assuming they are in <li> elements within a <ul>)
    glossary_items = soup.find_all('li', class_='glossary-item')
    
    # Initialize a list to store the scraped data
    glossary_data = []
    
    # Loop through each glossary item and extract the term and description
    for item in glossary_items:
        term = item.find('a').text.strip()  # Get the term
        description = item.find('p').text.strip() if item.find('p') else ''  # Get the description
        
        # Append the term and description to the list as a tuple
        glossary_data.append((term, description))
    
    # Print the scraped data
    for term, description in glossary_data:
        print(f'Term: {term}')
        print(f'Description: {description}')
        print('-' * 80)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
