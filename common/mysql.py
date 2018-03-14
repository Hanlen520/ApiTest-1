#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","chx175246","test" )

# 使用cursor()方法获取操作游标 
cursor1 = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()


# 使用execute方法执行SQL语句

cursor1.execute("SELECT count(*) from demo where name='chqtest1'")

# 使用 fetchone() 方法获取一条数据
data = cursor1.fetchone()
print "data = %s " % data


# 插入数据

sql = """INSERT INTO demo(userid,
         name, phone)
         VALUES (6, 'chqtest6', '457788966')"""
try:
   # 执行sql语句
   cursor2.execute(sql)
   # 提交到数据库执行
   db.commit()

except:
   # Rollback in case there is any error 语句有误就回滚
   db.rollback()


# SQL 查询语句

try:
   # 执行SQL语句
   cursor3.execute("SELECT * FROM demo WHERE name='chqtest1'")
   # 获取所有记录列表
   results = cursor3.fetchall()
   for row in results:
      t_userid = row[0]
      t_name = row[1]
      t_phone = row[2]
     
      # 打印结果
      print "t_userid=%d,t_name=%s,t_phone=%s" % \
             (t_userid, t_name, t_phone)
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()

