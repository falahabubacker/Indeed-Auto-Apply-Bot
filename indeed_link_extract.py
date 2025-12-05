from bs4 import BeautifulSoup as bs
from header_text_to_dict import convert_header_text_to_dict
import requests

# https://ae.indeed.com/jobs?q=ai+engineer&l=Abu+Dhabi&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B&from=searchOnDesktopSerp

url = "https://ae.indeed.com/jobs?q=ai+engineer&l=Abu+Dhabi&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B&from=searchOnDesktopSerp"

header_text = '''
    Host: ae.indeed.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br, zstd
    Connection: keep-alive
    Cookie: __cf_bm=p.OywU8mUHCDQTfvqHeA1IDMspj63z7VmyXsXs_M1w4-1764909390-1.0.1.1-e9bCq9WSx5j11kDPDRHPT5TQBlWGjAP_jfxHkkzUekNadyyWmNFqQBzkLUQERzGWAuX.QUHaN9REE_vttpPr9c8m6el1kRqtoUDVEKpO9zA; cf_clearance=LgtfAqm7IbdAZMLMcIiE.jS5OfrY9BXET5exK6pxmg8-1764909403-1.2.1.1-qZDO6YDyN5wk9F_fx2vhxGrsYK8uXRjCLMCDNNs0kHiWgekvBqbhdTiOwl8VO3.I2bKpM2tJ4o3C8XcwA6qM6JZ00PLY.YJChv07OjxGqDk5oDsNv16IZv195b6PfKJqVm.0patqnJCRSVOXLRelUhUbHD6iU0UQHfTzPNXIhqudzCOQY3_l95Y0DpEA8hIvHoKHxIvMcs_DVom2TAf7JuWfF1sFa5B29CCkdJDpObZJP6tZ0kC1K5aVgh2Q_32L; CTK=1jbmcoi78hbm2804; INDEED_CSRF_TOKEN=azMPqEzoJozBOih9lPTBYAfko2JuClXD; LV=LA=1764909402:CV=1764909402:TS=1764909402; PREF="TM=1764909402365:L=Abu+Dhabi"; RQ="q=ai+engineer&l=Abu+Dhabi&ts=1764909402366&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B"; _cfuvid=qegCZ5t.6eUxTG02mlKI_8lQ0gJXGuJjsELs08vqXeE-1764909402809-0.0.1.1-604800000; _sp_ses.27f6=*; _sp_id.27f6=f228a88e-0847-40d9-a0b6-2b500d4a2fcc.1764909405.1.1764909430..8f8a7e91-96fe-4c85-94e1-63c1028be61b..be51218a-1442-4062-b43d-3bbb7020901e.1764909404655.4; JSESSIONID=node0ly217govbhpp317nox2aawto6644616.node0; SURF=iy4YKiyzjNZoDlOyx5uVYNAoDH8Ydj7d; sp=528aa644-cf72-454f-be41-e138b1ad615c; LC=co=IN; g_state={"i_l":1,"i_ll":1764909406236,"i_b":"j8ly9nrcChxuyN162ndnpnRZ+j7C1eiYSFnTAE/HY7M","i_p":1764916609546}; _ga_LYNT3BTHPG=GS2.1.s1764909406$o1$g0$t1764909406$j60$l0$h766148402; _ga=GA1.1.364403099.1764909407; FPID=FPID2.2.eb240oI81PeDaMtBnu0ANmeS72MGTQwBiZ0c7YdcUMA%3D.1764909407; FPLC=swjTM%2BzmjJ91fDX5%2F4hMshJLFTrVLI5apnyk0%2BB0aRmhEVNajrdcvNmPYLXzst6dFX6ow4v9SvGquJttv0IV8NCEZCXOaIr2q2ZrdpmMIa%2F8Rkb9svC1JgeCNZft7g%3D%3D
    Upgrade-Insecure-Requests: 1
    Sec-Fetch-Dest: document
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: none
    Sec-Fetch-User: ?1
    Priority: u=0, i
    TE: trailers
'''

headers = convert_header_text_to_dict(header_text)

page = requests.get(url, headers=headers)
print(page.status_code)

soup = bs(page.content, "html.parser")

# soup.find_all('li', class_='css-1ac2h1w')