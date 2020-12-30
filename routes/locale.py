def run(app, db, c, json):
    @app.route("/locale/create", methods=["POST"])
    async def create(request):
        c.locale.create(db, request)
        return json({"message": "success"})

    @app.route("/locale", methods=["GET"])
    async def read(request):
        return json({"response": c.locale.read(db, request)})

    @app.route("/locale", methods=["POST"])
    async def update(request):
        c.locale.update(db, request)
        return json({"message": "success"})

    @app.route("/locale", methods=["DELETE"])
    async def delete(request):
        c.locale.delete(db, request)
        return json({"message": "success"})
