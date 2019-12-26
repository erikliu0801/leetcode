/* ToDo:


181. Employees Earning More Than Their Managers
Easy
SQL Schema

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+



-- Conditions & Concepts


*/
-- # Code
-- ## submit part
-- # Write your MySQL query statement below

-- ## test part

-- ## code here
-- #1
/*
1. create a void table like
+----+-------+--------+----------------+
| Id | Name  | Salary | Manager_Salary |
+----+-------+--------+----------------+
| 1  | Joe   | 70000  | 60000          |
| 2  | Henry | 80000  | 90000          |
| 3  | Sam   | 60000  | NULL           |
| 4  | Max   | 90000  | NULL           |
+----+-------+--------+----------------+
2. WHERE Salary > Manager_Salary

Unknown column 'Manager_Salary' in 'IN/ALL/ANY subquery'
*/
SELECT E.Name AS Employee
FROM Employee E
WHERE Salary > Manager_Salary IN (
	SELECT E1.Name, E1.Salary, E2.Salary AS Manager_Salary
	FROM Employee E1
	INNER JOIN Employee E2
	ON E1.Id = E2.ManagerId
)


/*
Wrong Answer
Runtime: 296 ms
Your input: {"headers": {"Employee": ["Id", "Name", "Salary", "ManagerId"]}, "rows": {"Employee": [[1, "Joe", 70000, 3], [2, "Henry", 80000, 4], [3, "Sam", 60000, null], [4, "Max", 90000, null]]}}
Output: {"headers": ["Employee"], "values": [["Max"]]}
Expected: {"headers": ["Employee"], "values": [["Joe"]]}

Success
Runtime: 615 ms, faster than 41.36% of MySQL online submissions for Employees Earning More Than Their Managers.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
*/
SELECT E.Employee
FROM (
	SELECT E2.Name AS Employee, E2.Salary, E1.Name AS Manager, E1.Salary AS Manager_Salary
	FROM Employee E1
	INNER JOIN Employee E2
	ON E1.Id = E2.ManagerId
) E
WHERE Salary > Manager_Salary

-- 1.1
/*
Wrong Output
{"headers": ["Employee", "Salary", "Manager", "Manager_Salary"], "values": [["Joe", 70000, "Sam", 60000], ["Henry", 80000, "Max", 90000]]}
*/
SELECT E2.Name AS Employee, E2.Salary, E1.Name AS Manager, E1.Salary AS Manager_Salary
FROM Employee E1
INNER JOIN Employee E2
ON E1.Id = E2.ManagerId

-- 1.2
/*
Wrong Output
{"headers": ["Name", "Salary", "Manager_Salary"], "values": [["Sam", 60000, 70000], ["Max", 90000, 80000], [null, null, 60000], [null, null, 90000]]}
*/
SELECT E1.Name, E1.Salary, E2.Salary AS Manager_Salary
FROM Employee E1
RIGHT JOIN Employee E2
ON E1.Id = E2.ManagerId

-- 1.3
/*
Wrong Output
{"headers": ["Name", "Salary", "Manager_Salary"], "values": [["Sam", 60000, 70000], ["Max", 90000, 80000], ["Joe", 70000, null], ["Henry", 80000, null]]}
*/
SELECT E1.Name, E1.Salary, E2.Salary AS Manager_Salary
FROM Employee E1
LEFT JOIN Employee E2
ON E1.Id = E2.ManagerId

-- 1.4
/*
Wrong Output
{"headers": ["Name", "Salary", "Manager_Salary"], "values": [["Sam", 60000, 70000], ["Max", 90000, 80000]]}
*/
SELECT E1.Name, E1.Salary, E2.Salary AS Manager_Salary
FROM Employee E1
INNER JOIN Employee E2
ON E2.ManagerId = E1.Id

-- 1.5
/*
Wrong Output
{"headers": ["Name", "Salary", "Manager_Salary"], "values": [["Sam", 60000, 70000], ["Max", 90000, 80000]]}
*/
SELECT E1.Name, E1.Salary, E2.Salary AS Manager_Salary
FROM Employee E2
INNER JOIN Employee E1
ON E2.ManagerId = E1.Id