import os
import yaml
import logging.config

# Load the configuration from the file


class ContextAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        kwargs["extra"] = self.extra
        return msg, kwargs


class EasyLoggingSetup:
    def __init__(self, enable_json_mode: bool = False) -> None:
        self.enable_json_mode = enable_json_mode
        self._setup()

    def _setup(self):
        with open(os.path.join(os.path.dirname(__file__), "log-config.yml"), "r") as f:
            config = yaml.safe_load(f.read())
        if self.enable_json_mode:
            config["handlers"]["default"]["formatter"] = "json"
        logging.config.dictConfig(config)


if __name__ == "__main__":
    from easylogging import EasyLogging

    EasyLoggingSetup(True)

    logger = logging.getLogger()
    ctxLogger = ContextAdapter(logger=logger, extra={"src": "abc"})

    log = EasyLogging.getLogger(__name__)
    ctxLogger2 = log.with_ctx({"hello": "world"})

    logger.info("AAAA")
    ctxLogger.info("AAAA")
    ctxLogger2.info("AAA")
