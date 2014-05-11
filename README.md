Poetification
----

####Give me text, get poems
A simple hack project built at HackBeanPot 2014. It uses natural language processing to pull an oauth'd users tweets, facebook posts, or github commits.

###Setup:

First install the basic dependencies.
```
sudo apt-get install python
sudo apt-get install nginx
sudo apt-get install git
sudo apt-get install build-essential python-dev
```
Get pip going,
```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```
Django setup:
```
sudo pip install Django
```
Dependencies for the project:
```
sudo pip install django-social-auth
export PYTHONPATH=$PYTHONPATH:$(pwd)/django-social-auth/
sudo apt-get install python-oauth2
sudo apt-get install python-openid
sudo pip install twython
```
Get numpy, nltk, nltk_contrib
```
sudo pip install -U numpy
sudo pip install -U nltk
wget https://nltk.googlecode.com/files/nltk_contrib-2.0.1rc1.zip
sudo python setup.py install
```
Download cmudict:
```
python
>>> import nltk
>>> nltk.download()
>>> b # download
>>> cmudict # cmudict
```
Set up a site-enabled config:
```
server {
    listen 80;
    server_name http://example.com/;
    access_log /var/log/nginx/poetification.access.log;
    error_log /var/log/nginx/poetification.error.log;

    location /static/ {
        alias /home/poetification/poetification/poetification/webpoet/static/;
        expires 30d;
    }

    location / {
        include fastcgi_params;
        fastcgi_pass 127.0.0.1:8080;
        fastcgi_split_path_info ^()(.*)$;
    }
}
```
If all went well start up fcgi
```
python ./manage.py runfcgi host=127.0.0.1 port=8080
```
Some enviroment variable will need to be set, they are keyed as follows:
```
export P_APP_KEY='#{twitter_app_key}'
export P_APP_SECRET='#{twitter_app_secret}'
export P_OAUTH_TOKEN='#{twitter_oauth_token}'
export P_OAUTH_SECRET='#{twitter_oauth_secert}'
export FACEBOOK_APP_ID='#{facebook_app_id}'
export FACEBOOK_API_SECRET='#{facebook_api_secret}'
export GITHUB_APP_ID='#{github_app_id}'
export GITHUB_API_SECRET='#{github_api_secret}'
```
and run the server
```
python manage.py runserver
```
