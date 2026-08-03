import sys
import logging
def error_message_details(error:Exception,error_details:sys) -> str:

    """
      Extract detailed error information including file name,
      line number, and the actual error message.

      :param error: The exception that occurred.
      :param error_details: The sys module to access traceback details.
      :return: A formatted error message.
      """

      # get exception traceback
    _,_,exc_tb = error_details.exc_info()

      # get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

      # get the line number where error the exception occured
   
    line_number = exc_tb.tb_lineno

    # Create the detailed error message
    error_message = (
        f"Error occured in Python script [{file_name}]"
        f"at line number [{line_number}]:str{str(error)}") 

    # Log the error

    logging.error(error_message)

    return error_message


class MyException(Exception):
    """
    Custom exception class for hadling application error
    """

    def __init__(self,error_message:Exception,error_details:sys):
        """
        Initialize the parent Exception class
        """
        super().__init__(str(error_message))

        # Create and store the detailed
        self.error_message = error_message_details(
            error_message,
            error_details)


    def __str__(self) -> str:
        """
        Return the formatted error message
        """

        return self.error_message

     
      
      