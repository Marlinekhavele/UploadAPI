from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repositories.file_repository import FileRepository
from app.schema.file import  FileResponse
from app.deps import get_db_session

router = APIRouter()

@router.post("/upload/", response_model=FileResponse)
async def upload_file(
    file: UploadFile,
    db: Session = Depends(get_db_session),
    file_repo: FileRepository = Depends(FileRepository)
):
    try:
        file_data = FileResponse(filename=file.filename, status="Processing")
        db_file = file_repo.create_file(file_data)
        with open(f"uploads/{db_file.id}_{file.filename}", "wb") as f:
            f.write(file.file.read())

        response_data = {
            "id": db_file.id,
            "filename": db_file.filename,
            "status": db_file.status
        }

        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to upload and process the file")





