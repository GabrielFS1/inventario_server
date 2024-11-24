# Inventory Management API

This project provides an API for managing inventory items, rooms, registers, and inventories. It supports various operations for creating, retrieving, updating, and deleting records for the following entities:

- Rooms
- Items
- Registers
- Inventories

The API is designed using Django and allows interaction with the database using RESTful principles.

---

## Table of Contents

1. API Endpoints
    - Rooms
    - Items
    - Registers
    - Inventories
2. Error Handling
3. Setup and Installation
4. Usage

---

## API Endpoints

### Rooms

#### `GET /salas_pesquisar`
- **Description**: Returns a list of rooms, with an optional `limit` query parameter to restrict the number of rooms.
- **Parameters**:
  - `limit` (optional): Integer specifying the number of rooms to return. Defaults to 3 if not provided.
- **Response**: JSON array with room data (id, name).

#### `GET /sala_consultar/{room_id}`
- **Description**: Returns a single room by its ID.
- **Parameters**:
  - `room_id`: The ID of the room to retrieve.
- **Response**: JSON object with room data (id, name).

#### `POST /sala_incluir`
- **Description**: Creates a new room.
- **Parameters**:
  - `name`: The name of the room.
- **Response**: Status code 201 indicating the room was created.

---

### Items

#### `GET /items_listar`
- **Description**: Returns a list of items, with an optional `limit` query parameter.
- **Parameters**:
  - `limit` (optional): Integer specifying the number of items to return. Defaults to 50 if not provided.
- **Response**: JSON array of items (id, name, barcode, room name).

#### `GET /item_consultar/{barcode}`
- **Description**: Returns a single item by its barcode.
- **Parameters**:
  - `barcode`: The barcode of the item to retrieve.
- **Response**: JSON object with item data (id, name, barcode, room).

#### `DELETE /item_deletar/{barcode}`
- **Description**: Deletes an item by its barcode.
- **Parameters**:
  - `barcode`: The barcode of the item to delete.
- **Response**: Status code 200 if deleted, or 404 if item not found.

#### `POST /item_incluir`
- **Description**: Creates a new item.
- **Parameters**:
  - `name`: The name of the item.
  - `barcode`: The barcode of the item.
  - `room`: The room ID where the item is located.
- **Response**: Status code 200 indicating the item was created.

---

### Registers

#### `GET /registros_listar`
- **Description**: Returns a list of all registers.
- **Response**: JSON array with register data (item name, room name, inventory name, author, date).

#### `POST /registro_incluir`
- **Description**: Creates a new register.
- **Parameters**:
  - `barcode`: Barcode of the item to register.
  - `room`: Room ID where the item is placed.
  - `inventory`: Inventory ID associated with the item.
  - `author` (optional): The author of the register.
- **Response**: Status code 201 indicating the register was created.

#### `DELETE /registro_deletar/{register_id}`
- **Description**: Deletes a register by its ID.
- **Parameters**:
  - `register_id`: The ID of the register to delete.
- **Response**: Status code 204 indicating the register was deleted.

---

### Inventories

#### `GET /inventarios_pesquisar`
- **Description**: Returns a list of all inventories.
- **Response**: JSON array of inventory data (id, name, date).

#### `GET /inventario_consultar/{id_inventario}`
- **Description**: Returns a single inventory by ID.
- **Parameters**:
  - `id_inventario`: The ID of the inventory to retrieve.
- **Response**: JSON object with inventory data (id, name, date).

#### `POST /inventario_incluir`
- **Description**: Creates a new inventory.
- **Parameters**:
  - `name`: The name of the inventory.
- **Response**: JSON object with the `id` of the newly created inventory.

#### `PUT /inventario_atualizar/{id_inventario}`
- **Description**: Updates an existing inventory by ID.
- **Parameters**:
  - `id_inventario`: The ID of the inventory to update.
  - `name`: The new name for the inventory (optional).
- **Response**: JSON object with the updated inventory `id`.

#### `DELETE /inventario_deletar/{id_inventario}`
- **Description**: Deletes an inventory by ID.
- **Parameters**:
  - `id_inventario`: The ID of the inventory to delete.
- **Response**: Status code 204 indicating the inventory was deleted.

---

### Additional Views

#### `POST /add_item`
- **Description**: Adds a new item to the database.
- **Parameters**:
  - `name`: The name of the item.
  - `barcode`: The barcode of the item.
  - `room`: The room ID where the item is located.
- **Response**: Status code 201 indicating the item was added.

#### `GET /get_item/{barcode}`
- **Description**: Retrieves an item by barcode.
- **Parameters**:
  - `barcode`: The barcode of the item.
- **Response**: JSON object with the item data.

#### `POST /add_read`
- **Description**: Adds a register entry with the given barcode and room ID.
- **Parameters**:
  - `barcode`: The barcode of the item.
  - `room`: The room ID associated with the item.
- **Response**: Status code 201 indicating the register entry was created.

#### `POST /add_register`
- **Description**: Adds a new register entry.
- **Parameters**:
  - `barcode`: The barcode of the item.
  - `room`: The room ID where the item is placed.
- **Response**: Status code 201 indicating the register entry was created.

#### `DELETE /del_register/{register_id}`
- **Description**: Deletes a register by its ID.
- **Parameters**:
  - `register_id`: The ID of the register to delete.
- **Response**: Status code 204 indicating the register was deleted.

---

### Error Handling

- **400 Bad Request**: Invalid parameters or data.
- **403 Forbidden**: Invalid HTTP method used (only supports GET, POST, PUT, DELETE as described).
- **404 Not Found**: The requested resource (item, room, register, inventory) was not found.
- **500 Internal Server Error**: An unexpected error occurred on the server.