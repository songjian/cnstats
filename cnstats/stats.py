from .common import easyquery

def stats(zbcode, datestr, regcode=None, dbcode='hgyd'):
    wds=[]
    dfwds=[]
    if zbcode:
        dfwds.append({"wdcode":"zb","valuecode":zbcode})

    if datestr:
        dfwds.append({"wdcode":"sj","valuecode":datestr})
    
    if regcode:
        wds.append({"wdcode":"reg","valuecode":regcode})

    ret=easyquery(dbcode=dbcode, dfwds=dfwds)
    if ret['returncode'] == 200 :
        data_dict = {}
        for n in ret['returndata']['wdnodes']:
            if n['wdcode'] == 'zb':
                data_dict['zb'] = {}
                for i in n['nodes']:
                    data_dict['zb'][i['code']] = i['cname']
            if n['wdcode'] == 'sj':
                data_dict['sj'] = {}
                for i in n['nodes']:
                    data_dict['sj'][i['code']] = i['cname']
            if n['wdcode'] == 'reg':
                data_dict['reg'] = {}
                for i in n['nodes']:
                    data_dict['reg'][i['code']] = i['cname']

        result = []
        for n in ret['returndata']['datanodes']:
            if n['data']['hasdata'] == True:
                if len(data_dict) == 2:
                    result.append(
                        [data_dict['zb'][n['wds'][0]['valuecode']],
                        n['wds'][0]['valuecode'],
                        n['wds'][1]['valuecode'],
                        n['data']['strdata']])
                if len(data_dict) == 3:
                    result.append(
                        [data_dict['zb'][n['wds'][0]['valuecode']],
                        n['wds'][0]['valuecode'],
                        n['wds'][1]['valuecode'],
                        n['wds'][2]['valuecode'],
                        n['data']['strdata']])
        return result