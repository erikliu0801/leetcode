/* ToDo:


197. Rising Temperature
Easy
SQL Schema

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+

For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+
-- Conditions & Concepts


*/
-- # Code
-- ## submit part
-- # Write your MySQL query statement below

-- ## test part
/*
create table Weather(Id int, RecordDate char(30), Temperature int);
insert into Weather values(1, '2015-01-01', 10);
insert into Weather values(2, '2015-01-02', 25);
insert into Weather values(3, '2015-01-03', 20);
insert into Weather values(4, '2015-01-04', 30);

*/
-- ## code here
-- #1
/*
*/
SELECT (Id + 1) temp_Id, Temperature
FROM Weather

-- 1.1
/*
Input: {"headers": {"Weather": ["Id", "RecordDate", "Temperature"]}, "rows": {"Weather": [[1, "2000-12-16", 3], [2, "2000-12-15", -1]]}}
Output: {"headers": ["Id"], "values": []}
Expected: {"headers":["Id"],"values":[[1]]}

Misunderstanding
*/
SELECT W.Id, (W.Temperature - W0.Temperature) AS D
FROM Weather W
LEFT JOIN (
	SELECT (Id + 1) temp_Id, Temperature
	FROM Weather) W0
ON W.Id = W0.temp_Id


SELECT W.Id
FROM Weather W
LEFT JOIN (
	SELECT (Id + 1) temp_Id, Temperature
	FROM Weather) W0
ON W.Id = W0.temp_Id
WHERE (W.Temperature - W0.Temperature) > 0

-- 1.2
