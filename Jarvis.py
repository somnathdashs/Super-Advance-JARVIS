from JarvisHelper import JARVIS_AI

jarvis = JARVIS_AI()

while True:
    command = jarvis.listen()
    if (command):
        jarvis.get_response(command)
    else:
        print("No, command found.")