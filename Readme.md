# Get Movie information from IMDB

Find all the information about a movie by using just it's name. 
This project runs in a docker container. 
APIs are made with flask. 
Project language is python. 
Once the container starts, search in a browser by `localhots:5000/movie/<<name>>`, which should return a json type reply.


## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will detail the expected value of the `data field`

## Lookup movies

`GET /movie/<movie_name>`

**Response**

- `404 Not Found` if the movie was not found
- `200 OK` on success

```json
{
    {
    "message": "Movie found",
    "data": {
        "Tomb Raider": [
            {
                "title": "Tomb Raider",
                "url": "https://www.imdb.com/title/tt1365519/",
                "year": "2018",
                "rating": "6.3",
                "votes": "181,201",
                "time": "1h 59min",
                "maturity_rating": "M",
                "genre": [
                    "Action",
                    "Adventure",
                    "Fantasy"
                ],
                "summary": "Lara Croft (Alicia Vikander), the fiercely independent daughter of a missing adventurer, must push herself beyond her limits when she discovers the island where her father, Lord Richard Croft (Dominic West) disappeared."
            }
        ]
    }
}
}
```

## Future
Connect with a dockerised instance of mongodb
Develop a front end

