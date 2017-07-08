# -*- coding: utf-8 -*-
"""
用于正式环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库设置, 正式环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': 'prod',                        # 数据库名 (默认与APP_ID相同)
        'USER': 'test',                            # 你的数据库user
        'PASSWORD': 'test',                        # 你的数据库password
        'HOST': 'rm-2zezm24r7p176s6rqo.mysql.rds.aliyuncs.com',                   		   # 数据库HOST
        'PORT': '3306',                        # 默认3306
    },
}
