import pytest
from cnstats.regcode import get_reg

@pytest.mark.vcr
def test_get_reg_provinces():
    # 测试获取默认分省代码 (fsyd / fsnd)
    provinces = get_reg()
    assert isinstance(provinces, list)
    assert len(provinces) > 30  # 中国有 30+ 个省级行政区
    
    # 验证数据结构
    first = provinces[0]
    assert "code" in first
    assert "name" in first
    # 验证具体数据 (如 北京 110000)
    beijing = next((p for p in provinces if p['code'] == '110000'), None)
    assert beijing is not None
    assert "北京" in beijing['name']

@pytest.mark.vcr
def test_get_reg_cities():
    # 测试获取主要城市代码 (csnd/csyd)
    cities = get_reg(dbcode='csnd')
    assert isinstance(cities, list)
    assert len(cities) >= 35  # 统计局 36 个城市分类
    
    # 验证青岛代码 370200
    qingdao = next((c for c in cities if c['code'] == '370200'), None)
    assert qingdao is not None
    assert "青岛" in qingdao['name']
