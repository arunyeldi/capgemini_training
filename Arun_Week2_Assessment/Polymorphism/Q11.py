class Logger:
    def log(self, message = None, error = None, warning = None, info = None):
        if error:
            print("This is an error")
        elif warning:
            print("This is a warning")
        elif info:
            print("This is an info")
        else:
            print("This is a normal message")

logger_obj = Logger()

logger_obj.log(message = "message")
logger_obj.log(warning = "warning")
logger_obj.log(error = "error")
logger_obj.log(info = "info")