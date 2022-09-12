create table categories(
id smallserial primary key,
parent_id smallint,
is_published boolean default(false),
name varchar(20) unique not null,
foreign key (parent_id) references categories(id) on delete cascade);
