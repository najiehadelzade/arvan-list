import requests
import pandas as pd
open_excel_ensani=pd.read_excel('انسانی-v1.xlsx')
print(open_excel_ensani)
dic={'Authorization':'apikey 9c7ea2c7-9587-5e17-95a7-b370363a8aff'}
r = requests.get('https://napi.arvancloud.ir/vod/2.0/channels',headers=dic)
print(r.json())
r = requests.get('https://napi.arvancloud.ir/vod/2.0/videos/85d99248-f9af-4207-beea-c42f83d8a58d',headers=dic)
print(r.json()['data']['video_url'])
