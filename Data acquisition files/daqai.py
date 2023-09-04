'''
Python3 update v0 Tue Mar 27 2018
Python3 update v1 Thu Aug 2 2018

'''

import PyDAQmx as daq
import numpy as np


def DAQmx_ReadAI(meas_duration, chanlist='Dev1/ai0', nchans=1, samplerate=10000, vrange=1.0):
    '''
    Read analog input(s) from NIDAQmx device(s). 
        meas_duration is the measurement duration (float, in seconds) for acquisition
        chanlist contains a valid channel, range, or list (string) of DAQmx channels
        nchans is the number of channels to be read (integer)
        samplerate is the data sampling rate in Hz (integer)
        vrange is the voltage range limit (same for each channel, float)
    
    returns numpy array((n_samples. nchans), dtype=float64) of readings.
    '''    
    
    ai=daq.Task()
    
    ai.CreateAIVoltageChan(chanlist, "", # DON'T change these, can change below:
                           daq.DAQmx_Val_Diff, # 
                           #   daq.DAQmx_Val_RSE, # Input coupling: Diff = V+ - V-, RSE = V+ - GND
                           -1.0*vrange, # -10.0 # Min voltage range: -1.0 or -10.0
                           1.0*vrange, # 10.0 # Max voltage range: 1.0 or 10.0 
                           daq.DAQmx_Val_Volts, None) # DON'T change these
        
    N_SAMPLES = int(meas_duration * samplerate)
    timeout = meas_duration + 10.0
    ai.CfgSampClkTiming("", samplerate, daq.DAQmx_Val_Rising, 
                        daq.DAQmx_Val_FiniteSamps, N_SAMPLES) # DON'T change these 
    read = daq.int32()
    SAMPLES = nchans * N_SAMPLES
    AIdata = np.zeros((N_SAMPLES, nchans), dtype=np.float64)
    ai.StartTask()
    ai.ReadAnalogF64(-1, timeout, daq.DAQmx_Val_GroupByScanNumber, 
                       AIdata, SAMPLES, daq.byref(read), None)
    ai.StopTask()
    ai.ClearTask()
    
    return AIdata
 

   
