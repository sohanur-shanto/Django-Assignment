Answer 03:

Hoisting is a JS concept where variable and function declarations are moved to the top of their scope for example,

    function example() {
                a=10;
                var b=20
            }
    example();
    console.log(b,a);

so the output of the program is undefined and 10, because without declaration of var it goes to the top of the scope and 
declare with var is still in the local scope. Let's have another example,

    var name='khan';
    var lastname='Salman'
    ( 
        function() {

        var name='Salman'
        lastname='khan'

    })();

    console.log(name,lastname);

the output of the program is khan khan, only the actual declarations are hoisted. In first phase of execution 
all the declared variables and functions are stored in memory and at the time of storing them in memory variables are 
assigned to undefined. And in second phase execution phase actual values are assigned to that memory locations.



Answer 04:

Part 01-

CREATE TABLE A (
  id INTEGER PRIMARY KEY
);
INSERT INTO A VALUES (1);
INSERT INTO A VALUES (2);
INSERT INTO A VALUES (3);
INSERT INTO A VALUES (4);
INSERT INTO A VALUES (5);
CREATE TABLE B (
  id INTEGER PRIMARY KEY
);
INSERT INTO B VALUES (3);
INSERT INTO B VALUES (4);
INSERT INTO B VALUES (6);
SELECT * 
FROM A
FULL OUTER JOIN B
ON A.id = B.id
WHERE A.id IS NULL
OR
B.id IS NULL;


part 2-

SELECT DISTINCT employee_name
FROM employee_info_dummy
ORDER BY employee_name DESC;
