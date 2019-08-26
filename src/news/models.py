from src import db
from datetime import datetime


class News(db.Model):
    __tablename__='news_test'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return 'News {} {}'.format(self.title, self.url)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    news_id = db.Column(db.Integer,
                        db.ForeignKey('news_test.id', ondelete='CASCADE'),
                        index=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )

    def __repr__(self):
        return '<Comment {}>'.format(self.id)
