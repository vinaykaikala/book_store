from book_store.database import db as mysql

class BookStore(mysql.Model):
    __tablename__ = ''
    columm_1 = mysql.Column(mysql.String(128), nullable=False , primary_key=True)
