import datetime
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text

HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

PARAMS = (('wpfilebase_ajax', '1'), )

DATA = {'root': '', 'wpfb_action': 'tree', 'type': 'browser', 'base': '1'}

TODAY = datetime.date.today()

response = requests.post('https://slvha.com/',
                         headers=HEADERS,
                         params=PARAMS,
                         data=DATA)

for fileupload in response.json():
    if 'wpfb-cat' in fileupload.get('text'):
        continue
    else:
        filelist = BeautifulSoup(fileupload.get('text'))
        link = filelist.find('a')['href']
        print(link)
        #response2 = requests.get(link)
        #data = extract_text(BytesIO(response2.content))
        #print('========================')
        #print(data)
        #print('========================')

        if datetime.date.today().strftime('%Y-%m') in link:
            response = requests.get(link)
            data = extract_text(BytesIO(response.content))
            print('========================')
            print(data)
            print('========================')
