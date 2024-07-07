import pytest
from clean_architecture_python.src.infra.db.settings.connection import DBConnectionHandle

@pytest.mark.skip(reason="Sensive Test")
def test_create_database_engine():
    db_connection_handle = DBConnectionHandle()

    engine = db_connection_handle.get_engine()

    assert engine is not None
