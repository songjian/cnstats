import pytest
from cnstats.stats import stats

@pytest.mark.vcr
def test_stats_industrial():
    # 测试工业增加值同比增长 (A020101) 2024年初的数据
    # 注意：2024年数据可能是不全的，所以我们断言返回结果是列表即可
    result = stats('A020101', '2024')
    assert isinstance(result, list)
    if result:
        first_row = result[0]
        assert len(first_row) >= 4
        assert "工业" in first_row[0]
        assert first_row[1] == 'A020101'

@pytest.mark.vcr
def test_stats_with_reg_annual():
    # 测试年度数据分地区：北京(110000)的 生产总值 (A010101)
    # 使用年度数据库 hgnd
    result = stats('A010101', '2023', regcode='110000', dbcode='fsnd')
    assert isinstance(result, list)
    if len(result) > 0:
        # [指标名称, 指标代码, 地区名称, 地区代码, 查询日期, 数值]
        assert len(result[0]) == 6
        assert "北京" in result[0][2]
        assert result[0][3] == '110000'

@pytest.mark.vcr
def test_stats_multi_period():
    # 测试多时期查询：202112,202201
    result = stats('A0D0101', '202112,202201')
    assert isinstance(result, list)
    # A0D0101 是期末值，两个月份应该有两条数据
    dates = [row[2] for row in result]
    assert '202112' in dates
    assert '202201' in dates
    assert len(result) >= 2

@pytest.mark.vcr
def test_stats_multi_zb():
    # 测试查询父级指标（会返回多个子指标）
    # A0D01 是货币供应量，包含 M0, M1, M2 等
    result = stats('A0D01', '202201')
    assert isinstance(result, list)
    assert len(result) > 1
    # 验证是否包含 M2 (A0D0101) 和 M1 (A0D0103)
    zbcodes = [row[1] for row in result]
    assert 'A0D0101' in zbcodes
    assert 'A0D0103' in zbcodes

@pytest.mark.vcr
def test_invalid_query():
    # 测试不存在的代码
    result = stats('INVALID_CODE', '2024')
    assert isinstance(result, list)
    assert len(result) == 0

@pytest.mark.vcr
def test_stats_as_df():
    # 测试 as_df=True 参数返回 DataFrame
    import pandas as pd
    # 简单宏观数据
    df1 = stats('A020101', '2024', as_df=True)
    assert isinstance(df1, pd.DataFrame)
    if not df1.empty:
        assert '数值' in df1.columns
        assert '地区代码' not in df1.columns
        
    # 带地区数据
    df2 = stats('A010101', '2023', regcode='110000', dbcode='fsnd', as_df=True)
    assert isinstance(df2, pd.DataFrame)
    if not df2.empty:
        assert '地区代码' in df2.columns
        assert df2['地区代码'].iloc[0] == '110000'
