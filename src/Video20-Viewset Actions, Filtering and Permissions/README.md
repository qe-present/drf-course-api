# 运行
```bash
rye run dev
```
# 迁移
```shell
python manage.py makemigrations;
python manage.py migrate;
```
# 下面代码什么意思
```python
    created_at= django_filters.DateTimeFilter(
        field_name='created_at__date',
    )
```
这段代码的意思是：  
定义了一个 `created_at` 过滤器，类型为 `DateTimeFilter`，用于过滤模型中的 `created_at` 字段（但实际过滤的是 `created_at` 字段的日期部分）。

- `field_name='created_at__date'` 表示过滤时只比较 `created_at` 的日期（不包括时间）。
- 用法举例：`/products/?created_at=2024-06-10`，会筛选出 `created_at` 日期为 `2024-06-10` 的数据。

代码示例：

```python
import django_filters

class ProductFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFilter(field_name='created_at__date')
```

这样可以通过接口参数过滤指定日期的数据 
# @action(detail=False, methods=['get'],url_path='user-orders') 什么意思
`@action(detail=False, methods=\['get'\], url_path='user-orders')` 的意思是：

- 在 `ViewSet` 里注册一个自定义接口（action）。
- `detail=False` 表示这是一个“列表级”接口，不针对某个具体对象，而是针对整个集合。
- `methods=['get']` 指定只允许 GET 请求。
- `url_path='user-orders'` 指定接口路径为 `/orders/user-orders/`。

这样你可以通过 GET 请求访问 `/orders/user-orders/`，执行你定义的逻辑（比如返回当前用户的订单列表）。