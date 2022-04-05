import os

output_path = './output'

track_path = './output/track'

def create_output_directories():
	if not os.path.exists(output_path):
		os.makedirs(output_path)
	if not os.path.exists(track_path):
		os.makedirs(track_path)
create_output_directories()
