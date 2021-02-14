# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 01:00:44 2020

@author: Nikita
"""

import AccurateTime
import inspect

def benchmark(function, trials : int , import_name : str = None, 
              obj : object = None, **kwargs) -> None:
    """
    Parameters
    ----------
    function : function name
        The function to be benchmarked.
    
    import_name : str, optional
        The name of the module that should be imported before running the rest
        of the code. The default is None : str.
 
    trials : int
        Number of calls to be made to function
    **kwargs : all
        Should be the parameters you wish to call the function with.

    Raises
    ------
    AttributeError
        If the attribute required for the function call is not present,
        this error gets raised. 
    """
    if (import_name):
        exec("from " + import_name + " import Solution")
        
    function_params_count = function.__code__.co_argcount
    function_vars = function.__code__.co_varnames
    function_name = function.__qualname__
    function_call = (function_name + "(")
    for i in range(function_params_count) :
        if (kwargs.get(function_vars[i])):
            function_call += (function_vars[i] + " = " + 
                              str(kwargs.get(function_vars[i])) + "," )
        else : 
            raise AttributeError("Function misses required argument '" + 
                                 str(function_vars[i]) + "'")
    function_call = function_call[:-1] + ")"
    
    # Benchmark
    first_part = """
total = 0
for i in range({}):
    begin = AccurateTime.micros()
"""
    second_part = """ 
    end = AccurateTime.micros() - begin
    total += end
print ("Total time spent in function for " + str(trials) + " trials : "    
           + str(total/10**6) + " seconds.")
print("On average, each call took " + 
          str(total/(trials*10**6)) + " seconds.")
    """
    exec(first_part.format(trials) + 
         "\n    " + function_call + "\n" + 
         second_part)