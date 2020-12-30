def create(db, request):
    return db.create(db.os.path.basename(db.os.path.realpath(__file__)[:-3]), **(db.json.loads(request.body)))


def read(db, request):
    return db.read(db.os.path.basename(db.os.path.realpath(__file__)[:-3]), **(db.json.loads(request.body)))


def update(db, request):
    return db.update(db.os.path.basename(db.os.path.realpath(__file__)[:-3]), **(db.json.loads(request.body)))


def delete(db, request):
    data = db.json.loads(request.body)
    return db.delete(db.os.path.basename(db.os.path.realpath(__file__)[:-3]), data['where'])
