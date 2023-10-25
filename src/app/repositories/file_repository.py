from sqlalchemy.orm import Session
from app.models.file import File
from app.schema.file import FileResponse

class FileRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_file(self, file_data: FileResponse):
        db_file = File(**file_data.dict())
        self.session.add(db_file)
        self.session.commit()
        self.session.refresh(db_file)
        return db_file

    def get_file_by_id(self, file_id: int):
        return self.session.query(File).filter(File.id == file_id).first()