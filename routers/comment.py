from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.comment import Comment
from models.post import Post
from models.user import User
from schemas.comment import CommentCreate, CommentUpdate, CommentResponse

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    post = db.query(Post).filter(Post.id == comment.post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    new_comment = Comment(
        content=comment.content,
        post_id=comment.post_id,
        user_id=user_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/", response_model=list[CommentResponse])
def list_comments(db: Session = Depends(get_db)):
    return db.query(Comment).all()

@router.get("/post/{post_id}", response_model=list[CommentResponse])
def list_post_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db.query(Comment).filter(Comment.post_id == post_id).all()

@router.put("/{comment_id}", response_model=CommentResponse)
def update_comment(comment_id: int, updated_comment: CommentUpdate, user_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != user_id:
        raise HTTPException(status_code=403, detail="You don't have the permission to edit this comment")
    
    comment.content = updated_comment.content
    db.commit()
    db.refresh(comment)
    return comment

@router.delete("/{comment_id}")
def del_comment(comment_id: int, user_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != user_id:
        raise HTTPException(status_code=403, detail="You don't have the permission to delete this comment")
    
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}