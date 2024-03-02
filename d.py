import logging as logg
from abc import ABC, abstractmethod

logg.basicConfig(level=logg.DEBUG)

class LoggingModule(ABC):
    @abstractmethod
    def log(self, info):
        pass 

class DebugModule(LoggingModule):
    def log(self, info):
        logg.debug(info)

class InfoModule(LoggingModule):
    def log(self, info):
        logg.info(info)

class WarningModule(LoggingModule):
    def log(self, info):
        logg.warning(info)

class ErrorModule(LoggingModule):
    def log(self, info):
        logg.error(info)

class CriticalModule(LoggingModule):
    def log(self, info):
        logg.critical(info)

class Logger:
    def __init__(self, logtype: LoggingModule):
        self.logtype = logtype

    def perform_log(self, info):
        self.logtype.log(info)

def main():
    logger = Logger(DebugModule())
    logger.perform_log("This is a debug message.")
    logger = Logger(InfoModule())
    logger.perform_log("User Logged In")
    logger = Logger(ErrorModule())
    logger.perform_log("User Login Failed")
    logger = Logger(WarningModule())
    logger.perform_log("Attempted Login to ADMIN Failed")
    logger = Logger(CriticalModule())
    logger.perform_log("UNRECOGNIZED LOGIN ATTEMPT TO ADMIN")

main()