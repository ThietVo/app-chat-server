from src import db
from src.models import Users, Messages
from sqlalchemy.sql import func


db.drop_all()
db.create_all()

u1 = Users(
    username='user1',
    password='123456',
    created_at=func.now(),
    updated_at=func.now()
)
u2 = Users(
    username='user2',
    password='123456',
    created_at=func.now(),
    updated_at=func.now()
)
u3 = Users(
    username='user3',
    password='123456',
    created_at=func.now(),
    updated_at=func.now()
)
m1 = Messages(
    message='message 1',
    type='http',
    created_at=func.now(),
    updated_at=func.now(),
    userId=1
)
m2 = Messages(
    message='message 2',
    type='http',
    created_at=func.now(),
    updated_at=func.now(),
    userId=2
)
m3 = Messages(
    message='message 1',
    type='http',
    created_at=func.now(),
    updated_at=func.now(),
    userId=3
)

db.session.add_all([u1, u2, u3, m1, m2, m3])

db.session.commit()