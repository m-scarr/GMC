def run(app, db, c, json):
    @app.route("/group/create", methods=["POST"])
    async def create(request):
        c.group.create(db, request)
        return json({"message": "success"})

    @app.route("/group", methods=["GET"])
    async def read(request):
        return json({"response": c.group.read(db, request)})

    @app.route("/group", methods=["POST"])
    async def update(request):
        c.group.update(db, request)
        return json({"message": "success"})

    @app.route("/group", methods=["DELETE"])
    async def delete(request):
        c.group.delete(db, request)
        return json({"message": "success"})
