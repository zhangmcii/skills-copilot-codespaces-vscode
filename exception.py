# 创建异常捕捉
class APIException(Exception):
    code = 500
    msg = 'server error'

    def __init__(self, code=None, msg=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg

    def __str__(self):
        return 'APIException: code: {}, msg: {}'.format(self.code, self.msg)
