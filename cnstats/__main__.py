from .stats import stats
from .zbcode import get_tree
from .regcode import get_reg
import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog='cn-stats',description='获取中国国家统计局网站数据Python包')
    parser.add_argument('--tree', action='store_const', const='zb', help='列出指标代码')
    parser.add_argument('--list-regcode', action='store_const', const='list_regcode', help='列出地区代码')
    parser.add_argument('--dbcode', nargs='?', const='hgyd', default='hgyd', help='数据库代码')
    parser.add_argument('--regcode', nargs='?', help='地区代码, 例如: 110000 是北京市')
    parser.add_argument('zbcode', help='指标代码', nargs='?')
    parser.add_argument('date', help='查询日期', nargs='?')
    args=parser.parse_args()
    if args.tree == 'zb':
        get_tree(args.tree, args.dbcode)
    elif args.list_regcode == 'list_regcode':
        print(args)
        for n in get_reg():
            print(n['code'], n['name'])
    else:
        r=stats(args.zbcode, args.date, args.regcode)
        for row in r:
            print(' '.join(row))
