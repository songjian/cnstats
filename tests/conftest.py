import pytest

@pytest.fixture(scope="module")
def vcr_config():
    return {
        # 排除 Cookie 避免泄露敏感信息
        "filter_headers": ["Cookie"],
        # 排除随机时间戳参数，确保回放匹配成功
        "filter_query_parameters": ["k1"],
        # 允许录制新的请求
        "record_mode": "once",
    }
