# encoding: utf-8

import ConfigParser

class Config():

    def __init__(self, env, servername):
        self.env = env
        self.servername = servername
    
    def load(self):
        print self.env
        config = ConfigParser.SafeConfigParser()
        config.read('setting_' + self.env + '.prop')
        for section in config.sections():
            if section == self.servername:
                self.ip = config.get(section, 'ip')
#                 for option in config.options(section):
#                    print config.get(section, option)
                break
        api_config = ConfigParser.SafeConfigParser()
        api_config.read('api.prop')
        print api_config.items("id1")[0]
        b =     api_config.items("id2")
        for key in b:
            if key[0] != 'uri':
                print key[0]
                print key[1]
#            help(key)

if __name__ == '__main__':
    print "load config file ..."
    c = Config("stg", "stg-api-app01")
    c.load()
    print c.ip
#    print c.env
    