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



/*
CREATE TABLE leaders
(
    leader_id integer,
    leader_name varchar(50),
    member_id integer

);

CREATE TABLE members
(
    member_id integer,
    member_name varchar(50),
    leader_id integer,
    user_id integer
);
*/
