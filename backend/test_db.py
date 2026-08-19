from app.database.connection import engine
from app.database.models import Base
from sqlalchemy import inspect

# Create all tables
Base.metadata.create_all(bind=engine)

# Show all tables
inspector = inspect(engine)
print("Tables:", inspector.get_table_names())