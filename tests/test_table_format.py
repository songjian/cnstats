from tabulate import tabulate

def test_table_format():
    sample_data = [
        ["指标 A", "A01", "202201", "100.5"],
        ["指标 B", "B02", "202202", "200.0"],
        ["测试长文本指标名称对齐情况", "C03", "202203", "300.75"]
    ]
    headers = ["指标名称", "指标代码", "查询日期", "数值"]
    
    # 使用与 __main__.py 相同的配置
    output = tabulate(sample_data, headers=headers, tablefmt="pretty")
    print("\n验证表格输出效果：")
    print(output)

if __name__ == "__main__":
    test_table_format()
