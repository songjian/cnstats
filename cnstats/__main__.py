from .stats import stats
from .zbcode import get_tree
from .regcode import get_reg
import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog='cn-stats',description='获取中国国家统计局网站数据Python包')
    parser.add_argument('--tree', action='store_const', const='zb', help='列出指标代码')
    parser.add_argument('--list-regcode', action='store_const', const='list_regcode', help='列出地区代码, 默认列出分省地区代码，列出主要城市代码添加 --dbcode csnd 参数')
    parser.add_argument('--dbcode', nargs='?', const='hgyd', default='hgyd', help='数据库代码, 默认: hgyd(宏观月度), 可选: hgjd(宏观季度), hgnd(宏观年度), fsyd(分省月度), fsjd(分省季度), fsnd(分省年度), csyd(城市月度), csjd(城市季度), csnd(城市年度)')
    parser.add_argument('--regcode', nargs='?', help='地区代码, 例如: 110000 是北京市')
    parser.add_argument('zbcode', help='指标代码', nargs='?')
    parser.add_argument('date', help='查询日期', nargs='?')
    args=parser.parse_args()
    if args.tree == 'zb':
        get_tree(args.tree, args.dbcode)
    elif args.list_regcode == 'list_regcode':
        if args.dbcode[:2] == 'cs':
            for n in get_reg('csnd'):
                print(n['code'], n['name'])
        else:
            for n in get_reg():
                print(n['code'], n['name'])
    else:
        # 如果 regcode 有值，并且后4位是0, dbcode等于fsyd,否则dbcode是csyd
        if args.regcode:
            if args.regcode[-4:] == '0000':
                args.dbcode='fsyd'
            else:
                args.dbcode='csyd'
        # print(args)
        r=stats(args.zbcode, args.date, args.regcode, args.dbcode)
        for row in r:
            print(' '.join(row))
