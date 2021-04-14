import datetime
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

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


layout_params = LAParams(line_margin=0.1)

for fileupload in response.json():
    if 'wpfb-cat' in fileupload.get('text'):
        continue
    else:
        filelist = BeautifulSoup(fileupload.get('text'),
                                 features="html.parser")
        link = filelist.find('a')['href']
        print(link)

        if datetime.date.today().strftime('%Y-%m') in link:
            response = requests.get(link)
            data = extract_text(BytesIO(response.content), laparams=layout_params)
            print('========================')
            print(data)
            print('========================')
