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
Connection: keep-alive
Cookie: CTK=1jbmg609mhab8800; indeed_rcc=LV; LV=LA=1764916892:LV=1764912988:CV=1764916892:TS=1764912988; cf_clearance=4rl9qNLG0UvSn5tpXy63wfDEuMnCDDjqSORakYY8gFA-1764917209-1.2.1.1-3HfMYgx_JW4_2aTo4zXV_JVatCwZzKBcEC9oNx6JWH6B_az97b1Ob32dDpAZ9FJMQTOFbJAo76vx_z6UWUN3qVr59ct.rbReCXmMkL.GmjPQKorHPYD5OalfptwXwU74pJ2aCE6miSRp2iIPRtBhPEVGHRk4OOQDaBSHu5eOWTDp_CvSIkCw1rDan9WEEsD9aIXCm92Yfi.hQMEDSuzB8Fe2Opq1gpJiyQcPApFw13aWwcH8erTwJtmXc5xkfpOG; _sp_ses.27f6=*; _sp_id.27f6=bd085610-fb31-4aad-bfcc-efef6cdb7f01.1764912990.1.1764917248..5f32cb07-27a0-4862-b65b-1bdfafe03380..dc825dab-4ade-423a-9ddd-8813cdda9c45.1764912990190.36; SURF=s4LKuwXsvAVmvfyuLk2BIYAn8fqrn0h0; sp=8a4e0706-acfc-438f-a58f-5c6a1a1e1a0c; _ga_LYNT3BTHPG=GS2.1.s1764912991$o1$g1$t1764917111$j59$l0$h1362396553; _ga=GA1.1.246824064.1764912992; FPID=FPID2.2.9Zef%2FVO%2FixM8weju6v8hq8IkNDU7KlwgA1tqunUtE2M%3D.1764912992; FPLC=0u9zQp%2BNMKZKfNLZE0jXrKIO%2Fm%2FGVLDYt51rBeb0WuZf1CA6ADxFot%2FfQ688Mg4Fmn906JyRGNyeKZLkxKQmq0R97BEGGWe74a5aPlQtWHg3A3Wf8i6LRnd%2BVtb7tA%3D%3D; g_state={"i_l":1,"i_ll":1764917111060,"i_b":"pDUsXQNoy6I8vFUytwHa5GLWexudJSMdmrlKkLNu21Q","i_p":1764920611509}; CSRF=gEj07X13YKfizxqRzf8w6D8cTTFEpxzY; INDEED_CSRF_TOKEN=LMfpXx09m6FslRnaq20W1jSbAoCCi9ij; __cf_bm=ogaSxCpkzUMJQtd1uvJVjWvdlWm6MaNejmVlwisbXz4-1764916893-1.0.1.1-7AFAldVNj1NGXSio2EsRNuJ_SWmYsor9UuG9_SyjI8NvoM1v1bRi5xi6lwsBwDYzKtFACNLXsuqrexIDpUP8qd6pL.xaP66S8WpsqV9KIIA; _cfuvid=s.Suf.VC1SfLu1JmNoWpxcC_LvRJZpuiTVFv5qKRqho-1764915332749-0.0.1.1-604800000; PREF="TM=1764916892940:L=Abu+Dhabi"; RQ=q=ai+engineer&l=Abu+Dhabi&ts=1764917110032&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B; JSESSIONID=node01icjf7ufzo9j71t7q48uosrh1c1320262.node0; LC=co=IN; indeed_rcc=CTK; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+05+2025+12%3A17%3A26+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f1861395-3127-435b-8ddc-8d6160ff4d31&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&intType=2&geolocation=IN%3BKL&AwaitingReconsent=false; OptanonAlertBoxClosed=2025-12-05T06:46:58.639Z
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
TE: trailers
"""

convert_header_text_to_dict(header_text)