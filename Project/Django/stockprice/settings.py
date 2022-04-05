#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'aws svr', #2
        'USER': '2zo', #3                      
        'PASSWORD': '2zo',  #4              
        'HOST': '18.182.177.124',   #5                
        'PORT': '3306', #6
    }
}
SECRET_KEY ='기존 settings.py에 있던 시크릿키를 붙여넣는다'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 설치된 앱을 다음과 같이 등록 해줍니다. 
INSTALLED_APPS += [ 
    'stockprice_app',
]