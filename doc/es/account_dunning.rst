#:after:account_dunning/account_dunning:section:configuracion#

Acciones planificadas
=====================

Se dispone de una acción planificada para generar las reclamaciones y se envia un
correo a los usuarios del resumen.

La acción planificada deberá configurarse que se ejecute una vez al día y cada día. Cuando se ejecuta
la acción, genera las reclamaciones por la fecha de hoy.

En la configuración de la contabilidad seleccione el grupo de usuarios que se enviará
el correo electrónico ( |dunning_group_cron| ). Es importante para el envío de correo
que los usuarios dispongan de un correo.

El correo se envia mediante el servidor de correo del sistema.

.. |dunning_group_cron| tryref:: account_dunning_cron.dunning_group_cron/complete_name
