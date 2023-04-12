# Web Scraper with Beautiful Soup

A simple web scraper that uses the Beautiful Soup library in Python to scrape links from a given URL. The script allows the user to input a website URL, includes a help menu that explains available options, and provides a verbose mode to display progress tracking. Additionally, it offers the option to save the scraped files to a temporary directory.

## Installation

1. Clone the repository:

```git clone https://github.com/Maleick/webscrapper.git```

2. Change the directory:

```cd webscrapper```

3. Install the required dependencies:

``` pip install -r requirements.txt```


## Usage

Run the script using the following command:

```python webscrapper.py [options]```


### Options

- `-h`, `--help`: Show the help menu and exit.
- `-v`, `--verbose`: Enable verbose mode for progress tracking.
- `-s`, `--save`: Save the scraped data to a file.

### Example

To run the script with verbose mode and save the scraped data to a file, use the following command:

```python webscrapper.py -v -s```
