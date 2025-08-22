# 运行
```bash
rye run dev
```
# 迁移
```shell
python manage.py makemigrations;
python manage.py migrate;
```
# 分页使用

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2
}
# views.py
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
# 分页类
    pagination_class = PageNumberPagination
# 页面大小
    pagination_class.page_size=3
# 设置分页参数
    pagination_class.page_query_param='page_num'
# 设置每页大小的参数
    pagination_class.page_size_query_param='s'
# 设置最大每页大小
    pagination_class.max_page_size=5
```