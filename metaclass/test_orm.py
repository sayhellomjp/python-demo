
class Field():
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
        
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'int')

# f = Field('name1', 'type1')
# print(f)
# s = StringField('sss')
# print(s)
# i = IntegerField('iii')
# print(i)

class ModelMetaclass(type):
    def __new__(cls, name, bases, args):
        if name == 'Model':
            return type.__new__(cls, name, bases, args)
        print('found model %s' % name)

        mapping = {}
        for k, v in args.items():
            if isinstance(v, Field):
                print('found mapping: %s ==> %s' % (k, v))
                mapping[k] = v
        # 因为都放到mapping里，所以把对应的args里的删掉
        for k in mapping.keys():
            args.pop(k)

        args['__mapping__'] = mapping
        args['__table__'] = name

        return type.__new__(cls, name, bases, args)

#继承dict，可以保存键值对
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError('attribute nof fount: %s' % key)

    # def __setattr__(self, key, value):
    #     self[key] = value

    def save(self):
        fields = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('sql : %s' % sql)
        print('args : %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id11111')
    name = StringField('username1111')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Batman', email='batman@nasa.org', password='iamback')
u.save()



