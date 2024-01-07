#imports
from vkbottle import BaseStateGroup
from vkbottle import CtxStorage

ctx = CtxStorage()


class states_reg(BaseStateGroup):
    NAME = 0
    AGE = 1
    GENDER = 2
    PHOTO = 3
    CONTENT = 4
    FIND_GENDER = 5
    CITY = 6
    #END = 200
