from pydoc import describe
from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse

from models.users.users_model  import userBase, UserDisplayBase, dbUser
from utils.hash import Hash


def create(db: Session, req: userBase):
    new_user = dbUser(
        username = req.username,
        password = Hash.bcrypt(req.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read_users(db: Session):
    return db.query(dbUser).all()


# def read_inventory_by_id(db: Session, id: int):
#     return db.query(DbInventory).filter(DbInventory.id == id).first()


# def delete(db:Session, id: int):
#     inventory = db.query(DbInventory).filter(DbInventory.id == id).first()
#     db.delete(inventory)
#     db.commit()
#     return JSONResponse(content={'details': f"inventory id {id} deleted"})


# def update(db:Session, id: int, req: InventoryBase):
#     inventory = db.query(DbInventory).filter(DbInventory.id == id).first()
#     inventory.description = req.description
#     inventory.price = req.price
#     inventory.stock = req.stock
#     db.commit()
#     db.refresh(inventory)
#     return inventory
