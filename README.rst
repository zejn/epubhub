
ePubHub
=======

This is a small Django e-bookshelf app. It has three main features:

 - it can convert from another format to .mobi (using Calibre),
 - it stores ebook collections in ZIP archives for easier management and
 - it provides search over the names of the files contained in archives.


Archives should be dropped into data folder. To index them and make them
findable, run:

::

  ./manage.py epubhub_reindex <zipfile.zip>


That's about it.




