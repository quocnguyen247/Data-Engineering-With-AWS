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

# Script generated for node Customer Trusted
CustomerTrusted_node1717873711088 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://cd0030bucketuswest2/customers/trusted/"], "recurse": True}, transformation_ctx="CustomerTrusted_node1717873711088")

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1717872580232 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://cd0030bucketuswest2/accelerometer/landing/"], "recurse": True}, transformation_ctx="AccelerometerLanding_node1717872580232")

# Script generated for node Join Customer
JoinCustomer_node1717873438029 = Join.apply(frame1=AccelerometerLanding_node1717872580232, frame2=CustomerTrusted_node1717873711088, keys1=["user"], keys2=["email"], transformation_ctx="JoinCustomer_node1717873438029")

# Script generated for node Drop Fields
DropFields_node1717907947351 = DropFields.apply(frame=JoinCustomer_node1717873438029, paths=["z", "y", "x", "timestamp", "user"], transformation_ctx="DropFields_node1717907947351")

# Script generated for node Amazon S3
AmazonS3_node1717872588118 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1717907947351, connection_type="s3", format="json", connection_options={"path": "s3://cd0030bucketuswest2/customers/curated/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1717872588118")

job.commit()