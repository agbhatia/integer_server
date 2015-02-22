# Overview

Integer server is a web service (written in python) designed to return either a specific element or the first n elements for integer sequences. The current supported sequences are:

* Fibonacci
* Happy numbers

### Setup

To run integer server there are a few python libraries that you must have installed. The libraries are also laid out in `requirements.txt`.

* Flask==0.10.1
* itsdangerous==0.24
* Jinja2==2.7.3
* MarkupSafe==0.23
* Werkzeug==0.10.1

These can all be installed via `pip`. Installing `Flask` should automatically install `Werkzeug`, `Jinja`, `MarkupSafe`, and `itsdangerous`.

### Running

To run the server, simply run `server.py`.  
Here is a guide of the commands:

```sh
$ git clone https://github.com/wrench604/integer_server.git integer_server
$ cd integer_server
$ python server.py
```

The urls supported are:

* `/sequences/{sequence_name}/{n}` (should return the nth term of sequence_name)
* `/sequences/{sequence_name}/first/{n}` (should return the first n terms, in order, of sequence_name)

The values that can be passed into `sequence_name` are:

* `fibonacci`
* `happy_numbers`

### Behavior

* FIB(0) will return 0. Because 0 is a valid index into fib, the first n elements will return up to fib(n-1). (The first 3 elements will be [0, 1, 1].

* HappyNumber(0) will return an exception. The happy number sequence starts at the index of 1. Thus the first n elements of the happy numbers sequence will return up to HappyNumber(n)

* Output will be in json. Here is the sample output for simply getting the nth element:
```
{
    "sequence": "fibonacci",
    "type": "sequence_element",
    "value": 5
}
```

    Here is the output for getting the first n elements:
```
{
    "sequence": "fibonacci",
    "type": "sequence_list",
    "values": [
        0,
        1,
        1,
        2
    ]
}
```

* For exceptions (i.e. if you try to use a random sequence name like this:  
    `GET /sequences/wrong_sequence_name/2)`
```
{
    "code": "invalid_sequence",
    "message": "Invalid sequence: wrong_sequence_name",
    "type": "exception"
}
```


### Testing

Unit tests were written using `unittest`. You can find the tests at `integer_server/calculators/test_calculators.py`.
The tests define a hard coded sequence of fibonacci and happy numbers sequences and make sure that the calculator functions match those hard coded lists. 

### Code Organization and Architecture

The code is organized such that all the apis are in the `api/` folder. Although there's only really one file per folder, I grouped it this way to show I would potentially group a bigger project. The apis define the route and validate the url inputs (using decorators). From there, the apis call into the appropriate services. 

This separation was made such that if we ever wanted to move to a service-oriented architecture there would be an easy divide there and not too much code would need to be changed. The service layer is response for calling into the appropriate calculator and then returning back a domain object. Domain objects are simply containers of data that know how to serialize themselves.

The calculators contain all the logic for actually retrieving the sequence information. We use a factory pattern to return the correct calculator to the service, and each calculator has a generic api that the service can call into. The calculator returns the value, the service layer then packages that data into a domain object and returns the domain object back to the api. The api then returns this back to the client.
