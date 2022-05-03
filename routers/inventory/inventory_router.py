from fastapi import APIRouter, Depends
from pydantic import BaseModel

from typing import List

from sqlalchemy.orm import Session
from models.database import get_db
from models.inventory.inventory_model import InventoryBase, InventoryDisplayBase

from routers.inventory import inventory_controller
from utils.oauth2 import accessUserToken

router = APIRouter(prefix="/inventory", tags=["inventory"], dependencies=[Depends(accessUserToken)])


@router.get("/", response_model=List[InventoryDisplayBase])
def getAllInventory(db: Session = Depends(get_db)):
    return inventory_controller.read_inventory(db)


@router.get("/{id}")
def inventoryByID(id: int, db: Session = Depends(get_db)):
    return inventory_controller.read_inventory_by_id(db, id)


@router.post("/")
def create_inventory(req: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.create(db, req)


@router.put("/{id}")
def putApi(id: int, req: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.update(db, id, req)


@router.delete("/{id}")
def deleteApi(id: int, db: Session = Depends(get_db)):
    return inventory_controller.delete(db, id)
