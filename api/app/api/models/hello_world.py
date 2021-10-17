from flask_restx import fields


class HelloWorldDTO:

    response = {
        'message': fields.String(description='The message')
    }
