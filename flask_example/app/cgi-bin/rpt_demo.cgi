#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
@app.route('/app/cgi-bin/rpt_demo.cgi')
def run_experiment:
    #import experiment_runner
    #experiment_runner.runExperiment("demo", "/cgi-bin/sequence.txt", "/cgi-bin/english.txt", disableRefresh=False)        
    return 'Hello you made it!'

    
