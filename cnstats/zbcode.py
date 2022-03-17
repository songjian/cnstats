import requests

header={
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Referer':'https://data.stats.gov.cn/easyquery.htm?cn=A01',
        'Host':'data.stats.gov.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'_trs_uv=l0krufmy_6_30qm; JSESSIONID=JkGLaObMfWG3_P3_bNKa59cUydvE_nJDUpJOsskem4S-E-wgJeA7!-2135294552; u=1'
       }

def easyquery(id='zb'):
    url='https://data.stats.gov.cn/easyquery.htm'
    obj={'id': id, 'dbcode': 'hgyd', 'wdcode': 'zb', 'm': 'getTree'}
    requests.packages.urllib3.disable_warnings()
    r=requests.post(url, data=obj, headers=header, verify=False)
    return r.json()

def get_tree(id='zb'):
    for n in easyquery(id):
        print(n['id'], n['name'])
        if n['isParent']: get_tree(n['id'])

if __name__ == '__main__':
    get_tree('zb')