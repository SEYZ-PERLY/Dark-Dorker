# Dark Dorker

Dark Dorker is a Python script that allows you to perform searches on the regular web using DuckDuckGo and on the Dark Web using Ahmia. It provides a simple command-line interface with an animated banner and colored output.

## Features

* **Web Search:** Uses the DuckDuckGo API to fetch relevant results.
* **Dark Web Search:** Queries Ahmia to retrieve results from the Tor network.
* **CLI Interface:** Displays a colorful and animated banner.
* **Translation:** Automatically translates search results to your chosen language.
* **Deep Search:** If no results are initially found, the script performs a deeper search.
* **Language Selection:** You can choose the language for your search results.
* **Tor Compatibility:** Supports requests via a SOCKS5 proxy.

## Requirements

Before running this script, ensure you have the following dependencies installed:

* Python 3.x
* Requests (`pip install requests`)
* BeautifulSoup4 (`pip install beautifulsoup4`)
* googletrans (`pip install googletrans==4.0.0-rc1`)
* Tor (required for Dark Web searches)

## Installation

1.  Clone this repository:

    ```bash
    git clone [https://github.com/SEYZ-PERLY/Dark-Dorker.git](https://github.com/SEYZ-PERLY/Dark-Dorker.git)
    cd Dark-Dorker
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Start Tor on your system (ensure the SOCKS5 proxy is running on 127.0.0.1:9050).

4.  Run the script:

    ```bash
    python main.py
    ```

## Usage

1.  When launched, the script displays an animated banner and provides three search options:

    * Regular Web Search
    * Dark Web Search
    * Change Language

2.  Choose an option by entering "1", "2", or "3", then type your search query.

3.  The results will be displayed with a title and a link, in your chosen language.

4.  After each search, you can enter a new query or exit the program.

## Disclaimer

This script is provided to help you understand how search engines work and how to access different information on the internet. It's important to use it responsibly and ethically.

* **Respect the law:** Do not use this script to access illegal content or to infringe copyrights.
* **Protect your information:** Never share sensitive personal information on the Dark Web.
* **Be cautious:** The Dark Web can contain shocking or dangerous content. Do not click on suspicious links or download unknown files.
* **Use a VPN:** For added security, use a virtual private network (VPN) when accessing the Dark Web.

Remember, you are responsible for how you use this script. The author cannot be held responsible for your actions.
