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
            try:
                login = self.db_session.query(Users).filter(Users.username == username).first()
                return login
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def technology_choices(self):

            try:
                technologies = self.db_session.query(Technologies).all()
                return technologies
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def category_choices(self):

            try:
                categories = self.db_session.query(Categories).all()
                return categories
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def get_category(self, category_name):
            try:
                category = self.db_session.query(Categories).filter(Categories.name == category_name).first()
                return category
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def get_technology(self, technology_name):

            try:
                technology = self.db_session.query(Technologies.id).filter(Technologies.name == technology_name).first()
                return technology
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def add_new_technology(self, name, image):
            try:
                 technology = Technologies(
                    name = name,
                    image = image)
                 self.db_session.add(technology)
                 self.db_session.commit()
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def add_project(self, title, timestamp, lookup_category, lookup_technologies, description, url, youtube):
            try:
                project = Projects(
                    title = title,
                    timestamp = timestamp,
                    lookup_categories = lookup_category,
                    lookup_technologies = lookup_technologies,
                    description = description,
                    url = url,
                    youtube = youtube
                    )
                self.db_session.add(project)
                self.db_session.commit()
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def get_projects(self):

            projects = self.db_session.query(Projects.title.label('title'),
                                             Technologies.image.label('image'),
                                             Projects.timestamp.label('timestamp'),
                                             Technologies.name.label('technology'),
                                             Categories.name.label('category'),
                                             Projects.description.label('description'),
                                             Projects.url.label('url'),
                                             Projects.youtube.label('youtube')).\
                outerjoin(Technologies, Projects.lookup_technologies == Technologies.id).\
                outerjoin(Categories, Projects.lookup_categories == Categories.id).\
                order_by(Projects.timestamp.desc()).all()
            return projects