from trumania.core import circus

example_circus = circus.Circus(name="example1", 
                               master_seed=12345,
                               start=pd.Timestamp("1 Jan 2017 00:00"),
                               step_duration=pd.Timedelta("1h"))
