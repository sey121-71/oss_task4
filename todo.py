from fastapi import APIRouter
from model import Todo  
import json
import os

todo_router = APIRouter()
FILE_PATH = "data.json"  


def load_todos():
    if not os.path.exists(FILE_PATH):
        return []  
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return [] 

def save_todos(todos):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        
        json.dump(todos, f, ensure_ascii=False, indent=4)

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    
    todos = load_todos()           
    todos.append(todo.dict())      
    save_todos(todos)              
    
    return {
        "msg" : "과목 정보가 JSON 파일에 성공적으로 저장되었습니다."
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    todos = load_todos()           
    return {
        "todos" : todos
    }
