from typing import Optional, List
from sqlmodel import Field, Session, SQLModel, create_engine, select



class Tarea(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    completada: bool = Field(default=False)


sqlite_file_name = "tareass.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)


def agregar_tarea(titulo: str) -> Tarea:
    with Session(engine) as session:
        nueva_tarea = Tarea(titulo=titulo)
        session.add(nueva_tarea)
        session.commit()
        session.refresh(nueva_tarea)
        return nueva_tarea

def obtener_tareas() -> List[Tarea]:
    with Session(engine) as session:
        statement = select(Tarea)
        return session.exec(statement).all()