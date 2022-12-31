ALTER TABLE region
    ADD PRIMARY KEY (id);

ALTER TABLE sales_reps
    ADD PRIMARY KEY (id);

ALTER TABLE sales_reps
    ADD FOREIGN KEY (region_id) REFERENCES region(id);

ALTER TABLE accounts
    ADD PRIMARY KEY (id);

ALTER TABLE accounts
    ADD FOREIGN KEY (sales_rep_id) REFERENCES sales_reps(id);

ALTER TABLE orders
    ADD PRIMARY KEY (id);

ALTER TABLE orders
    ADD FOREIGN KEY (account_id) REFERENCES accounts(id);

ALTER TABLE web_events
    ADD PRIMARY KEY (id);

ALTER TABLE web_events
    ADD FOREIGN KEY (account_id) REFERENCES accounts(id);