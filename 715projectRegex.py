import pyperclip, re

phoneRegex = re.compile(r'''(
    (\+)?
    (\s|-|\.)?
    (([0]{0,2})*/d{2})?
    (\+)?
    (\s|-|\.)?
    (([0]{1})*/d{2})?
    (\+)?
    (\s|-|\.)?
    (\s|\d{3}}?
    (\s|-|\.)?
    (\s|\d{4}}?
    (\s|-|\.)?
    (\s|\d{4}}?
)'''
, re.VERBOSE)

emailRegex = re.complie(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9]+
    
)'''
, re.VERBOSE)

