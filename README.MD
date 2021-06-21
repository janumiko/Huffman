## Huffman coding encryptor 
Single python program which encodes input given by user using Huffman algorithm.  [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)

How to use:
install python3 and virtual environment of Your choice, for example virtualenv.

Enter into virtualenv and install dependencies from requirements.txt
```
pip install -r requirements.txt
```

Execute the run.py in main folder of the project.  
```
python run.py
```
Type in text which you want to encode.  
Results should have been printed out. 
You will be asked if you want to save output to a file.  
If you agreed, results will be saved in text file in directory called "output" inside main directory.  
Press enter to exit from the program.  

# Testing
You need to install required dependencies from requirements.txt. 

To test the program enter into your project virtual enviroment.  

And type:
```
pytest
```
You should see results of pytest tests.  

To change or add additional tests for the program, make a file in tests directory.  
I created some tests already, which are located inside tests folder.