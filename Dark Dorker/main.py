import requests
import time
import os
from bs4 import BeautifulSoup

def clear_screen():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Affiche la bannière Dark Dorker au démarrage, centrée et clignotante en rouge."""
    banner = '''
  LOADING...
    '''
    columns = os.get_terminal_size().columns
    banner_lines = banner.split('\n')
   
    for line in banner_lines:
        print(f"\033[1;31m{' ' * ((columns - len(line)) // 2)}{line}\033[0m")
        time.sleep(0.3) # Délai pour l'effet de clignotement
        clear_screen()

def search_web(query):
    """Effectue la recherche sur DuckDuckGo en utilisant l'API JSON."""
    # Diviser la requête en mots séparés
    keywords = query.split()
   
    search_engine = f'https://api.duckduckgo.com/?q={query}&format=json'
   
    try:
        response = requests.get(search_engine, timeout=10)
        response.raise_for_status() # Vérifier si la réponse HTTP est OK
        
        data = response.json()
        
        # Si aucune réponse n'est trouvée
        if 'RelatedTopics' not in data or not data['RelatedTopics']:
            return ["Aucun résultat trouvé."]
        
        results = []
        for topic in data['RelatedTopics']:
            if 'Text' in topic and 'FirstURL' in topic:
                title = topic['Text']
                url = topic['FirstURL']
                # Vérifier si tous les mots-clés sont présents dans le titre
                if all(keyword.lower() in title.lower() for keyword in keywords):
                    results.append(f"{title} - {url}")
        
        if not results:
            return ["Aucun résultat trouvé."]
       
        return results
   
    except requests.exceptions.RequestException as e:
        return [f"[ERROR] Problème avec DuckDuckGo API : {str(e)}"]

def search_tor(query):
    """Effectue la recherche sur Ahmia (Dark Web)."""
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    dark_web_engine = f'http://ahmia.fi/search/?q={query}'

    try:
        response = requests.get(dark_web_engine, proxies=proxies, timeout=10)
        response.raise_for_status() # Vérifier si la réponse HTTP est OK
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Cherche les liens sur la page de résultats
        links = soup.find_all('a', {'class': 'search-result'})

        if not links:
            return ["Aucun résultat trouvé."]
       
        results = []
        for link in links:
            title = link.get_text()
            link_url = link['href']
            # Vérifier si tous les mots-clés sont présents dans le titre
            if all(keyword.lower() in title.lower() for keyword in query.split()):
                results.append(f"{title} - {link_url}")
       
        if not results:
            return ["Aucun résultat trouvé."]
       
        return results
    except requests.exceptions.RequestException as e:
        return [f"[ERROR] Impossible de récupérer les résultats. {str(e)}"]

def main():
    """Fonction principale du programme."""
    clear_screen()
    display_banner()

    time.sleep(2)
    clear_screen()

    while True:
        print("\033[1;32m[INFO] Choisissez l'option de recherche:\033[0m")
        print("1. Web classique")
        print("2. Dark Web (lancer Tor Browser en arrière plan")
        print("Tapez 'exit' pour quitter.\n")
       
        choice = input("Entrez 1 ou 2 pour choisir le type de recherche: ").strip().lower()
       
        if choice == 'exit':
            clear_screen()
            break
        elif choice not in ['1', '2']:
            print("\033[1;33m[ERROR] Choix invalide, essayez à nouveau.\033[0m")
            continue
       
        query = input("Entrez votre requête de recherche: ").strip()
       
        if choice == '1':
            print(f"\033[1;32m[INFO] Recherche pour: {query}...\033[0m\n")
            results = search_web(query)
        elif choice == '2':
            print(f"\033[1;32m[INFO] Recherche sur le Dark Web pour: {query}...\033[0m\n")
            results = search_tor(query)

        # Affichage des résultats
        if results:
            print("\n\033[1;34mRésultats trouvés:\033[0m\n")
            for result in results:
                print(f"- \033[1;37m{result}\033[0m")
        else:
            print("\033[1;33mAucun résultat trouvé.\033[0m\n")
       
        print("\n\033[1;32mAppuyez sur Entrée pour faire une nouvelle recherche ou tapez 'exit' pour quitter...\033[0m")
        user_input = input().strip().lower()
        if user_input == 'exit':
            clear_screen()
            break
        clear_screen()

if __name__ == '__main__':
    main()

