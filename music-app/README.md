# Music App

The Python program you are asked to implement is a music application, which takes two files as input, which content is correct (no errors in the files). 

**Music.dat** : this file contains records about music songs. Each record is composed of the following fields:

```
song name; artist or group; genre 1; genre 2; ...; genre N
```

where the song name and the artist or group are strings, including spaces, and genres and strings composed of a single word. A song may belong to many genres, which number is not known in advance.

**Users.dat** : this file contains records about the users of the app. Each record is composed of the following fields:

```
name and surname; preferred genre 1; preferred genre 2
```

where each user has exactly two preferred genres. 

The Python program associates and prints to screen every user the list of songs according to the user's genre preference; moreover the songs suggested to each user must be printed after teh name and surname (see the example bellow).

Songs with preferred genre 1 should be listed before songs in the preferred genre 2. A song cannot be displayed more than once for a single user. The output for each preferred genre must be in alphabetic order. 

Per every user, the output message format is the following:


```
User name and surname, number of songs: Rooz, 5 songs
   - Black Hole Sun
   - Come as You Are
   - Just
   - Flying
   - Lithium
```
