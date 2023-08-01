# Newsletter App

Application to send Newsletter emails to a list of recipients. The database schema allows to have multiple Newsletters related to multiple Recipients. A Newsletter requires an `email_template` which must be saved in the `templates/email` folder, this way our app knows which template should be sent to the Recepients.
Recepients can be subscribed to multiple Newsletters and can choose to unsubscribe by clicking a link within received emails. If the Recepient clicked in the mentioned link then will be removed from the specific Newsletter.

After running the project, two Newsletter will be created and five Recepients will be subscribed automatically.

To run a test, just visit http://localhost:3000, click on the Newsletter that you want to send, provide a comma separated list of emails, optionally choose a png or pdf file which will be attached to the email, check/uncheck the option to send
the Newsletter to all the subscribers and press the "Send Newsletter" button.

- [Stack](#stack)
- [Run the project](#run-the-project)
- [Emails sent](#emails-sent)

## Stack

- Backend: Django
- Frontend: React App Using Typescript

## Run the project

Just run the command `docker-compose up` and you will be able to access the app on http://localhost:3000.

## Emails sent

Django was configured in such a way that emails sent are going to be displayed in the console. So every single email will be logged in the backend container standard output.
