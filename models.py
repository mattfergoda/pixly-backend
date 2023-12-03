"""Models for Pixly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Image(db.Model):
    """Data model for Image"""

    __tablename__ = "images"

    file_name = db.Column(
        db.String(50),
        primary_key=True)

    caption = db.Column(
        db.String(200)
    )

    description = db.Column(
        db.Text()
    )

    aws_image_src = db.Column(
        db.String(100)
    )

    exif_data = db.Column(
        db.JSON()
    )

    uploaded_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now()
    )


    def serialize(self):
        """Serialize to a dictionary."""

        return {
            "file_name": self.file_name,
            "caption": self.caption,
            "description": self.description,
            "aws_image_src": self.aws_image_src,
            "exif_data": self.exif_data,
            "uploaded_at": self.uploaded_at
        }



def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


# class Metadata(db.Model):
#     """ Data model for exif tags on images """

#     __tablename__ = "metadata"

#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#         autoincrement=True)

#     # 37377
#     tag = db.Column(
#         db.Integer,
#         nullable=False
#     )

#     # 'ShutterSpeedValue'
#     tag_name = db.Column(
#         db.String,
#     )

#     # 1/400
#     tag_value = db.Column(
#         db.String(200),

#     )



    # def to_dict(self):
    #     """Serialize cupcake to a dict of cupcake info."""

    #     return {
    #         "id": self.id,
    #         "flavor": self.flavor,
    #         "rating": self.rating,
    #         "size": self.size,
    #         "image_url": self.image_url,
    #     }


