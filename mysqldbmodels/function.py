# coding=utf-8
class ERPFunction():
    def fullOBJ(self):
        product = {}
        for (k, v) in self.__dict__.items():
            if k != '_state':
                product.setdefault(k, v)
        return product