#建议使用jupyter来调试学习
#PYSPARK_DRIVER_PYTHON=ipython PYSPARK_PYSPARK_DRIVER_PYTHON_OPTS="notebook" pyspark
from pyspark import SparkConf,SparkContext,SparkSesssion
from pyspark.sql import Row

global Path
if sc.master[0:5]=="local":
    Path="file://home/my/work/data/"
else:
    Path="hdfs://localhost:9000/user/my/data/"
    
#创建RDD
FileUserRDD=sc.textFile(Path+"u.user")
FileUser.take(5)
UserRDD=FileUserRDD.map(lambda x:x.split("|")
UserRDD.take(5)
                        

#创建DataFrame
sqlContext=SparkSession.builder.getOrCreate()
user_Rows=userRDD.map(lambda x: Row(userid=int(p[0]),age=int(p[1]),gender=p[2],occupation=p[3],zipcode=p[4]))
user_Rows.take(5)
user_df=sqlContext.createDataFrame(user_Rows)
#查看DataFrame的Schema                       
user_df.printSchema()
user_df.show(5)
#设置DataFrame的别名                       
df=user_df.alias("df")
df.show(5)                        

#注册Spark SQL
user_df.registerTemple("user_table")
sqlContext.sql("SELECT count(*) counts FROM user_table").show()
                        
#SELECT 显示部分字段
userRDDnew=userRDD.map(lambda x:(x[0],x[3],x[2],x[1])
userRDDnew.take(5)
                       
user_df.select("userid","occupation","gender","age").show(5)
user_df.select(user_df.userid,user_df.occupation,user_df.gender,user_df.age).show(5)
df.select(df.userid,df.occupation,df.gender,df.age).show(5)
df[df['userid'],df['occupation'],df['gender'],df['age']].show(5)

sqlContext.sql("SELECT userid,occupation,gender,age FROM user_table").show(5)                       

#增加计算字段
#x[1]是年龄，添加的字段为用户出生年份                       
userRDDnew=userRDD.map(lambda x:(x[0],x[3],x[2],x[1],2019-int(x[1]))                       
userRDDnew.take(5)

df.select("userid","occupation","gender","age",2019-df.age).show(5)
df.select("userid","occupation","gender","age",(2019-df.age).alias("birthyear").show(5)                       
  
