/* ToDo:


175. Combine Two Tables
Easy
SQL Schema

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     | PK
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     | PK
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State

-- Conditions & Concepts


*/
-- # Code
-- ## submit part
-- # Write your MySQL query statement below

-- ## test part

-- ## code here
-- #1
/*
Your input: {"headers": {"Person": ["PersonId", "LastName", "FirstName"], "Address": ["AddressId", "PersonId", "City", "State"]}, "rows": {"Person": [[1, "Wang", "Allen"]], "Address": [[1, 2, "New York City", "New York"]]}}

Output: {"headers": ["FirstName", "LastName", "City", "State"], "values": [["Allen", "Wang", "New York City", "New York"]]}

Expected: {"headers": ["FirstName", "LastName", "City", "State"], "values": [["Allen", "Wang", null, null]]}
*/
SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
FROM Person, Address

-- #1.1
/*
Output: {"headers": ["FirstName", "LastName", "City", "State"], "values": []}
*/
-- SELECT Person.PersonId, Address.PersonId, Person.FirstName, Person.LastName, Address.City, Address.State 
SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
FROM Person, Address 
WHERE Person.PersonId = Address.PersonId
-- GROUP BY Person.FirstName

-- #1.2 inner join
/*
Output: {"headers": ["FirstName", "LastName", "City", "State"], "values": []}

Success
Runtime: 714 ms, faster than 8.04% of MySQL online submissions for Combine Two Tables.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
*/
SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;
