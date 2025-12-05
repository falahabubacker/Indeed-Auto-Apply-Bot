from bs4 import BeautifulSoup as bs
import requests

# https://ae.indeed.com/jobs?q=ai+engineer&l=Abu+Dhabi&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B&from=searchOnDesktopSerp

url = "https://ae.indeed.com/jobs?q=ai+engineer&l=Abu+Dhabi&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B&from=searchOnDesktopSerp"
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ml;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"143.0.7499.41"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.41", "Chromium";v="143.0.7499.41", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}

cookies = {
    'CTK': '1ibob8de9kred800',
    'optimizelySession': '1753424966172',
    'RF': 'TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtRlZ3JLVA2rIrZNC-c07cSA=',
    'SURF': 'EwMzRFhCNvKMCdSCUXPSf3HbAfVk4I8K',
    'sp': 'c254cec4-3fe9-425a-8a8b-0cd512d60db2',
    '_ga': 'GA1.1.1731386354.1753424966',
    'FPID': 'FPID2.2.8SqDZ93hlmlorc%2BtHb6rkosiYAs%2FHMPuSiQIFvgeDCA%3D.1753424966',
    'LC': 'co=IN',
    'INDEED_CSRF_TOKEN': 'AM6QMYdKUyqV6CFLUMAgTHQRUTuvKiwP',
    'LV': 'LA=1764839770:LV=1764735832:CV=1764839770:TS=1764735832',
    '_cfuvid': 'ZS0Zi9bNlhlTQFXx1Y_5HfuO.A1lhYdzOOBPX1tHYYc-1764839770741-0.0.1.1-604800000',
    '_sp_ses.27f6': '*',
    'FPLC': '7y9c9lHdqCo4CPxwJ8WfuRTxgjetkGANND9A6n5OwQvjojFkhplugl40FZ8%2B502aezi%2B43006QL81bJ34fu3CVqvgAdqhj2eEgPjOHxJEEtLcXxPzZOwrJ5vrKv3Fw%3D%3D',
    'CSRF': 'rOJUzZyAPWOy2ZJHM8a0Po5lbZ9KBSA6',
    'indeed_rcc': 'PREF:LV:CTK:RQ',
    'SHARED_INDEED_CSRF_TOKEN': 'AM6QMYdKUyqV6CFLUMAgTHQRUTuvKiwP',
    'CO': 'AE',
    'LOCALE': 'en_AE',
    'MICRO_CONTENT_CSRF_TOKEN': 'GGCIJcliExKSR11PKtvl5W7lcwFCI25Q',
    'PPID': '',
    '__cf_bm': '8wsEruduZqlJEDKs0lvmxIjnHHZGVLQMP7bcnKFkntk-1764841709-1.0.1.1-mwghb1akabZuzoPP.tfUkoidxNFAuaR8F7fkMdA3_LfHQVKniPdzxpsvZmA1yY0A9rKsHFSHuwL8OJcwNSo2adrcoEdKkLRe2gt9WyCpAnk',
    'cf_clearance': 'k6qOPOD9vEJy6_.r4A3hvOH5gq1MAKVY4KVZ87hkm68-1764841896-1.2.1.1-1cP8_xjmhFdecnBSgvYj3dTOc5T3n96T9Qegc2IqGMjfK0_YbUW0RJagp5CFbMGMX6qfWyUeU2HS6vs2XyNMrDT5fLn0aaNHvDi5HZSqpLYWe7h.Jby152kFSb2PyzoMy4fFugGNNCPctQfsJE0Ofvap7x_ATo6FehiJD1n9XhWIrlDXfAprxAr1jVzETJiqDQTtd3QTg62DzQ05LscfF8fBeTCryL4aw36jGbAVQ.Y',
    'PREF': 'TM=1764736440776:L=Abu+Dhabi',
    'RQ': 'q=ai+engineer&l=Abu+Dhabi&ts=1764842112708&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B:q=&l=Abu+Dhabi&ts=1764736497157',
    'JSESSIONID': 'node0475b9zzgv13fzm2aieuq7pc03716187.node0',
    'g_state': '{"i_l":0,"i_ll":1764842360147,"i_b":"Gr/9MkrXMICkzs801kqZNCUeNmAqTgagS9BV/H/xI9s"}',
    '_ga_LYNT3BTHPG': 'GS2.1.s1764839776$o2$g1$t1764842477$j60$l0$h1370678114',
    '_sp_id.27f6': '1f18c3cf-dc8c-4ecb-959b-27b66347217b.1764735817.2.1764842475.1764738291.40d1baaa-e6e7-42fe-b69b-8fc29d0c82bc.137029d6-4160-40b0-8fd5-fb7b80eea8ca.a055ad4d-9335-4223-be58-d060c4a6bd29.1764839774888.61'
}

page = requests.get(url, headers=headers, cookies=cookies, verify=False)
print(page.status_code)

soup = bs(page.content, "html.parser")

# soup.find_all('li', class_='css-1ac2h1w')