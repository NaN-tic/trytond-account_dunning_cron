# This file is part account_dunning_cron module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.tools import get_smtp_server
from trytond.config import config
import logging

from email.mime.text import MIMEText
from email.header import Header

__all__ = ['Dunning']
__metaclass__ = PoolMeta


class Dunning:
    __name__ = 'account.dunning'

    @classmethod
    def __setup__(cls):
        super(Dunning, cls).__setup__()
        cls._error_messages.update({
                'request_title': '[%s] New dunnings generated',
                'request_body': ("New dunnings are generated and pending "
                    "to done:\n\n%s")
                })
    
    @classmethod
    def generate_today_dunnings(cls):
        """
        Generate Account Today Dunnigs
        """
        pool = Pool()
        Date = pool.get('ir.date')
        User = pool.get('res.user')
        Config = pool.get('account.configuration')

        today = Date.today()
        cls.generate_dunnings(date=today)

        config = Config(1)
        group = config.dunning_group_cron

        emails = None
        records = []
        for dunning in cls.search([
                    ('state', '=', 'draft'),
                    ('blocked', '=', False),
                    ('maturity_date', '=', today),
                    ]):
            records.append('%s, %s, %s' % (
                    dunning.party.rec_name,
                    dunning.amount,
                    dunning.maturity_date,
                    ))

        if records:
            records.sort()
            users = User.search([
                    ('groups', 'in', [group.id]),
                    ])
            emails = [user.email for user in users if user.email]

            if not emails:
                logging.getLogger('account dunning cron').info(
                    'Unable to deliver dunny email. '
                    'Add email dunning group users')

        if emails:
            subject = cls.raise_user_error('request_title',
                (Transaction().cursor.dbname),
                raise_exception=False)
            body = cls.raise_user_error('request_body',
                ('\n'.join(records)),
                raise_exception=False)

            from_addr = config.get('smtp_default_from_email')
            to_addr = list(set(emails))

            msg = MIMEText(body, _charset='utf-8')
            msg['To'] = ', '.join(to_addr)
            msg['From'] = from_addr
            msg['Subject'] = Header(subject, 'utf-8')

            try:
                server = get_smtp_server()
                server.sendmail(from_addr, ', '.join(to_addr), msg.as_string())
                server.quit()
            except Exception, exception:
                logging.getLogger('account dunning cron').info(
                    'Unable to deliver email (%s):\n %s'
                    % (exception, msg.as_string()))
