AirBnB_clone
This project consists in develop a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
enter image description here

The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
File Structure
[AUTHORS]- list of contributors
[console.py] - command interpreter
do_create - create a new instance of a class
do_show - prints string representation of an instance based on class name and id
do_all - prints all string representation of all instances based or not on the class name
do_destroy - deletes an instance based on the class name and id
do_update - updates an instance based on the class name and id by adding or updating attribute
emptyline - ensures that hitting ‘enter’ will not remember the last command
do_quit - quit program
do_EOF - exit at end of file
[file_storage.py] - class FileStorage
all - returns the dictionary __objects
new - sets in __objects the obj with key .id
save - serializes __objects to the JSON file (path: __file_path)
reload - deserializes the JSON file to __objects
[base_model.py]- parent class that will take care of initialization/serialization/deserialization of future instances
__init__ - initialize instance attributes
__str__ - creates formatted string representation of instance
__repr__ - returns string representation of instance
save - updates public instance attribute updated_at with current datetime
to_dict - creates a dictionary containing all keys/values of __dict__ of the instance
Installation
https://github.com/dagute/AirBnB_clone.git
cd AirBnB_clone



Usage
Interactive Mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
SH BUGS
No known bugs.

Environment
Language: Python3

OS: Ubuntu 14.04 LTS
Style guidelines: PEP 8 (version 1.7)
AUTHORS
Faber Ruiz, David Agudelo Theran
