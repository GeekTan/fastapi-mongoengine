
```
使用说明:
1.创建MongoEngine Model时添加meta={"db_alias":"xxx"}属性。
  例如：
  db = FastApiMongEngine()
  class User(db.Document):
    name = StringField(primary_key=True, unique=True, max_length=20)
    phone = StringField(max_length=11)  
    meta = {"db_alias": "test_db"} 

   db.init_app(_app, {
        "test_db": {
            "host": "mongodb://127.0.0.1:27017/test_db"
        }

    })
    将mongo配置添加{"alias":"xxxxx"} 
3.Benchmark:
  
  server单线程:
  Running 10s test @ http://127.0.0.1:8000/?name=xiaoming1
  20 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    90.77ms    7.48ms 191.82ms   98.69%
    Req/Sec    55.23     15.73   101.00     88.28%
  11005 requests in 10.02s, 1.43MB read
  Requests/sec:   1098.45
  Transfer/sec:    145.89KB

  
```