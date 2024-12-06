# this is the app/drinks_challenge.py file...

# LOCAL DEV (ENV VARS)

import requests
import json

def fetch_drinks_json(n=20):

    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)

    full_drinks_list = parsed_response["drinks"]

    drinks_list = full_drinks_list[:n]

    return drinks_list

if __name__ == "__main__":

    data = fetch_drinks_json()
    print(data)
