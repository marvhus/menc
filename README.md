# MENC
## Short for "Martin's Encryption"

This is something I made for fun.

It encrypts the given text where the output is a given string, and you get given a key that you keep private.
Since the output can be the same for multiple inputs it makes it unbreakable/uncrackable

Have fun! :)

----

# Usage

----

## menc.py
Ways you can utilize this.

### Unique key, and unbreakable

-iT "Hello"  
the text to be encrypted

-oT "World"  
the encrypted output text

### Shared password, and secure, but not unbreakble (it could be brute forced)

-iT "Hello"  
the text to be encrypted

-oT "World"  
the password

----

## mdenc.py
Whays you can utilize this

### Unique key, and unbreakable

-eT "World"  
the encrypted text

-eK "0F0A060054"  
the encryption key

### Shared password, and secure, but not unbreakable (it could be brute forced)

-eT "World"  
the password

-eK "0F0A060054"  
the data to be decrypted

----
