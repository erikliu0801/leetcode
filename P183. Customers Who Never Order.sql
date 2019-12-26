/* ToDo:


183. Customers Who Never Order
Easy
SQL Schema

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Table: Orders.
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Using the above tables as example, return the following:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

-- Conditions & Concepts


*/
-- # Code
-- ## submit part
-- # Write your MySQL query statement below

-- ## test part

-- ## code here
-- #1
/*
*/
SELECT Name AS Customers
FROM Customers
WHERE buy_times = 0

-- #1.1
/*
{"headers": ["CustomerId", "buy_times"], "values": [[1, 1], [3, 1]]}
*/
SELECT CustomerId, COUNT(CustomerId) AS buy_times
FROM Orders
GROUP BY CustomerId

-- #1.2
/*
{"headers": ["Id", "Name", "buy_times"], "values": [[1, "Joe", 1], [2, "Henry", null], [3, "Sam", 1], [4, "Max", null]]}
*/
SELECT C.Id, C.Name, O.buy_times
FROM Customers C
LEFT JOIN (
	SELECT CustomerId, COUNT(CustomerId) AS buy_times
	FROM Orders
	GROUP BY CustomerId) O
ON C.Id = O.CustomerId

-- #1.3
/*
{"headers": ["Id", "Name", "buy_times"], "values": [[2, "Henry", null], [4, "Max", null]]}
*/
SELECT C.Id, C.Name, O.buy_times
FROM Customers C
LEFT JOIN (
	SELECT CustomerId, COUNT(CustomerId) AS buy_times
	FROM Orders
	GROUP BY CustomerId) O
ON C.Id = O.CustomerId
WHERE O.buy_times IS null

-- #1.4
/*
Success
Runtime: 685 ms, faster than 28.02% of MySQL online submissions for Customers Who Never Order.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
*/
SELECT C.Name AS Customers
FROM Customers C
LEFT JOIN (
	SELECT CustomerId, COUNT(CustomerId) AS buy_times
	FROM Orders
	GROUP BY CustomerId) O
ON C.Id = O.CustomerId
WHERE O.buy_times IS null