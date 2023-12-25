# Integration

    *****************************************************
    *                                                   *
    *     Report of Computer and programming project    *
    *                                                   *
    *****************************************************

                Numerical Integration

-------------------------------------------------------------

 - First Part : The C++ program

-------------------------------------------------------------

When you have ask the project, you have asking on the C++ language
I know just bases on C++ so I have create my numerical integration program
to be the easiest posible.

1. The user should make his function to integrate in the first function of the program
2. The user should determinate the integration range
3. The user can also change the number of integration part

For exemple -> 
    float f(float x)
    {
        return 1-x*x; // Make your own function here
    }

    int main()
    {
        int n = 1000; // Put your own number of integration part
        float x_min = -1; // Put your own minimal range 
        float x_max = 1; // Put your own maximal range
        ...
        ...
        ...
    }

4. The user should compile the program
5. Execute the program
6. And now have the result of the integration


-------------------------------------------------------------

 - Secund Part : The python program

-------------------------------------------------------------

The python program is a little bit complicated because I have better skills in python.
The project is organized on a folder.

> Integration 
    > __pycache__   // it's a folder where create by python at each running
    - __main__.py   // the main file
    - Classe.py     // the file which groups all the classes
    - Fonction.py   // the file wich groups the functions
    - icone.ico     // the icone of the window application
    - Parameter.py  // the file wich groups the parameters of the program
- Integration.bat   // the file to execute the application

So, to open the application, you have just to open the Integration.bat file.
You can also open this application with the cmd before the folder Integration
with the command : python -m Integration

On the first page, you can add your function with the kayboard matrix (an automatic function
transform your function on a function which can understand by the cumputer)
Dont forget to put 'x' for the paramiter.
you should parameter the integration range in the two entry zone (it's impossible to write an other 
entry as a decimal number)

On the secund page, you have the function draw on a figure and the result of the numerical integration.

For more information, please contact me
+33 7 68 02 46 86
corentin.roche@insa-cvl.fr
