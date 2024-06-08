### 
# You might have noticed this code in the screencast.
#
# import findspark
# findspark.init('spark-2.3.2-bin-hadoop2.7')
#
# The findspark Python module makes it easier to install
# Spark in local mode on your computer. This is convenient
# for practicing Spark syntax locally. 
# However, the workspaces already have Spark installed and you do not
# need to use the findspark module
#
###

import pyspark
sc = pyspark.SparkContext(appName="maps_and_lazy_evaluation_example")


# Starting off with a regular python list
log_of_songs = [
        "Despacito",
        "Nice for what",
        "No tears left to cry",
        "Despacito",
        "Havana",
        "In my feelings",
        "Nice for what",
        "despacito",
        "All the stars"
]

# parallelize the log_of_songs to use with Spark
songs_rdd = sc.parallelize(log_of_songs)

# Collect all the elements of the RDD
collected_songs = songs_rdd.collect()

# Compare the collected elements with the original list
if collected_songs == log_of_songs:
    print("The original input data is preserved.")
else:
    print("The original input data is not preserved.")

# Print the original list and the collected elements
print("Original List: ", log_of_songs)
print("Collected Elements: ", collected_songs)


# create a python function to convert strings to lowercase
def convert_song_to_lowercase(song):
    return song.lower()

print(convert_song_to_lowercase("Songtitle"))
# use the map function to transform the list of songs with the python function that converts strings to lowercase
lowercase_songs_rdd = songs_rdd.map(convert_song_to_lowercase) 
lowercase_songs_rdd.foreach(print) 

# Show the original input data is still mixed case
songs_rdd.foreach(print) 

# Use lambda functions instead of named functions to do the same map operation
lowercase_songs_rdd = songs_rdd.map(lambda song: song.lower()).foreach(print)
lowercase_songs_rdd = songs_rdd.map(lambda x: x.lower()).foreach(print)