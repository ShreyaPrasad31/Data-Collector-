from email.mimetext import MIMEText 
import smtplib 

def send_email(email, salary , average_salary,count):
	from_email = shreyaprasad31121998@gmail.com
	from_password = Sh31121998!
	to_email = email

	subject = "Coop Data"
	message = "Hey there, your entered data is <i>%s </i>.And average salary is <i> %s </i>. The sample size used is <i> %s </i>",  % (salary,average_salary,count)

	msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmal.send_message(msg)