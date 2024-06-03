from pool_conexion import Conexion
from logger_base import log
class CursorDelPool():
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f"iniciando el enter")
        self._conexion =Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb): #son los diferentes excepciones tipo, valor y detalle
        log.debug(f"se ejecuta el exit")
        if exc_type is not None:
            self._conexion.rollback()
            log.error(f'ocurrio una excepcion: {exc_type} {exc_val} {exc_tb}')
        else:
            self._conexion.commit()
            log.debug(f'se hizo el commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())

