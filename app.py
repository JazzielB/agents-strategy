import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Model, Transcriber, Voice, PhoneNumberConfig, PhoneNumberManager
from asistant import Assistant


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Leer la cadena de conexión de la variable de entorno
CONN_STRING = os.getenv('CONN_STRING')

# Verifica si la variable de entorno está configurada
if not CONN_STRING:
    raise ValueError("La variable de entorno 'CONN_STRING' no está configurada")

# Crear un motor de conexión
engine = create_engine(CONN_STRING)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
# Define la estructura de la tabla
class PhoneNumber(Base):
    __tablename__ = 'phone_numbers'
    
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(50), unique=True, nullable=False)
    account_sid = Column(String(50), nullable=False)
    auth_token = Column(String(50), nullable=False)
    label = Column(String(50), nullable=False)
    assigned_assistant = Column(String(50), nullable=True)


Base.metadata.create_all(engine)
class PhoneNumberManager:
    def __init__(self, phone_number, account_sid, auth_token, label):
        self.phone_number = phone_number
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.label = label
        self.assigned_assistant = None

    def save_to_database(self):
        new_phone_number = PhoneNumber(
            phone_number=self.phone_number,
            account_sid=self.account_sid,
            auth_token=self.auth_token,
            label=self.label,
            assigned_assistant=self.assigned_assistant
        )
        session.add(new_phone_number)
        session.commit()

# Ejemplo de uso
manager = PhoneNumberManager('1234567890', 'test312312', 'test433123', 'My Label test122')
manager.save_to_database()