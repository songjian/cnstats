from .common import easyquery

def get_reg():
    wds=[{"wdcode":"zb","valuecode":"A01010101"}]
    dfwds=[]
    ret = easyquery(m='QueryData', dbcode='fsyd', rowcode='reg', colcode='sj', wds=wds, dfwds=dfwds)
    if ret['returncode'] == 200:
        return ret['returndata']['wdnodes'][1]['nodes']
        
if __name__ == '__main__':
    for n in get_reg():
        print(n['code'], n['name'])
