# log analysis 

an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

# Requirements for run this project:

* install python 2.7.
* download database (newdata.zip).
* install vagrant .
* install vm provider (virualbox).
* text editor.

# How to run project using termial:

1. download and unzip fsnd-virtual-machine.zip
2. download and unzip newdata.zip inside folder vagrant .
3. save reporting_tool.py inside folder vagrant.
4. cd fsnd-virtual-machine/FSND-Virtual-Machine/vagrant/

* Startup the VM. (This may take a while)
<code> $ vagrant up </code>

* Log in to the VM.
<code> $ vagrant ssh </code>

* Enter the shared vagrant directory and load the data from newsdata.sql.
<code> $ cd /vagrant
$ psql -d news -f newsdata.sql </code>

* cd to tool file than run the tool using terminal 
<code> python reporting_tool.py </code>

it will run the tool and show the output in terminal .
                       
