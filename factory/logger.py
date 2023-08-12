from enum import Enum


class LoggerType(Enum):
    CONSOLE = 1
    FILE = 2
    CLOUD = 3


class Logger:
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print("Console Log:", message)


class FileLogger(Logger):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(message + '\n')
        print("File Log:", message)


class CloudLogger(Logger):
    def log(self, message):
        # Simulate sending log to the cloud
        print("Cloud Log:", message)


class LoggerFactory:
    @staticmethod
    def create_logger(logger_type):
        if logger_type == LoggerType.CONSOLE:
            return ConsoleLogger()
        elif logger_type == LoggerType.FILE:
            return FileLogger()
        elif logger_type == LoggerType.CLOUD:
            return CloudLogger()
        else:
            raise ValueError("Invalid logger type")


# Client code
logger_type = LoggerType.CONSOLE  # You can switch between different logger types
logger = LoggerFactory.create_logger(logger_type)
logger.log("This is a log message")
