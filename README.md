# CS2450-Final-Project
Final Project Repository for Software Engineering

My Program is a simple Reservation Manager for a small boat harbor.

  You will need to be able to run Python on your computer as well as a MySql database. I used VSCode and MySQL Worbench. You will need to create a database instance on your computer with these specifications:

            host="localhost",
            user="root",
            password="<Your passworde here>",
            database="final_reservations_db"


  Then execute the database creation file. Then the last thing you need to do is enter the password you created for your database at the top of the finalgui.py file with the rest of the database specs. 

  When you execute the python file the tkinter gui will automatically open. From there you will want to create a few customers and boats. The only preloaded data is three slips numbered 2, 3, and 4. Any customers, boats, and reservations you make will be automatically commited to the database. You will want to keep track of the customers unique id's when you are going to create a boat it will prompt you to enter that in so that the boat and owner are linked.
