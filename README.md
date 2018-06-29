# celery-exp

This example demonstrates use of 

 - celery chord 
 - celery queue 
 - chord with callback 
 - callback with args 

# Enable the virtual environment 
source venv/bin/activate 

# Take a peak at celery_app.py 
 - In first case we have RabbitMQ as the broker and Redis as the backend 
 - In second case we have Redis as both broker and the backend 

```python
app = Celery('tasks', broker='amqp://test:test@localhost:5672/test_vhost', backend='redis://localhost:6379/0')

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
```

# Start the redis server in one tab 
```sh
$ redis-server /usr/local/etc/redis.conf 
```

# If RabbitMQ is used as broker 
```sh 
$ rabbitmqctl add_vhost celery_vhost
$ rabbitmqctl set_permissions -p test_vhost test ".*" ".*" ".*"
$ # Start the RabbitMQ server 
$ /usr/local/sbin/rabbitmq-server
```

# Start the celery worker in other tab
This command should be started from directory which has celery_app.py and tasks.py 
```sh
$ celery -A tasks worker --loglevel=INFO -Q dev,default
```
