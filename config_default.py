configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'password',
        'database': 'pure_blog'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}
import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
print(path)