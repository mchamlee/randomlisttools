# randomlisttools

A collection of, well, *random list tools*. Some are useful, some were personal challenges, others were just fun
to create.

If you *randomly* found your way here, congrats, I think. Review the code, feel free to take anything you find useful,
let me know what you like, and if you feel the need share what you think could be improved and why.

My documentation is simple right now. I have plans to enhance it with Sphinx or reStructured Text.

---

## stringparse

#### ConsecutiveChars:
Accepts a list of strings, 1-n members. All strings must be the same length.
> `ConsecutiveChars(['abXyz', 'befgh', 'cFvwX', 'DGjhY'])`

`get_parsed_list()`: Returns the parsed list, as a list object.
> `ConsecutiveChars(['abXyz', 'befgh', 'cFvwX', 'DGjhY']).get_parsed_list()`

`get_printed_list()`: Returns the parsed list, printed to the console/terminal.
> `ConsecutiveChars(['abXyz', 'befgh', 'cFvwX', 'DGjhY']).get_printed_list()`

Can be called from a Terminal. Accepts a list of strings or a file containing a list of strings.
> `python stringparse.py ConsecutiveChars "abXyz,befgh,cFvwX,DGjhY"`
>
> `python stringparse.py ConsecutiveChars ..\tests\test_files\array_of_strings.txt`