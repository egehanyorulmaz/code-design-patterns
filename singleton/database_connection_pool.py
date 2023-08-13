class DatabaseConnectionPool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnectionPool, cls).__new__(cls)
            cls._instance._pool = []  # Pool to hold the connections
            cls._instance._max_connections = 5
        return cls._instance

    def acquire_connection(self):
        if len(self._pool) > 0:
            return self._pool.pop()
        elif len(self._pool) < self._max_connections:
            # Create a new connection if pool is not full
            new_connection = "DatabaseConnection"  # Normally, this would be a real database connection
            return new_connection
        else:
            raise Exception("Maximum connections reached")

    def release_connection(self, connection):
        self._pool.append(connection)  # Return connection to the pool


# Usage
db_pool1 = DatabaseConnectionPool()
connection1 = db_pool1.acquire_connection()

db_pool2 = DatabaseConnectionPool()
connection2 = db_pool2.acquire_connection()

db_pool1.release_connection(connection1)
db_pool2.release_connection(connection2)

print(db_pool1 == db_pool2)  # Output: True
