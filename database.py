from sqlmodel import SQLModel, create_engine, Session
import config

# Crear el engine con los datos del config
DATABASE_URL = f"mysql+mysqlconnector://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DATABASE}"
engine = create_engine(DATABASE_URL, echo=True)

# Crear tablas (llamar una vez al iniciar)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency para FastAPI
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()