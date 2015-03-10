from pony.orm import PrimaryKey, Required, Set
from Todo import db

class Todo(db.Entity):
    id = PrimaryKey(int, auto=True)
    text = Required(unicode)
    tags = Set("Tag")


class Tag(db.Entity):
    id = PrimaryKey(int, auto=True)
    text = Required(unicode)
    todos = Set(Todo)



