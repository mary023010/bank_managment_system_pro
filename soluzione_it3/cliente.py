


class Cliente:

    def __init__(self,id,nome_cliente,numero_telefono):
        self.__id = id
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono

    def __repr__(self):
        return f"Cliente {self.nome_cliente} telefono {self.numero_telefono}"

    def __get_id(self):
        return self.__id
    def __set_id(self,id):
        self.__id = id
    id = property(__get_id,__set_id)

    def __get_nome_cliente(self):
        return self.__nome_cliente
    def __set_nome_cliente(self,nome_cliente):
        self.__nome_cliente = nome_cliente
    
    nome_cliente = property(__get_nome_cliente,__set_nome_cliente)

    def __get_numero_telefono(self):
        return self.__numero_telefono
    def __set_numero_telefono(self,numero_telefono):
        self.__numero_telefono = numero_telefono
    
    numero_telefono = property(__get_numero_telefono,__set_numero_telefono)