from app import db

class Item(db.Model):
    # __tablename__ = 'Item'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300))
    name = db.Column(db.String(200))
    price = db.Column(db.Float)
    category = db.Column(db.String(50))
    image = db.Column(db.String(200))
    description = db.Column(db.Text)
    brand = db.Column(db.String(100))
    rating = db.relationship("Rating", backref='item', lazy=True)
    item_id  = db.relationship("Cart", backref='item', lazy=True)
    item_id  = db.relationship("Order", backref='item', lazy=True)

class Rating(db.Model):
    # __tablename__ = 'Rating'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # rating should be any number between 1 to 5
    rating = db.Column(db.Integer)

class Cart(db.Model):
    # __tablename__ = 'Cart'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    count = db.Column(db.String(100))

class Order(db.Model):
    # __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_name = db.Column(db.String(200))
    item_price = db.Column(db.Float)
    count = db.Column(db.Integer)
    order_time = db.Column(db.Date, default=_get_date)

class User(db.Model):
    # __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(10))
    password = db.Column(db.String(10))
    rating = db.relationship("Rating", backref='user', lazy=True)
    user_id = db.relationship("Cart", backref='user', lazy=True)
    user_id = db.relationship("Order", backref='user', lazy=True)

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    shipping_address = db.Column(db.String(100))

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    rating = db.Column(db.Integer)

