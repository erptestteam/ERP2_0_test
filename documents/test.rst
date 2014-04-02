一级标题
========

二级标题
--------

三级标题
~~~~~~~~

四级标题
^^^^^^^^

五级标题
++++++++

六级标题
````````

*emphasis*
**strong emphasis**
`interpreted text`
``inline literal``
http://docutils.sf.net/
This is a paragraph.

Paragraphs line up at their left 
edges, and are normally separated 
by blank lines.

Bullet lists:
- This is item 1 
- This is item 2

- Bullets are "-", "*" or "+". 
  Continuing text must be aligned 
  after the bullet and whitespace.

Note that a blank line is required 
before the first item and after the 
last, but is optional between items.

Enumerated lists:
3. This is the first item 
4. This is the second item 
5. Enumerators are arabic numbers, 
   single letters, or roman numerals 
6. List items should be sequentially 
   numbered, but need not start at 1 
   (although not all formatters will 
   honour the first index). 
#. This item is auto-enumerated

Definition lists: 

what 
  Definition lists associate a term with 
  a definition. 

how 
  The term is a one-line phrase, and the 
  definition is one or more paragraphs or 
  body elements, indented relative to the 
  term. Blank lines are not allowed 
  between term and definition.

  :Authors: 
    Tony J. (Tibs) Ibbs, 
    David Goodger
    (and sundry other good-natured folks)

:Version: 1.0 of 2001/08/08 
:Dedication: To my father.

-a            command-line option "a" 
-b file       options can have arguments 
              and long descriptions 
--long        options can be long also 
--input=file  long options can also have 
              arguments 
/V            DOS/VMS-style options too

| Line blocks are useful for addresses, 
| verse, and adornment-free lists. 
| 
| Each new line begins with a 
| vertical bar ("|"). 
|     Line breaks and initial indents 
|     are preserved. 
| Continuation lines are wrapped 
  portions of long lines; they begin 
  with spaces in place of vertical bars.

  Block quotes are just:
    Indented paragraphs,

        and they may nest.

Doctest blocks are interactive 
Python sessions. They begin with 
"``>>>``" and end with a blank line.

>>> print "This is a doctest block." 
This is a doctest block.

Grid table:

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+

Grid table:

Header 1	Header 2	Header 3
body row 1	column 2	column 3
body row 2	Cells may span columns.
body row 3	Cells may
span rows.	
Cells
contain
blocks.
body row 4
Simple table:

=====  =====  ====== 
   Inputs     Output 
------------  ------ 
  A      B    A or B 
=====  =====  ====== 
False  False  False 
True   False  True 
False  True   True 
True   True   True 
=====  =====  ======

A transition marker is a horizontal line 
of 4 or more repeated punctuation 
characters.

------------

A transition should not begin or end a 
section or document, nor should two 
transitions be immediately adjacent.

External hyperlinks, like Python_.
.. _Python: http://www.python.org/

External hyperlinks, like `Python 
<http://www.python.org/>`_.

Internal crossreferences, like example_.
.. _example:

This is an example crossreference target.

Python_ is `my favourite 
programming language`__.
.. _Python: http://www.python.org/

__ Python_