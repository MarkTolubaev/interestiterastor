class ReadOnlyDescriptor:
    """
    Дескриптор доступа к атрибутам класса только для чтения
    """
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{owner.__name__}__{name}'

    def __set__(self, instance, value):
        if hasattr(instance, self.private_name):
            raise AttributeError("attribute is read only")

        setattr(instance, self.private_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __delete__(self, instance):
        raise AttributeError("attribute is read only")
