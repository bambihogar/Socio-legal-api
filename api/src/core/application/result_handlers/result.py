from src.core.application.error import Error
class Result[T]:
    value:T
    error: Error
    
    def __init__(self, value: T | None, error: Error | None):
        if (value is None) and (error is None):
            raise ValueError("The result must recibe one input, this has both attributes as None")
        if (value is not None) and (error is not None):
            raise ValueError("The result must recibe JUST ONE input, this has both attributes value, and error with values ")
        self.value = value
        self.error = error


    def develop(self) -> T:
        if(self.value is not None):
            return self.value

    def is_succes(self):
        return self.value is not None

    def is_error(self):
        return self.error is not None
    
    def get_error_message(self):
        if(self.error):
            return self.error.description
        raise 'There is no Error message'
    
    @staticmethod
    def success(value: T):
        return Result(value=value, error=None)
    
    @staticmethod
    def failure(error: Error):
        return Result(value=None, error=error)    