import requests
from bs4 import BeautifulSoup
import re

def extract_email(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        emails = re.findall(r"[\w\.-]+@[\w\.-]+", soup.text)
        return emails[0] if emails else None

    except:
        return None
