from flask_script import Manager, Server
from app import init_app
from config import config

config = config["development"]
app = init_app(config)

manager = Manager(app)
manager.add_command("runserver", Server(host="127.0.0.1", port=5000))

if __name__ == '__main__':
    manager.run()
