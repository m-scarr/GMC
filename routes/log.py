def run(app, db, c, json):
    @app.route("/log/create", methods=["POST"])
    async def create(request):
        c.log.create(db, request)
        return json({"message": "success"})

    @app.route("/log", methods=["GET"])
    async def read(request):
        return json({"response": c.log.read(db, request)})

    @app.route("/log", methods=["POST"])
    async def update(request):
        c.log.update(db, request)
        return json({"message": "success"})

    @app.route("/log", methods=["DELETE"])
    async def delete(request):
        c.log.delete(db, request)
        return json({"message": "success"})
