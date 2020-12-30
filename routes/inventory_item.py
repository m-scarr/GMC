def run(app, db, c, json):
    @app.route("/inventory_item/create", methods=["POST"])
    async def create(request):
        c.inventory_item.create(db, request)
        return json({"message": "success"})

    @app.route("/inventory_item", methods=["GET"])
    async def read(request):
        return json({"response": c.inventory_item.read(db, request)})

    @app.route("/inventory_item", methods=["POST"])
    async def update(request):
        c.inventory_item.update(db, request)
        return json({"message": "success"})

    @app.route("/inventory_item", methods=["DELETE"])
    async def delete(request):
        c.inventory_item.delete(db, request)
        return json({"message": "success"})
