def run(app, db, c, json):
    @app.route("/group_member/create", methods=["POST"])
    async def create(request):
        c.group_member.create(db, request)
        return json({"message": "success"})

    @app.route("/group_member", methods=["GET"])
    async def read(request):
        return json({"response": c.group_member.read(db, request)})

    @app.route("/group_member", methods=["POST"])
    async def update(request):
        c.group_member.update(db, request)
        return json({"message": "success"})

    @app.route("/group_member", methods=["DELETE"])
    async def delete(request):
        c.group_member.delete(db, request)
        return json({"message": "success"})
