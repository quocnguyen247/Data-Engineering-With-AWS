import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Customer Landing
CustomerLanding_node1717865056699 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://cd0030bucketuswest2/customers/landing/"], "recurse": True}, transformation_ctx="CustomerLanding_node1717865056699")

# Script generated for node Share With Research
ShareWithResearch_node1717865089648 = Filter.apply(frame=CustomerLanding_node1717865056699, f=lambda row: (not(row["shareWithResearchAsOfDate"] == 0)), transformation_ctx="ShareWithResearch_node1717865089648")

# Script generated for node Trusted Customer Zone
TrustedCustomerZone_node1717865101149 = glueContext.write_dynamic_frame.from_options(frame=ShareWithResearch_node1717865089648, connection_type="s3", format="glueparquet", connection_options={"path": "s3://cd0030bucketuswest2/trusted/", "partitionKeys": []}, format_options={"compression": "gzip"}, transformation_ctx="TrustedCustomerZone_node1717865101149")

job.commit()