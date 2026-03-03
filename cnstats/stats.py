from .common import easyquery
import pandas as pd

def stats(zbcode, datestr, regcode=None, dbcode='hgyd', as_df=False):
    wds=[]
    dfwds=[]
    if zbcode:
        dfwds.append({"wdcode":"zb","valuecode":zbcode})

    if datestr:
        dfwds.append({"wdcode":"sj","valuecode":datestr})
    
    if regcode:
        wds.append({"wdcode":"reg","valuecode":regcode})

    ret=easyquery(dbcode=dbcode, wds=wds, dfwds=dfwds)
    if ret['returncode'] == 200:
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

        # 获取维度映射
        wd_map = {}
        for idx, node in enumerate(ret['returndata']['wdnodes']):
            wd_map[node['wdcode']] = idx

        result = []
        for n in ret['returndata']['datanodes']:
            # 基础项：指标和时间
            zb_code = n['wds'][wd_map['zb']]['valuecode']
            sj_code = n['wds'][wd_map['sj']]['valuecode']
            
            # 指标名称
            zb_name = data_dict['zb'].get(zb_code, zb_code)
            
            # 数值
            data_val = n['data']['strdata']
            
            if 'reg' in wd_map:
                reg_code = n['wds'][wd_map['reg']]['valuecode']
                reg_name = data_dict['reg'].get(reg_code, reg_code)
                # [指标名称, 指标代码, 地区名称, 地区代码, 查询日期, 数值]
                result.append([zb_name, zb_code, reg_name, reg_code, sj_code, data_val])
            else:
                # [指标名称, 指标代码, 查询日期, 数值]
                result.append([zb_name, zb_code, sj_code, data_val])
                
        if as_df:
            if 'reg' in wd_map:
                columns = ['指标名称', '指标代码', '地区名称', '地区代码', '查询日期', '数值']
            else:
                columns = ['指标名称', '指标代码', '查询日期', '数值']
            df = pd.DataFrame(result, columns=columns)
            if '数值' in df.columns:
                df['数值'] = pd.to_numeric(df['数值'], errors='coerce')
            return df
            
        return result
    return pd.DataFrame() if as_df else []