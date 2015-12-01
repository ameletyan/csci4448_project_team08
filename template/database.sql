/*
CREATE TABLE boards
(
    board_id integer,
    board_name varchar(50),
    user_id integer
);

CREATE TABLE users
(
    user_id integer,
    leader boolean,
    email varchar(50),
    name varchar(50)
);

CREATE TABLE tasks
(
    task_id integer,
    description varchar(255),
    user_id integer
);
*/

CREATE TABLE boards
(
    board_id integer,
    board_name varchar(50),
    task_id integer,
    leader_id integer
)

CREATE TABLE tasks
(
    task_id integer,
    task_title varchar(50),
    task_description varchar(256),
    task_state varchar(5),
    user_id integer 
)

CREATE TABLE members
(
    member_id integer,
    member_name varchar(50),
    email varchar(50),
	password varchar(50),
	boards varchar(256)
)

CREATE TABLE leaders
(
    leader_id integer,
    leader_name varchar(50),
    member_id integer,
    email varchar(5)
)
