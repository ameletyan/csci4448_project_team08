from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'employees'

TABLES = {}

TABLES['boards'] = (
    "CREATE TABLE `boards` ("
    "  `boardid` int(11) NOT NULL AUTO_INCREMENT,"
    "  `boardName` varchar(20) NOT NULL,"
    "  `leaderid` int(11) NOT NULL,"
    "  `member1id` int(11) NOT NULL,"
    "  `member2id` int(11) NOT NULL,"
    "  `member3id` int(11) NOT NULL,"
    "  `member4id` int(11) NOT NULL,"
    "  `member5id` int(11) NOT NULL,"
    "  `member6id` int(11) NOT NULL,"
    "  `member7id` int(11) NOT NULL,"
    "  `member8id` int(11) NOT NULL,"
    "  `member9id` int(11) NOT NULL,"
    " PRIMARY KEY (`boardid`)"
    ") ENGINE=InnoDB")


