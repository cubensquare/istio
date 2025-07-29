from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        db = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'mysql'),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_PASSWORD', 'root'),
            database=os.environ.get('MYSQL_DATABASE', 'testdb')
        )
        cursor = db.cursor()
        cursor.execute("SELECT 'Hello from MySQL!'")
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
