def run(app, db, c, json):
    @app.route("/hero/create", methods=["POST"])
    async def create(request):
        c.hero.create(db, request)
        return json({"message": "success"})

    @app.route("/hero", methods=["GET"])
    async def read(request):
        return json({"response": c.hero.read(db, request)})

    @app.route("/hero", methods=["POST"])
    async def update(request):
        c.hero.update(db, request)
        return json({"message": "success"})

    @app.route("/hero", methods=["DELETE"])
    async def delete(request):
        c.hero.delete(db, request)
        return json({"message": "success"})
