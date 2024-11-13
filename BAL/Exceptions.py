"""Exceptions
Contains all exceptions in BAL
"""

class BALError(Exception):
	pass

class InvalidEnvConfig(BALError):
	"""The environment variables have not been configured properly."""