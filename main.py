# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import Flask
data_one = 23
app = Flask(__name__)
@app.route("/")
@app.route("/home")

def Home():
    return render_template("README.md")

if __name__ == '__main__':
    app.run(debug= True,port=5001)
#data_one = 23
#print(data_one)
