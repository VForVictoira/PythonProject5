import mysql.connector

# 连接数据库
conn = mysql.connector.connect(
    host="localhost",
    user="youruser",           # 替换为你的用户名
    password="yourpassword"    # 替换为你的密码
)

cursor = conn.cursor()

# 创建数据库
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
cursor.execute("USE testdb")

# 创建表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")

# 插入数据
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Alice", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Bob", 22))
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 关闭连接
cursor.close()
conn.close()
