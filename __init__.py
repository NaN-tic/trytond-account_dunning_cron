#This file is part account_dunning_cron module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .account import *
from .dunning import *

def register():
    Pool.register(
        Configuration,
        Dunning,
        module='account_dunning_cron', type_='model')

