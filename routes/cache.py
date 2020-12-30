def run(app, db, c, json):
    @app.route("/cache/create", methods=["POST"])
    async def create(request):
        c.cache.create(db, request)
        return json({"message": "success"})

    @app.route("/cache", methods=["GET"])
    async def read(request):
        return json({"response": c.cache.read(db, request)})

    @app.route("/cache", methods=["POST"])
    async def update(request):
        c.cache.update(db, request)
        return json({"message": "success"})

    @app.route("/cache", methods=["DELETE"])
    async def delete(request):
        c.cache.delete(db, request)
        return json({"message": "success"})
