import requests
import pandas as pd

def get_top_crypto_info():
    api_key = '74399dc4-89e3-46f5-9d34-a1b3b3c8d1a2'
    api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'limit': 250,
        'convert': 'USD',
    }
    headers = {
        'X-CMC_PRO_API_KEY': api_key,
    }

    # Excel dosyasını oku
    excel_read = pd.read_excel('track.xlsx')

    response = requests.get(api_url, params=parameters, headers=headers)

    if response.status_code == 200:
        data = response.json()
        top_cryptos = data['data']

        for crypto in top_cryptos:
            name = crypto['name']
            symbol = crypto['symbol']
            price = crypto['quote']['USD']['price']
            volume_change_24h = crypto['quote']['USD']['volume_change_24h']
            percent_change_24h = crypto['quote']['USD']['percent_change_24h']
            percent_change_7d =crypto['quote']['USD']['percent_change_7d']
            percent_change_30d =crypto['quote']['USD']['percent_change_30d']
            percent_change_1h=crypto['quote']['USD']['percent_change_1h']
            if percent_change_24h > 0.12 and volume_change_24h >5 and percent_change_7d>0 and percent_change_1h>0: 
                new_row = {
                    'coin name': name,
                    'price': price,
                    'symbol':symbol,
                    'volume_change_24h': volume_change_24h,
                    'percent_change_24h': percent_change_24h,
                    'percent_change_1h':percent_change_1h,
                    'percent_change_30d':percent_change_30d,
                    'percent_change_7d':percent_change_7d
                }
                excel_read = pd.concat([excel_read, pd.DataFrame([new_row])], ignore_index=True)
                print('EKLENDİ')
        # Değişiklikleri kaydet
        
    else:
        print(f"Error: {response.status_code} - {response.text}")
    excel_read.to_excel('track.xlsx', index=False)
if __name__ == "__main__":
    get_top_crypto_info()
