imgmatch
========

A Python/Imagemagick utility for reuniting identical but misnamed images
------------------------------------------------------------------------

### This is designed for one-to-one matches of files in two groups that can be identified by Regex matching their filenames. It is likely a useful start for other, similar problems.

*Requirements*
+ Requires [Imagemagick](http://www.imagemagick.org/), probably at least version 6.8 
+ Original application only involved .png files of identical size; the matching uses the identify command's signature field, so you may want to [check other file types](http://www.imagemagick.org/script/identify.php)
+ Creating the output matching csv may require permissions

*Usage*
+ Pass two or three arguments: the location of the files, the regex for list A, and, optionally, the regex for list B
` python imgmatch.py filedir exp1 exp2 `

