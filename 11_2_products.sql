create table products(
id serial primary key,
category_id smallint,
price float,
media varchar(20) unique not null,
total float,
name varchar(20) unique not null,
foreign key (category_id) references categories(id) on delete no action);
