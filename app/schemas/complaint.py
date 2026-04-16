from pydantic import BaseModel


class ComplaintCreate(BaseModel):
    description: str
    format: str
    tone: str

class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    generated_text: str | None
    format: str | None
    tone: str | None
    status: str

    class Config:
        orm_mode = True


