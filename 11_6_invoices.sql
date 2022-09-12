create table invoices(
id serial primary key,
user_id smallint,
data_create timestamp,
total float,
status_id smallint,
foreign key (user_id) references users(id) on delete cascade,
foreign key (status_id) references statuses(id) on delete cascade);
