from database import engine, Base

# Create the database table
Base.metadata.create_all(bind=engine)

print("Database created successfully!")
