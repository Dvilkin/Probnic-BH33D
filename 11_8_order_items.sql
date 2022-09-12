create table order_items(
id serial primary key,
order_id smallint,
product_id smallint,
total float,
foreign key (order_id) references orders(id) on delete no action,
foreign key (product_id) references products(id) on delete no action);
