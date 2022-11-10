import json

if __name__ == '__main__':
    price_data = None
    price = []
    with open('data.json', encoding='utf8') as f:
        price_data = f.read()

    if price_data is not None:
        json_price_data = json.loads(price_data)
for d in json_price_data:
    price.append({'name': d['name'], 'price': d['technodom_price'], 'url': d['technodom_url']})
    price.append({'name': d['name'], 'price': d['sulpak_price'], 'url': d['sulpak_url']})
    price.append({'name': d['name'], 'price': d['mechta_price'], 'url': d['mechta_url']})
    minPricedItem = min(price, key=lambda x: float(x['price']))
    store_name = ''

    if 'technodom' in minPricedItem['url'].lower():
        store_name = 'Technodom'
    elif 'sulpak' in minPricedItem['url'].lower():
        store_name = 'Sulpak'
    elif 'mechta' in minPricedItem['url'].lower():
        store_name = 'Mechta'
    print('{} is available in cheap price at {}. The price is {} tg.'.format(minPricedItem['name'], store_name,
                                                                             minPricedItem['price']))
    price = []
