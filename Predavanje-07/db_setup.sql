CREATE DATABASE myblogdbname;
CREATE USER myblog_adminuser WITH PASSWORD '%mbaoP$yvVxjAiQ7OTzR#rY!e8!TPAMUo7590NzC8#G96t@XEn';
ALTER ROLE myblog_adminuser SET client_encoding TO 'utf8';
ALTER ROLE myblog_adminuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myblog_adminuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myblogdbname TO myblog_adminuser;


