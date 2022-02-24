import json
"""this module will save load and give anything   
    """


class FileStorage:
    """this is the main main class resposninle for save and load

    Returns:
        none : none 
    """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """thiis return __ obj to consule 

        Returns:
            dict: this will return obj
        """
        # print(self.__objects)
        return FileStorage.__objects

    def new(self, obj) -> None:
        """this will add new object to __objects 

        Args:
            obj (obj)
        """
        #print("*****>", obj.id, "passed here")
        x = "{}".format(obj.__class__.__name__ + "." + obj.id)
        self.__objects[x] = obj
        # print(self.__objects)

    def save(self) -> None:
        """this will save the lodded object ist to json file 
        """
        with open(self.__file_path, 'w') as f:
            # print(json.dumps({k: v.to_dict()
            #  for k, v in self.__objects.items()}))
            json.dump({k: v.to_dict()
                      for k, v in self.__objects.items()}, f, indent=2)
        # with open(self.__file_path, 'r') as f:
            #print("file is like \n", f.read(), "\n\n")

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        # print('******************')
        try:
            with open('file.json', 'r') as f:
                dict = json.loads(f.read())
                # print('i #print the dict here from file reload ', dict)
                try:
                    for value in dict.values():
                        cls = value["__class__"]
                        from models.base_model import BaseModel
                        from models.user import User
                        from models.amenity import Amenity
                        from models.city import City
                        from models.place import Place
                        from models.state import State
                        from models.review import Review
                        self.new(eval(cls)(**value))
                except Exception:
                    return 'error with the eval'
            return "okay"
        except Exception:
            return "empty file"
