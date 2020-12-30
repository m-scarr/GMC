def run(app, db, c, json):
    @app.route("/event/create", methods=["POST"])
    async def create(request):
        c.event.create(db, request)
        return json({"message": "success"})

    @app.route("/event", methods=["GET"])
    async def read(request):
        return json({"response": c.event.read(db, request)})

    @app.route("/event", methods=["POST"])
    async def update(request):
        c.event.update(db, request)
        return json({"message": "success"})

    @app.route("/event", methods=["DELETE"])
    async def delete(request):
        c.event.delete(db, request)
        return json({"message": "success"})
