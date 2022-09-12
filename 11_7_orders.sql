create table orders(
id serial primary key,
user_id smallint,
data_create timestamp,
status_id smallint,
invoice_id smallint,
foreign key (user_id) references users(id) on delete no action,
foreign key (status_id) references statuses(id) on delete no action,
foreign key (invoice_id) references invoices(id) on delete no action);
