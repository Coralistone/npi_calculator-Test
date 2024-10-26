from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import os

# Configuration de la base de données PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:Mikam_99@db/npi_calculator")

# Création de la base de données avec SQLAlchemy
database = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True)
metadata = MetaData()

# Déclaration du modèle de calcul pour la base de données
calculations = Table(
    "calculations",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("expression", String, nullable=False),
    Column("result", Float, nullable=False)
)

# Configuration de la session asynchrone
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Création de l'application FastAPI
app = FastAPI()

# Configuration CORS pour autoriser les connexions depuis n'importe où (à personnaliser si besoin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèle Pydantic pour la requête de calcul
class CalculationRequest(BaseModel):
    expression: str

# Endpoint pour effectuer un calcul en NPI
@app.post("/calculate/")
async def calculate(request: CalculationRequest):
    try:
        # Calcul en utilisant une pile pour la notation polonaise inverse
        result = evaluate_rpn(request.expression)
        
        # Sauvegarder le calcul dans la base de données
        query = calculations.insert().values(expression=request.expression, result=result)
        await database.execute(query)
        
        return {"expression": request.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Fonction pour évaluer une expression en notation polonaise inverse
def evaluate_rpn(expression: str) -> float:
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  # Si le token est un nombre
            stack.append(float(token))
        elif token in {"+", "-", "*", "/"}:  # Si le token est un opérateur
            if len(stack) < 2:
                raise ValueError("Expression invalide")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ValueError("Division par zéro")
                stack.append(a / b)
        else:
            raise ValueError(f"Token inconnu : {token}")
    
    if len(stack) != 1:
        raise ValueError("Expression invalide")
    
    return stack[0]

# Endpoint pour exporter les calculs sous forme de CSV
@app.get("/export-csv/")
async def export_calculations_csv():
    query = calculations.select()
    results = await database.fetch_all(query)
    csv_content = "id,expression,result\n" + "\n".join(
        f"{r['id']},{r['expression']},{r['result']}" for r in results
    )
    return csv_content

# Événements de démarrage et d'arrêt pour connecter et déconnecter la base de données
@app.on_event("startup")
async def startup():
    await database.connect()
    async with engine.begin() as conn:
        # Créer les tables dans la base de données si elles n'existent pas encore
        await conn.run_sync(metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
