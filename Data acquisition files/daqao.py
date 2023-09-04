# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:15:23 2016
Python3 update v0 Tue Mar 27 2018

@author: lcfl72
"""

import PyDAQmx as daq
import numpy as np

    
def DAQmx_WriteSingleAO(chan='Dev1/ao0', val=0.0, vmin=0.0, vmax=5.0):
        
    written = daq.int32()
    npval = val * np.ones(1)
    
    ao = daq.Task()
    ao.CreateAOVoltageChan(chan, "", vmin, vmax, daq.DAQmx_Val_Volts, None)
    ao.StartTask()
    
    ao.WriteAnalogF64(1, True, 0, daq.DAQmx_Val_GroupByScanNumber,
                      npval, written, None)
    
    ao.StopTask()
    ao.ClearTask()
    
    
def DAQmx_WriteAO(task, chan, vals_ndarray): #NOT TESTED
    
    ao = daq.Task()
    ao.CreateAOVoltageChan(chan, "", 0.0, 5.0, daq.DAQmx_Val_Volts, None)
    ao.StartTask()
    
    written=daq.int32()
    ao.WriteAnalogF64(1, True, 0, daq.DAQmx_Val_GroupByScanNumber, vals_ndarray, written, None)
    
    ao.StopTask()
    ao.ClearTask()
   

if __name__ == '__main__':
    DAQmx_WriteSingleAO(chan='Dev1/ao0',val=0.0)

