SELECT * FROM parks_and_recreation.employee_demographics;

SELECT first_name, last_name, birth_date, age, age + 10
FROM parks_and_recreation.employee_demographics;
-- my comment
# my comment

SELECT distinct first_name, gender
FROM parks_and_recreation.employee_demographics;

SELECT *
from parks_and_recreation.employee_demographics
WHERE gender != 'Female'
;

SELECT *
from parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01'
;

SELECT *
from parks_and_recreation.employee_demographics
WHERE first_name LIKE 'a__'
;

SELECT *
from parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01'
AND gender = 'male'
;


SELECT *
from parks_and_recreation.employee_salary
where salary < 60000;

