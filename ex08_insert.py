import pymysql as ps
import spidevRead as sr
import time
# 접속 경로를 담고 있는 객체
# (오라클의 connection과 같음)
conn = ps.connect(
    host='localhost',
    user='root',
    passwd='1234',
    db='test')
# SQL문장을 전달하는 객체
# (오라클의 PrepareStatement와 같음)
curs = conn.cursor()
while True:
    readData = sr.analog_read(0)
    sql='insert into sensordb(sensing) values({})'.format(readData)
    curs.execute(sql)
    conn.commit()
    time.sleep(5)
    


