-- creates a new user and set password
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- grants privileges
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;