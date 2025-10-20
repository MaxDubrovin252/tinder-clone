from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from .base import Base
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User
    
class Profile(Base):
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    bio:Mapped[str] = mapped_column()
    gender:Mapped[str] = mapped_column()
    location:Mapped[str] = mapped_column()
    time_created:Mapped[datetime] = mapped_column(default=datetime.now())
    time_updated:Mapped[datetime] = mapped_column(default=datetime.now())
    
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship("User", back_populates="profile")