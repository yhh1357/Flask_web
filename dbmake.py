import pymysql
db = pymysql.connect(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db = 'busan'
)
sql = '''
  CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
sql_1 = "INSERT INTO `busan`.`users` (`name`, `email`, `username`, `password`) VALUES ('한희', 'yhh9133@naver.com', 'LIM', '12345');"
sql_2 = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
cursor = db.cursor()
title = input('제목을 적으세요')
body = input('내용을 적으세요')
author = input('누구세요?')
input_data = [title,body,author]

# cursor.execute(sql)
cursor.execute(sql_2,input_data)
db.commit()
db.close()
# cursor.execute('SELECT * FROM users;')
#cursor.execute('SELECT * FROM users;')
#users = cursor.fetchall()
#print(cursor.rowcount, users)