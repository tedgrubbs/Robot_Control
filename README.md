# Robot_Control
My attempt of giving other users the ability to control a robot through a php form on my website. I wanted to see if I could do this with as little as possible. 

How it works: A PHP form at tegrubbs.me/Robot/Robot.php takes any valid commands submitted by users and adds them to a database on the server. On the server, a bash script is constantly checking for the file called "GO_FLAG" which is just a small txt file. Whenever the robot has no commands to run a local machine sends this file to the server's home directory via sftp. When the bash script detects this it queries the database for all commands currently listed and prints them to a text file called "Output.txt". It then erases all entries in the database table to keep from repeating any entries. It also deletes GO_FLAG. The server then moves the Output.txt file to the webpage's Robot directory. When the robot has no commands to run, the local machine is also constantly grabbing Output.txt using wget. In python I use numpy to extract the command strings from the file and send them to an arduino microcontroller via echo commands.

These two loops continue repeatedly until I shut them down a SIGINT (ctrl+c).

I don't have any of the code that the server runs here because it's barely twenty lines. So far this seems to work pretty well, but I don't know how it will behave if several people try to send commands at the same time. Some commands could be lost - I don't know. 

Right now all these commands do is turn on a few LEDs on the Arduino. I still need to build the actual robot lol.
