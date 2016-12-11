from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, aliased
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
                                       isolation_level="READ UNCOMMITTED", convert_unicode=True,
                                       pool_reset_on_return="rollback", pool_size=100, pool_recycle=600)
                Base.metadata.create_all(engine)
                Base.metadata.bind = engine
                Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
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

        def technology_choices(self, technology_id=None):

            try:
                if technology_id:
                    case_conditions = case([(Technology.id == technology_id, None)], else_=Technology.name).label("case_condition")
                    technologies = self.db_session.query(Technology).order_by(case_conditions.asc()).all()
                else:
                    technologies = self.db_session.query(Technology).order_by(Technology.name.asc()).all()
                return technologies
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()

        def category_choices(self, category_id=None):

            try:
                if category_id:
                    # categories = self.db_session.query(Category).order_by(case([(Category.id == category_id),], else_ = Category.name.asc())).all()

                    case_conditions = case([(Category.id == category_id, None)], else_=Category.name).label("case_condition")
                    categories = self.db_session.query(Category).order_by(case_conditions.asc()).all()
                else:
                    categories = self.db_session.query(Category).order_by(Category.name.asc()).all()
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
                technology = self.db_session.query(Technology).filter(Technology.name == technology_name).first()
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

        def add_project(self, title, category_id, technology_id, description, url, youtube):
            try:
                project = Project(
                    title = title,
                    timestamp = datetime.datetime.now(),
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

        def update_project(self, project_id, title, category_id, technology_id, description, url, youtube):
            try:
                self.db_session.query(Project).filter(Project.id == project_id).update({'title': title, 'timestamp': datetime.datetime.now(),
                                                                                        'category_id': category_id, 'technology_id': technology_id,
                                                                                        'description': description, 'url': url, 'youtube': youtube})
                self.db_session.commit()
            except:
                self.db_session.rollback()
                raise
            finally:
                self.db_session.close()


        def project(self, project_id=None):

            if project_id:
                get_project = self.db_session.query(Project.title.label('title'),
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
            else:
                get_project = self.db_session.query(Project.id.label('id'),
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

            return get_project

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

        def project_tracking(self):
            try:
                print "In try"
                hovers = aliased(ProjectTracking, name='hovers')
                git_clicks = aliased(ProjectTracking, name='git_clicks')
                youtube_clicks = aliased(ProjectTracking, name='youtube_clicks')

                get_project_stats = self.db_session.query(Project.title.label('title'),
                                                          func.count(hovers.id.distinct()).label('hovers'),
                                                          func.count(git_clicks.id.distinct()).label('git_clicks'),
                                                          func.count(youtube_clicks.id.distinct()).label('youtube_clicks')).\
                    outerjoin(hovers, and_(func.datediff(hovers.timestamp, datetime.datetime.now().date()) == 0,
                           hovers.interaction_type == "hover", hovers.project_id == Project.id)).\
                    outerjoin(git_clicks, and_(func.datediff(git_clicks.timestamp, datetime.datetime.now().date()) == 0,
                           git_clicks.interaction_type == "click-git", git_clicks.project_id == Project.id)).\
                    outerjoin(youtube_clicks, and_(func.datediff(youtube_clicks.timestamp, datetime.datetime.now().date()) == 0,
                           youtube_clicks.interaction_type == "click-youtube", youtube_clicks.project_id == Project.id)).\
                    group_by(Project.title).all()
                return get_project_stats
            except:
                print "In except"
                self.db_session.rollback()
                return False
            finally:
                self.db_session.close()

        def close_connection(self):
            self.db_session.close()


