try:
    from mywebsite import app
    from flask import render_template
except Exception as e:
    print("Modules are Missing : {} ".format(e))

