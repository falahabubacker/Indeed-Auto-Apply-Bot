def convert_header_text_to_dict(header_text):
    headers = {}
    lines = header_text.strip().strip('{}').strip().split('\n')

    for line in lines:
        if line and ':' in line:
            key, value = line.split(':', 1)
            
            headers[key.strip()] = value.strip()

    print(headers)
    return headers

header_text = """
Host: ae.indeed.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br, zstd
Sec-GPC: 1
Connection: keep-alive
Cookie: CTK=1jbmqecejhn7s800; indeed_rcc=LV; CSRF=0Du65TIJ6BpAREwpM4kYO7JGvmwWPNWH; INDEED_CSRF_TOKEN=2okIlGnK7j3QdXehfGbLb3LPketi9vUz; LV=LA=1764923748:CV=1764923748:TS=1764923748; __cf_bm=ZsmMZFkxwVqk.pDW.8gV4XOs42lTnUaeRZ.mKMT03wM-1764923748-1.0.1.1-gECSS1vvxP8tnIvcaQPe1o6.KR8h0y84wnBAnk_bFqOtmujw_VPHRWoe4TocSH82qP_QL5wv4jgLIkkaW2.1i8U3TCgZMU4VpRc930lktsQ; _cfuvid=cLoj.UkkD1SvY6IM.F1Z9FMvn5OSik6XTx0srWK9RZo-1764923748878-0.0.1.1-604800000; JSESSIONID=node01mmtr962k9djt158tgvy5ye1x231877.node0; _sp_ses.27f6=*; _sp_id.27f6=76e8d4bd-cea5-4785-b057-f0fa426ed8a4.1764923750.1.1764923769..bea38851-b001-4529-9261-7e5fc23ef2f6..96b6c235-b129-47cc-88b4-5bf1961d4c43.1764923750368.4; cf_clearance=lVfQaXpRMhP9s4aQyoI90mR4PWuisfUicHqZoE9LHDE-1764923750-1.2.1.1-8rRMcbOTwTsAsaep1tkAVbdDwuK332HW979CulOLbqFAMBE.nv3jTX6xPfagcy79b5SvhAmMvBtxoIrgEZie_NhTIUa4TJMDxNL1S51rAPENzZE6cmvxkch5XN1Lm_zRuR4QbBEdUF300EdUEktKSm_Dk2GpAknyVEOk9soHrCo2dm4XpWyVYVMtmObkcWPaaqgMpXzHiu_L8U1NEMeiZIELCUXLmBtpdQ6yweKjIlU; SURF=USwWglmgh5HDD7DXtlWkduwKLbTS6VtU; sp=2e07b7c0-c076-4e41-b19f-2ecab492273c; _ga_LYNT3BTHPG=GS2.1.s1764923753$o1$g1$t1764923763$j50$l0$h922238883; _ga=GA1.1.1144982561.1764923754; FPID=FPID2.2.N4vSBRPU89hB6ygv19tzTJTY9MiiNCyu5tCrdn1YWXI%3D.1764923754; FPLC=kAbjBKhXjLcohLwzILsf1qmKphGa6gDPoHM8Q5v8S0X1WfgdQQPCKTCZ%2F9gADLc5kuk2nSDop7cV9dcvS16lpvqtltjv9yNqchdJPInaCtdC1rRnuT0gnL02XPxEzg%3D%3D; g_state={"i_l":1,"i_ll":1764923764792,"i_b":"nRrQzNlRrFKF6O4kWWYs8lh3QrSX4kh7SJCUpC9aiDk","i_p":1764930961709}; PREF="TM=1764923762264:L=Abu+Dhabi"; RQ=q=ai+engineer&l=Abu+Dhabi&ts=1764923762264; LC=co=IN
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
TE: trailers
"""

convert_header_text_to_dict(header_text)