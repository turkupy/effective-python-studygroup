**1. What's a character encoding?**

It’s a way of translating characters (such as letters, punctuation, symbols, whitespace, and control characters) to integers and ultimately to bits. 
In ASCII, letter S is represented as 19, a question mark is 63 and number 6 is 54. Using bits, those would be 0010011, 0111111, 0110110.

**2. What's ASCII?**

It's a character encoding standard that contains 128 characters (numbers, letters from the English alphabet, special characters). 
The ASCII table only requires 7 bits (2^7=128). And because modern computers store data in 8 bits (or 1 byte), this means that the ASCII table is half empty (2^8=256). 
The ASCII table was extended to hold 128 additional characters, but it didn't work well since no one agreed to what characters would be included. E.g. integer 130 could correspond to letter é, but in Israel it would map to some Hebrew letter. This means ASCII didn't work well if you wanted to use something other than English. 

**3. What's Unicode?**

Unicode is a standard used for encoding, representing and handling text that includes most of writing systems. Compared to ASCII it works in a slightly different way: while in ASCII a letter or character was mapped to some bits, in Unicode those are mapped to a codepoint. The codepoints in Unicode use hexadecimal numbers (to keep them short) and look like this: U+00639

**4. What are UTF-8, UTF-16 and UTF-32?**

Because computers use bytes to store data, Unicode codepoints need to be encoded into bytes. UTF-8, 16 and 32 are all encoding standards that use Unicode characters. The difference is in the amount of bytes used for encoding those codepoints. 
UTF-8 can use 1, 2, 3 and 4 bytes to encode the codepoints. It is compatible with ASCII, since ASCII also uses 1 byte to encode characters. To encode non-English characters, UTF-8 will just use more than 1 byte to do it. 
UTF-16 uses 2 and 4 bytes for encoding. It is works very well for many non-English characters (for example Asian characters) because it will use 2 bytes per each character. It is better to use UTF-16 when dealing with text written in Chinese, for example, because UTF-8 will use 3 or more bytes for those higher order characters. 
UTF-32 uses 4 bytes and can encode any Unicode character in the world. It will use a lot of memory, so it's not recommended to use it. 

**5. Wait... what is encoding and decoding again?**

To encode a character is to convert the unicode codepoints to bytes.
To decode is to convert bytes to unicode codepoints. 
Encoding and decoding usually happen when reading files and converting its content into strings.

**6. How does Python handle Unicode?**

Python2 is a bit of a mess because 'str' stores bytes and 'unicode' stores unicode code points. Default encoding for 'str' is ASCII. This works fine for English texts, but reading a file with Cyrillic characters requires decoding it first. 
Python3 works differently. 'str' now stores unicode codepoints. To store strings in files Python3 uses bytes and the default encoding is UTF-8. 
Beware that Python assumes that files and code you generate are encoded with UTF-8. Most data these days is encoded with UTF-8, but you should check the encoding when working with external files. 

Here is a small example that shows what happens when we don't use the right encoding:
```
my_str = 'mila'
my_str_bytes = mystr.encode('utf-8')
my_str_unicode = my_str_bytes.decode('utf-8')
print(my_str_unicode) # returns 'mila'

my_str_new = my_str_bytes.decode('utf-16')
print(my_str_new) # returns '業慬', oops!
```

**More examples can be found from these great sources:**

https://realpython.com/python-encodings-guide/#one-byte-two-bytes-three-bytes-four
http://kunststube.net/encoding/
https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
https://towardsdatascience.com/a-guide-to-unicode-utf-8-and-strings-in-python-757a232db95c
 
