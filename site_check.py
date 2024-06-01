import requests
from bs4 import BeautifulSoup

def does_still_exists(url: str, text: str):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    exact_match = soup.find(text=text)

    if exact_match:
        return True
    
    return False



        