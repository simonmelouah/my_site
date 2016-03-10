from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import urllib
from models import *


class DbInteraction(object):

        def __init__(self, db_user, db_password, db_host, db_name):

            try:
                engine = create_engine('mysql://'+ db_user +':' + db_password + '@' + db_host + '/' + db_name,
                                       convert_unicode=True, isolation_level="READ UNCOMMITTED")
                Base.metadata.create_all(engine)
                Base.metadata.bind = engine
                Session = sessionmaker(bind=engine)
                self.db_session = Session()

            except ValueError, e:
                print e.message


        def get_user(self, username):

            login = self.db_session.query(Users).filter(Users.username == username).first()
            return login

