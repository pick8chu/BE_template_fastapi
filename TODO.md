# web client setting is done
- need to make a test
- pytest is not working well, maybe i need to make APIs controller and test it through the APIs.

# DB part. 

# make it like a template so that i can use it with no understanding.

--
# 2022-07-06
## make CRUD for service
## make test for those CRUDs 

--
# 2022-07-07
## test transaction scope has not been working

--
# 2022-07-08
## Need to combine sessions of client(routes) and service.... how?

--
# 2022-07-17
## using Base.metadata.create_all(bind=engine), I can create all the db and use that for the test. -> need to try that out to see how it works

--
# 2022-08-03
## So with testDB, it worked but i have to commit so that it can get the data. 
## made few changes on DB part - it will automatically commit when session closes.

- So to test the DB, it seems, 
    1. make a database named 'test_db'
    2. make a sequence
    3. and do the test.

hopefully I can find better way to make it work.
