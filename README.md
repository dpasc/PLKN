# plkn


Problem:
Product vendors must carry out a regular tender process to have their products sold by large retailers. Every product category has different dates for documentation that is required for submission throughout the tender process. The issue is,these dates are subject to change randomly without any notification to the vendors. Vendors may have many products across various categories, as you can imagine this could get a little tricky to manage.


Project Mission:
Provide a platform for vendors that allows them to view and sign up for notifications that detail any changes in the dates within a product category.

Methodology:
Develop a web scraper that checks retailers sites for changes to information relating to the tender process
Provide an easy platform for vendors to interface with to review and subscribe to changes
Provide an API for developers to work with the information that has been collected

Architecture
User Interface:
This platform uses a React SPA for users to interface with.
Server Side

The web scrapers are written in Python using Pandas SqlAlchemy,pg8000 and Numpy;The scrapers are set up on a server that executes twice daily via a cron job. The scrapers collect the data, formats the data and compares the data for any discrepancies against what is in the database.The server side core runs on .NET Core 3.1,Entity Framework Core is used as the ORM on the server to map the server data to models. I used the repository pattern in the architecture as it has the advantage of allowing me to change the type of database. The platform uses a REST API to interact with the REACT SPA. Developers can also interact with the API to access the data collected by the platform.

Database:
This platform uses a PostgreSQL relational database, this was chosen for the open source nature of PostgreSQL.The schema is very basic and is designed in a way that each retailer has it’s own table.After starting this project I began to learn about NoSQL databases. I think it would be more appropriate to use a document database and may make changes to the platform in future.
Deployment

The program is set up to run on a single server,this seemed like a simple solution for a basic project.I recently began playing around with AWS services and put together a network diagram of how the platform could potentially operate using cloud services.This would mean slight changes to the architecture of the program.

https://dpasc-site-pictures.s3-ap-southeast-2.amazonaws.com/plkn_aws.png

How to run program

Ensure you have the .NET Core run time, PostgreSQL and Python3 installed on your machine.

1.Edit the connection string:
ServerSide/Domain/Data/EntityFrameworkModels/Contexts/ContextWoolworths.cs HOST=localhost;DB=woolworths_db;UID=username;PWD=password;Port=5432;

2.Set up database:
Run Entity Framework ‘dotnet ef database update’ in ServerSide/API/

3.Configure scrapers:
Open:DataCollection/DataCleaner/WoolworthsDataCleaner.py DataCollection/DataMananger/WoolworthsDataManager.py DataCollection/Scraper/ScraperWow.py And edit the file path variables to somewhere the script can access the data

4.Get data:
The data collection tools are set up using cron jobs however,to test the data collection tools run the/DataCollection/ShellScripts/PipPackages.sh script to install the dependencies Run the DataCollection/ShellScripts/WoolworthsDataCollection.sh this will run the data collecton scripts and populate the database

5.Execute program:
Move to ServerSide/API/and run ‘dotnet run’
