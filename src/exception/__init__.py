import sys
import logging


def error_message_details(error: Exception, error_details: sys) -> str:
    """
    Extract detailed error information including file name,
    line number, and the original error message.

    Parameters:
        error (Exception): The original exception.
        error_details (sys): The sys module used to access traceback information.

    Returns:
        str: Formatted error message.
    """

    _, _, exc_tb = error_details.exc_info()

    # In case no traceback is available
    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"at line number [{line_number}] : {str(error)}"
    )

    # Log the error
    logging.error(error_message)

    return error_message


class MyException(Exception):
    """
    Custom exception class for the project.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        """
        Initialize the custom exception.

        Parameters:
            error_message (Exception): Original exception object.
            error_detail (sys): sys module used for traceback information.
        """

        self.error_message = error_message_details(
            error_message,
            error_detail
        )

        super().__init__(self.error_message)

    def __str__(self) -> str:
        """
        Return the formatted error message.
        """
        return self.error_message