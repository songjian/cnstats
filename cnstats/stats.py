import requests
import time

header={
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Referer':'https://data.stats.gov.cn/easyquery.htm?cn=A01',
        'Host':'data.stats.gov.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'_trs_uv=l0krufmy_6_30qm; JSESSIONID=JkGLaObMfWG3_P3_bNKa59cUydvE_nJDUpJOsskem4S-E-wgJeA7!-2135294552; u=1'
       }

def random_timestamp():
    return str(int(round(time.time() * 1000)))

def stats(code, datestr):
    url='https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"'+code+'"},{"wdcode":"sj","valuecode":"'+datestr+'"}]&k1='+random_timestamp()
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url,headers=header, verify=False)
    ret=r.json()
    if ret['returncode'] == 200 :
        for n in ret['returndata']['datanodes']:
            if n['data']['hasdata'] == True:
                print(n['wds'][0]['valuecode'],n['wds'][1]['valuecode'],n['data']['data'])