class Result[T]:
    value:T
    error: Exception
    
    def __init__(
            self, 
            value: T | None, 
            error: Exception | None
            ):
        if (value is None) and (error is None):
            raise ValueError("The result must recibe one input, this has both attributes as None")
        if (value is not None) and (error is not None):
            raise ValueError("The result must recibe JUST ONE input, this has both attributes value, and error with values ")

    def develop(self) -> T:
        if(self.value is not None):
            return self.value
        raise self.error

    def isSucces(self):
        return self.value is not None

    def isError(self):
        return self.error is not None
    
    @staticmethod
    def success(value: T) -> Result[T]:
        return Result(value=value, error=None)
    
    @staticmethod
    def failure(error: Exception) -> Result[T]:
        return Result(value=None, error=error)    