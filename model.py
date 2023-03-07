from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import class_mapper
from datetime import datetime
import pytz

db = SQLAlchemy()
tz = pytz.timezone('Asia/Singapore')

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    last_updated_dt = db.Column(db.String(50), nullable=False)

    def to_json(self):
        columns = [c.key for c in class_mapper(type(self)).columns if c.key != "id"]
        return {c: str(getattr(self, c)) for c in columns}

    @staticmethod
    def insert(itemQo):
        new_item = Inventory(name=itemQo.name, 
                                  category=itemQo.category,
                                  price=itemQo.price)
        if Inventory._is_exsisted(new_item):
            new_item.last_updated_dt = datetime.now(tz)
            query = Inventory.query.filter_by(name=new_item.name)
            item_id = query.first().id
            query.update(new_item.to_json())
            db.session.commit()
            return {"id": item_id}
        else:
            db.session.add(new_item)
            db.session.commit()
            db.session.refresh(new_item)
            return {"id": new_item.id}
    
    @classmethod
    def _is_exsisted(cls, itemQo) -> bool:
        return bool(cls.query.filter_by(name=itemQo.name).count())