
from sqlalchemy.orm import Session

from app.models.ai_request import AIRequest


def create_ai_request(
    db: Session,
    user_id: int,
    domain: str,
    input_text: str
):
    new_request = AIRequest(
        user_id=user_id,
        domain=domain,
        input_text=input_text
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request


def get_ai_request_by_id(db: Session, request_id: int):
    return (
        db.query(AIRequest)
        .filter(AIRequest.id == request_id)
        .first()
    )


def get_user_ai_requests(db: Session, user_id: int):
    return (
        db.query(AIRequest)
        .filter(AIRequest.user_id == user_id)
        .order_by(AIRequest.created_at.desc())
        .all()
    )


def update_ai_request_status(
    db: Session,
    request_id: int,
    new_status: str
):
    ai_request = get_ai_request_by_id(db, request_id)

    if ai_request is None:
        return None

    ai_request.status = new_status

    db.commit()
    db.refresh(ai_request)

    return ai_request


def delete_ai_request(db: Session, request_id: int):
    ai_request = get_ai_request_by_id(db, request_id)

    if ai_request is None:
        return False

    db.delete(ai_request)
    db.commit()

    return True
