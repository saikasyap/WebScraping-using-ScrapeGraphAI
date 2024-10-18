import csv
import json
import nest_asyncio
from scrapegraphai.graphs import SmartScraperGraph
import os
os.environ['CUDA_VISIBLE_DEVICES'] ='3'
# Apply nest_asyncio to handle async issues in Jupyter or similar environments
nest_asyncio.apply()

# Configuration settings for the scraper graph
graph_config = {
    "llm": {
        "model": "ollama/gemma2",  # Specifies the large language model to use
        "temperature": 0,          # Temperature controls randomness; 0 makes it deterministic
        "format": "json",          # Output format is set to JSON
        "base_url": "http://localhost:11434",  # Base URL where the Ollama server is running
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specifies the embedding model to use
        "temperature": 0,                    # Keeps the generation deterministic
        "base_url": "http://localhost:11434",  # Base URL for the embeddings model server
    },
    "verbose": True,  # Enables verbose output for more detailed log information
}

# Load URLs from the CSV file
urls = []
with open('/home/SaiKashyap/ner/glossary_terms.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        urls.append(row[1])  # Assumes that the URLs are in the first column

# Dictionary to hold the results
scraping_results = {}

# Iterate over each URL from the CSV file
for url in urls:
    try:
        # Create an instance of SmartScraperGraph for each URL
        smart_scraper_graph = SmartScraperGraph(
            prompt="Extract Sanskrit dictionary and Relevant Text separately",
            source=url,  # Use the current URL
            config=graph_config
        )

        # Run the scraper and store the result
        result = smart_scraper_graph.run()
        
        # Save the result in the dictionary with the URL as the key
        scraping_results[url] = result
    
    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")

# Save the scraping results to a JSON file
with open('scraping_results.json', 'w') as output_file:
    json.dump(scraping_results, output_file, indent=4)

print("Scraping completed and results saved to 'scraping_results.json'")
