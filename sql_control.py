import pymysql
# "delete from employee where E_ID=%s"%self.delete_data.get()
# "update %s set C_sex='%s' where C_ID=2"%self.delete_data.get()
# "insert into customer(C_password,C_name,C_sex,C_phone) values %s"%self.delete_data.get()
# "select * from customer where C_ID=2"%self.delete_data.get()
# sql_control.sql_control(sql)
# sql_control.sql_control(sql).result


class sql_control:
    def __init__(self,sql):
        self.conn=pymysql.connect(host="localhost",
                           user="root",
                           password="123456",
                           port=3306,
                           charset='utf8',
                           db='restaurant_system')
        self.cursor=self.conn.cursor()

        self.cursor.execute(sql)
        self.result=self.cursor.fetchall()
        self.cursor.execute("select last_insert_id()")
        self.last_insert_id=self.cursor.fetchall()
        self.conn.commit()

        self.cursor.close()
        self.conn.close()



# print(sql_control(sql).result)