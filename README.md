# 微服务配置加载器

## 如何使用

```python
from py_bootstrap import config,get_app_homepage

print(config.get('你的配置')) # config 是由 项目根目录 bootstrap.py 文件内可json化数据与 spring-config服务获取你的服务配置的合并
print(get_app_homepage("服务名")) # 可通过该方法获取服务ip

```

## 功能

- 配置加载
- 日志初始化
- eureka注册
- 服务发现接口

