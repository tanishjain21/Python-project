import requests


def fetch_jokes_api():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/100"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        
        jokes = user_data["content"]
        jokes_id = user_data["id"]
        
        return jokes,jokes_id
    else:
        raise Exception ("failed to fetch jokes")
    


def main():
    try:
       jokes,jokes_id  = fetch_jokes_api()
       print(f"Joke:{jokes}\n  id: {jokes_id}")
    except Exception as e:
        print(str(e))
        
if  __name__ == "__main__":
    
    main()

        
         