dslibpy.templatetags
====================

Templatetags for Numbers:
-------------------------

### deccomma(amount, decimals=4)

Formats any number into the standard 99,999.0000 in templates. The decimal
portion is rounded when passed a parameter less than 4.

example for amount == 1234.5678:

    {{ amount|deccomma:"2" }}

will produce:

    1,234.57

### deccomma_color_html(amount)

Returns an html `<span>` element with the formatted number in standard form
99,999.00. The decimal portion is rounded when it contains more than 2 digits.
The `<span>` element will have the class attribute:

* "negative" ==> when the number is negative.
* "positive" ==> when the number is positive.
* "zero" ==> when the number is zero.

example for amount == -1234.5645:

    {{ amount|deccomma_color_html }}

will produce:

    <span class="negative">-1,234.56</span>

### percent_color_html(amount)

This templatetag is basically the same with deccomma_color_html except that this
will append a percent sign (%) to the number.

example for amount == 45.678:

    {{ rate|percent_color_html }}

will produce:

    45.68%


[(Back to Main Page)](/README.rst)
