from app.database import SessionLocal
from app.models import User
from app.utils import get_password_hash
from faker import Faker


def seed_users():
    db = SessionLocal()
    fake = Faker()
    for _ in range(10):
        user = User(
            name=fake.name(),
            email=fake.unique.email(),
            hashed_password=get_password_hash("password")
        )
        db.add(user)
    db.commit()
    db.close()
    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_users()
