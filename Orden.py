ingredientsList = ["cebolla", "salsa", "cilantro", "aguacate", "frijoles"]
tacoTypesList = ["taco", "quesadilla", "mulita", "tostada", "vampiro"]
meatTypesList = ["asada", "adobada", "cabeza", "lengua", "suadero", "veggie", "tripa"]

class Orden:
    def __init__(self, datetime, request_id, subOrdenes):
        this.datetime = datetime #String
        this.request_id = request_id #String
        this.subOrdenes = subOrdenes #List of subOrden objects

class subOrden:
    def __init__(self, part_id, tacoType, meatType, quantity, ingredients):
        this.part_id = part_id #String
        this.tacoType = tacoType #String
        this.meatType = meatType #String
        this.quantity = quantity #Integer
        this.ingredients = ingredients #List of strings
        this.remainingTacos = quantity #Integer (Counter to keep track of remaining tacos)
