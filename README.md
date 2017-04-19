# ESCI8980_Assignment2

#### Assignment includes all inputs for final Age Calculation function, to be completed as final project


Assignment includes files agecalc.py, isocalc.py, isofilter.py, test.py, and accompanying Excel files. 
Shown below are the divisions of each file: 



##### isofilter.py
---------
Requires openpyxl and numpy.
* class IsoFilter(): requires filename, columnletter, and filternumber inputs.
Calculates mean, standard deviation, and total counts of filtered and unfiltered data.

  * def getMean(): calculates mean of unfiltered data
  * def getStanddev(): calculates standard deviation of unfiltered data
  * def getCounts(): calculates counts of unfiltered data
  * def Filtered_mean(): filters data depending on criteria and calculates resulting mean
  * def Filtered_err(): filters data dpending on criteria and calculates resulting 2s error
  * def Filtered_counts(): filters data dpending on criteria and calculates resulting counts

* class chem_blank(): requires filename, columnletter, and isotope analyzed. 
Calculates mean, counts, and relative 2s error for chemistry blanks, for use with Age Calculation. 

  * def calc(): calculates and returns list of mean, counts, and relative 2s error for specified isotope


##### isocalc.py
--------
Requires isofilter, numpy, and pandas.
* class Ucalculation(): requires spike used, abundance sensitivity, U filename, and printing option. 
Calculates ratios and cps values from U run needed for use in Th and Age Calculation functions. 

  * def U_normalization_forTh(): calculates and returns list of measured 236/233 ratio and error, normalized 235/233 ratio and error, and corrected 236/233 ratio and error, for use in Th function. 
  * def U_normalized_forAge(): calculates and returns list of normalized 235/233 ratio and error, 234/235 normalized and corrected ratio and error, unfiltered cycles of 233 and filtered cycles of 234/235, and unfiltered mean of 233, for use in Age Calculation function. 

* class Thcalculation(): requires spike used, abundance sensitivity, Th filename, printing option, and U_normalized_forTh() output. 
Calculates ratios and cps values from Th run needed for use in Age Calculation function.

  * def Th_normalization_forAge(): calculates and returns a list of corrected and normalized 230/229 ratio and error, corrected and normalized 232/229 ratio and error, and unfiltered mean and cycles of 229, for use in Age Calculation function. 
  
* class background_values(): requires U wash file, Th wash file, and printing option.
Calculates wash values for use in Age Calculation function.

  * def U_wash(): calculates and returns list of 233, 234, and 235 wash values in cps for use in Age Calculation function. 
  * def Th_wash(): calculates and returns 230 wash value in cpm for use in Age Calculation function.

* class chemblank_values(): requires spike used, chem spike weight, wash and run files for U, wash and run files for Th, printing option, and filename if you desire to export your chem blank values to an Excel spreadsheet. 
Calculates chem blank values for use in Age Calculation function, and gives you the option to export your chem blank data into Excel format for your own use.

  * def blank_calculate(): calculates and returns a list of 238 chem blank value and error in pmol, 232 chem blank value and error in pmol, and 230 chem blank value and error in fmol, for use in Age Calculation function. If you have requested to export your data, it creates and Excel spreadsheet with data for your 230 value and error in ag, 232 value and error in fg, 234 value and error in ag, 235 value and error in fg, and 238 value and error in fg. 
 

##### agecalc.py
--------
Requires isocalc

  * def Age_Calculation(): requires U and Th run and wash files for sample, U and Th run and wash files for chem blank, abundance sensitivity, sample weight, spike weight, spike weight for chem blank, spike used, and printing option. Currently Age Calculation function contains all input values, but does not calculate age, as of 4/19/17. 
  
  
##### test.py
--------
Requires agecalc
Includes code to run Age Calculation function with given Excel files. Age_Calculation parameters have been included, and should look like the following: 

```
import agecalc

agecalc.Age_Calculation('72U_011517.xlsx', '72Th_011517.xlsx', '72U_wash_011517.xlsx', '72Th_wash_011517.xlsx', 
                '71U_chemblank.xlsx', '71Th_chemblank.xlsx', '71U_chemblank_wash.xlsx', '71Th_chemblank_wash.xlsx', 
                6E-7, 0.1, 0.1, 0.0026,
                'DIII-B', inquiry_input)
```
                

Run in command line after importing the isofilter, isocalc, and agecalc. Print "y" on printing option prompt to see resulting analysis.          
  


