
Use parks_and_recreation;

call salary_data;


show create PROCEDURE salary_data;

delete from employee_salary
where employee_id = 12;
call salary_data;


create table expenses(
    expense_id int PRIMARY KEY AUTO_INCREMENT,
    expense_name varchar(255),
    expense_total decimal(10,2)
);
insert into expenses (expense_name, expense_total)
values ("salaries", 0), ("supplies", 0), ("taxes", 0);
select * from expenses;


update expenses
set expense_total = (select sum(salary) from employee_salary)
where expense_name = 'salaries'
;

DELIMITER $$
create trigger after_salary_delete
after delete on employee_salary
for each row
begin
    update expenses
    set expense_total = (select sum(salary) from employee_salary)
    where expense_name = 'salaries';
end$$
delimiter ;

delete from employee_salary
where employee_id = 11
;
select * from expenses;

create trigger before_hourly_pay_update
before update on employee_salary
for each row
set new.hourly_pay = (new.salary / 2080);


create trigger after_salary_insert
after insert on employee_salary
for each ROW
update expenses
set expense_total = (select sum(salary) from employee_salary)
where expense_name = 'salaries';

use parks_and_recreation;
show TRIGGERs;
call user_data;
show create PROCEDURE user_data;

insert into employee_salary VALUES (11, "Khaled", "Khedr", "Software Engineer", 120000, 55, 1 );
call salary_data;


delimiter $$ ;
CREATE TRIGGER before_hourly_pay
BEFORE UPDATE ON employee_salary
[begin_label:]
BEGIN
[statement_list]
FOR EACH ROW;
SET NEW.hourly_pay = (NEW.salary / 2080);
END$$
[end_label]
delimiter ;



delimiter $$
create procedure my_procedure_loacl_variables()
begin
declare a int DEFAULT 10;
declare b, c int;
set a = a + 100;
set b = 2;
set c = a + b;
BEGIN
DECLARE c int;
set c = 5;
select a, b, c;
end;
select a,b,c;
end $$
delimiter ;

call my_procedure_loacl_variables();


