def run(app, db, c, json):
    @app.route("/enemy/create", methods=["POST"])
    async def create(request):
        c.enemy.create(db, request)
        return json({"message": "success"})

    @app.route("/enemy", methods=["GET"])
    async def read(request):
        return json({"response": c.enemy.read(db, request)})

    @app.route("/enemy", methods=["POST"])
    async def update(request):
        c.enemy.update(db, request)
        return json({"message": "success"})

    @app.route("/enemy", methods=["DELETE"])
    async def delete(request):
        c.enemy.delete(db, request)
        return json({"message": "success"})
