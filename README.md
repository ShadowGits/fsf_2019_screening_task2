  Steps to run this application :

1)Install Python(3.6) and PyQt5 and other dependencies with the given command

'pip install -r requirements.txt' (Add requirments.txt to the project folder)
         

Name of Application : Data Handler And Plotter

Features:

Data Window : Base window for displaying data in tabular view

1) File Menu:

      a) Load : Loads a csv file into a tabular view
      
      b) Save : Helps to save .csv files
      
      c) Save Plots : Saves plots without displaying plots as a png file , with a dialog box for selected coloumns
      
	        i)   Save_Scatter_Points : For saving a scatterplot
          
         ii)   Save_Scatter_Points_Lines : For saving a scatterplot with smoothlines
         
	       iii)  Save_Lines : For saving a plot with lines
         
      d) Add Data
      
         i) Add Row : Add extra row at the end
         
         ii) Add Column : Add extra col at the end 

      e) Clear : Clear data from the window
      
      f) Quit : exit from the window 

2) Edit Menu:

      a) Edit Data : Helps to make loaded data editable by double clicking

3) Remove Data Pushbutton 
      
         i) Delete Row : remove the selected row 
         
         ii) Delete Column : remove the selected col
         
4) Scatterplot pushbutton:
	Generates a new window which has the following:
  
	a) Reverse : Plots a new graph swapping X and Y respectively
  
	b) Save as png : opens a dialog box for location to save the plot
  
5) Scatterplot with smooth lines pushbutton:
   Generates a new window which has the following:
   
	a) Reverse : Plots a new graph swapping X and Y respectively
  
	b) Save as png : opens a dialog box for location to save the plot
  
6) Scatterplot with lines pushbutton:

	Generates a new window which has the following:
  
	a) Reverse : Plots a new graph swapping X and Y respectively
  
	b) Save as png : opens a dialog box for location to save the plot

Error Handlers : Integrated every handling for errors that can be commited during plotting 

	a)If user selects more than two coloumns 
  
	b)If user selects invalid coloumn i.e maybe character data for plotting
