# sporty_restapi

Random author poem test:
Test to verify that the number of lines in a random poem from the database is the same as "linecount" variable.
Verification of the system that calculates lines for the "linecount" variable.

| Step                                                                  | Test Data                                | Expected result                |
|-----------------------------------------------------------------------|------------------------------------------|--------------------------------|
| Make request for ramdom poem of random author                         | https://poetrydb.org/author/{}:abs/title | Poem is returned by the server |
| Compare number of lines in a poem with number in "linecount" variable | Number of lines in "lines" == "linecount"|  Numbers are the same          |


Authors poem count test:
Test to verify that dead authors for example do not get any new poems to added them.
Number of the titles of the authors can be found at {link_to_confluence_page}

| Step                                                      | Test Data                                      | Expected result                       |
|-----------------------------------------------------------|------------------------------------------------|---------------------------------------|
| Make request for the titles of an author                  | https://poetrydb.org/author/{author}:abs/title | Titles of certain author are returned |  
| Compare the total number of returned titles with constant | Number of titles in "titles" == constant       | Numbers are the same                  |


For validation, I used pydantic models, which add implicit verification of the server responses. Also, the models are easy to access by key values.