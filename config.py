'''
Connection variables
'''
nick    = 'brunbot2'
ident   = 'botvz'
name    = 'brunobot'
server = 'efnet.port80.se'
#server  = 'holmes.freenode.net'
channel = '#brbot'
port    = 6667

'''
User config
'''
owner = [['vz', '~vz', 'veiset.org']]

#admin = [['*', '*', 'veiset.org']]


'''
Modules
'''
core = True 
modules_extra = ['typofixer']
modules_plugin = []


command_prefix = "."


''' 
Advanced config. Do not touch unless you are
100% sure what you are doing. If you think 
you know, then you don't. So don't break anything
here.
'''

userhost = lambda a,b,c: a+"!"+b+"@"+c
