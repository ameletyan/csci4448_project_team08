CREATE TABLE boards
(
    board_id integer,
    board_name varchar(50),
    task_ids varchar(256),
	leader_id integer,
	member_ids varchar(256),
)

CREATE TABLE tasks
(
    task_id integer,
    task_description varchar(256),
    task_state varchar(5),
   	member_id integer 
)

CREATE TABLE members
(
    member_id integer,
    member_name varchar(50),
    email varchar(50),
	password varchar(50),
	board_ids varchar(256)
)

/*Probably not needed*/
CREATE TABLE leaders
(
    leader_id integer,
    leader_name varchar(50),
    member_id integer,
    email varchar(5)
)
