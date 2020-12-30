def run(app, db, c, json):
    @app.route("/game/create", methods=["POST"])
    async def create(request):
        c.game.create(db, request)
        return json({"message": "success"})

    @app.route("/game", methods=["GET"])
    async def read(request):
        return json({"response": c.game.read(db, request)})

    @app.route("/game", methods=["POST"])
    async def update(request):
        c.game.update(db, request)
        return json({"message": "success"})

    @app.route("/game", methods=["DELETE"])
    async def delete(request):
        c.game.delete(db, request)
        return json({"message": "success"})
