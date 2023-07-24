import hashlib

filename = "project-238-sonic-picture.jpg"
with open(filename, "rb") as f:
	file_data = f.read()

image_hash = hashlib.sha3_256(file_data).hexdigest()