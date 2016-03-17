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

        def technology_choices(self):

            technologies = self.db_session.query(Technologies).all()
            return technologies

        def category_choices(self):

            categories = self.db_session.query(Categories).all()
            return categories

        def get_technology(self, technology_name):

            technology = self.db_session.query(Technologies.id).filter(Technologies.name == technology_name).first()
            return technology

        def add_new_technology(self, name, image):

             technology = Technologies(
                name = name,
                image = image)
             self.db_session.add(technology)
             self.db_session.commit()

        def add_project(self, title, timestamp, lookup_technologies, description, url):

            project = Projects(
                title = title,
                timestamp = timestamp,
                lookup_technologies = lookup_technologies,
                description = description,
                url = url
                )
            self.db_session.add(project)
            self.db_session.commit()

        def get_projects(self):

            projects = self.db_session.query(Projects.title.label('title'),
                                             Technologies.image.label('image'),
                                             Projects.timestamp.label('timestamp'),
                                             Technologies.name.label('technology'),
                                             Projects.description.label('description'),
                                             Projects.url.label('url')).outerjoin(Technologies, Projects.lookup_technologies == Technologies.id).all()
            return projects