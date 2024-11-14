from sqlalchemy.orm import declarative_base


Base = declarative_base()

from .location import Location
from .device_info import DeviceInfo
from .user_details import UserDetail
from .explosive_sentence import ExplosiveSentence
from .hostage_sentence import HostageSentence
