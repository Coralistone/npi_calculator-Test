import pytest
from httpx import AsyncClient
from main import app, database

@pytest.mark.asyncio
async def test_calculate_addition():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/calculate/", json={"expression": "3 4 +"})
        assert response.status_code == 200
        assert response.json() == {"expression": "3 4 +", "result": 7.0}

@pytest.mark.asyncio
async def test_calculate_complex():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/calculate/", json={"expression": "5 1 2 + 4 * + 3 -"})
        assert response.status_code == 200
        assert response.json() == {"expression": "5 1 2 + 4 * + 3 -", "result": 14.0}

@pytest.mark.asyncio
async def test_invalid_expression():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/calculate/", json={"expression": "4 +"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid RPN expression"}

@pytest.mark.asyncio
async def test_division_by_zero():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/calculate/", json={"expression": "4 0 /"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Division by zero"}

@pytest.mark.asyncio
async def test_export_csv():
    # Ajouter un calcul pour tester l'export CSV
    await database.execute("INSERT INTO calculations (expression, result) VALUES ('3 4 +', 7.0)")
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/export-csv/")
        assert response.status_code == 200
        assert "3 4 +" in response.text
