from .common import easyquery

def get_reg(dbcode='fsyd'):
    wds=[{"wdcode":"zb","valuecode":"A01010101"}]
    ret = easyquery(dbcode=dbcode, rowcode='reg', wds=wds)
    if ret['returncode'] == 200:
        return ret['returndata']['wdnodes'][1]['nodes']
        
if __name__ == '__main__':
    for n in get_reg():
        print(n['code'], n['name'])
