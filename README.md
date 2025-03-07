# Dark Dorker

Dark Dorker is a Python script that allows you to perform searches on the regular web using DuckDuckGo and on the Dark Web using Ahmia. It provides a simple command-line interface with an animated banner and colored output.

## Features

- Web Search: Uses the DuckDuckGo API to fetch relevant results.  
- Dark Web Search: Queries Ahmia to retrieve results from the Tor network.  
- CLI Interface: Displays a colorful and animated banner.  
- Tor Compatibility: Supports requests via a SOCKS5 proxy.  

## Requirements

Before running this script, make sure you have the necessary dependencies installed:

- Python 3.x  
- Requests (`pip install requests`)  
- BeautifulSoup4 (`pip install beautifulsoup4`)  
- Tor (required for Dark Web searches)  

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/dark-dorker.git
   cd dark-dorker

2. Install the dependencies:

```bash
pip install -r requirements.txt

3. Start Tor on your system (make sure the SOCKS5 proxy is running on 127.0.0.1:9050).

4. Run the script:

```bash
python main.py

## Usage

1. When launched, the script displays an animated banner and provides two search options:

```bash
Regular Web Search
Dark Web Search

2. Choose an option by entering "1" or "2", then type your search query.

3. The results will be displayed as a list with a title and a link.

4. After each search, you can enter a new query or exit the program.

## Disclaimer

This script is provided for educational purposes only. Accessing the Dark Web carries risks and should be done responsibly. The author of this script is not responsible for how it is used.

You can copy and paste this into your `README.md` file.

