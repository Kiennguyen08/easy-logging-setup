import os
import yaml
import logging.config

# Load the configuration from the file


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
    log = EasyLoggingSetup()
    logger = logging.getLogger()
    logger.info("AAAA")
