# file: runme.py

# Try importing the Compiled C++ extension modules.
# This will try windows first, before trying to load the Linux modules.
try:
   import fibw as fib
except:
    try:
        import fibl as fib
    except:
        print("Error Loading Extension Modules")

# Import the Flask API modules.
from flask import Flask, request,jsonify, render_template

# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
TEMPLATES_AUTO_RELOAD = True
app.logger.info

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/fib", methods=['GET'])
def calc():
    value = request.args.get("n")
    try:
        value = int(value)
        if value >= 0:
            arr = []
            for i in range(0,int(value)):
                if value <= 1475:
                    arr.append(round(fib.Fibonacci(i)))
                else:
                    arr.append(fib.Fibonacci(i))
        result = {"Result":"Success","Value": arr}
        
    except:
        result = {"Result": "Error!","Details":"Improper Input ASCI Character or Negative Integer!"}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
    
    
