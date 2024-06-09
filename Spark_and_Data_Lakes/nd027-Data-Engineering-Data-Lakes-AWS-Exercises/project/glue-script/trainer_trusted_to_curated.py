import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Step Trainer
StepTrainer_node1717917423167 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://cd0030bucketuswest2/step_trainer/trusted/"], "recurse": True}, transformation_ctx="StepTrainer_node1717917423167")

# Script generated for node Accelerometer Records
AccelerometerRecords_node1717917425109 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://cd0030bucketuswest2/accelerometer/trusted/"], "recurse": True}, transformation_ctx="AccelerometerRecords_node1717917425109")

# Script generated for node MapApply
MapApply_node1717917429137 = Join.apply(frame1=AccelerometerRecords_node1717917425109, frame2=StepTrainer_node1717917423167, keys1=["timestamp"], keys2=["sensorReadingTime"], transformation_ctx="MapApply_node1717917429137")

# Script generated for node Drop Fields
DropFields_node1717917624946 = DropFields.apply(frame=MapApply_node1717917429137, paths=["user"], transformation_ctx="DropFields_node1717917624946")

# Script generated for node Machine Learning Curated
MachineLearningCurated_node1717917489951 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1717917624946, connection_type="s3", format="json", connection_options={"path": "s3://cd0030bucketuswest2/accelerometer/curated/", "partitionKeys": []}, transformation_ctx="MachineLearningCurated_node1717917489951")

job.commit()