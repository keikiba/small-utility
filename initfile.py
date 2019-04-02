import configparser
import os.path

class ConfigInit:
    default_section_name = 'DEFAULT'

    def __init__(self, program_name, fn):
        self.inifile = fn
        self.program_name = program_name
        self.conf = configparser.ConfigParser()

        if os.path.isfile(self.inifile) or os.path.islink(self.inifile):
            self.conf.read(self.inifile)
            for k in self.conf:
                # Set name in all sections
                self.conf[k]['program_name'] = self.program_name
        else:
            raise FileNotFoundError
    
    def get_section(self, section):
        if section in self.conf:
            return self.conf[section]
        else:
            return {}

    def get_default(self):
        return self.get_section(self.default_section_name)


def test_main():
    ini_file = "test.ini"
    try:
        ini = ConfigInit("TEST", ini_file)
    except FileNotFoundError as e:
        print( f"file not found: {ini_file}" )
    else:
        d_section = ini.get_default()
        print("keys/values in DEFAULT section")
        print( f"  File: {d_section['file']}" )

        l_section = ini.get_section('LOG')
        print("keys/values in LOG section")
        for k in l_section:
            print(f"  {k}: {l_section[k]}")


if __name__ == "__main__":
    test_main()
