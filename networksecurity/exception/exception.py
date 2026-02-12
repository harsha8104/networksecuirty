import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is not None:
            self.line_no = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.line_no = None
            self.file_name = None

        self.error_message = error_message

    def __str__(self):
        return f"Error occurred in python script name [{self.file_name}] line number [{self.line_no}] error message [{self.error_message}]"


if __name__ == "__main__":
    try:
        logger.info("Entered the try block")
        a = 1 / 0
    except Exception as e:
        raise NetworkSecurityException(e, sys)
