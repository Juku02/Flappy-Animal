from configparser import ConfigParser
import yaml

class Parser(ConfigParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def read_yaml(self, file_path):
        with open("flappy_animal/config/" + file_path, 'r') as file:
            config_dict = yaml.safe_load(file)

        for section, options in config_dict.items():
            self.add_section(section)
            for option, value in options.items():
                self.set(section, option, str(value))

    def write_yaml(self, file_path):
        with open("flappy_animal/config/" + file_path, 'w') as file:
            config_dict = {}
            for section in self.sections():
                config_dict[section] = {}
                for option, value in self.items(section):
                    config_dict[section][option] = value
            yaml.dump(config_dict,file,default_flow_style=False)