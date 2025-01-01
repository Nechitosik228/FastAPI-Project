from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session


from ..db import Comment
from ..schemas import UserModel


comment_router = APIRouter(prefix="/comments", tags=["Comments"])

@comment_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_comment(data: Comment, session:Annotated[Session]):
    None