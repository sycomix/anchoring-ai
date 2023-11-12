"""User service."""
from model.user import DbUser


def get_user_by_id(user_id):
    """Get user by ID."""
    if user := DbUser.query.filter_by(id=user_id).first():
        return user
    else:
        raise ValueError("invalid user id", False)
