"""

1. Create/Drop table:
CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
INTEGER);
DROP TABLE shopping
---------------------------------------------------
create is creating a table.
drop is removing the table.
---------------------------------------------------

2. Rename table:
ALTER table shopping RENAME to shopp
ALTER table shopp RENAME to shopping
---------------------------------------------------
renaming the table name.
---------------------------------------------------


3. Insert rows into table:
INSERT INTO shopping VALUES (1, 'Avokado', 5);
INSERT INTO shopping VALUES (2, 'Milk', 2);
INSERT INTO shopping VALUES (3, 'Bread', 3);
INSERT INTO shopping VALUES (4, 'Chocolate', 8);
INSERT INTO shopping VALUES (5, 'Bamba', 5);
INSERT INTO shopping VALUES (6, 'Orange', 10);
---------------------------------------------------
inserting desired stuff into certain location in the table.
---------------------------------------------------

4. Display table:
select * from shopping
---------------------------------------------------
selects the whole table.
---------------------------------------------------

5. ?
SELECT id, name FROM shopping
---------------------------------------------------
selects all the id and names in the column.
---------------------------------------------------

6. ?
SELECT * FROM shopping WHERE amount > 5
SELECT * FROM shopping WHERE amount = 2
SELECT * FROM shopping WHERE name LIKE 'Bamba'
---------------------------------------------------
displays all content in a certain condition.
---------------------------------------------------

7. ?
DELETE from shopping WHERE name like 'Orange';
---------------------------------------------------
deletes values from a given place in the table.
---------------------------------------------------

8. ?
UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'
---------------------------------------------------
updates (changes) a given name from a given place in the table.
---------------------------------------------------

9. ?
ALTER TABLE shopping ADD COLUMN maavar
---------------------------------------------------
add another column with the given name.
---------------------------------------------------

10. ?
UPDATE shopping SET maavar=6 WHERE id=1;
UPDATE shopping SET maavar=3 WHERE id=2;
UPDATE shopping SET maavar=12 WHERE id=3;
UPDATE shopping SET maavar=8 WHERE id=4;
UPDATE shopping SET maavar=5 WHERE id=5;
---------------------------------------------------
updates (changes) the "maavar" rows for every id.
---------------------------------------------------

11. ?
SELECT * FROM shopping WHERE amount > 1 AND maavar > 5
SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5
---------------------------------------------------
displays all values in a certain conditions.
---------------------------------------------------

12. ?
SELECT * FROM shopping ORDER BY maavar
SELECT * FROM shopping ORDER BY maavar DESC
---------------------------------------------------
arranges the table from the biggest amount in the maavar column to the smallest.
---------------------------------------------------

13. ?
CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
DELETE FROM books;
---------------------------------------------------
create a table named books, inserts two values, then deletes it.
---------------------------------------------------

14. ?
SELECT COUNT(*)from shopping
SELECT MAX(amount) from shopping
SELECT AVG(amount) from shopping
SELECT MIN(amount) from shopping
---------------------------------------------------
displays the count, the max, the avg and the min from the shopping table.
---------------------------------------------------

15. ?
INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
Select maavar, COUNT(*)FROM shopping GROUP BY maavar
---------------------------------------------------
inserts the given values in the desired columns.
---------------------------------------------------

16. ?
SELECT id AS "SECRET", name, amount, maavar FROM shopping
---------------------------------------------------
displays the given columns and changes the the id column to secret.
---------------------------------------------------

17. ?
Select maavar, COUNT(*)FROM shopping GROUP BY maavar HAVING COUNT(*)>1
---------------------------------------------------
displays the maavar values that appears more then once in the shopping table.
---------------------------------------------------

18. ?
CREATE TABLE prices (id INTEGER PRIMARY KEY, price INTEGER);
INSERT INTO prices VALUES (1, 3);
INSERT INTO prices VALUES (2, 7);
INSERT INTO prices VALUES (3, 12);
INSERT INTO prices VALUES (4, 5);
INSERT INTO prices VALUES (5, 3);
INSERT INTO prices VALUES (6, 2);
INSERT INTO prices VALUES (7, 10);
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id
---------------------------------------------------
creates new table named prices, and insert values to it.
---------------------------------------------------

מה מחושב בתוך SECRET ? 19.
SELECT s.id, s.name, s.amount, s.maavar, p.price, s.amount * p.price AS
"SECRET" FROM shopping s JOIN prices p ON s.id=p.id
---------------------------------------------------
multiplies the quantity by the price for each item and labels it as SECRET.
---------------------------------------------------

20. ?
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id WHERE p.price = (SELECT MAX(price) FROM
prices)
---------------------------------------------------
selects items with the highest price.
---------------------------------------------------

)2( פתור:

Students
ID (INTEGER)PRIMARY KEY NAME (TEXT) CITY (TEXT) BIRTH (INTEGER)
1 SHALOM TEL AVIV 1974
2 YURI RAANANA 1980
3 ANAT RISHON 1994
4 DANA REHOVOT 1990
5 OMER JERUSALEM 1987

GRADE

- כתוב את השאילתות ליצירת הטבלאות )ללא האיכלוס(
___________________________________________________________________
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, city TEXT,
birth INTEGER);
___________________________________________________________________
CREATE TABLE grades (id INTEGER PRIMARY KEY, grade INTEGER);
___________________________________________________________________
- כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל
___________________________________________________________________
INSERT INTO grades VALUES (1, 95);
INSERT INTO grades VALUES (2, 70);
INSERT INTO grades VALUES (3, 85);
INSERT INTO grades VALUES (4, 99);
INSERT INTO grades VALUES (5, 91);
___________________________________________________________________
INSERT INTO students VALUES (1, 'SHALOM', "Tel Aviv", 1974);
INSERT INTO students VALUES (2, 'YURI', "Raanana", 1980);
INSERT INTO students VALUES (3, 'ANAT', "Rishon", 1994);
INSERT INTO students VALUES (4, 'DANA', "Rehovot", 1990);
INSERT INTO students VALUES (5, 'OMER', "Jerusalem", 1987);
___________________________________________________________________
- כתוב שאילתא אשר מחשבת את הממוצע הכיתתי
___________________________________________________________________
SELECT AVG(grade) from grades
___________________________________________________________________
- כתוב שאילתא להוספת עמודה EXCELLENT. כעת שים YES כאשר הציון גבוה מ90- אחרת שים NO
___________________________________________________________________
ALTER TABLE grades ADD COLUMN EXCELLENT
___________________________________________________________________
UPDATE grades SET EXCELLENT="yes" WHERE grade > 90;
UPDATE grades SET EXCELLENT="no" WHERE grade < 90;
___________________________________________________________________

- *כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל רק עבור
התלמידים אשר קיבלו מעל הממוצע
___________________________________________________________________
___________________________________________________________________
- * כתוב שאילתא אשר מדפיסה את התלמיד ואת ציונו עבור התלמיד אשר קיבל את הציון הגבוה
ביותר_______________________________________________________________
_______________________________________________________________

"""