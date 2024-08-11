
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


create trigger after_salary_insert
after insert on employee_salary
for each ROW
update expenses
set expense_total = (select sum(salary) from employee_salary)
where expense_name = 'salaries';


show TRIGGERs;

insert into employee_salary VALUES (11, "Khaled", "Khedr", "Software Engineer", 120000, 55, 1 );
call salary_data;

CREATE TRIGGER before_hourly_pay
BEFORE UPDATE ON employee_salary
FOR EACH ROW
SET NEW.hourly_pay = (NEW.salary / 2080);

