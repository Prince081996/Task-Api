*To run locally, do the usual:*

1. Create a Python 3.6.7 virtualenv and activate:

            virtualenv -p python3 virtualenv-name
            source virtualenv-name/bin/activate
            
            
2. Install dependencies:
      
       pip install -r requirements.txt

4. Run migrations:

        python manage.py migrate
        
5. Run project server on local :

        python manage.py runserver



*API DOCUMENTATION*

1. API to schedule another API:
        
        Endpoint /task (on local: localhost:8000/task) 
        Type - GET
        enabled params - URL & DATETIME
        note: DATETIME should be in format 09/19/18 13:55:00

        FOR EXAMPLE:
        GET localhost:8000/test?DATETIME=09/19/18 13:55:00&URL=https://www.google.com

        Response Type - HTTP Response 
        Success response - 'Yes , it worked'
        Failure response - Handled all cases, 
        Case 1: In case of datetime not macthing with current - 'Datetime does mot match with current datetime'
        Case 2 : When wrong url entered - 'Entered URL is not reachable'
        Case 3 : When param url does not give 200 status code - 'The entered url failed with status code {status code}'


2. API to test server is live or not:
        It's simple GET api which returns json response     
        Endpoint /ping (on local: localhost:8000/ping) 
        Type - GET  
        Response Type - JSON Response 
        Success response - {'status':'ok'}



    



        
