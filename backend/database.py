from sqlmodel import create_engine, Session, select
from models import User

class Database:
    """ Database functions """

    def __init__(self, uri):
        self.uri = uri

    @property
    def engine(self):
        return create_engine(self.uri, echo=True) #TODO: Turn off echo in production

    @property
    def session(self) -> Session:
        return Session(self.engine)

    # Creating a new user
    def create_user(self, user: User):
        with self.session as session:
            session.add(user)
            session.commit()
    
    # Validate if username already exists
    def validate_username(self, username: str) -> bool:
        with self.session as session:
            user = session.exec(select(User).where(User.username == username)).first()
        return not user

    # Deleting an existing user
    def delete_user(self, user_id: int):
        with self.session as session:
            user = session.exec(select(User).where(User.id == user_id))
            session.delete(user)
            session.commit()

    # Getting a specific user based on user id
    def get_user(self, user_id: int):
        with self.session as session:
            user = session.exec(select(User).where(User.id == user_id))
            return user

        