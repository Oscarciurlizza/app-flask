class Config:
    SECRET_KEY = "B!asj1la%njio$*a6D23*a"


# Clase para configuracion que hereda de la configuracion
class DeveleopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"
    MYSQL_DB = "store-flask"


config = {
    "development": DeveleopmentConfig,
    "default": DeveleopmentConfig
}
