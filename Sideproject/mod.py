from flask import Flask  
      
app = Flask(__name__) #creating the Flask class object   
# The route() function of the Flask class defines the URL mapping of the associated function. The syntax is given below    
@app.route('/') #decorator drfines the   app.route(rule, options)  
def home():  
    return "<h1>hello, this is our first flask website</h1>";  
      
if __name__ =='__main__':
    # app.run(host, port, debug, options)  
    app.run(debug = True)  
# 1 	host 	The default hostname is 127.0.0.1, i.e. localhost.
# 2 	port 	The port number to which the server is listening to. The default port number is 5000.
# 3 	debug 	The default is false. It provides debug information if it is set to true.
# 4 	options 	It contains the information to be forwarded to the server.  