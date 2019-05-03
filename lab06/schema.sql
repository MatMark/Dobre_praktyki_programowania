DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id integer primary key autoincrement,
    name text not null,
    surname text not null,
    time integer not null
);

INSERT INTO users (id, name, surname, time)
VALUES (null, 'Janusz', 'Sumaryczny', 5);
INSERT into users (id, name, surname, time)
VALUES (null, 'Adrian', 'Dluznik', -2);

DROP TABLE IF EXISTS oferts;
CREATE TABLE oferts (
    id integer primary key autoincrement,
    title text not null,
    time integer not null,
    end boolean not null,
    owner integer not null,
    FOREIGN KEY(owner) REFERENCES users(id)
);

INSERT INTO oferts (id, title, time, end, owner)
VALUES (null, 'Praca w ogrodzie', 2, 0, 1);
INSERT INTO oferts (id, title, time, end, owner)
VALUES (null, 'Mycie okien', 3, 1, 2);