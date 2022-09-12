create table users(
id serial primary key,
balance float,
language_id smallint,
foreign key (language_id) references languages(id) on delete cascade);
