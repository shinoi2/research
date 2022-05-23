workers = 16
bind = '0.0.0.0:5000'
# worker_class = 'gevent'
proc_name = 'gunicorn.pid'
timeout = 120
debug = True
accesslog = '/root/gunicorn/gunicorn.access.log'
access_log_format = '%(h)s-%(I)s-%(u)s-%(t)s'
errorlog = '/root/gunicorn/gunicorn.error.log'
loglevel = 'info'
# info:普通级别；
# warning:警告消息；
# error:错误消息；
# critical:严重错误消息；
