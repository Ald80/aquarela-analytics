import enum


class StatusColaboradorEnum(enum.Enum):
    Ativo = 1
    Demitido = 2
    Afastado = 3

    @classmethod
    def is_demitido(cls, id_status):
        return id_status == cls.Demitido.value
