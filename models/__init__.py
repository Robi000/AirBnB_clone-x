from .engine.file_storage import FileStorage
storage = FileStorage()
x = storage.reload()
print(x)
