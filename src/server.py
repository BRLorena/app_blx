
from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # permitir front usar API

app = FastAPI()

#permissions
origins = ['http://127.0.0.1:5500']

#cadastrar os interceptors (middleware) permite CORS p/ algumas requests
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


#common
@app.get("/animais")
async def list_animals():
  return db

@app.get("/animal/{id_animal}")
async def getAnimal(id_animal: str):
  for animal in db:
    if animal.id == id_animal:   
      return {'mensagem': f'O id do {animal.name} é {id_animal}' }
  return {'mensagem': 'Animal not found'}

@app.post("/animal")
async def create_animal(animal: Animal):
  animal.id = str(uuid4()) #gerar id automatico -> cast to str
  db.append(animal)
  return {'Animal ': f' {animal.name} cadastrado com sucesso' }

@app.delete("/animal/{id_animal}")
async def remove_animal(id_animal: str):
  posicao_animal = -1
  for i, animal in enumerate(db):
    if animal.id == id_animal:
      posicao_animal = i
      break #encontrou posso parar
  if posicao_animal != -1:
    db.pop(posicao_animal)
    return {'mensagem': 'Animal removido com sucesso'}
  else:  
    return {'mensagem ': f'Animal não localizado' }
