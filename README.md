#Todo list

Ett vanligt sätt att skriva webapplikationer är att göra ett API ( *Application Programming Interface*). Programmet består då av endpoints (uri) som acessas via http verben, GET,PUT,DELETE

Er uppgift är att göra ett sådant. Till er hjälp har ni det här projekt, med testcase och kataloger på plats.
Det fattas naturligtvis en del kod.  



Här är en tänkbar början till er-modell


    +---------------+             XX XX            +--------------+
      |               |          XXX     XX          |              |
      |               |        XXX        XX         |              |
      |    TODO       | 0..*  XX            XX  0..* |    TAG       |
      |               +------+XX    HAR    XXX-------+              |
      |               |         XX       XX          |              |
      |               |          XX     XX           |              |
      |               |           XX  XXX            |              |
      +---------------+             XXX              +--------------+



##Forka det här projekt så har ni en början

Ni ska skapa en datamodell, lägg dom i Todo/Models/models.py

Vyerna (enpoints) lägger ni i Todo/Resources/Resources.py

Läs nedanför under endpoints, vilka endpoints ni behöver skriva

## Test

Det finns en testfil test/todo_test.py

Ni kan köra testerna från rooten på projektet med

python test/todo_test.py

Det kan vara bra att läsa testfilen, så ni vet vad som testas


## Endpoints

### /todos

#### GET

lista på alla todo´s



**exempel på retur värde**

200 OK

Content-Type: application/json

    {
      "2": {
          "tags": {
              "1": "coffe",
              "2": "Breakfast"
          },
          "text": "buy more milk"
      }
    }



### PUT

lägger till en todo

**exempel på payload**

Content-Type: application/json

    text: Todo text, Requiered
    tags: List of tags, optional

**exempel på returvärden**

    {
      "text":"buy more milk",
      "tags":["coffe","Breakfast"]
    }




### /todo/<*todo.id*>

hanterar enskilda todo item

#### GET

returnerar todo item med todo.id

**exempel /todo/1**

returnerar 200 OK, om todo id finns

Content-Type: application/json

    {
        "Todo": 1,
        "tags": [
            "coffe",
            "Breakfast"
        ]
    }

returnerar **404 Not Found** om id inte finns

#### Delete

tar bort todo item med todo.id

**exempel /todo/1**

returnerar **204 No Content** om todo tagits bort

returnerar **404 Not Found** om id inte finns


## Bedömning

Ni ska göra en själbedömning av erat arbete på learnpoint

TODO: mall för bedöming kommer näsat vecka


## TIPS

Förutom ponyorm och webbkursen som vi jobbat med kan ni se på exemplet, IFK,  finns updaterat på github
https://github.com/itgsodbojo/flask_rest_db

Jag har också tittat på http://nafiulis.me/a-todo-app-with-flask-and-pony.html
