# 微服务配置加载器

## 如何使用

```python
from py_bootstrap import config,get_app_homepage

print(config.get('你的配置')) # config 是由 项目根目录 bootstrap.py 文件内可json化数据与 spring-config服务获取你的服务配置的合并
print(get_app_homepage("服务名")) # 可通过该方法获取服务ip

```


## bootstrap 文件配置解读

- `app_name` 应用名称 与 eureka注册,config获取挂钩
- `config_server_name` spring-config 服务名
- `eureka_url` eureka地址
- `register` 是否注册eureka(该配置可以从远程的config-file覆盖)
- `profile` 启动模式(dev|prod)
- `extra_profiles` 额外的配置文件加载( 逗号隔开会加载所有spring-config-file中的 application-文件名.yml 配置 )

其余的可json化配置也会加载到config中,但是会被远程覆盖

## 功能

- 配置加载
- 日志初始化
- eureka注册
- 服务发现接口

