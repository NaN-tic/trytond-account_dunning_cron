=================================================
Contabilidad. Generar reclamaciones mediante cron
=================================================

Mediante un cron, se genera todas las reclamaciones de pagos pendientes
en el dia de la activación del cron. Se enviará un correo a todos los usuarios
del grupo Reclamación notificando que hay reclamaciones pendientes.

- El cron debería ejecutarse solamente una vez al día.
- Añade en la configuración de contabilidad el grupo Dunning.
- Añade usuarios al grupo Dunning y que tengan un correo electrónico.
- El idioma del correo se envía según idioma de la instalación inicial.
