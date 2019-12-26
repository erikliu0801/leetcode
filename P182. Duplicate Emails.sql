/* ToDo:


182. Duplicate Emails
Easy
SQL Schema

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+


-- Conditions & Concepts


*/
-- # Code
-- ## submit part
-- # Write your MySQL query statement below

-- ## test part

-- ## code here
-- #1
/*
Success
Runtime: 752 ms, faster than 5.01% of MySQL online submissions for Duplicate Emails.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
*/
SELECT P.Email
FROM (
	SELECT Id, Email, COUNT(Email) AS email_count
	FROM Person
	GROUP BY Email) P
WHERE email_count > 1; 


-- 1.1
/*
{"headers": ["Id", "Email", "email_count"], "values": [[1, "a@b.com", 2], [2, "c@d.com", 1]]}
*/
SELECT Id, Email, COUNT(Email) AS email_count
FROM Person
GROUP BY Email
