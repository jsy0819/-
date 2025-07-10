#./app/main.py
from fastapi import FastAPI, Query, Depends, HTTPException, status, Request
#html 인식
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse

from typing import Optional, List
#sqlmodel 핵심 기능
from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Text, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload #selectinlload
#pydantic BaseModel 출력용으로 사용
from pydantic import BaseModel

# AsyncSessionLocal은 startup에서 데이터 삽입용
from database import engine, AsyncSessionLocal, get_session
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    profile:Optional["Profiles"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "primaryjoin":"Users.id == Profiles.user_id",
            "foreign_keys":"[Profiles.user_id]",
            "uselist":False,
            "cascade":"all, delete-orphan"
        }
    )

    posts:List["Posts"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "primaryjoin":"Users.id == Posts.user_id",
            "foreign_keys":"[Posts.user_id]",
            "cascade":"all, delete-orphan"
        }
    )

class Profiles(SQLModel, table=True):
    #user_id:Optional[int] = Field(default=None, primary_key=True)
    user_id:Optional[int] = Field(sa_column=Column(Integer, primary_key=True, autoincrement=False))
    bio: Optional[str] = Field(sa_type=Text, nullable=True)
    phone:Optional[str] = Field(default=None, max_length=20, nullable=True)

    user:Optional["Users"] = Relationship(
        back_populates="profile",
        sa_relationship_kwargs={
            "primaryjoin":"Profiles.user_id == Users.id",
            "foreign_keys":"[Profiles.user_id]",
            "uselist":False
        }
    )

class Posts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(default=None, max_length=100)
    content: Optional[str] = Field(default=None, sa_type=Text, nullable=True)
    user_id: Optional[int] = Field(default=None, nullable=True)
    cnt: Optional[int] = Field(default=0, ge=0)
    
    user:Optional["Users"] = Relationship(
        back_populates="posts",
        sa_relationship_kwargs={
            "primaryjoin":"Posts.user_id == Users.id",
            "foreign_keys":"[Posts.user_id]",
        }
    )

#nullable=True

class UsersProfile(BaseModel):
    id: int
    username:str
    email:str
    # phone과 bio 필드를 최상위 레벨에 Optional로 추가
    phone: Optional[str] = None
    bio: Optional[str] = None

class UserProfile(BaseModel):
    id: int
    username:str
    email:str
    profile: Optional[Profiles] = None
    class Config:
        from_attributes = True

class PostOutput(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    cnt: int
    class Config:
        from_attributes = True
class UserPosts(BaseModel):
    id: int
    username:str
    email:str
    posts: List[PostOutput] 
    class Config:
        from_attributes = True

class UserRead(BaseModel):
    id:int
    username:str
    email:str
    class Config:
        from_attributes = True # orm 객체에서 속성 가져오기 허용

class ProfileRead(BaseModel):
    user_id: int
    bio:Optional[str] = None
    phone:Optional[str] = None
    class Config:
        from_attributes = True # orm 객체에서 속성 가져오기 허용

class PostRead(BaseModel):
    id:int
    title:str
    content:Optional[str] = None
    user_id:Optional[int] = None
    cnt:Optional[int] = None
    class Config:
        from_attributes = True

class UserCreate(SQLModel):
    username: str
    email: str

class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[str] = None

class PostCreate(SQLModel):
    title: str
    content: Optional[str] = None
    user_id: int

class PostUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="../static"), name="static")

@app.on_event("startup")
async def on_startup():
    #SQLModel.metadata.create_all(engine)
    async with engine.begin() as conn: # 비동기 컨넥션 시작
        await conn.run_sync(SQLModel.metadata.create_all)

@app.get("/register/", response_class=HTMLResponse)
async def get_register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "form_type" : "new_user"
        }
    )

@app.post("/users/init/")
def init_users():
    sample_users = [
        Users(username=f"User{i}", email=f"user{i}@example.com") for i in range(1, 21)
    ]
    with Session(engine) as session:
        for user in sample_users:
            session.add(user)
        session.commit()
    return {"message": "20 users initialized"}

# 특정 사용자 조회 (ID로 한 명)
@app.get("/users/{user_id}/edit", response_class=HTMLResponse)
async def get_user_edit_form(
        request: Request,
        user_id: int, 
        session: AsyncSession=Depends(get_session)
    ):
    user = await session.get(Users, user_id)  # ID로 조회
    if not user:  # 없으면 404 에러
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "form_type": "edit_user",
            "user": user
        }
    )

@app.get("/posts/create/{user_id}", response_class=HTMLResponse)
async def get_post_create_form(
    request: Request,
    user_id: int,
    session: AsyncSession = Depends(get_session)
):
    user = await session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="게시글을 작성할 사용자를 찾을 수 없습니다.")
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "form_type": "new_post",
            "user_id": user_id
        }
    )

@app.get("/posts/{post_id}/edit", response_class=HTMLResponse)
async def get_post_edit_form(
    request: Request,
    post_id: int,
    session: AsyncSession = Depends(get_session)
):
    post = await session.get(Posts, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "form_type": "edit_post",
            "post": post
        }
    )

@app.get("/users/all/", response_class=HTMLResponse)
async def read_all_users_html(request: Request, session: AsyncSession=Depends(get_session)):
    statement = select(Users).order_by(Users.id.desc())
    result = await session.execute(statement)
    users = result.scalars().all() 
    return templates.TemplateResponse(
        "user_list.html",
        {
            "request": request,
            "users": users
        }
    )

@app.patch("/users/{user_id}", response_model=UserRead)
async def update_user(
    user_id:int, 
    user_update:UserUpdate,
    session: AsyncSession=Depends(get_session) 
):
    print(f"입력받은 데이터 (user_update): {user_update}")
    user = await session.get(Users, user_id)
    if not user:  # 없으면 404 에러
        raise HTTPException(status_code=404, detail="User not found")
    print(f"업데이트 전 사용자 정보: id={user.id}, username={user.username}, email={user.email}")

    user_data = user_update.model_dump(exclude_unset=True)
    if not user_data:
        raise HTTPException(status_code=400, detail="업데이트할 칼럼이 없습니다.")
    print(f"업데이트될 데이터 (user_data): {user_data}")
    for key, value in user_data.items():
        setattr(user, key, value)
    print(f"업데이트될 데이터 (user): {user}")
    #session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id:int,
    session: AsyncSession=Depends(get_session)
):
    print(f"{user_id} 들어왔는 지 알아보고 들어왔으면 delete 시작")
    user = await session.get(Users, user_id)  # ID로 조회
    print(f"user 값 확인 : {user} ")
    if not user: #없으면 404에러
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    
    await session.delete(user)
    await session.commit()
    return

@app.post("/posts/", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(post_data: PostCreate, session: AsyncSession=Depends(get_session)):
    db_post = Posts.model_validate(post_data)
    try:
        session.add(db_post)
        await session.commit()
        await session.refresh(db_post)
        logger.info(f"Post created: {db_post.title} by user ID {db_post.user_id}")
        return db_post
    except Exception as e:
        await session.rollback()
        logger.error(f"Error creating post: {e}")
        raise HTTPException(status_code=500, detail="Failed to create post.")
    
@app.patch("/posts/{post_id}", response_model=PostRead)
async def update_post(
    post_id: int,
    post_update: PostUpdate,
    session: AsyncSession = Depends(get_session)
):
    """특정 게시글의 정보를 업데이트합니다."""
    post = await session.get(Posts, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    update_data = post_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="업데이트할 내용이 없습니다.")
    for key, value in update_data.items():
        setattr(post, key, value)
    await session.commit()
    await session.refresh(post)
    return post

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    session: AsyncSession = Depends(get_session)
):
    """특정 게시글을 삭제합니다."""
    post = await session.get(Posts, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    await session.delete(post)
    await session.commit()
    return

@app.get("/users/", response_model=List[UserRead])
async def read_paging_users(page:int=Query(1,ge=1),session: Session=Depends(get_session)):
    size = 10
    offset = (page-1)*size
    statement = select(Users).offset(offset).limit(size)
    result = await session.execute(statement)
    users = result.scalars().all()  # 결과에서 스칼라 객체 추출
    return users

@app.get("/posts/", response_model=List[PostRead])
async def read_paging_posts(page:int=Query(1,ge=1),session: AsyncSession=Depends(get_session)):
    size = 10
    offset = (page-1)*size
    statement = select(Posts).offset(offset).limit(size)
    result = await session.execute(statement)
    posts = result.scalars().all()  # 결과에서 스칼라 객체 추출
    return posts
    
@app.get("/users/", response_model=List[UserRead])
async def read_paging_users(page:int = Query(1, ge=1), session: AsyncSession=Depends(get_session)):
    size = 10
    offset = (page - 1) * size
    statement = select(Users).offset(offset).limit(size)
    result = await session.execute(statement)
    users = result.scalars().all()
    return users

@app.post("/users/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    db_user = Users.model_validate(user)
    try:
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)

        db_profile = Profiles(user_id=db_user.id, bio="자기소개를 입력해주세요.", phone=None)
        session.add(db_profile)
        await session.commit()
        await session.refresh(db_profile)

        logger.info(f"User {db_user.username} created with ID {db_user.id}")
        return db_user
    except Exception as e:
        await session.rollback()
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Failed to add user.")

@app.get("/users/profile/{id}", response_model=UserProfile)
async def read_user_profile(id: int, session: AsyncSession = Depends(get_session)):
    statement = select(Users).options(selectinload(Users.profile)).where(Users.id == id)
    result = (await session.execute(statement)).scalar_one_or_none()

    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    user = result
    return UserProfile(
        id=user.id,
        username=user.username,
        email=user.email,
        profile=user.profile
    )

@app.get("/users/profile/", response_model=List[UsersProfile])
async def read_paging_user_profile(page: int = Query(1, ge=1), session: AsyncSession = Depends(get_session)):
    size = 10
    offset = (page - 1) * size
    
    statement = (
        select(Users).options(selectinload(Users.profile))
        .offset(offset).limit(size)
    )
    results = (await session.execute(statement)).scalars().all()

    user_profiles_list = []
    for user in results:
        phone_data = user.profile.phone if user.profile else None
        bio_data = user.profile.bio if user.profile else None

        user_profiles_list.append(
            UsersProfile(
                id=user.id,
                username=user.username,
                email=user.email,
                phone=phone_data,
                bio=bio_data
            )
        )
    return user_profiles_list

@app.get("/users/posts/{user_id}/", response_model=UserPosts)
async def read_user_posts(user_id: int, page: int = Query(1, ge=1), session: AsyncSession = Depends(get_session)):
    size = 10
    offset = (page - 1) * size

    user_stmt = select(Users).where(Users.id == user_id)
    user_result = await session.execute(user_stmt)
    user = user_result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    posts_stmt = (
        select(Posts)
        .where(Posts.user_id == user_id)
        .offset(offset)
        .limit(size)
    )
    posts_result = await session.execute(posts_stmt)
    posts_list_from_db = posts_result.scalars().all()

    return UserPosts(
        id=user.id,
        username=user.username,
        email=user.email,
        posts=[PostOutput.model_validate(post, from_attributes=True) for post in posts_list_from_db]
    )