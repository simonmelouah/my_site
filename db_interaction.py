from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import urllib
from models import *
import datetime
import os


class DbInteraction(object):

        def __init__(self):

            try:
                environment = os.environ.get("ENVIRONMENT")
                if environment == "production":
                    db_user = os.environ.get("DB_USER")
                    db_password = os.environ.get("PASSWORD")
                    db_host = os.environ.get("DB_HOST")
                    db_name = os.environ.get("DB_NAME")
                else:
                    db_user = "my_site_login"
                    db_password = "abc123"
                    db_host = "localhost"
                    db_name = "my_site"
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
                login = self.db_session.query(User).filter(User.username == username).first()
                return login
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def technology_choices(self):

            try:
                technologies = self.db_session.query(Technology).all()
                return technologies
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def category_choices(self):

            try:
                categories = self.db_session.query(Category).all()
                return categories
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def get_category(self, category_name):
            try:
                category = self.db_session.query(Category).filter(Category.name == category_name).first()
                return category
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def get_technology(self, technology_name):

            try:
                technology = self.db_session.query(Technology.id).filter(Technology.name == technology_name).first()
                return technology
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def add_new_technology(self, name, image):
            try:
                 technology = Technology(
                    name = name,
                    image = image)
                 self.db_session.add(technology)
                 self.db_session.commit()
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def add_project(self, title, timestamp, category_id, technology_id, description, url, youtube):
            try:
                project = Project(
                    title = title,
                    timestamp = timestamp,
                    category_id = category_id,
                    technology_id = technology_id,
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

        def projects(self):

            get_projects = self.db_session.query(Project.id.label('id'),
                                                 Project.title.label('title'),
                                                 Technology.image.label('image'),
                                                 Project.timestamp.label('timestamp'),
                                                 Technology.name.label('technology'),
                                                 Category.name.label('category'),
                                                 Project.description.label('description'),
                                                 Project.url.label('url'),
                                                 Project.youtube.label('youtube')).\
                outerjoin(Technology, Project.technology_id == Technology.id).\
                outerjoin(Category, Project.category_id == Category.id).\
                order_by(Project.timestamp.desc()).all()
            return get_projects

        def single_project(self, project_id):

            get_single_project = self.db_session.query(Project.title.label('title'),
                                             Technology.image.label('image'),
                                             Project.timestamp.label('timestamp'),
                                             Technology.name.label('technology'),
                                             Category.name.label('category'),
                                             Project.description.label('description'),
                                             Project.url.label('url'),
                                             Project.youtube.label('youtube')).\
                outerjoin(Technology, Project.technology_id == Technology.id).\
                outerjoin(Category, Project.category_id == Category.id).\
                filter(Project.id == project_id).\
                order_by(Project.timestamp.desc()).first()
            return get_single_project

        def add_project_tracking(self, project_id, interaction_type):
            try:
                project_tracking = ProjectTracking(
                    project_id = project_id,
                    timestamp = datetime.datetime.now(),
                    interaction_type = interaction_type,
                    )
                self.db_session.add(project_tracking)
                self.db_session.commit()
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()



