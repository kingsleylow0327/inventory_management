import os
from dotenv import load_dotenv

class Config():
    def __init__(self) -> None:
        load_dotenv()
        _host = os.getenv('HOST')
        _password = os.getenv('PASSWORD')
        _ip = os.getenv('IP')
        _port = os.getenv('PORT')
        _schema = os.getenv('SCHEMA')
        self.DB_PATH = f'mysql+pymysql://{_host}:{_password}@{_ip}:{_port}/{_schema}'
