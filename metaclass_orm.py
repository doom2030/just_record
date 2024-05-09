from typing import *


class ModelMeta(type):
    def __new__(cls, name: str, bases: Tuple[str, ...], attrs: Dict[str, Any]):
        if name != "Model":
            mappings = {}
            for k, v in attrs.items():
                if isinstance(v, Column):
                    mappings[k] = v
            attrs["__mappings__"] = mappings
            attrs["__table__"] = name.lower()
        return type.__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    def save(self):
        columns = []
        values = []
        for k, v in self.__mappings__.items():
            columns.append(v.column_name)
            values.append(getattr(self, k))
        sql = f"insert into {self.__table__} ({','.join(columns)}) values ({','.join(map(str, values))})"
        print(sql)

    def update(self):
        pass

    def query(self):
        pass

    def delete(self):
        pass

class Column(object):
    def __init__(self, column_name, column_type) -> None:
        self.column_name = column_name
        self.column_type = column_type


class UserInfo(Model):
    name = Column(column_name="name", column_type="varchar(30)")
    age = Column(column_name="age", column_type="int")


if __name__ == "__main__":
    user_info = UserInfo()
    user_info.name = "yzj"
    user_info.age = 30
    user_info.save()
