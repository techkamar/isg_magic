#!/usr/bin/python3
import os

ISG_EXEC_LOCATION = "/home/kamar/Infinite-Storage-Glitch-master/target/release/isg4real"

def convert_file_to_video(filename):
	command = f"{ISG_EXEC_LOCATION} embed -i {filename} --preset optimal --mode binary --threads 2 --block-size 4 --fps 24 --resolution 720"
	os.system(command)

def get_file_name_with_avi_extension(filename):
	reverse_string = filename[::-1]
	length_of_extension = reverse_string.find(".")
	filename_without_extension = filename[0:len(filename)-(length_of_extension+1)]
	return f"{filename_without_extension}.avi"

def convert_all_files(working_directory,destination_directory):
	print(f"Current directory : {working_directory}")
	all_files = os.listdir(working_directory)
	all_files.remove("output")
	all_files.sort()
	for filename in all_files:
		full_file_name_with_path = f"{working_directory}/{filename}"
		print(f"Converting file : {filename}")
		convert_file_to_video(filename)
		output_file_name = get_file_name_with_avi_extension(filename)
		print(f"Moving file  to ouput directory: {output_file_name}")
		os.system(f"mv output.avi \"{output_file_name}\"")
		os.system(f"mv {output_file_name} \"{destination_directory}\"")

if __name__ == "__main__":
	working_directory = os.getcwd()
	destination_directory = working_directory+"/output"
	try:
		os.makedirs(destination_directory)
	except:
		pass
	convert_all_files(working_directory,destination_directory)
	print("Done!!!")
