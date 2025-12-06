# CS2450-Final-Project
Final Project Repository for Software Engineering

My Program is a simple Reservation Manager for a small boat harbor.

  You will need to be able to run Python on your computer as well as a MySql database. I used VSCode and MySQL Worbench. You will need to create a database instance on your computer with these specifications:

            host="localhost",
            user="root",
            password="<Your passworde here>",
            database="final_reservations_db"


Then run the 


The four tables in the database are reservations, customers,
boats and slips. I used Tkinter to make a menu page that allows the user to navigate to
separate windows for four different functions. The four functions are Search Customer, Search
Boat, Create Customer, and Create Boat. Reservations can be made on a customer's page. I
did not include a function to create slips because regular harbor staff would never do that. That
would happen when the harbor is built and the software is installed. By searching by boat or
customer you can navigate to a customer page that allows you to edit customer information, see
the boats and reservations attached to that customer, and create new reservations. To create a
new reservation you enter the length of the boat that you need and the search function will
return a list of slips that meet the length requirement. When you select a slip it will automatically
be entered in the slip number field that is used to create a reservation. This is the main problem
that needed solving. Now to find a viable slip you just need to enter in the length and select a
slip.
