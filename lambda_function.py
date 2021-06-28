import pyjokes

def lambda_handler(event, context):
    print(pyjokes.get_joke())
    return "Ramon"
