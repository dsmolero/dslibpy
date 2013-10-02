dslibpy.numbers
===============
NUMERIC FUNCTIONS
-----------------
##### Darwinian Software Library for Python
Author: [Darwin Molero](http://blog.darwiniansoftware.com/about)


deccomma(amount, decimals=4)
----------------------------
Returns: string

Formats amount into the standard form 99,9999.0000. Amount can be an integer,
a decimal or a float.

If `amount` has more digits in its decimal portion than the `decimals`
parameter, the resulting number is rounded.

for example:

    deccomma(1234.5678, 2)

returns the string "1,234.57"


<< [Back to Main](../../README.md)
