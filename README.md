Princess Print: For Pretty Printing and the Pretty Princesses Who Print Pretty Things (Prettily)

(Written in Python 2.7)

You're living your busy life as a Princess, (you know, coding and stuff) when suddenly you need to print something! [Audience: OH NO!]
You could json.dumps(), but it still looks all gunky [Audience: Ewwww...], and other pretty printers require PARAMETERS before it'll print ANYTHING. [Audience: GASP!]
With Princess Print you can simply throw any dictionary, list, string, integer, or nested combination thereof directly into the pripri() function and have it spit out something any citizen of your empire could read. [Audience: YAAAAY!!]

How to be a Princess:
* Import your file: probably like "pp=__import__('princess_print')" or something.
* Princess Print your data: maybe "pp.pripri(FOO)" where FOO=['lists','of','junk','but','also',{'dict':'works','and':'nested','items':['like','this']}]
* If you'd like certain keys to be printed first, pass them as a list after your data: pp.pripri(FOO,['items','dict']) will print "items", then "dict", then anything else in your dictionary.
* Non-default number of columns: The default is three (3), but pass a number as the third argument if you would like to override this parameter. (This has not been tested and only really affects printing lists at the moment.)
* Let them eat cake: Princess Print functions recursively in order to handle any depth of nesting you can conjure. Consequently, if you care about things like "overhead" or "not using all of the RAM" this may not be the printing library for your empire, and you should just write your own iterative function to print your data. If, like me, you don't have the time or inclination to care about the exact nature of your data and you just want to print *all of it* in a single go without having to put forth any effort, then you should probably grab that little '.py' file up there.

Criticism is welcome! Let me know what you think and if you encounter anything you especially like or dislike!
