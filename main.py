import fastapi
import uvicorn
import MenuItem
import DatabaseSQL

app = fastapi.FastAPI()

pizza_db = DatabaseSQL.Database('pizza_menu')
pizzas = '''
CREATE TABLE IF NOT EXISTS pizzas(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL
)
'''
pizza_db.create_table(pizzas)


@app.post('/create',status_code=201)
async def create_menu_item(item:MenuItem.Pizza):
    pizza_db.create_item('pizzas',item.name,item.description,item.price)

@app.get('/items',status_code=201)
async def read_menu_items():
    available_pizzas = pizza_db.get_items('pizzas')
    return available_pizzas

@app.put('/update/{item_id}',status_code=200)
async def update_menu_item(item_id:int,item:MenuItem.Pizza):
    pizza_db.update_item('pizzas',item_id,item.dict(exclude_unset=True))

@app.delete("/delete/{item_id}", status_code=204)
async def delete_pizza(item_id: int):
    pizza_db.delete_item("pizzas", item_id)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
