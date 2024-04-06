import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()
# 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')

# 데이터 삽입
cursor.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ('John', 30))

# 쿼리 실행
cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 연결 종료
conn.commit()
conn.close()