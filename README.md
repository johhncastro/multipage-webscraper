"""
# Multi-Movie Transcript Web Scraping Script

## Overview

This Python script is designed to scrape transcripts from multiple movies from a website using the BeautifulSoup library for HTML parsing and the Requests library for fetching web pages. It offers a more versatile solution compared to the previous example, allowing you to scrape transcripts for numerous movies listed on the target website (https://subslikescript.com/movies).

## Script Workflow

1. **Import Libraries**: The script begins by importing the necessary libraries, BeautifulSoup and Requests.

2. **Fetching Web Content**: It sends an HTTP request to the main movie listing page (https://subslikescript.com/movies) to retrieve the HTML content of the page.

3. **HTML Parsing**: BeautifulSoup is used to parse the HTML content, making it easier to navigate and extract specific elements.

4. **Extracting Movie Links**: The script identifies and extracts the links to individual movie pages from the main listing page. These links are stored in the `links` list.

5. **Iterating Over Movie Pages**: It then iterates through each movie link and performs the following steps for each movie:

   - Sends an HTTP request to the movie's page to retrieve its HTML content.
   - Parses the HTML content.
   - Extracts the title of the movie and the transcript text.
   - Writes the transcript to a text file named after the movie's title.

6. **File Naming**: Each transcript is saved in a separate text file named after the movie's title, providing easy identification and access.

## How to Use

1. Ensure you have Python installed on your system.

2. Install the required libraries using pip:
3. pip install beautifulsoup4 
4. pip install requests

5. Copy and paste the provided script into a Python file (e.g., `multi_movie_transcript_scraper.py`).

6. Run the script, and it will fetch and save the transcripts of multiple movies listed on the website.

## Benefits

- **Automation**: The script automates the process of scraping transcripts for multiple movies from a web page, eliminating the need for manual extraction.

- **Data Accessibility**: Extracted transcripts for each movie are stored in separate files for easy access and reference.

- **Scalability**: This script can be used to scrape transcripts for an extensive list of movies by simply modifying the target website or listing page.

## Conclusion

This Python script provides a flexible solution for scraping transcripts from multiple movies listed on a web page. By leveraging BeautifulSoup and Requests, it streamlines the process of collecting dialogue data from various sources, making it a valuable tool for movie enthusiasts and researchers.
"""


