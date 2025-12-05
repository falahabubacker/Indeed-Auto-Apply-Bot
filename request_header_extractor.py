from seleniumwire import webdriver
from selenium.webdriver.firefox.service import Service

def extract_headers(url):
    service = Service(executable_path="./geckodriver")
    driver = webdriver.Firefox(service=service)

    headers = {}

    try:
        driver.get(url)

        for request in driver.requests:

            if "ae.indeed.com" in request.url:
                print(f"URL: {request.url}")
                print("Request Headers:")
                for header, value in request.headers.items():
                    print(f"    {header}: {value}")
                    headers[f"{header}"] = f"{value}"
                break 
    finally:
        driver.quit()
    
    return headers

# extract_headers("https://ae.indeed.com/jobs?q=ai+engineer&l=Abu+Dhabi&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B&from=searchOnDesktopSerp")