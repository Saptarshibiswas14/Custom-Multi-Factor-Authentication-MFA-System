# Run this once in a script or shell
from app import db, User
import bcrypt
db.create_all()
hashed = bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt())
user = User(username='admin', password=hashed, email='youremail@example.com')
db.session.add(user)
db.session.commit()
