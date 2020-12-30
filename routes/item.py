def run(app, db, c, json):
    @app.route("/item/create", methods=["POST"])
    async def create(request):
        c.item.create(db, request)
        return json({"message": "success"})

    @app.route("/item", methods=["GET"])
    async def read(request):
        return json({"response": c.item.read(db, request)})

    @app.route("/item", methods=["POST"])
    async def update(request):
        c.item.update(db, request)
        return json({"message": "success"})

    @app.route("/item", methods=["DELETE"])
    async def delete(request):
        c.item.delete(db, request)
        return json({"message": "success"})
