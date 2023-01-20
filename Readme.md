## Description

The **client.py** program basicially establish a socket connection with the server that is on the host **proj1.3700.network**. The connection is established when the client sends a JSON msg with "type:hello". The server responds with JSON response with "type:start". The client later sends different word guesses to the server which determines how close the value is to the actual words by assigning each letter with number which is as follows:

Value | Seconds 
--- | --- 
0 | 	Letter does not appear in the secret word 
1 | Letter appears in the secret word, but not in this position 
2 | Letter appears in the secret word in this position


If the guess was correct, the server will respond with a bye message <br>

```RUBY
{"type": "bye", "id": <string>, "flag": <string>}\n
```
## How to Run the code

In the command line, please paste the following code according to your need and preferences

- To establish connect to a specific port without TLS encryption
```ruby
$ python client.py <-p port> <hostname> <username>
```

- To establish connect to a  port with TLS encryption
```ruby
$ python client.py <-s> <hostname> <username>
```

- Since the flags <-s> and <-p> are options so without them and with it would connect to standard port

```ruby
$ python client.py <-s> <-p port> <hostname> <username>
```

```ruby
$ python client.py <hostname> <username>
```


## Implementation

I mainly used the **socket** library to create the client side that interacts with the host. Also I included **argparser, JSON and urllib** libraries for respective jobs. 

At first using the urllib, i fetched the word list data in a variable and change it into string so that program and identify correctness of the word in our program. 

Using the argparser library, i was able to read the command from the command line and we then pick the username, host and different flags from the command line. We choose different ports according the flags as mentioned in the table above (under description). 

Later, we work with the sockets by first connecting to the HOST & PORT. We then send different JSON messages to the server and get the server response. WE send the word packed in a JSON format to the server and the response we get is the closness to which the word letters are to the actual word. 
In the END if the guess is correct then the server sends a UNIQUE FLAG and we then open a file and save it into file. We can recieve two different flag based on which connections we establish either TLS encrypted (with <-s> flag) or without. 

## Problems and Solutions

Since we are using third party client, it behaved strangely to certain responses. For instances 

1. If i get an error message from the server the next time i make the mistake, the connection breaks and serve doesnt send anything. 

Hence when the word != 5 or the word is invalid but 5 letters, it use to give an error and when same mistake would be repeated the connection broke and no response was given
#

<h3>Solution: </h3> 
1. We implimented a while loop and used a library i.e <b> urllib </b> to get the word list and check if the word is invalid or not in the condition of while loop

#

## Making guess easy!!!

We constantly print the response from the server on top of the word guessed by the user. So easy letter has a 0,1 or 2 on top of it so user to know which letter he has to keep fixed and which one should be in the word and which shouldn't be.

In order to further ease it, i wanted to added word suggester function where if user chooses word with letter in exact position then that feature would give suggested words with that specific letter in that position
It barely easy to implement as we would just find the index of that correct letter and crawl throught the list of words with same letter at the same position. But because of limited time and me being lazy, I am skipping the plan heheh :)




