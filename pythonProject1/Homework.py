andrey@WIN-DD1Q4R6SQRR:~$ sudo service redis-server start
[sudo] password for andrey:
andrey@WIN-DD1Q4R6SQRR:~$ redis-cli
127.0.0.1:6379> set username 'Andrey'
OK
127.0.0.1:6379> rpush todo_list 'Go to the store'
Invalid argument(s)
127.0.0.1:6379> rpush todo_list 'Go to the gym'
(integer) 1
127.0.0.1:6379> lrange todo_list 0 -1
1) "Go to the gym"
127.0.0.1:6379> rpush todo_list 'Goto the store'
(integer) 2
127.0.0.1:6379> lrange todo_list 0 -1
1) "Go to the gym"
2) "Goto the store"
127.0.0.1:6379> hmset user_data age 25 country 'Ukrain'
OK
127.0.0.1:6379> hgetall user_data
1) "age"
2) "25"
3) "country"
4) "Ukrain"
127.0.0.1:6379> sadd tags 'programming'
(integer) 1
127.0.0.1:6379> sadd tags 'redis'
(integer) 1
127.0.0.1:6379> sadd tags 'tutorial'
(integer) 1
127.0.0.1:6379> smembers tags
1) "programming"
2) "redis"
3) "tutorial"
127.0.0.1:6379> incrby page_views 5
(integer) 5
127.0.0.1:6379> get page_views
"5"
127.0.0.1:6379> setex session_token 60 'abc123'
OK
127.0.0.1:6379> del username
(integer) 1
127.0.0.1:6379> exists username
(integer) 0
127.0.0.1:6379> set user:1:name 'Andrey'
OK
127.0.0.1:6379> keys user:123
(empty array)
127.0.0.1:6379> setbit online_status 0 1
(integer) 0
127.0.0.1:6379> getbit online_status 0
(integer) 1
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> incrby balance 500
QUEUED
127.0.0.1:6379(TX)> get balance
QUEUED
127.0.0.1:6379(TX)> exec
1) (integer) 500
2) "500"
127.0.0.1:6379> rpush cache:popular_articles 01 02 03
(integer) 3
127.0.0.1:6379> sadd set1 'a' 'b' 'c'
(integer) 3
127.0.0.1:6379> sadd set2 'b' 'c' 'd'
(integer) 3
127.0.0.1:6379> sunionstore union_set set1 set2
(integer) 4
127.0.0.1:6379> sinterstore intersection_set set1 set2
(integer) 2
127.0.0.1:6379> subscribe messages
1) "subscribe"
2) "messages"
3) (integer) 1
127.0.0.1:6379(subscribed mode)> geoadd locations 30.35 56.34 'Kyiv'
(error) ERR Can't execute 'geoadd': only (P|S)SUBSCRIBE / (P|S)UNSUBSCRIBE / PING / QUIT / RESET are allowed in this context
127.0.0.1:6379(subscribed mode)> geoadd locations 35 46 'Kyiv'
(error) ERR Can't execute 'geoadd': only (P|S)SUBSCRIBE / (P|S)UNSUBSCRIBE / PING / QUIT / RESET are allowed in this context
127.0.0.1:6379(subscribed mode)> geoadd locations 24.0297 49.8397 'Lviv'
(error) ERR Can't execute 'geoadd': only (P|S)SUBSCRIBE / (P|S)UNSUBSCRIBE / PING / QUIT / RESET are allowed in this context
127.0.0.1:6379(subscribed mode)> geoadd locations 30.35 56.28 "Kyiv"
(error) ERR Can't execute 'geoadd': only (P|S)SUBSCRIBE / (P|S)UNSUBSCRIBE / PING / QUIT / RESET are allowed in this context
127.0.0.1:6379(subscribed mode)> rpush tasks "Task 1"
(error) ERR Can't execute 'rpush': only (P|S)SUBSCRIBE / (P|S)UNSUBSCRIBE / PING / QUIT / RESET are allowed in this context
127.0.0.1:6379> geoadd locations 30.25 56.48 'Kyiv'
(integer) 1
127.0.0.1:6379> geoadd locations 24.48 23.56 'Lviv'
(integer) 1
127.0.0.1:6379> rpush tasks 'Task 1'
(integer) 2
127.0.0.1:6379> rpush task 'Task 2'
(integer) 1
127.0.0.1:6379> rpush task 'Task 3'
(integer) 2
127.0.0.1:6379> rpush task 'Play to game'
(integer) 3
127.0.0.1:6379> rpush task 'Drive a car'
(integer) 4
127.0.0.1:6379> lrange task 0 -1
1) "Task 2"
2) "Task 3"
3) "Play to game"
4) "Drive a car"
127.0.0.1:6379> rpush tasks 'Goto job'
(integer) 3
127.0.0.1:6379> lpop tasks
"task1"
127.0.0.1:6379> lpop tasks
"Task 1"
127.0.0.1:6379> lpop tasks
"Goto job"
127.0.0.1:6379> lrange tasks 0 -1
(empty array)
127.0.0.1:6379> rpush tasks 'repair car'
(integer) 1
127.0.0.1:6379> rpush tasks 'to learn'
(integer) 2
127.0.0.1:6379> lrange tasks 0 -1
1) "repair car"
2) "to learn"
127.0.0.1:6379> pfadd unique_user 'Andrey' 'Admin' 'User'
(integer) 1
127.0.0.1:6379> rpush message_queue 'Hello'
(integer) 1
127.0.0.1:6379> rpush message_queue 'How are you'
(integer) 2
127.0.0.1:6379> lrange message_queue 0 -1
1) "Hello"
2) "How are you"
127.0.0.1:6379>quit
andrey@WIN-DD1Q4R6SQRR:~$ sudo systemct1 stop redis-server
[sudo] password for andrey:
sudo: systemct1: command not found
andrey@WIN-DD1Q4R6SQRR:~$ quit
Command 'quit' not found, but can be installed with:
sudo snap install quit
andrey@WIN-DD1Q4R6SQRR:~$ sudo service redis-server stop