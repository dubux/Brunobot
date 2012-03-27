class BrunobotConfig():
    cfgfile = 'config.conf'

    def __init__(self):
        import ConfigParser
        self.config = ConfigParser.SafeConfigParser(allow_no_value=True)
        self.load()

    def get(self, section, variable):
        try:
            return self.config.get(section, variable)
        except:
            return None

    def set(self, section, variable, content=None):
        if content:
            self.config.set(section, variable, content)
        else:
            self.config.set(section, variable)

        self.save()

    def rem(self, section, variable):
        self.config.remove_option(section, variable)
        self.save()

    def load(self):
        self.config.read(self.cfgfile)

    def save(self):
        with open(self.cfgfile,'wb') as configfile:
            self.config.write(configfile)

    def list(self, section):
        return [key for (key,value) in self.config.items(section)]
    
    def printConfig(self):
        print " .. Configuration [connection]"

        if self.get('connection', 'host'):
    	    print " ..    ip address: %s" % (self.get('connection', 'host'))
        
        print " ..        server:   %s (%s)" % (self.get('connection','server'),self.get('connection','port'))
        print " ..          nick:   %s (%s, %s)" % (self.get('connection','nick'),
                                            self.get('connection','ident'),
                                            self.get('connection','name'))
        print " ..      channels:   %s " % ", ".join(self.list('channels'))
        print " .."
        print " .. Configuration [module]"
        print " ..  max_run_time:   %s" % (self.get('module','max_run_time')) 
        print " ..        prefix:   %s" % (self.get('module','prefix')) 
        for module in self.list('modules'):
            print " ..        module:   %s" % module
        print " .."
        print " .. Configuration [owners]"
        for owner in self.list('owners'):
            user, ident, host = owner.replace(' ','').split(',')
            print " ..         owner:   %s!%s@%s" % (user, ident, host)
        print " "


#cfg = BrunobotConfig()
#cfg.load()
#print cfg.get('connection','nick')
#cfg.add('modules','extra','test')
#cfg.set('modules','cmdtest')
#cfg.rem('modules','cmdtest')
#print cfg.list('channels')
#print cfg.list('modules')

#cfg.save()
