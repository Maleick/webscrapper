# !/usr/bin/env python3

# webscrapper.py
# Author: Maleick
# Date: 04-12-2023
# Description: A simple web scraper using Beautiful Soup

import os
import tempfile
import argparse
import requests
from bs4 import BeautifulSoup

# Function to handle user input for the website URL
def get_input_url():
    url = input("Please enter the URL of the website you want to scrape: ")
    return url

# Function to create a temporary directory to hold the data
def create_temp_directory():
    temp_dir = tempfile.mkdtemp()
    print(f"Temporary directory created: {temp_dir}")
    return temp_dir

# Function to scrape the website
def scrape_website(url, verbose=False):
    # Send an HTTP request and get the content
    response = requests.get(url)
    content = response.content

    # Use Beautiful Soup to parse the content
    soup = BeautifulSoup(content, "html.parser")

    # Print the status if verbose mode is enabled
    if verbose:
        print("Scraping in progress...")

    # Find all the links and save them to a list
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)

            # Print the link if verbose mode is enabled
            if verbose:
                print(f"Found link: {href}")

    return links

# Function to save the scraped links to a file
def save_links_to_file(links, temp_dir):
    file_path = os.path.join(temp_dir, "scraped_links.txt")
    with open(file_path, "w") as f:
        for link in links:
            f.write(f"{link}\n")
    print(f"Links saved to file: {file_path}")

# Function to display the help menu
def display_help():
    help_text = '''
    Web Scraper with Beautiful Soup

    Options:
    -h, --help          Show this help message and exit
    -v, --verbose       Enable verbose mode
    -s, --save          Save the scraped data to a file

    Example:
    python webscrapper.py -v -s
    '''
    print(help_text)

def main():
    # ASCII Art banner
    banner = r"""
     _    _      _     _____                                      
    | |  | |    | |   /  ___|                                     
    | |  | | ___| |__ \ `--.  ___ _ __ __ _ _ __  _ __   ___ _ __ 
    | |/\| |/ _ \ '_ \ `--. \/ __| '__/ _` | '_ \| '_ \ / _ \ '__|
    \  /\  /  __/ |_) /\__/ / (__| | | (_| | |_) | |_) |  __/ |   
     \/  \/ \___|_.__/\____/ \___|_|  \__,_| .__/| .__/ \___|_|   
                                            | |   | |              
                                            |_|   |_|              
    """
    print(banner)

    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description="Web Scraper with Beautiful Soup", add_help=False)
    parser.add_argument("-v", "--verbose", help="Enable verbose mode", action="store_true")
    parser.add_argument("-s", "--save", help="Save the scraped data to a file", action="store_true")
    parser.add_argument("-h", "--help", help="Show this help message and exit", action="store_true")

    args = parser.parse_args()

    # Show the help menu if the help flag is present
    if args.help:
        display_help()
        return

    # Get the user input for the URL
    url = get_input_url()

    # Scrape the website with the given URL
    links = scrape_website(url, verbose=args.verbose)

    # Save the scraped links to a file if the save flag is present
    if args.save:
        temp_dir = create_temp_directory()
        save_links_to_file(links, temp_dir)

if __name__ == "__main__":
    main()