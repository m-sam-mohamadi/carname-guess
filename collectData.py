import requests 
import csv 
import json
from re import sub
ad_list = []
counter=0
with open('./output.csv','w',newline="") as file:
    for j in range(20):
        print('processing request %i ...'%j)
        url = "https://bama.ir/cad/api/search?pageIndex=%i" % j
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'})
        convertToJson = json.loads(page.text)
        ads = convertToJson['data']['ads']
        for ad in ads:
            counter+=1
            if ad['detail'] is not None and 'title' in ad['detail'] and ad['price'] is not None and 'price' in ['price']:
                if ad['price']['type'] !='installment' and ad['price']['type'] !='negotiable':  
                    ad_info = [
                        "".join(str(ad['detail']['title']).split("،")).strip() ,
                        "".join(str(sub(r'کیلومتر','',ad['detail']['mileage'])).split(",")).strip() ,
                        ad['detail']['year'], 
                       str(ad['detail']['location']).split("/")[0].strip() ,
                        ad['price']['price']
                    ]
                    ad_list.append(ad_info)

        writer = csv.writer(file, delimiter='#')
        for ad in ad_list:
            writer.writerow(ad)
    print('done with %i data.'%counter)  
