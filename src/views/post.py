from datetime import datetime

from pydantic import AwareDatetime, BaseModel  # type: ignore


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: AwareDatetime | None
