# from datetime import datetime

from pydantic import BaseModel, NaiveDatetime


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: NaiveDatetime | None
