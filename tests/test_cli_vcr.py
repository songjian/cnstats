import pytest
import sys
from cnstats.__main__ import main

@pytest.mark.vcr
def test_cli_simple_query(capsys, monkeypatch):
    # 模拟命令行参数: cnstats A0D0101 202201
    test_args = ['cn-stats', 'A0D0101', '202201']
    monkeypatch.setattr(sys, 'argv', test_args)
    
    main()
    
    captured = capsys.readouterr()
    # 验证输出包含表格边框
    assert "+---" in captured.out
    # 验证包含指标名称和代码
    assert "货币和准货币(M2)供应量_期末值" in captured.out
    assert "A0D0101" in captured.out
    assert "202201" in captured.out

@pytest.mark.vcr
def test_cli_reg_query(capsys, monkeypatch):
    # 模拟命令行参数: cnstats A010101 202312 --regcode 110000
    # 验证是否自动推断为 6 列输出 (包含地区名称)
    test_args = ['cn-stats', 'A010101', '202312', '--regcode', '110000']
    monkeypatch.setattr(sys, 'argv', test_args)
    
    main()
    
    captured = capsys.readouterr()
    assert "+---" in captured.out
    assert "北京市" in captured.out
    assert "地区名称" in captured.out
    assert "地区代码" in captured.out

@pytest.mark.vcr
def test_cli_tree_query(capsys, monkeypatch):
    # 模拟命令行参数: cnstats A0101 --tree
    test_args = ['cn-stats', 'A0101', '--tree']
    monkeypatch.setattr(sys, 'argv', test_args)
    
    main()
    
    captured = capsys.readouterr()
    # 验证输出了指标树结构 (不应带表格边框)
    assert "+---" not in captured.out
    assert "A010101" in captured.out
    assert "居民消费价格分类指数" in captured.out

@pytest.mark.vcr
def test_cli_list_regcode(capsys, monkeypatch):
    # 模拟命令行参数: cnstats --list-regcode
    test_args = ['cn-stats', '--list-regcode']
    monkeypatch.setattr(sys, 'argv', test_args)
    
    main()
    
    captured = capsys.readouterr()
    assert "110000 北京市" in captured.out
    assert "310000 上海市" in captured.out
