import requests
import time
import os
from bs4 import BeautifulSoup

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Displays the Dark Dorker banner at startup, centered and blinking red."""
    banner = '''
  LOADING...
    '''
    columns = os.get_terminal_size().columns
    banner_lines = banner.split('\n')
    
    for line in banner_lines:
        print(f"\033[1;31m{' ' * ((columns - len(line)) // 2)}{line}\033[0m")
        time.sleep(0.3) # Delay for blinking effect
        clear_screen()

def search_web(query):
    """Performs search on DuckDuckGo using the JSON API."""
    # Split the query into separate words
    keywords = query.split()
    
    search_engine = f'https://api.duckduckgo.com/?q={query}&format=json'
    
    try:
        response = requests.get(search_engine, timeout=10)
        response.raise_for_status() # Check if HTTP response is OK
        
        data = response.json()
        
        # If no response is found
        if 'RelatedTopics' not in data or not data['RelatedTopics']:
            return ["No results found."]
        
        results = []
        for topic in data['RelatedTopics']:
            if 'Text' in topic and 'FirstURL' in topic:
                title = topic['Text']
                url = topic['FirstURL']
                # Check if all keywords are present in the title
                if all(keyword.lower() in title.lower() for keyword in keywords):
                    results.append(f"{title} - {url}")
        
        if not results:
            return ["No results found."]
        
        return results
    
    except requests.exceptions.RequestException as e:
        return [f"[ERROR] Problem with DuckDuckGo API: {str(e)}"]

def search_tor(query):
    """Performs search on Ahmia (Dark Web)."""
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    dark_web_engine = f'http://ahmia.fi/search/?q={query}'

    try:
        response = requests.get(dark_web_engine, proxies=proxies, timeout=10)
        response.raise_for_status() # Check if HTTP response is OK
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find links on the results page
        links = soup.find_all('a', {'class': 'search-result'})

        if not links:
            return ["No results found."]
        
        results = []
        for link in links:
            title = link.get_text()
            link_url = link['href']
            # Check if all keywords are present in the title
            if all(keyword.lower() in title.lower() for keyword in query.split()):
                results.append(f"{title} - {link_url}")
        
        if not results:
            return ["No results found."]
        
        return results
    except requests.exceptions.RequestException as e:
        return [f"[ERROR] Could not retrieve results. {str(e)}"]

def main():
    """Main function of the program."""
    clear_screen()
    display_banner()

    time.sleep(2)
    clear_screen()

    while True:
        print("\033[1;32m[INFO] Choose search option:\033[0m")
        print("1. Regular Web")
        print("2. Dark Web (start Tor Browser in background)")
        print("Type 'exit' to quit.\n")
        
        choice = input("Enter 1 or 2 to choose search type: ").strip().lower()
        
        if choice == 'exit':
            clear_screen()
            break
        elif choice not in ['1', '2']:
            print("\033[1;33m[ERROR] Invalid choice, try again.\033[0m")
            continue
        
        query = input("Enter your search query: ").strip()
        
        if choice == '1':
            print(f"\033[1;32m[INFO] Searching for: {query}...\033[0m\n")
            results = search_web(query)
        elif choice == '2':
            print(f"\033[1;32m[INFO] Searching Dark Web for: {query}...\033[0m\n")
            results = search_tor(query)

        # Display results
        if results:
            print("\n\033[1;34mResults found:\033[0m\n")
            for result in results:
                print(f"- \033[1;37m{result}\033[0m")
        else:
            print("\033[1;33mNo results found.\033[0m\n")
        
        print("\n\033[1;32mPress Enter to search again or type 'exit' to quit...\033[0m")
        user_input = input().strip().lower()
        if user_input == 'exit':
            clear_screen()
            break
        clear_screen()

if __name__ == '__main__':
    main()
