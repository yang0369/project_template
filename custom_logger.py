import logging
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import torch
from pytz import timezone

TZ = timezone('Asia/Singapore')
CURRENT = datetime.now(tz=TZ)
TIME = CURRENT.strftime("%Y_%m_%d_%H_%M")
FORMAT = "[%(name)s: %(asctime)s, %(levelname)s] - %(message)s"

ROOT = Path(__file__).parents[0]
logging.basicConfig(filemode="a")


@dataclass
class CustomLogger(object):
    """A customized logger class

    Raises:
        Exception: user must choose where to display the logged messages

    """
    name: str = __name__
    level: int = logging.INFO
    stream_console: Any = sys.stdout
    logger_path: Optional[Path] = ROOT / "loggers" / "energy.log"
    format: Optional[str] = FORMAT

    def __post_init__(self):
        """create and configure logger
        """
        self._logger = logging.getLogger(self.name)
        self._logger.setLevel(self.level)
        log_formatter = logging.Formatter(self.format, "%Y-%m-%d %H:%M:%S")
        if self.stream_console is None and self.logger_path is None:
            raise ValueError(
                "either stream_console or logger_path must be specified")

        if self.stream_console:
            # log at console
            console_handler = logging.StreamHandler(stream=self.stream_console)
            console_handler.setFormatter(log_formatter)
            self._logger.addHandler(console_handler)

        if self.logger_path:
            if not self.logger_path.parents[0].exists():
                self.logger_path.parents[0].mkdir(parents=True, exist_ok=True)

            # save log to a file
            file_handler = logging.FileHandler(f"{self.logger_path.as_posix()}")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)

    def log(self, msg: str, level: str = "info") -> None:
        """log a message

        Args:
            msg (str): string
            level (str, optional): log level. Defaults to "info".
        """
        if level == "info":
            self._logger.info(msg)
        elif level == "debug":
            self._logger.debug(msg)


# demo
energy_tracker = CustomLogger()

energy_tracker.log("start time")

num_of_gpus = torch.cuda.device_count()
energy_tracker.log(f"No. of GPUs used: {num_of_gpus}")


energy_tracker.log("end time")
