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

# Script generated for node Customer Curated
CustomerCurated_node1717915849842 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://cd0030bucketuswest2/customers/curated/"], "recurse": True}, transformation_ctx="CustomerCurated_node1717915849842")

# Script generated for node Step Traner
StepTraner_node1717915870808 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://cd0030bucketuswest2/step_trainer/landing/"], "recurse": True}, transformation_ctx="StepTraner_node1717915870808")

# Script generated for node Customer And StepTranner
CustomerAndStepTranner_node1717915854429 = Join.apply(frame1=CustomerCurated_node1717915849842, frame2=StepTraner_node1717915870808, keys1=["serialNumber"], keys2=["serialNumber"], transformation_ctx="CustomerAndStepTranner_node1717915854429")

# Script generated for node Drop Fields
DropFields_node1717915857219 = DropFields.apply(frame=CustomerAndStepTranner_node1717915854429, paths=["customerName", "email", "birthDay", "serialNumber", "registrationDate", "lastUpdateDate", "shareWithPublicAsOfDate", "shareWithResearchAsOfDate", "shareWithFriendsAsOfDate"], transformation_ctx="DropFields_node1717915857219")

# Script generated for node Amazon S3
AmazonS3_node1717915860688 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1717915857219, connection_type="s3", format="json", connection_options={"path": "s3://cd0030bucketuswest2/step_trainer/trusted/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1717915860688")

job.commit()