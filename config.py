
###settings for Flask-WTF extension
CSRF_ENABLED = True
SECRET_KEY = '34rKHEyi__756^%4hglwtjgnosiet-jflHOY!EH&7986%T9y8*7Ljl'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/08/id'},
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
