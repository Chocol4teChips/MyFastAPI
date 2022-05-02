from pydoc import describe
from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse
# from sympy import content
from models.inventory.inventory_model import DbInventory, InventoryBase


def create(db: Session, req: InventoryBase):
    new_inventory = DbInventory(
        description = req.description,
        price = req.price,
        stock = req.stock
    )
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


def read_inventory(db: Session):
    return db.query(DbInventory).all()


def read_inventory_by_id(db: Session, id: int):
    return db.query(DbInventory).filter(DbInventory.id == id).first()


def delete(db:Session, id: int):
    inventory = db.query(DbInventory).filter(DbInventory.id == id).first()
    db.delete(inventory)
    db.commit()
    return JSONResponse(content={'details': f"inventory id {id} deleted"})


def update(db:Session, id: int, req: InventoryBase):
    inventory = db.query(DbInventory).filter(DbInventory.id == id).first()
    inventory.description = req.description
    inventory.price = req.price
    inventory.stock = req.stock
    db.commit()
    db.refresh(inventory)
    return inventory
