import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Identity

db = SQLAlchemy()

class AuthType(db.Model):
    __tablename__ = 'auth_type'

    guid = db.Column(
        UUID(as_uuid=True),
        unique=True,
        primary_key=True,
        nullable=False
    )
    enumname = db.Column(
        db.String(100)
    )
    enumorder = db.Column(
        db.Numeric(10),
        nullable=False
    )

    def __init__(self, guid, enumname, enumorder):
        self.guid = guid
        self.enumname = enumname
        self.enumorder = enumorder

    def __repr__(self):
        return f"{self.guid}:{self.enumname}:{self.enumorder}"


class Datasources(db.Model):
    __tablename__ = 'datasources'

    guid = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False)
    code = db.Column(db.Integer, Identity())
    description = db.Column(db.String(150))
    ref_auth_type = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('auth_type.guid'),
        nullable=False)
    httpaddress = db.Column(db.String(150))
    apibaseurl = db.Column(db.String(150))
    apischemeurl = db.Column(db.String(150))           
    authorizationjson = db.Column(db.String(150))       
    autorizationlogin = db.Column(db.String(150))      
    autorizationpassword = db.Column(db.String(150))      
    autorizationtoken = db.Column(db.String(150))      
    marked = db.Column(db.Boolean)       

    def __init__(self, guid, description, ref_auth_type, 
    httpaddress, apibaseurl, apischemeurl,authorizationjson,
    autorizationlogin, autorizationpassword, autorizationtoken, marked):
        self.guid = guid
        self.description = description
        self.ref_auth_type = ref_auth_type
        self.httpaddress = httpaddress
        self.apibaseurl = apibaseurl
        self.apischemeurl = apischemeurl
        self.authorizationjson = authorizationjson
        self.autorizationlogin = autorizationlogin
        self.autorizationpassword = autorizationpassword
        self.autorizationtoken = autorizationtoken
        self.marked = marked
