import requests
import time
import os
from bs4 import BeautifulSoup
from googletrans import Translator

def clear_screen():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Affiche une bannière au démarrage."""
    banner = '''
  LOADING...
    '''
    columns = os.get_terminal_size().columns
    banner_lines = banner.split('\n')
    for line in banner_lines:
        print(f"\033[1;31m{' ' * ((columns - len(line)) // 2)}{line}\033[0m")
        time.sleep(0.3)
        clear_screen()

def search_web(query, language='en-US'):
    """Effectue une recherche sur le web avec DuckDuckGo."""
    search_engine = f'https://api.duckduckgo.com/?q={query}&format=json&kl={language}'
    try:
        response = requests.get(search_engine, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'RelatedTopics' not in data or not data['RelatedTopics']:
            return []
        results = []
        for topic in data['RelatedTopics']:
            if 'Text' in topic and 'FirstURL' in topic:
                title = topic['Text']
                url = topic['FirstURL']
                results.append(f"{title} - {url}")
        return results
    except requests.exceptions.RequestException as e:
        return [f"[ERROR] Problème avec l'API DuckDuckGo: {str(e)}"]

def search_tor(query):
    """Effectue une recherche sur le Dark Web avec Ahmia."""
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    dark_web_engine = f'http://ahmia.fi/search/?q={query}'
    try:
        response = requests.get(dark_web_engine, proxies=proxies, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', {'class': 'search-result'})
        if not links:
            return []
        results = []
        for link in links:
            title = link.get_text()
            link_url = link['href']
            results.append(f"{title} - {link_url}")
        return results
    except requests.exceptions.RequestException as e:
        return [f"[ERROR] Impossible de récupérer les résultats. {str(e)}"]

def translate_results(results, target_language='fr'):
    """Traduit les résultats de recherche."""
    translator = Translator()
    translated_results = []
    for result in results:
        try:
            translation = translator.translate(result, dest=target_language)
            translated_results.append(translation.text)
        except Exception as e:
            translated_results.append(f"[ERROR] Traduction impossible: {str(e)}")
    return translated_results

def deep_search(query, language='en-US'):
    """Effectue une recherche approfondie sur DuckDuckGo."""
    search_engine = f'https://html.duckduckgo.com/html/?q={query}&kl={language}'
    try:
        response = requests.get(search_engine, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', {'class': 'result__a'})
        results = []
        for link in links:
            title = link.text
            url = link['href']
            results.append(f"{title} - {url}")
        return results
    except requests.exceptions.RequestException as e:
        return [f"[ERROR] Problème avec l'API DuckDuckGo: {str(e)}"]

def main():
    """Fonction principale du programme."""
    clear_screen()
    display_banner()
    time.sleep(2)
    clear_screen()

    default_language = 'fr'  # Langue par défaut
    current_language = default_language

    while True:
        print(f"\033[1;32m[INFO] Langue actuelle: {current_language}\033[0m")
        print("\033[1;32m[INFO] Choisir l'option de recherche:\033[0m")
        print("1. Web normal")
        print("2. Dark Web")
        print("3. Changer la langue") # Option pour changer la langue
        print("Tapez 'exit' pour quitter.\n")
        choice = input("Entrez 1, 2 ou 3 pour choisir: ").strip().lower()

        if choice == 'exit':
            clear_screen()
            break
        elif choice == '3': # Changer la langue
            new_language = input("Entrez le nouveau code de langue (par exemple, en-US, fr-FR): ").strip()
            if len(new_language) != 5 or '-' not in new_language:
                print("\033[1;33m[ERROR] Code de langue invalide. Format attendu: xx-XX (par exemple, en-US).\033[0m")
                time.sleep(1.5)
                clear_screen()
                continue
            current_language = new_language
            continue
        elif choice not in ['1', '2', '3']: # Modification ici
            print("\033[1;33m[ERROR] Choix invalide, essayez à nouveau.\033[0m")
            time.sleep(1.5)
            clear_screen()
            continue

        query = input("Entrez votre requête de recherche: ").strip()

        if choice == '1':
            print(f"\033[1;32m[INFO] Recherche en cours: {query}...\033[0m\n")
            results = search_web(query, current_language)
        elif choice == '2':
            print(f"\033[1;32m[INFO] Recherche sur le Dark Web en cours: {query}...\033[0m\n")
            results = search_tor(query)

        if results:
            print("\n\033[1;34mRésultats trouvés:\033[0m\n")
            translated_results = translate_results(results, current_language)
            for result in translated_results:
                print(f"- \033[1;37m{result}\033[0m")
        else:
            print("\033[1;33mAucun résultat trouvé. Recherche approfondie en cours...\033[0m\n")
            deep_results = deep_search(query, current_language)
            if deep_results:
                print("\n\033[1;34mRésultats de la recherche approfondie:\033[0m\n")
                translated_deep_results = translate_results(deep_results, current_language)
                for result in translated_deep_results:
                    print(f"- \033[1;37m{result}\033[0m")
            else:
                print("\033[1;33mAucun résultat trouvé même après une recherche approfondie.\033[0m\n")

        print("\n\033[1;32mAppuyez sur Entrée pour effectuer une nouvelle recherche ou tapez 'exit' pour quitter...\033[0m")
        user_input = input().strip().lower()
        if user_input == 'exit':
            clear_screen()
            break
        clear_screen()

if __name__ == '__main__':
    main()
