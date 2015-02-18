# Librarian

The purpose of this library is to "democratise data" either in a company or for clients.

Often we wish to allow people to access our data who don't need or want to know where it comes from or the best
way to access it.  The easier the process of getting data can be the more people will do with the data.

As such the module makes a number of design decisions focussed on easy of use over efficiency or pure design beauty:

  1) Using Python over a type safe language
  
  2) Limiting the externally facing API to just a single module
  
  3) Encapsulating the class structure away from the end user
  
  4) Having a functional layer of pre-defined functions to be customised for the situation
  
However, I have also tried to make the back end well designed, robust and extensionable.

There are two main types of classes:

  1) DataState - represents either abstract or concrete data values
  
  2) Extractors - represent a place in memory (either hypothetical or real)
  
The relationship between them can be roughly viewed as container (Extractor) and content.  Data sits in the place in memory and can be extracted out.

Extending:

The module is at the moment just a proof of concept as is limited to file system and FTPS.  However, it is very much designed to be extended to fit whatever needs.  This comes in two types

  1) Application of already existing Extractors:
  
      To make the process of extracting data as easy as possible, the interpreter script is populated with ready to use            functions and lists of functions to be plugged into the main function
      
      New functions and lists of functions should be created here for people to use.  A good example of this is the                "store_or_ftp" list in there as default which first checks the local file system and then looks in an FTP
      
      
  2) Adding new Extractors:
  
      Data comes from more places than just file systems and FTP, so the ability to add new extractors is key.
      
      To this end, there is a BaseExtractor ABC(abstract base class) to provide a template.  Simply subclass this like the         file system and ftp classes do and then the new class can be used immediately.  

Future Additions:

The mean functionality yet to be added is to use the as yet unused Insterers.  The idea is that repeatedly pulling the same file from a server is a waste of everyone's resources.  Better to have an optional archiveMode in which all new files downloaded and stored in the base location (normally file system) so that on subsequent occasions they can be pulled straight from there. 
