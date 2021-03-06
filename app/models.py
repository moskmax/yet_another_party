# -*- coding: utf-8 -*-
from app import db

class Attribute(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Attribute {}>'.format(self.text)


class AttributeMapper(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'))
    text = db.Column(db.String(64), index=True)
    attribute_value_id = db.Column(db.Integer, index=True)
    
    def __repr__(self):
        return '<AttributeMapper {}-{}>'.format(self.text, self.attribute_value_id)
        
        
class RestInfo(db.Model):
    __tablename__ = 'rest_info'

    id = db.Column(db.Integer, primary_key=True)
    id_rest = db.Column(db.Integer, index=True) 
    name = db.Column(db.String(256)) 
    address = db.Column(db.String(256))
    url = db.Column(db.String(256)) 
    phone = db.Column(db.String(64)) 
    latitude = db.Column(db.String(64)) 
    longitude = db.Column(db.String(64))
    billMin = db.Column(db.String(64)) 
    billMax = db.Column(db.String(64))
    description = db.Column(db.String(4096))
    photourl = db.Column(db.String(256))

    def __repr__(self):
        return u'<RestInfo: {}>'.format(self.id)


class AtrCity(db.Model):
    __tablename__ = 'atr_city'

    id_atr = db.Column(db.Integer, primary_key=True)
    text_atr = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<AtrCity {}>'.format(self.id_atr)


class AtrRecommendedFor(db.Model):
    __tablename__ = 'atr_recommend'

    id_atr = db.Column(db.Integer, primary_key=True)
    text_atr = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<AtrRecommendedFor {}>'.format(self.id_atr)


class AtrMetro(db.Model):
    __tablename__ = 'atr_metro'

    id_atr = db.Column(db.Integer, primary_key=True)
    text_atr = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<AtrMetro {}>'.format(self.id_atr)


class AtrAverageBill(db.Model):
    __tablename__ = 'atr_averagebill'

    id_atr = db.Column(db.Integer, primary_key=True)
    text_atr = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<AtrAverageBill {}>'.format(self.id_atr)


class AtrFeatures(db.Model):
    __tablename__ = 'atr_features'

    id_atr = db.Column(db.Integer, primary_key=True)
    text_atr = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<AtrFeatures {}>'.format(self.id_atr)


class AtrTypes(db.Model):
    __tablename__ = 'atr_types'

    id_atr = db.Column(db.Integer, primary_key=True)
    text_atr = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<AtrTypes {}>'.format(self.id_atr)


class AtrKitchens(db.Model):
    __tablename__ = 'atr_kitchens'

    id_atr = db.Column(db.Integer, primary_key=True)
    text_atr = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<AtrKitchens {}>'.format(self.id_atr)


class QuickSearch(db.Model):
    __tablename__ = 'quick_search'

    id = db.Column(db.Integer, primary_key=True)
    id_rest = db.Column(db.Integer, index=True)
    id_atr_city = db.Column(db.Integer, index=True)
    id_atr_recommend = db.Column(db.Integer, index=True)
    id_atr_metro = db.Column(db.Integer, index=True)
    id_atr_averagebill = db.Column(db.Integer, index=True)
    id_atr_features = db.Column(db.Integer, index=True)
    id_atr_types = db.Column(db.Integer, index=True)
    id_atr_kitchens = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<QuickSearch {}'.format(self.id_rest)