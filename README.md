# mhdb-tables2api

Convert MHDB google sheets spreadsheets to a postgres DB and Django Rest Framework API.

## Features
* download spreadsheets from the google sheets
* reformat into Django Fixtures
* run database in Docker

## To Do

[X] Set Up DRF boilerplate
[  ] define schema & create models  
[  ] create fixtures to populate the database  
[  ] dockerize rest api  
[  ] replace sqlite database with postrgres  
[  ] see if GraphQL provides more flexible querying (see [django-restql](https://github.com/yezyilomo/django-restql))  
[  ] 