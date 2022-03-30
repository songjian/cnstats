from .stats import stats
import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('code', help='zbcode')
    parser.add_argument('date', help='查询日期')
    args=parser.parse_args()
    stats(args.code, args.date)
