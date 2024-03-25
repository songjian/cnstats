import requests
import time
import json

_header={
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Referer':'https://data.stats.gov.cn/easyquery.htm?cn=A01',
        'Host':'data.stats.gov.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'_trs_uv=l0krufmy_6_30qm; JSESSIONID=JkGLaObMfWG3_P3_bNKa59cUydvE_nJDUpJOsskem4S-E-wgJeA7!-2135294552; u=1'
       }

def _random_timestamp():
    return str(int(round(time.time() * 1000)))

def easyquery(m='QueryData', dbcode='hgyd', rowcode='zb', colcode='sj', wds=[], dfwds=[], id=None):
    url='https://data.stats.gov.cn/easyquery.htm'
    obj={
        'm': m,
        'dbcode': dbcode,
        'rowcode': rowcode,
        'colcode': colcode,
        'wds': json.dumps(wds),
        'dfwds': json.dumps(dfwds),
        'k1': _random_timestamp(),
        'h': '1',
        }
    if id: obj['id'] = id
    requests.packages.urllib3.disable_warnings()
    r=requests.post(url, data=obj, headers=_header, verify=False)
    return r.json()