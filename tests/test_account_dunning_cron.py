# This file is part of the account_dunning_cron module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AccountDunningCronTestCase(ModuleTestCase):
    'Test Account Dunning Cron module'
    module = 'account_dunning_cron'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountDunningCronTestCase))
    return suite