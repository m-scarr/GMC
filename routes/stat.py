def run(app, db, c, json):
    @app.route("/stat/create", methods=["POST"])
    async def create(request):
        c.stat.create(db, request)
        return json({"message": "success"})

    @app.route("/stat", methods=["GET"])
    async def read(request):
        return json({"response": c.stat.read(db, request)})

    @app.route("/stat", methods=["POST"])
    async def update(request):
        c.stat.update(db, request)
        return json({"message": "success"})

    @app.route("/stat", methods=["DELETE"])
    async def delete(request):
        c.stat.delete(db, request)
        return json({"message": "success"})
