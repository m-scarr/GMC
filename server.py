from sanic import Sanic
import routes.index as routes
import models.index as db
import controllers.index as controllers_
db.initialize()

server = Sanic(__name__)

routes.run(server, db, controllers_)

if __name__ == '__main__':
    server.run(host=db.config["server_host"], port=db.config["server_port"])
