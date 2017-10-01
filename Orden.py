ingredientsList = ["cebolla", "salsa", "cilantro", "aguacate", "frijoles"]
tacoTypesList = ["taco", "quesadilla", "mulita", "tostada", "vampiro"]
meatTypesList = ["asada", "adobada", "cabeza", "lengua", "suadero", "veggie", "tripa"]

class Orden:
    def __init__(self, datetime, request_id, subOrdenes):
        this.datetime = datetime #String
        this.request_id = request_id #String
        this.subOrdenes = subOrdenes #List of subOrden objects
        this.startTime = -1
        this.endTime = -1
        this.steps = [] #List of stepObjects that will be inserted

    def addNewStep(step):
        this.steps.append(step)

    def getLastStep():
        n = len(this.steps)
        if n > 0:
            return this.steps[n-1]
        else:
            return -1

class subOrden:
    def __init__(self, part_id, tacoType, meatType, quantity, ingredients):
        this.part_id = part_id #String
        this.tacoType = tacoType #String
        this.meatType = meatType #String
        this.quantity = quantity #Integer
        this.ingredients = ingredients #List of strings
        this.remainingTacos = quantity #Integer (Counter to keep track of remaining tacos)

class Step:
    def __init__(self, stepNumber, startTime, action):
        this.stepNumber = stepNumber #Integer
        this.startTime = startTime #String
        this.action = action #String
        this.endTime = -1 #Integer (undefined when the object is created)

