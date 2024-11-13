"""
Logger

Implements logging to a default log file
"""
from dotenv import load_dotenv
import os
from datetime import datetime
from .Exceptions import *

load_dotenv()

class Logger:
	def __init__(self) -> None:
		try:
			self._filepath = os.environ.get('LOGPATH')
		except:
			raise InvalidEnvConfig("Log path (LOGPATH) has not been configured.")

	def log(self, exception, value, traceback):
		"""Logs to the designated log file"""
		content = f"""
[{datetime.now().date()} {datetime.now().time()}]:
	Exception: {exception}
	Value: {value}
	Traceback: {traceback}
"""
		self.append_to_file(content)

	def append_to_file(self, content):
		"""Writes the log content to file"""
		with open(self._filepath, 'a') as logFileHandle:
			logFileHandle.writelines(content)