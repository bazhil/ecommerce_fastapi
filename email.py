from fastapi import BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig



conf = ConnectionConfig(
    MAIL_USERNAME='',
    MAIL_PASSWORD='',
    MAIL_FROM='',
    # порт может отличаться в зависимости от используемого сервиса
    MAIL_PORT=587,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


