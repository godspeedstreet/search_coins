import requests
import re

def fetch_data():
    url = "https://openapi.bitunix.com/api/spot/v1/common/coin/coin_network/list"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
        return None

def extract_tokens(data):
    code_chain_ca = []
    for coin in data.get("data", []):
        coin_name = coin.get("name", "N/A") 
        networks = coin.get("networks", [])
        for network in networks:
            chain = network.get("chain", "N/A").split("_")[0].lower()  
            contract = network.get("contractAddress", "") or "" 

            
            match = re.search(r'0x[a-fA-F0-9]{40}', contract)
            contract = match.group(0) if match else "N/A"  

            code_chain_ca.append((chain, coin_name, contract))
    return code_chain_ca

if __name__ == "__main__":
    data = fetch_data()
    if data:
        tokens = extract_tokens(data)
        print("\nСписок токенов (chain, name, contractAddress):")
        for token in tokens:
            print(token)
