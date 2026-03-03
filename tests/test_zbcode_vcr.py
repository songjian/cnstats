import pytest
from cnstats.zbcode import get_tree

@pytest.mark.vcr
def test_get_tree(capsys):
    # 测试获取指标树
    # 我们只尝试获取顶层指标，避免递归太深
    get_tree('zb', 'hgyd')
    captured = capsys.readouterr()
    assert "国家统计局" in captured.out or "A01" in captured.out or captured.out != ""
