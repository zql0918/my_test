from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/my_sql?charset=utf8mb4')

print(engine)
