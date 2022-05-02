from ttdiagnosis.database.engine import session
from ttdiagnosis.models.user import User


class UserRepository:
    def __init__(self):
        """Docstring."""
        self.session = session

    def add(self, batch):
        self.session.add(batch)
        self.session.commit()

    def get_by_id(self, reference):
        return self.session.query(User).filter_by(id=reference).one()

    def list(self):
        return self.session.query(User).all()
