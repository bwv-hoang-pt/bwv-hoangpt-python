import os

class Config:
    # ... các cấu hình khác ...

    # SQLAlchemy configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://hoangphan:hoangphan@localhost/python_survey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY="hoangphan"