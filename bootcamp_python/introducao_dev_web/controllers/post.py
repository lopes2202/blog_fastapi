 
from fastapi import Response, FastAPI, status, Cookie, Header, APIRouter
from schemas.post import PostIn
from views.post import PostOut
from models.post import posts
from database import database



@router.get("/", response_model=list[PostOut])
async def read_posts(
               published: bool, 
               limit: int, 
               skip: int = 0, 
              
    ):
    query = posts.select()
    return await database.fetch_all(query)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=PostOut)
async def list_posts(id: int):
    query = (
        posts.select()
        .where(posts.c.id == id)
    )
    return await database.fetch_one(query)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    command = posts.insert().values(title=post.title, content=post.content, published_at=post.published_at, published=post.published)
    
    last_id = await database.execute(command)
    return {**post.model_dump(), "id": last_id}


@router.put("/{post_id}", status_code=status.HTTP_200_OK, response_model=PostOut)
async def update_post(post_id: int, post: PostIn):
    command_update = (
    posts.update()
    .where(posts.c.id == post_id)
    .values(title=post.title, content=post.content)
)
    await database.execute(command_update)
    return {**post.model_dump(), "id": post_id}

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    command_delete = (
    posts.delete().where(posts.c.id == post_id)
    )
    await database.execute(command_delete)
    return None