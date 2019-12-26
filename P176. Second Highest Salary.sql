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
/*
Output: {"headers": ["SecondHighestSalary"], "values": [[300], [200]]}


Input: {"headers": {"Employee": ["Id", "Salary"]}, "rows": {"Employee": [[1, 100]]}}
Output: {"headers": ["SecondHighestSalary"], "values": []}
Expected: {"headers":["SecondHighestSalary"],"values":[[null]]}
*/
SELECT Employee.Salary AS 'SecondHighestSalary'
FROM Employee
ORDER BY Salary DESC
LIMIT 1,1

-- #1.2
/*
Output: {"headers": ["SecondHighestSalary"], "values": [[300], [200]]}
*/
SELECT Employee.Salary AS 'SecondHighestSalary'
FROM Employee
ORDER BY Salary DESC
-- WHERE ROWNUM = 2
-- OFFSET 1 ROWS
-- FETCH NEXT 1 ROWS ONLY

-- #1.2
INSERT INTO Employee.Salary (Id, Salary) VALUES ('0','null');
INSERT INTO Employee.Salary (Id, Salary) VALUES ('0','null');
SELECT Employee.Salary AS 'SecondHighestSalary'
FROM Employee
ORDER BY Salary DESC
LIMIT 1,1