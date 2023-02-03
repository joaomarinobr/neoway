USE db_neoway;

DROP TABLE tb_user;
DROP TABLE tb_user_address;
DROP TABLE tb_user_contact;

CREATE TABLE tb_user_address (
	user_address_id int NOT NULL AUTO_INCREMENT,
    address varchar(120) NOT NULL,
    full_address varchar(200) NOT NULL,
    number int NOT NULL,
    city varchar(80) NOT NULL,
    state varchar(60) NOT NULL,
    country varchar(10) NOT NULL,
    postcode varchar(10) NOT NULL,
    latitude decimal(11,7) NOT NULL,
    longitude decimal(11,7) NOT NULL,
    PRIMARY KEY(user_address_id)
);

CREATE TABLE tb_user_contact (
	user_contact_id int NOT NULL AUTO_INCREMENT,
    email varchar(120) NOT NULL,
    phone varchar(14) NOT NULL,
    cell varchar(14) NOT NULL,
    PRIMARY KEY(user_contact_id)
);

CREATE TABLE tb_user (
    user_id int NOT NULL AUTO_INCREMENT,
    first_name varchar(80) NOT NULL,
    last_name varchar(80) NOT NULL,
    gender varchar(10) NOT NULL,
    birthday datetime NOT NULL,
    age int NOT NULL,
    nationality varchar(2) NOT NULL,
    registered_date datetime NOT NULL,
    user_classification varchar(20) NOT NULL,
    purpose_use varchar(40) NOT NULL,
    url varchar(120) NOT NULL,
    load_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMp,
    user_address_id int NOT NULL,
    user_contact_id int NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_address_id) REFERENCES tb_user_address(user_address_id),
    FOREIGN KEY (user_contact_id) REFERENCES tb_user_contact(user_contact_id)
);
