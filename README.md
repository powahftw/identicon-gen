## Example

![example](http://i.imgur.com/wFrRbQ1.jpg)

# identicon-gen
Create Identicon like images.
The script is now randomly driven for placing blocks and doesn't produce the same result each time.
If the option to use a STRING as input is True then you always get the same RGB Color. 
In the future i'm planning to extend the input to predetermine the pattern so that both the color and the figure will be the same for a given string each time.

```
python identicon.py
```

### Prerequisites

This script make uses of the Python Imaging Library.

There are a few settings you can play with

```
N_CHUNK is the number of pixel block for each row/column | Default is 5
BORDER is the distance it keep from the margin of the picture | Default is 20
SIZE is the dimension of the image (SIZE*SIZE) | Default is 420 (No pun intended, it's the one github uses)
PLACE_PROBABILITY is the probability a block get colored | Default is 0.5 (Half the times) 
COLOR pick a random color from a set of RGB values
STRING if the option is active then it will determine the color of the final sprite
```

### Other Examples

Playing with settings can achive result like this 

![example](http://i.imgur.com/QYzlcZP.png)


