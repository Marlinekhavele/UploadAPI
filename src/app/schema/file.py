from pydantic import BaseModel

class FileResponse(BaseModel):
    id: int
    filename: str
    status: str


    class Config:
        orm_mode= True
