from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import class_mapper
from datetime import datetime
import pytz

db = SQLAlchemy()
tz = pytz.timezone('Asia/Singapore')


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    category = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Float, nullable=False)
    last_updated_dt = db.Column(db.String(50), nullable=False)

    def to_json_exclude(self, exclude_list):
        # Default Exclusion
        exclude_list.append("last_updated_dt")
        columns = [c.key for c in class_mapper(type(self)).columns if c.key not in exclude_list]  # noqa: E501
        return {c: str(getattr(self, c)) for c in columns}

    @classmethod
    def _is_exsisted(cls, itemQo) -> bool:
        return bool(cls.query.filter_by(name=itemQo.name).count())

    @staticmethod
    def insert(itemQo):
        new_item = Inventory(name=itemQo.name.lower(),
                             category=itemQo.category.lower(),
                             price=itemQo.price)
        if Inventory._is_exsisted(new_item):
            new_item.last_updated_dt = datetime.now(tz)
            query = Inventory.query.filter_by(name=new_item.name)
            item_id = query.first().id
            query.update(new_item.to_json_exclude(["id"]))
            db.session.commit()
            return {"id": item_id}
        else:
            db.session.add(new_item)
            db.session.commit()
            db.session.refresh(new_item)
            return {"id": new_item.id}

    @staticmethod
    def filter(filterQo):
        query = Inventory.query.filter(Inventory.
                                       last_updated_dt.
                                       between(filterQo.dt_from,
                                               filterQo.dt_to)).all()
        item_list = [item.to_json_exclude([]) for item in query]
        total_price = sum([float(item["price"]) for item in item_list])
        return {"item": item_list, "total_price": total_price}

    @staticmethod
    def categorize(category):
        cat = category.lower()
        query = db.session.query(
            Inventory.category.label('category'),
            func.count(Inventory.category).label('count'),
            func.sum(Inventory.price).label('total_price')
        ).group_by(Inventory.category)
        if cat != "all":
            query = query.filter(Inventory.category == cat)
        items = query.all()
        ret_json = {'items': []}
        for item in items:
            ret_json['items'].append({
                'category': item.category,
                'count': item.count,
                'total_price': item.total_price
            })
        return ret_json
