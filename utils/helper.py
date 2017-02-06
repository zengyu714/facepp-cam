# define helper functions

def print_result(hit, result):
    from pprint import pformat

    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))

# speak pre-defined results in res file
def play_music(file_name):
    import pygame as pg

    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get right sound)
    pg.mixer.init(freq, bitsize, channels, buffer)

    pg.mixer.music.load(file_name)
    pg.mixer.music.play()

def init():
    with open('../api_key.config','r') as f:
        for line in f:
            if line:          # skip blank line
                exec(line)

    srv = locals().get('SERVER')
    API_KEY = locals().get('API_KEY')
    API_SECRET = locals().get('API_SECRET')

    from facepp import API
    return API(API_KEY, API_SECRET, srv = srv)
