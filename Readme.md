# Get Movie information from IMDB

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

