from rag.sql_executor import is_query_safe

def test_safe_queries():
    assert is_query_safe("SELECT * FROM customers")
    assert not is_query_safe("DROP TABLE customers")
    assert not is_query_safe("DELETE FROM orders")
