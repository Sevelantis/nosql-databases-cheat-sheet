-- c) Produce a report (CBD_L301_<NMEC>.TXT) with all iterations with the "cqlsh". Comment on some of the operations.

-- example history commands
DESCRIBE KEYSPACES ;
create keyspace alien_keyspace;
create keyspace "alien_keyspace";
CREATE KEYSPACE alien_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3}; -- 'class': 'SimpleStrategy' is recommended when the data is not supposed to be shared across multiple datacenters (it is just one datacenter in a docker container so far)
CREATE KEYSPACE alien_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}; -- 'replication_factor': 1 instead of 3 because of the lab purposes, and not production environment. My environment has got only 1 node, so there is no point to replicate the data across more than 1. In the future this can be changed.
DROP KEYSPACE alien_keyspace ;
CREATE KEYSPACE alien_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
DESCRIBE KEYSPACEs;
use alien_keyspace ; -- use created keyspace
describe TABLES ;
create table aliens ( name text, planet text, age int, reincarnations int, universe text, id int, primary key(id) ); -- created example table with a primary key(id)
describe TABLES ;
describe aliens;
use alien_keyspace ;
SELECT * from aliens ;
INSERT INTO aliens (id, age, name, planet, reincarnations , universe ) VALUES (1,999,"qNavin","Pluto", 340, "HD1"); -- inserted some example values
INSERT INTO aliens (id, age, name, planet, reincarnations , universe ) VALUES (1,999,'Navin','Pluto', 340, 'HD1');
select * from aliens ;
INSERT INTO aliens (id, age, name, planet, reincarnations , universe ) VALUES (2,666,'Noyer','Mars', 12, 'HD1');
select * from aliens ;

