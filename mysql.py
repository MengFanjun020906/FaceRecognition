
import pymysql



class Sql:
    def __init__(self,db):
        self.sql = pymysql.connect(host='localhost',user='root',password='',db=db)

    def get_version(self):
        # 创建游标对象
        self.cursor = self.sql.cursor()
        query = 'select version();'
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        print(res)

    def creat_table(self):
        query = '''

        '''




if __name__ == '__main__':
    Sql('students').get_version()





