import uuid
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse, FileResponse
from models.sourse import Main_User, Main_UserDB, New_Respons
import hashlib
from typing import Union, Annotated

users_router = APIRouter()

def coder_passwd(cod: str):
    result = cod * 2


users_list = [Main_UserDB(name='Ivanov', id=108, password= "********************"), Main_UserDB(name='Petrov', id=148, password= "******************")]

def find_user(id):
   for user in users_list:
        if user.id == id:
           return user
   return None



@users_router.get("/api/users")
def get_users():
    return users_list



@users_router.get("/api/users/{id}")
def get_user(id):
    user = find_user(id)
    print(user)
    if user == None:
        return New_Respons(message="Пользователь не найден")
    return user


@users_router.post("/api/users")
def create_user(item: Annotated[Main_User, Body(embed=True, description="Новый пользователь")]):
    user = Main_UserDB(name=item.name, id=item.id, password=coder_passwd(item.name))
    users_list.append(user)
    return user


@users_router.put("/api/users")
def edit_user(item: Annotated[Main_User, Body(embed=True, description="Изменяем данные пользователя по его id")]):
    user = find_user(item.id)
    if user == None:
        return New_Respons(message="Пользователь не найден")
    user.name = item.name
    return user


@users_router.delete("/api/users/{id}")
def delete_user(id):
    user = find_user(id)
    if user == None:
        return New_Respons(message="Пользователь не найден")
    users_list.remove(user)
    return users_list
