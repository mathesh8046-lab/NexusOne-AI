
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.models.user import User

from app.schemas.ai_request import (
    AIRequestCreate,
    AIRequestResponse,
    AIRequestStatusUpdate
)

from app.services.ai_request_service import (
    create_ai_request,
    get_ai_request_by_id,
    get_user_ai_requests,
    update_ai_request_status,
    delete_ai_request
)


router = APIRouter()


# Create AI Request
@router.post(
    "/",
    response_model=AIRequestResponse,
    status_code=status.HTTP_201_CREATED
)
def create_request(
    request_data: AIRequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_ai_request(
        db=db,
        user_id=current_user.id,
        domain=request_data.domain,
        input_text=request_data.input_text
    )


# Get all requests of logged-in user
@router.get(
    "/",
    response_model=list[AIRequestResponse]
)
def get_my_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_ai_requests(
        db=db,
        user_id=current_user.id
    )


# Get individual request
@router.get(
    "/{request_id}",
    response_model=AIRequestResponse
)
def get_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ai_request = get_ai_request_by_id(db, request_id)

    if ai_request is None or ai_request.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AI request not found"
        )

    return ai_request


# Update request status
@router.patch(
    "/{request_id}/status",
    response_model=AIRequestResponse
)
def update_request_status(
    request_id: int,
    status_data: AIRequestStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ai_request = get_ai_request_by_id(db, request_id)

    if ai_request is None or ai_request.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AI request not found"
        )

    return update_ai_request_status(
        db=db,
        request_id=request_id,
        new_status=status_data.status
    )


# Delete request
@router.delete("/{request_id}")
def delete_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ai_request = get_ai_request_by_id(db, request_id)

    if ai_request is None or ai_request.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AI request not found"
        )

    delete_ai_request(db, request_id)

    return {
        "message": "AI request deleted successfully"
    }
