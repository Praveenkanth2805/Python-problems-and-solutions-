class bike():
    def key_on(s):
        print("key on")
        s.start_bike()
    
    def start_bike(s):
        print("bike going to start")
        s.start_engine()
        
    def start_engine(s):
        print("engine started")
        print("bike started")
        
b=bike()
b.key_on()


