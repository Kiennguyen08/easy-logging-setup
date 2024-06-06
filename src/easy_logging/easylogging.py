import logging


class EasyLogging:
    @classmethod
    def getLogger(self, name):
        self.logger = logging.getLogger(name)
        return self

    @classmethod
    def with_ctx(self, context=None):
        logger = logging.LoggerAdapter(self.logger, extra=context)
        return logger
