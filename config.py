from decouple import config


class Config:
    SECRET_KEY = "B!asj1la%njio$*a6D23*a"


# Clase para configuracion que hereda de la configuracion
class DeveleopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"
    MYSQL_DB = "store-flask"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "ciurlizza1000@gmail.com"
    MAIL_PASSWORD = config("MAIL_PASSWORD")


config = {
    "development": DeveleopmentConfig,
    "default": DeveleopmentConfig
}
