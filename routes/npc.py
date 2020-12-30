def run(app, db, c, json):
    @app.route("/npc/create", methods=["POST"])
    async def create(request):
        c.npc.create(db, request)
        return json({"message": "success"})

    @app.route("/npc", methods=["GET"])
    async def read(request):
        return json({"response": c.npc.read(db, request)})

    @app.route("/npc", methods=["POST"])
    async def update(request):
        c.npc.update(db, request)
        return json({"message": "success"})

    @app.route("/npc", methods=["DELETE"])
    async def delete(request):
        c.npc.delete(db, request)
        return json({"message": "success"})
