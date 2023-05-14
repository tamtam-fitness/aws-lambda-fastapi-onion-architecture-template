from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="module")
def client() -> Generator:  # type: ignore
    with TestClient(app) as c:
        yield c
