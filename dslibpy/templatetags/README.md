dslibpy.templatetags
====================

TEMPLATETAGS
------------
##### Darwinian Software Library for Python
Author: [Darwin Molero](http://blog.darwiniansoftware.com/about)


### deccomma(amount, decimals=4)

Formats any number into the standard 99,999.0000 in templates. If `amount` has
more digits in its decimal portion than the `decimals` parameter, the resulting
number is rounded.

example for amount == 1234.5678:

    {{ amount|deccomma:"2" }}

will output:

    1,234.57

### deccomma_color_html(amount)

Returns an html `<span>` element with the formatted number in standard form
99,999.00. The decimal portion is rounded when it contains more than 2 digits.

The `<span>` element will have the class attribute:

* "negative" ==> when the number is negative.
* "positive" ==> when the number is positive.
* "zero" ==> when the number is zero.

example for amount == -1234.5678:

    {{ amount|deccomma_color_html }}

will output:

    <span class="negative">-1,234.57</span>

### percent_color_html(amount)

This templatetag is basically the same with `deccomma_color_html` except that
it will append a percent sign (%) to the number.

example for rate == 45.678:

    {{ rate|percent_color_html }}

will output:

    <span class="positive">45.68%</span>


<< [Back to Main](../../README.md)
