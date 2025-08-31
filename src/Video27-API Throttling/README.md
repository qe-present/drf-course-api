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
# 解释代码
```python
from rest_framework.throttling import UserRateThrottle
class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'
```
这两行代码定义了两个自定义限流类，分别用于不同的限流策略：
BurstRateThrottle：继承自 UserRateThrottle，设置 scope 为 'burst'，用于短时间内的高频请求限流。
SustainedRateThrottle：同样继承自 UserRateThrottle，设置 scope 为 'sustained'，用于长期持续请求的限流。
你可以在 settings.py 的 REST_FRAMEWORK 配置中分别为 'burst' 和 'sustained' 设置不同的限流速率。例如
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'api.throttle.BurstRateThrottle',
        'api.throttle.SustainedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'burst': '20/minute',
        'sustained': '100/day',
    }
}

```
# 'rest_framework.throttling.ScopedRateThrottle',怎么使用
ScopedRateThrottle 用于为不同的 API 视图或接口设置不同的限流速率。
你需要在视图类中设置 throttle_scope 属性 ，
然后在 settings.py 的 DEFAULT_THROTTLE_RATES 中为该 scope 配置速率。
例如：
```python
'DEFAULT_THROTTLE_RATES': {
    'products': '5/minute',
    # 其他 scope...
}
# throttle_classes = [ScopedRateThrottle]什么意思
`throttle_classes = [ScopedRateThrottle]` 的意思是：  
该视图会使用 `ScopedRateThrottle` 这个限流类进行请求速率限制。  
你可以通过设置 `throttle_scope` 属性和在 `settings.py` 的 `DEFAULT_THROTTLE_RATES` 
配置不同的速率，实现针对不同接口的限流策略。