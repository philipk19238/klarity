from ..extensions import db

class CRUDMixin(object):

    @classmethod 
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance 

    @classmethod
    def create_all(cls, items):
        instances = [cls(**item) for item in items]
        db.session.create_all(instances)
        db.session.commit()
        return instances

    @classmethod 
    def update_all(cls, items):
        updated_instances = []
        for item in items:
            dao = cls.find_by_id(item['id'])
            dao = dao.update(**items)
            updated_instances.append(dao)
        return updated_instances

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr) and value != None:
                setattr(self, attr, value)
        db.session.commit()
        return self 

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def delete_all(cls, id_list):
        for _id in id_list: 
            dao = cls.find_by_id(_id)
            if not dao: 
                raise NotFoundException(_id)
            dao.delete()

    def create_or_update(self, **kwargs):
        _id = kwargs.get('id')
        dao = self.query.get(_id)
        if not dao: 
            self.create(**kwargs)
        else:
            self.update(**kwargs)

    @classmethod 
    def find_by_id(cls, id):
        dao = cls.query.get(id)
        return dao

    @classmethod 
    def find_by_elem(cls, **kwargs): 
        dao = cls.query.filter_by(**kwargs).first()
        return dao  

    @classmethod 
    def find_all_by_elem(cls, **kwargs):
        dao = cls.query.filter_by(**kwargs).all()
        return dao 
        
    @classmethod 
    def find_all(cls):
        return cls.query.all()

class Base(db.Model, CRUDMixin):
    __abstract__ = True