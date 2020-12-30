def run(app, db, c, json):
    @app.route("/user/create", methods=["POST"])
    async def create(request):
        c.user.create(db, request)
        return json({"message": "success"})

    @app.route("/user", methods=["GET"])
    async def read(request):
        return json({"response": c.user.read(db, request)})

    @app.route("/user", methods=["POST"])
    async def update(request):
        c.user.update(db, request)
        return json({"message": "success"})

    @app.route("/user", methods=["DELETE"])
    async def delete(request):
        c.user.delete(db, request)
        return json({"message": "success"})
