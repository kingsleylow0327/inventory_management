from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    last_updated_dt = db.Column(db.String(50), nullable=False)

    @staticmethod
    def insert(itemQo):
        new_item = Inventory(name=itemQo.name, 
                                  category=itemQo.category,
                                  price=itemQo.price)
        db.session.add(new_item)
        db.session.commit()
        db.session.refresh(new_item)
        return {"id": new_item.id}