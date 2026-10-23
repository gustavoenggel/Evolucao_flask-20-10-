
# CONTÉM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
# BOOK REPRESENTA A ENTIDADE BOOK

from uuid import uuid4
from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID
from db import db


class BooK(db.Model):
    # Define o nome da tabela
    __tablename__ = "book"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    title = db.Column(
        String(255),
        nullable=False
    )

    author = db.Column(
        String(255),
        nullable=False
    )

    description = db.Column(
        Text,
        nullable=False
    )

    id_reading = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    id_finished = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    # Converter o objeto em dicionário
    def as_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "id_reading": self.id_reading,
            "id_finished": self.id_finished
        }
