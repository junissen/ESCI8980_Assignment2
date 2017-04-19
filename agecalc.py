#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Age Calculation function to analyze U-Th data using an MC-ICP-MS. 

Created by Julia Nissen, 2017, for use in Edwards' Isotope Lab.
"""

import isocalc

inquiry_input = raw_input("Would you like to print as you go? [y/n] : ")

def Age_Calculation(U_file, Th_file, U_wash, Th_wash, 
                    U_chemblank, Th_chemblank, U_chemblank_wash, Th_chemblank_wash, 
                    AS, sample_wt, spike_wt, chem_spike_wt, 
                    spike_input, inquiry_input):
    
    chemblank_inquiry = raw_input("Would you like to export your chem blank values? [y/n]: ")
    
    if str(chemblank_inquiry.lower()) == 'y':
        question2 = raw_input("What file would you like to write to (please include type, i.e. '.xlsx')?: ")
        chemblank_filename = str(question2)
    else: chemblank_filename = False    
    
    wb_1 = isocalc.Ucalculation(spike_input, AS, U_file, inquiry_input)
    
    a = wb_1.U_normalization_forTh() #provides a list to use in Th normalization

    b = wb_1.U_normalization_forAge() #provides a list to use in Age calculation

    wb_2 = isocalc.Thcalculation(spike_input, AS, Th_file, inquiry_input, a)

    c = wb_2.Th_normalization_forAge() #provides a list to use in Age calculation

    wb_3 = isocalc.background_values(U_wash, Th_wash, inquiry_input)

    d = wb_3.U_wash() #provides a list of 233, 234, 235 wash values to use in Age calculation

    e = wb_3.Th_wash() #provides the 230 darknoise cpm to use in Age calculation
    
    wb_4 = isocalc.chemblank_values("1H", chem_spike_wt,
                                            U_chemblank_wash, Th_chemblank_wash, 
                                            U_chemblank, Th_chemblank, inquiry_input, chemblank_filename)
    f = wb_4.blank_calculate() #calculates chem blanks

    #Age Calculation function has been completed up to the inputs. Actual age calculation will be completed for final 
    #project.

