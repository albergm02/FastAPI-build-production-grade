from sqlmodel import SQLModel, create_engine, Session

#database url
DATABASE_URL="sqlite:///./kitaab.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)
    return engine

def get_session():
    with Session(engine) as session:
        yield session