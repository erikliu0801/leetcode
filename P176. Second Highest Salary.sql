/* ToDo:


176. Second Highest Salary
Easy
SQL Schema

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+



-- Conditions & Concepts


*/
-- # Code
-- ## submit part
-- # Write your MySQL query statement below

-- ## test part

-- ## code here
-- #1
/*
Output: {"headers": ["SecondHighestSalary"], "values": [[300], [200], [100]]}
*/
SELECT Employee.Salary AS 'SecondHighestSalary'
FROM Employee
ORDER BY Salary DESC


-- #1.1
SELECT * FROM Employee ORDER BY Salary;

