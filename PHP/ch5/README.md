# 언제까지, 레거시입니까?

```bash
# PHP Built-in Server
php -S localhost:8080 -t public
```

## 데이터베이스 (MySQL)

```sql
CREATE DATABASE phpblog;

use phpblog;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL
);

CREATE TABLE posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT DEFAULT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,

    FOREIGN KEY(user_id) REFERENCES users(id)
);
```
