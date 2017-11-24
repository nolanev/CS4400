# CS4400
Assignments repo for Internet Applications module.
Goal is to implement a centralised chat server with functionality so clients can join chat rooms, post messages and retrieve messages, and leave chat rooms.

Project was begun in Haskell but due to a number of difficulties canged to Python and the server is implemented using Sockets

Implemenation to be graded is in "CS4400/PythonChatserver"

I have been testing my implementation agaisnt the test server but am getting stuck at around 30%
Server takes in and deals with the HELO, ANYTHING and JOIN messages fine but after receiving and responding to JOIN MESSAGE seems to hang waiting for the next message from the test server
I cant see the issue in the code causing this but think that my code in theory has all the functionality nessesary for the assignment but because of this error I cannot test past these three messages
