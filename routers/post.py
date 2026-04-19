from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.post import Post
from models.user import User
from schemas.post import PostCreate, PostResponse

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, author_id: int, db: Session = Depends(get_db)):
    author = db.query(User).filter(User.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="User not found")
    if not author.is_author:
        raise HTTPException(status_code=403, detail="User does not have the permission to create posts")
    
    new_post = Post(
        title=post.title,
        content=post.content,
        author_id=author_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=list[PostResponse])
def list_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@router.get("/{post_id}", response_model=PostResponse)
def fetch_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, updated_post: PostCreate, author_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != author_id:
        raise HTTPException(status_code=403, detail="You don't have the permission to edit this post")
    
    post.title = updated_post.title
    post.content = updated_post.content
    db.commit()
    db.refresh(post)
    return post

@router.delete("/{post_id}")
def del_post(post_id: int, author_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != author_id:
        raise HTTPException(status_code=403, detail="You dont have the permission to delete this post")
    
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}