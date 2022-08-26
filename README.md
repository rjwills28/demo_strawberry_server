# demo_strawberry_server
The is a small demo Strawberry server that can be used to demonstrate whether the 'finally' statement in a try-finally is executed if included in 
the subscription method.

The code will print out a debug message when the finally statement is called for each subscription and keep a toal of the number of finally calls
 versus the number of subscriptions created. if all is functioning correctly we would expect these values to be the same.
 
 ## Prerequisites 
 - Python > 3.7
 
 ## Installation
 - Clone this repo.
 - Create a Python virtual environment to install dependencies and run code.
 
    `python -m venv venv`
    
    `source venv/bin/activate`
- Install dependencies from setup file:

  `python setup.py install`
  
- Start the server:

  `demo_strawberry_server`
