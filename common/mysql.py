#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","chx175246","test" )

# 使用cursor()方法获取操作游标 
cursor1 = db.cursor()
cursor3 = db.cursor()


# 使用execute方法执行SQL语句

cursor1.execute("SELECT count(*) from demo where name='chqtest1'")

# 使用 fetchone() 方法获取一条数据
data = cursor1.fetchone()
print "data = %s " % data


# 执行sql

def Setdata(sql):
   db = MySQLdb.connect("localhost","root","chx175246","test" )
   cursor = db.cursor()
   try: 
      cursor.execute(sql) # 执行sql语句
      db.commit() # 提交到数据库执行
   except Exception, e:
      print e
      db.rollback() # Rollback in case there is any error 语句有误就回滚
   finally:
      if db:
         db.close()

# SQL 查询语句

try:
   # 执行SQL语句
   cursor3.execute("SELECT * FROM demo WHERE name='chqtest1'")
   # 获取所有记录列表
   results = cursor3.fetchall()
   datas=tuple(results)
   for row in results:
      t_userid = row[0]
      t_name = row[1]
      t_phone = row[2]
     
      # 打印结果 
   print "t_userid=%d,t_name=%s,t_phone=%s" % \
         (t_userid, t_name, t_phone)
except Exception, e:
   print e

# 关闭数据库连接
db.close()

