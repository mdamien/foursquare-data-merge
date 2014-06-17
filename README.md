=== Using the data

Final result is in `data/scored.json` as

  [
    {
      'venue':
          //4sq data ...
      'store':
          //sears data ... [ matching store found for the venue ]
      'analysis':
          //similarity score between the two
          'fq_address': ...
          'sears_address': ...
          'score': similarity score from 0-100 between the two address. If < 90, you should replace the 4sq address is probably wrong
    },
  ]
  
  
=== Generating and playing with the scoring

You can also play with the data to obtain this nice recap:

![run example](https://raw.githubusercontent.com/MDamien/foursquare-data-merge/master/screenshot.png "Example of a `python score.py` run")

Just `pip install fuzzywuzzy` and run `python score.py`

If you want to filter, just pass an expression as a third argument:

`python score.py "0 < score < 70"` to get really bad addresses present in foursquare
