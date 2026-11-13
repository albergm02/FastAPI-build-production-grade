from fastapi import FastAPI, Query, HTTPException
from data import menu_items
from models import MenuItem, MenuResponse

app = FastAPI(
    title="Chai Menu API",
    description="An API for managing a menu of chai drinks.",
)

@app.get("/")
def welcome():
    return {"message": "Welcome to the Chai Menu API!"}

@app.get("/menu", response_model=MenuResponse)
def get_menu(category: str | None = Query(None, description="Filter by Chai, snack or combo")):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail="No items found for the specified category.")
        return MenuResponse(count=len(filtered), items=filtered)
    return MenuResponse(count=len(menu_items), items=menu_items)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_menu_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Menu item with id {item_id} not found.")