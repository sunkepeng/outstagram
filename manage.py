# -*- coding: utf-8 -*-

from outstagram import app, db
from flask_script import Manager
from outstagram.models import User, Image, Comment
import random, unittest, tests

manager = Manager(app)


def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'


@manager.command
def run_test():
    #init_database()
    db.drop_all()
    db.create_all()
    tests = unittest.TestLoader().discover('./')
    unittest.TextTestRunner().run(tests)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('test' + str(i), 'a' + str(i)))

        for j in range(0, 3):  # 每人发三张图
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('这是一条评论' + str(k), 1 + 3 * i + j, i + 1))
    db.session.commit()


if __name__ == '__main__':
    manager.run()
