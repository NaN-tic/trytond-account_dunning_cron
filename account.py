#This file is part account_dunning_cron module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields


__all__ = ['Configuration']
__metaclass__ = PoolMeta


class Configuration:
    __name__ = 'account.configuration'
    dunning_group_cron = fields.Property(fields.Many2One('res.group',
            'Dunning Group Cron'))
