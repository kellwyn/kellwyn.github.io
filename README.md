Purpose of the Database:

Sparkify, a music streaming service wants to analyze and identify ways to best monetize and improve their platform. THey are interested in utilizing data points collected from users activity on the app, and build a database that allows running queries for reporting and analytical purposes.

The metadata source is a subset of the Million Song Dataset. There are 2 main directories available to build from, the Songs metadata which forms the detailed information on relevant song attributes such as artist name, location, year of release etc. The second source is a Logs dataset logging user information attributes and their activity.

Star schema is used for dimensional modeling, as we can easily query the relevant information using simplified queries and faster aggregation.It also allows for denormalized tables. 

Fact table: songplays
Dimensions tables: songs, artist, users, time.


In addition to the data files, the project includes six files:

test.ipynb displays the first few rows of each table to let me check my database.
create_tables.py drops and creates tables. I run this file to reset my tables before each time I run the ETL scripts.
etl.ipynb reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
etl.py reads and processes files from song_data and log_data and loads them into the tables. It's based on my work in the ETL notebook.
sql_queries.py contains all my sql queries, and is imported into the last three files above.
README.md then provides an introduction to this project.

Examples
%load_ext sql
%sql postgresql://student:student@127.0.0.1/sparkifydb
%%sql
SELECT COUNT(*) from songplays;
postgresql://student:***@127.0.0.1/sparkifydb

1 rows affected.

Out[1]: count 6820