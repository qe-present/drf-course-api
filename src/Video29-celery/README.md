# 运行
```bash
rye run dev
```

# 迁移
```shell
python manage.py makemigrations;
python manage.py migrate;
```
# 限流  throttling
```

{
    "detail": "Request was throttled. Expected available in 52 seconds."
}
```
# CELERY_BROKER_URL = "redis://127.0.0.1:6379"
# CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379"什么意思
这两行配置是用来设置 Celery 的消息中间件和结果存储后端，意思如下：

- `CELERY_BROKER_URL`：指定 Celery 用来发送和接收任务消息的中间件，这里用的是本地的 Redis 服务（地址为 127.0.0.1，端口 6379）。
- `CELERY_RESULT_BACKEND`：指定 Celery 任务执行结果的存储后端，这里同样用的是本地的 Redis。

这样配置后，Celery 会通过 Redis 进行任务分发和结果存储。