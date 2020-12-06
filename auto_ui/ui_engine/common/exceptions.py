class UiOperationException(Exception):

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return "Message: %s\n" % self.msg


class TooParamException(UiOperationException):

    def __init__(self, limit: int, given: list):
        self.limit = limit
        self.given = given

    def __str__(self):
        return ('Too many parameters given: the param is limited in %d but %d given, parameters: %s \n' % (
            self.limit, len(self.given), str(self.given)))


class MissParamException(UiOperationException):

    def __init__(self, param: str):
        self.param = param

    def __str__(self):
        return ('Missing required parameter: %s \n' % self.param)


class UnsupportedValueException(UiOperationException):

    def __init__(self, param_name: str, param_value, expect):
        self.name = param_name
        self.value = param_value
        self.expect = expect

    def __str__(self):
        return ('Unsupported parameter value: \n param_name : %s param_value: %s \n Expected in %s \n' % (
            self.name, str(self.value), str(self.expect)))
