import sqlite3


class Database:

    def __init__(self, db):
        self.db = db
        self.connection = self.connect()

    def connect(self):
        try:
            connection = sqlite3.connect(self.db)
            print('Connected')
            return connection
        except sqlite3.Error:
            print('Connection failed')

    def create_table(self, table):
        try:
            conn = self.connection.cursor()
            conn.execute(table)
        except sqlite3.Error:
            print('Creation failed')

    def create_item(self,table_name:str, name:str,description:str,price:float):
        query = f'''INSERT INTO {table_name}(name,description,price) VALUES(?,?,?)'''
        query_exec = self.connection.cursor()
        query_exec.execute(query,(name,description,price))
        self.connection.commit()


    def get_items(self,table_name:str):
        query_exec = self.connection.cursor()
        query_exec.execute(f'SELECT * FROM {table_name}')
        pizza_rows = query_exec.fetchall()
        pizza_columns = [description[0] for description in query_exec.description]

        return [dict(zip(pizza_columns,row)) for row in pizza_rows]

    def update_item(self,table_name:str, item_id:int, item_data:dict):
        columns = ', '.join([f'{k}=?' for k in item_data.keys()])
        values = list(item_data.values()) + [item_id]
        update_query = f'UPDATE {table_name} SET {columns} WHERE id=?'

        query_exec = self.connection.cursor()
        query_exec.execute(update_query,values)
        self.connection.commit()

    def delete_item(self, table_name: str, item_id: int):
        delete_query = f'DELETE FROM {table_name} WHERE id=?'
        query_exec = self.connection.cursor()
        query_exec.execute(delete_query, (item_id,))
        self.connection.commit()

    def disconnect(self):
        if self.connection:
            self.connection.close()


