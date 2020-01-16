/* ToDo:


196. Delete Duplicate Emails
Easy

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.

For example, after running your query, the above Person table should have the following rows:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Note:

Your output is the whole Person table after executing your sql. Use delete statement.

-- Conditions & Concepts


*/
-- # Code
-- ## submit part
-- # Write your MySQL query statement below

-- ## test part
-- [Online SQL IDE](https://www.jdoodle.com/execute-sql-online/)
create table Person(Id int, Email char(255));

insert into Person values(1, 'john@example.com');
insert into Person values(2, 'bob@example.com');
insert into Person values(3, 'john@example.com');
-- ## code here
-- #1
/*
{"headers": ["Id", "Email"], "values": [[1, "john@example.com"], [2, "bob@example.com"], [3, "john@example.com"]]}
*/
SELECT Id, Email, COUNT(Email) AS email_times
FROM Person
GROUP BY Email

-- 1.1
/*
3|john@example.com|
*/
SELECT * 
FROM Person P1
LEFT JOIN (
	SELECT Id, Email
	FROM Person
	GROUP BY Email) P2
ON P1.Id = P2.Id
WHERE P2.Id IS NULL;

-- 1.2
SELECT P1.Id
FROM Person P1
LEFT JOIN (
	SELECT Id, Email
	FROM Person
	GROUP BY Email) P2
ON P1.Id = P2.Id
WHERE P2.Id IS NULL;


-- 1.3
/*
You can't specify target table 'Person' for update in FROM clause
解决方法：select的结果再通过一个中间表select多一次，就可以避免这个错误
https://blog.csdn.net/fdipzone/article/details/52695371
*/
DELETE 
FROM Person
WHERE Id IN (
	SELECT P1.Id
	FROM Person P1
	LEFT JOIN (
		SELECT Id, Email
		FROM Person
		GROUP BY Email) P2
	ON P1.Id = P2.Id
	WHERE P2.Id IS NULL);

-- 1.4
/*
Every derived table must have its own alias

Wrong Answer

Input: {"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[2, "abc@efg.com"], [1, "abc@efg.com"]]}}
Output: {"headers": ["Id", "Email"], "values": [[2, "abc@efg.com"]]}
Expected: {"headers":["Id","Email"],"values":[[1,"abc@efg.com"]]}
=> ORDER BY

create table Person(Id int, Email char(255));
insert into Person values(2, 'abc@efg.com');
insert into Person values(1, 'abc@efg.com');
*/
DELETE 
FROM Person
WHERE Id IN (
	SELECT Id FROM (
		SELECT P1.Id
		FROM Person P1
		LEFT JOIN (
			SELECT Id, Email
			FROM Person
			GROUP BY Email) P2
		ON P1.Id = P2.Id
		WHERE P2.Id IS NULL) P );

-- 1.5
/*
Wrong Answer

Input: {"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[2, "abc@efg.com"], [1, "abc@efg.com"]]}}
Output: {"headers": ["Id", "Email"], "values": [[2, "abc@efg.com"]]}
Expected: {"headers":["Id","Email"],"values":[[1,"abc@efg.com"]]}
*/
DELETE 
FROM Person
WHERE Id IN (
	SELECT P.Id FROM (
		SELECT P1.Id
		FROM Person P1
		LEFT JOIN (
			SELECT P0.Id, P0.Email
			FROM (SELECT Id, Email FROM Person ORDER BY Id) P0
			GROUP BY Email) P2
		ON P1.Id = P2.Id
		WHERE P2.Id IS NULL) P );