import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient

from app.main import app 
from app.repositories.file_repository import FileRepository
from app.models import File  
from conftest import TEST_BASE_URL 

client = TestClient(app)

@pytest.mark.asyncio
async def test_upload_file_success(client: AsyncClient, test_db_session, test_file_repository):
    file_data = {"filename": "test.txt", "status": "Processing"}
    test_file = File(**file_data)
    test_db_session.add(test_file)
    test_db_session.commit()
    files = {"file": ("test.txt", "file contents")}

    response = await client.post(f"{TEST_BASE_URL}/upload/", files=files)
    assert response.status_code == 200
    assert "id" in response.json()
    assert "filename" in response.json()
    assert "status" in response.json()

@pytest.mark.asyncio
async def test_upload_file_failure(client: AsyncClient):
    pass

