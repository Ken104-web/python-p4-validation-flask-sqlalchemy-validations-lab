from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    @validates('name')
    def  validates_name(self, key, name):
        if  not name:
            raise ValueError('No name provided')
        return name
    phone_number = db.Column(db.String)
    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if len(value) !=10:
            raise ValueError('Wrong number')
        return value
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
   
   

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    @validates('title')
    def validate_title(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait):
            raise ValueError("No clickbait found")
        return title
    content = db.Column(db.String)
    category = db.Column(db.String)
    @validates("category")
    def validate_category(self,key,value):
        if value not in ("Fiction", "Non-Fiction"):
            raise ValueError("invalid category selection")
        return value
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    @validates('content')
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError('Post has many content')
        return value
    
    @validates('summary')
    def validate_summary(self, key, value):
        if len(value) >= 250:
            raise ValueError('invalid summary input')
        return value
    

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'


    # @validates('email', 'backup_email')
    # def validate_email(self, key, address):
    #     if '@' not in address:
    #         raise ValueError("failed simple email validation")
    #     return address