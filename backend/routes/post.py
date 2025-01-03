from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select, update
from sqlalchemy.orm import Session


from ..db import Post, get_session
from ..schemas import PostModel


post_router = APIRouter(prefix="/posts", tags=["Posts"])


@post_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_post(data: PostModel, session: Annotated[Session, Depends(get_session)]):
    post = Post(**data.model_dump())
    session.add(post)
    return post


@post_router.put("/update")
def update_post(
    data: PostModel, post_id: int, session: Annotated[Session, Depends(get_session)]
):
    post = session.scalar(select(Post).where(Post.id == post_id))
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")

    post_update = update(Post).where(Post.id == post_id).values(**data.model_dump())
    session.execute(post_update)
    session.commit()
    return {"detail": f"Post with id {post_id} updated successfully"}


@post_router.delete("/delete_post/{post_id}")
def delete_post(post_id: int, session: Annotated[Session, Depends(get_session)]):
    post = session.scalar(select(Post).where(Post.id == post_id))
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    session.delete(post)
    session.commit()
    return {"detail": f"Post with id {post_id} deleted successfully"}


@post_router.delete("/delete_all_posts")
def delete_all_posts(session: Annotated[Session, Depends(get_session)]):
    posts = session.query(Post).all()
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found to delete")

    for post in posts:
        session.delete(post)

    session.commit()
    return {"detail": "All posts deleted successfully"}
