# Changelog

## [0.1.2] - 2026-03-03

### Fixed
- **地区过滤失效**：修复了 `stats.py` 未向 API 正确传递 `wds` 参数的问题，该问题曾导致 `--regcode` 参数在实际请求中被忽略。
- **数据列对齐**：重构了数据解析逻辑，根据 API 返回的维度代码（`wdcode`）动态映射列索引，解决了包含地区信息时表头与数据错位的问题。
- **文档修正**：更新了 `README.md` 中过时的时间段指标代码，避免用户在查询 2021 年之后的数据时得到空结果。

### Added
- **地区名称支持**：区域查询结果中新增“地区名称”列（如显示“北京市”、“青岛市”）。
- **增强型 `--tree`**：现在支持通过 `cnstats [指标代码] --tree` 钻取查看子分类，便于在大类下定位特定年份段的指标。

## [0.1.1] - 2026-03-03

### Added
- 迁移项目管理到 `uv`，使用 `pyproject.toml` 替代 `setup.py`。
- 命令行工具支持表格化输出 (使用 `tabulate` 和 `wcwidth`)。
- 增加 `pytest` 测试框架及初步冒烟测试。
- \`stats\` 函数新增 \`as_df=False\` 参数，原生支持以 `pandas.DataFrame` 格式返回数据。

## 2025-05-24

- 主分支从 `master` 改为 `main`

## [0.0.9] - 2024-04-11

### Changed

- Removed specific versions for pandas and requests dependencies

## [0.0.8] - 2024-03-26

### Added

- 增加了分省/城市查询功能
