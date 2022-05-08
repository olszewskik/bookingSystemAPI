import pytz
from datetime import datetime

from app.core.config import settings


class Utils:
    def get_current_datetime(self):
        return datetime.now(pytz.timezone(settings.TIMEZONE))


utils = Utils()
