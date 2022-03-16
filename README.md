# 获取中国国家统计局网站数据

数据源：http://www.stats.gov.cn/

## PyPi安装

```bash
pip install cn-stats
```

## cn-stats使用

```python
from cnstats.stats import stats

stats('A0D01', '202201')
```

## 代码

代码 | 说明
---|---
A0D01|货币供应量
A0C01|国家财政预算收入
