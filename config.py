
# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'yunanfuwu'
HOST = '139.196.94.212'
PORT = '3306'
DATABASE = 'remoteControlCar'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# jsonify 返回数据中文显示
JSON_AS_ASCII = False
